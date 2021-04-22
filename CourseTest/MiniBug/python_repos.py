import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?&q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code = {r.status_code}")

# 将api响应返回的结果赋值给一个变量，这里应该是一个字典
response_dict = r.json()
print(f"Total repositories:{response_dict['total_count']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Respositories returned :{len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\n Keys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

print(response_dict.keys())
