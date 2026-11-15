#!/usr/bin/env python3
"""Validate actual Jekyll output. Missing legacy links are reported separately."""
import argparse, collections, json, posixpath, re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=collections.Counter(); self.meta=collections.defaultdict(list)
        self.canonical=[]; self.alternates=[]; self.links=[]; self.ld=[]; self.script=None; self.lang=''; self.title=''; self.in_title=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags[tag]+=1
        if tag=='html': self.lang=a.get('lang','')
        if tag=='title': self.in_title=True
        if tag=='meta':
            for key in ('name','property'):
                if key in a: self.meta[a[key].lower()].append(a.get('content',''))
        if tag=='link':
            rel=a.get('rel','').lower().split()
            if 'canonical' in rel: self.canonical.append(a.get('href',''))
            if 'alternate' in rel and a.get('hreflang'): self.alternates.append((a['hreflang'],a.get('href','')))
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag=='script' and a.get('type','').lower()=='application/ld+json': self.script=''
    def handle_data(self,data):
        if self.in_title:self.title+=data
        if self.script is not None:self.script+=data
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if tag=='script' and self.script is not None:self.ld.append(self.script);self.script=None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('site',type=Path);ap.add_argument('--origin',default='https://softmeal.org');ap.add_argument('--baseurl',default='');ap.add_argument('--strict-link-page',action='append',default=[]);ap.add_argument('--report',type=Path);ap.add_argument('--strict-links',action='store_true');args=ap.parse_args()
    root=args.site.resolve(); base=args.baseurl.rstrip('/'); pages={}; errors=[]; missing=[]; redirects=[]
    def error(url,code,**details):errors.append(dict(page=url,issue=code,**details))
    for f in sorted(root.rglob('*.html')):
        rel='/'+f.relative_to(root).as_posix(); url=base+(rel[:-10] if rel.endswith('/index.html') else rel)
        p=Page();p.feed(f.read_text(encoding='utf-8'));pages[url]=p
    if not pages:error('', 'no_built_html')
    def lookup(path):
        path=unquote(path)
        if base and not path.startswith(base+'/'):return None
        rel=path[len(base):] if base else path
        if path in pages:return path
        if not path.endswith('/') and path+'/' in pages:return path+'/'
        f=root/rel.lstrip('/')
        if f.is_file():return path
        # Cloudflare Pages removes .html for existing foo.html files; it does not
        # imply that a missing foo.html route redirects to foo/index.html.
        if not posixpath.splitext(path)[1] and f.with_suffix('.html').is_file():return path+'.html'
        return None
    for url,p in pages.items():
        for tag in ('html','head','body'):
            if p.tags[tag]!=1:error(url,'document_structure',tag=tag,count=p.tags[tag])
        if not p.title.strip():error(url,'missing_title')
        if not p.lang:error(url,'missing_html_language')
        if len(p.canonical)!=1:error(url,'canonical_count',count=len(p.canonical));continue
        canonical=p.canonical[0]; expected=args.origin+url
        if unquote(canonical)!=unquote(expected):error(url,'canonical_not_self',actual=canonical,expected=expected)
        if p.meta['og:url']!=[canonical]:error(url,'og_url_mismatch',values=p.meta['og:url'],canonical=canonical)
        if len(p.meta['description'])!=1:error(url,'description_count',count=len(p.meta['description']))
        for raw in p.ld:
            try:obj=json.loads(raw)
            except (ValueError,TypeError) as ex:error(url,'invalid_json_ld',detail=str(ex));continue
            for entity in obj if isinstance(obj,list) else [obj]:
                if isinstance(entity,dict) and entity.get('@type') in ('Article','BlogPosting','CreativeWork','WebPage'):
                    if entity.get('url',canonical)!=canonical:error(url,'schema_url_mismatch',actual=entity.get('url'))
        if len(set(lang.lower() for lang,_ in p.alternates))!=len(p.alternates):error(url,'duplicate_hreflang_language')
        own=set((lang.lower(),unquote(href)) for lang,href in p.alternates)
        if own and not any(href==unquote(canonical) for _,href in own):error(url,'hreflang_missing_self')
        for lang,href in p.alternates:
            target=urlsplit(href);key=unquote(target.path);other=pages.get(key)
            if target.scheme!='https' or target.netloc!=urlsplit(args.origin).netloc or not other:
                error(url,'invalid_hreflang_target',language=lang,target=href);continue
            if other.canonical!=[href]:error(url,'hreflang_not_canonical',target=href)
            if lang.lower()!=other.lang.lower():error(url,'hreflang_html_language_mismatch',target=href,language=lang,html_language=other.lang)
            if own!=set((l.lower(),unquote(h)) for l,h in other.alternates):error(url,'hreflang_not_reciprocal',target=href)
        for href in p.links:
            t=urlsplit(urljoin(args.origin+url,href))
            if t.scheme not in ('http','https') or t.netloc!=urlsplit(args.origin).netloc:continue
            path=unquote(t.path); resolved=lookup(path)
            if resolved is None:
                item=dict(page=url,target=href,path=path);missing.append(item)
                if url in args.strict_link_page:error(url,'missing_changed_page_link',target=href)
            elif resolved!=path:redirects.append(dict(page=url,target=href,resolved=resolved))
    rules={}
    if not (root/'_redirects').is_file():error('', 'missing_redirect_file')
    if (root/'_redirects').is_file():
        for line in (root/'_redirects').read_text().splitlines():
            if not line.strip() or line.lstrip().startswith('#'):continue
            if len(line)>1000:error('', 'redirect_line_too_long')
            bits=line.split()
            if len(bits)!=3 or bits[2]!='301':error('', 'invalid_redirect_rule',rule=line);continue
            source,target=map(unquote,bits[:2]);source=base+source;target=base+target
            if source in rules:error('', 'duplicate_redirect_source',source=source)
            rules[source]=target
            if source in pages or (root/source[len(base):].lstrip('/')).is_file():error('', 'redirect_overrides_file',source=source)
            if target not in pages or [unquote(c) for c in pages[target].canonical]!=[args.origin+target]:error('', 'redirect_target_not_canonical',target=target)
            if source==target:error('', 'redirect_loop',source=source)
    if len(rules)>2000:error('', 'too_many_static_redirects')
    # Account for explicit static redirects in legacy link checks.
    missing=[x for x in missing if x['path'] not in rules]
    if args.strict_links:
        for x in missing:error(x['page'],'missing_internal_link',target=x['target'])
    sm=root/'sitemap.xml' 
    if not sm.is_file():error('', 'missing_sitemap')
    else:
        for node in ElementTree.parse(sm).getroot().iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
            path=unquote(urlsplit(node.text or '').path)
            if path not in pages:error('', 'sitemap_missing_html',target=node.text)
            elif pages[path].canonical!=[node.text]:error(path,'sitemap_canonical_mismatch',target=node.text)
    if not (root/'404.html').is_file():error('', 'missing_top_level_404')
    report=dict(html_pages=len(pages),error_counts=dict(collections.Counter(x['issue'] for x in errors)),errors=errors,missing_internal_links=missing,routable_noncanonical_links=redirects,missing_link_targets=len(set(x['path'] for x in missing)),alternate_pages=sum(bool(p.alternates) for p in pages.values()),redirect_rules=len(rules))
    if args.report:args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('errors','missing_internal_links','routable_noncanonical_links')},ensure_ascii=False))
    return bool(errors)
if __name__=='__main__':sys.exit(main())
