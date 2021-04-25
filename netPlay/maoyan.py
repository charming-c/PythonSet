import requests
from bs4 import BeautifulSoup
import re


def getMovies(offset):
    proxy = {
        'http': 'http://127.0.0.1:51837'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
        'cookie': '__mta=208960173.1618923731947.1619331010262.1619331972827.11; uuid_n_v=v1; uuid=9BF5D7C0A1D811EBA5216760317F62A729C80466D4CF4FFABC5A782E8E7911A6; _csrf=d6387db599ead817b92741f3f472f12797e6988f8cdce1735d8e271c8b25ea00; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1618923731; _lxsdk_cuid=178ef5fb81fc8-0285ef215be32f-1f3b6054-13c680-178ef5fb81fc8; _lxsdk=9BF5D7C0A1D811EBA5216760317F62A729C80466D4CF4FFABC5A782E8E7911A6; __mta=208960173.1618923731947.1618923731947.1618923736173.2; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1619331972; _lxsdk_s=17907a34b8d-163-ee7-cc8%7C%7C8'
    }
    response = requests.get(
        url=f"https://maoyan.com/board/4?offset={offset}", headers=header, proxies=proxy)
    print(response.status_code)
    return response.text


item_title = []
body = getMovies("0")
print(body)
soup = BeautifulSoup(body, "lxml")
if(soup.find(class_="content")):
    print("find")
    list = soup.find(class_="content")
    print(list)
    for item in list:
        item_title = item.find(class_='title').toString()
print(soup)
