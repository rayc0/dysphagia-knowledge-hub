#!/usr/bin/env python3
"""Regression cases for failure modes previously shipped by the site."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path
CHECKER=Path(__file__).with_name('validate_site.py')
ORIGIN='https://softmeal.org'
def document(path,alternates=''):
 return f'<html lang="en"><head><title>Guide</title><meta name="description" content="A guide"><link rel="canonical" href="{ORIGIN}{path}"><meta property="og:url" content="{ORIGIN}{path}">{alternates}<script type="application/ld+json">{{"@type":"WebPage","url":"{ORIGIN}{path}"}}</script></head><body><h1>Guide</h1></body></html>'
class RegressionTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
  (self.root/'en').mkdir();(self.root/'en/index.html').write_text(document('/en/'))
  (self.root/'404.html').write_text(document('/404.html'))
  (self.root/'_redirects').write_text('/old.html /en/ 301\n')
  (self.root/'sitemap.xml').write_text(f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{ORIGIN}/en/</loc></url></urlset>')
 def tearDown(self):self.temp.cleanup()
 def run_check(self):
  report=self.root/'report.json';r=subprocess.run([sys.executable,str(CHECKER),str(self.root),'--strict-links','--report',str(report)],capture_output=True,text=True)
  return r.returncode,json.loads(report.read_text())
 def mutate(self,old,new):
  p=self.root/'en/index.html';p.write_text(p.read_text().replace(old,new))
 def test_clean(self):self.assertEqual(self.run_check()[0],0)
 def test_conflicting_canonical(self):
  self.mutate('</head>','<link rel="canonical" href="https://softmeal.org/other/"></head>');self.assertIn('canonical_count',self.run_check()[1]['error_counts'])
 def test_og_disagreement(self):
  self.mutate('property="og:url" content="https://softmeal.org/en/"','property="og:url" content="https://softmeal.org/other/"');self.assertIn('og_url_mismatch',self.run_check()[1]['error_counts'])
 def test_fabricated_language_target(self):
  self.mutate('</head>','<link rel="alternate" hreflang="ja" href="https://softmeal.org/missing/"></head>');self.assertIn('invalid_hreflang_target',self.run_check()[1]['error_counts'])
 def test_broken_relative_link(self):
  self.mutate('</body>','<a href="missing.md">Guide</a></body>');self.assertIn('missing_internal_link',self.run_check()[1]['error_counts'])
 def test_invalid_json(self):
  self.mutate('"@type":"WebPage"','"@type":broken');self.assertIn('invalid_json_ld',self.run_check()[1]['error_counts'])
 def test_missing_wrapper(self):
  self.mutate('<html lang="en"><head>','');self.assertIn('document_structure',self.run_check()[1]['error_counts'])
 def test_missing_404(self):
  (self.root/'404.html').unlink();self.assertIn('missing_top_level_404',self.run_check()[1]['error_counts'])
 def test_bad_redirect(self):
  (self.root/'_redirects').write_text('/old.html /missing/ 301\n');self.assertIn('redirect_target_not_canonical',self.run_check()[1]['error_counts'])
 def test_legacy_redirect_link(self):
  self.mutate('</body>','<a href="/old.html">Old guide</a></body>');self.assertEqual(self.run_check()[0],0)
 def test_encoded_redirect_target(self):
  p=self.root/'ko/한글';p.mkdir(parents=True);(p/'index.html').write_text(document('/ko/%ED%95%9C%EA%B8%80/'))
  (self.root/'_redirects').write_text('/old.html /ko/%ED%95%9C%EA%B8%80/ 301\n');self.assertEqual(self.run_check()[0],0)
 def test_hreflang_language_mismatch(self):
  self.mutate('</head>','<link rel="alternate" hreflang="ja" href="https://softmeal.org/en/"></head>');self.assertIn('hreflang_html_language_mismatch',self.run_check()[1]['error_counts'])
 def test_valid_self_language(self):
  self.mutate('</head>','<link rel="alternate" hreflang="en" href="https://softmeal.org/en/"></head>');self.assertEqual(self.run_check()[0],0)
if __name__=='__main__':unittest.main()
