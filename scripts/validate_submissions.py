from pathlib import Path
import json,re
from urllib.parse import urlparse
p=Path(__file__).resolve().parents[1]/'data/community-submissions.json'
d=json.loads(p.read_text(encoding='utf-8'))
assert isinstance(d,list),'Expected an array'
seen=set()
for r in d:
 for k in ['id','name','description','location','officialURL','sourceURLs','contributor','license']:
  assert k in r and r[k],f'Missing {k}'
 assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',r['id']),'Invalid id'
 assert r['id'] not in seen,'Duplicate id'
 seen.add(r['id'])
 assert r['license']=='CC-BY-4.0','Original submissions must specify CC-BY-4.0'
 assert isinstance(r['sourceURLs'],list) and r['sourceURLs'],'Sources required'
 for u in [r['officialURL']]+r['sourceURLs']:
  parsed=urlparse(u);assert parsed.scheme=='https' and parsed.netloc and not parsed.username,'Invalid public HTTPS URL'
print(f'PASS: {len(d)} community submissions validated')
