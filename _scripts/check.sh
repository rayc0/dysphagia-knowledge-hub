#!/usr/bin/env bash
set -euo pipefail
ruby _scripts/validate_frontmatter.rb
python3 _scripts/test_validate_site.py
bundle exec jekyll clean
build_log=$(mktemp)
trap 'rm -f "$build_log"' EXIT
JEKYLL_ENV=production bundle exec jekyll build --trace 2>&1 | tee "$build_log"
if grep -Eq 'YAML Exception|Build Warning:|Liquid Exception|Liquid Warning:' "$build_log"; then
  echo 'Build warnings must be resolved before deployment.' >&2
  exit 1
fi
python3 _scripts/validate_site.py _site --strict-links
