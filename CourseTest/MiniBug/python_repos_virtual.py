import requests
from plotly.graph_objs import Bar
from plotly import offline

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?&q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers = headers)
print(f"status code = {r.status_code}")

repo_names, stars = [],[]

# 将api响应返回的结果赋值给一个变量，这里应该是一个字典
response_dict = r.json()

# 探索有关仓库的信息
repo_dicts = response_dict['items']

for reponse in repo_dicts:
    repo_names.append(reponse['name'])
    stars.append(reponse['stargazers_count'])

data = [{
    'type':'bar',
    'x':repo_names,
    'y':stars,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width': 1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]

my_layout = {
    'title':"GitHub最受欢迎python项目",
    'titlefont':{'size' : 28},
    'xaxis':{
        'title':'Repository',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
        },
    'yaxis':{
        'title':'Stars',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
        },
    
}

fig = {'data':data,'layout': my_layout}
offline.plot(fig, filename = 'python_repo.html')