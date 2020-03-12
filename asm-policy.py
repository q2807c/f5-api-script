import requests
import json
from requests.auth import HTTPBasicAuth

url = "https://10.200.159.170/mgmt/tm/asm/policies/"
headers = {"Content-Type": "application/json"}
requests.packages.urllib3.disable_warnings()
r = requests.get(url, headers=headers, auth=HTTPBasicAuth('admin', 'admin'), verify=False).json()
json_data = r.get('items')

print("Policy_Name", "\t", "Hash_Value")
for item in range(len(json_data)):
    policy = json_data[item]
    name = policy.get('name')
    hash = policy.get('plainTextProfileReference').get('link').split("/", 9)[7]
    print(name, "\t", hash)





