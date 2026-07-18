#!/bin/bash
# Baidu Real-time URL Push for softmeal.org
# Usage: BAIDU_TOKEN=your_token bash scripts/baidu-url-submit.sh
# Get token from: https://ziyuan.baidu.com/linksubmit/index

SITE="https://softmeal.org"
TOKEN="${BAIDU_TOKEN:-YOUR_TOKEN_HERE}"
API="http://data.zz.baidu.com/urls?site=${SITE}&token=${TOKEN}"

# Collect all URLs from sitemap or by listing pages
URLS=(
  "https://softmeal.org/"
  "https://softmeal.org/zh-hans/"
  "https://softmeal.org/en/"
)

# Submit in batches of 20
echo "Submitting ${#URLS[@]} URLs to Baidu..."
printf '%s\n' "${URLS[@]}" | curl -s -H 'Content-Type: text/plain' --data-binary @- "$API"
echo ""
echo "Done. Check Baidu Webmaster Tools for indexing status."
