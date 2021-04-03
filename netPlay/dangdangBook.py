import requests
import re
import json


def getBooks(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


items = []
map = []
base_url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'
for i in range(1, 6):
    html = getBooks(base_url+str(i))

    '''正则表达式要好好看看'''
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    items.append(re.findall(pattern, html))

for item in items:
    for single in item:
        map.append({
            '排名': single[0],
            '封面': single[1],
            '书名': single[2],
            '价格': single[6]
        })

print('开始写入数据 ====> ' + str(map))
with open('book.json', 'a', encoding='UTF-8') as f:
    for m in map:
        f.write(json.dumps(m, ensure_ascii=False) + '\n')
    f.close()
