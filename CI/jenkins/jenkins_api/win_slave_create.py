import json
import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
slavename = 'win_slave'

with open('win_slave.json', 'r') as load_f:
    postdata = json.load(load_f)

url = f'http://admin:11108c1d093a24fcebe11e945de3bcece4@192.168.30.8:8080/computer/doCreateItem?name={slavename}&type=hudson.slaves.DumbSlave'
response = requests.post(url, data=f'json={json.dumps(postdata)}', headers=headers)
# print(response.text)
print(response.status_code)
assert response.status_code==400


# 查看节点是否存在
url = f"http://192.168.30.8:8080/manage/computer/{slavename}/api/json?tree=displayName"
# jnlpurl = f'http://192.168.30.8:8080/manage/computer/{slavename}/jenkins-agent.jnlp | sed "s/.*<application-desc><argument>\\([a-z0-9]*\\).*/\\1/"'
jnlpurl = f'http://192.168.30.8:8080/manage/computer/{slavename}/jenkins-agent.jnlp'
username = "admin"
api_token = "11f8790b23a9983c0a218ba125aa855f61"
res = requests.get(url, auth=(username, api_token), verify=False)
try:
    res = res.json()
    print(res)
    if res["displayName"] == slavename:
        print(f"节点 {slavename} 已经存在")
        secret = requests.get(jnlpurl, auth=(username, api_token), verify=False)
        print(secret.text)
except:
    print(f"节点 {slavename} 不存在")
    





