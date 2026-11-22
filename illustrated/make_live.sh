#!/bin/bash
# Builds the live version of the pilot into out_live/ with the live site's URL names, then copies it into the repo checkout.
set -e
cd "$(dirname "$0")"
rm -rf out_live; mkdir -p out_live/feel out_live/need out_live/door out_live/mindbody out_live/emotion; ln -sfn ../out/media out_live/media
LIVE=1 python3 gen.py >/dev/null 2>&1
python3 - <<'PY'
import glob,os,re
for f in glob.glob('out_live/**/*.html',recursive=True):
    s=open(f,encoding='utf-8').read(); o=s
    s=s.replace('need/rhythm.html','need/rhythm-light.html').replace('need/safe.html','need/safe-place.html')
    s=s.replace('"rhythm.html"','"rhythm-light.html"').replace('"safe.html"','"safe-place.html"')
    s=s.replace('<section class="steps" id="start">','<section class="steps" id="start"><span id="feelings"></span>') if f.endswith('out_live/index.html') else s
    s=s.replace('<title>The Mindful Map</title>','<title>The Mindful Map | A science-based map of mind and body</title>') if f.endswith('out_live/index.html') else s
    if s!=o: open(f,'w',encoding='utf-8').write(s)
os.rename('out_live/need/rhythm.html','out_live/need/rhythm-light.html'); os.rename('out_live/need/safe.html','out_live/need/safe-place.html')
PY
echo built
