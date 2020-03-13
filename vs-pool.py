import requests
import json
from requests.auth import HTTPBasicAuth

url_vs = "https://10.154.10.12/mgmt/tm/ltm/virtual"
headers = {"Content-Type": "application/json"}
requests.packages.urllib3.disable_warnings()
r = requests.get(url_vs, headers=headers, auth=HTTPBasicAuth('admin', 'admin'), verify=False).json()
r = r.get('items')

# print(r)

result = []

for dic in r:
    map = {}
    for key in dic.keys():
        if key == 'name':
            map[key] = dic[key]
        elif key == 'destination':
            map[key] = dic[key]
        elif key == 'pool':
            pool = dic[key]
            map[key] = dic[key]

    result.append(map)

for vs in result:
    print(vs)






