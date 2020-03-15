import requests
import json
import getpass
from requests.auth import HTTPBasicAuth

# 输入设备管理地址和admin用户密码
bigip = input("Enter the BIGIP's managment IP:")
password = getpass.getpass("Enter the admin password:")

# 获取VS相关信息并进行格式化处理
url_vs = "https://{}/mgmt/tm/ltm/virtual".format(bigip)
headers = {"Content-Type": "application/json"}
requests.packages.urllib3.disable_warnings()
response = requests.get(url_vs, headers=headers, auth=HTTPBasicAuth('admin', '%s' % password), verify=False).json()
response_data = response.get('items')


print("VS名称", "------->", "VS IP端口", "--------------->", "pool名称", "------->", "pool members")

# 循环获取每个VS以及对应pool的信息

for config in response_data:
    pool_lst = []
    vs = config['name']
    destination = config['destination']

    # 判断VS是否关联了pool

    if "pool" in config:
        pool = config['pool']
        # 循环获取pool member信息
        pool = repr(pool).replace('/', '~').strip('\'')  # 适配API格式，将/替换为~
        pool_url = "https://%s/mgmt/tm/ltm/pool/%s/members" % (bigip, pool)
        pool_response = requests.get(pool_url, headers=headers, auth=HTTPBasicAuth('admin', '%s' % password),
                                     verify=False).json()
        pool_response = pool_response.get('items')
        # 定义列表存放pool member信息
        for pool_member in pool_response:
            member = pool_member['fullPath']
            pool_lst.append(member)

        pool = repr(pool).replace('~', '/').strip('\'')  # 将~替换回/

    else:
        pool = 'No_Pool_In_Configuration'


    print( vs, "--->", destination, "--->", pool, "--->", pool_lst)


