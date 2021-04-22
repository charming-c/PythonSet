import requests
from bs4 import BeautifulSoup
import re


def getMovies(offset):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
    response = requests.get(
        url=f"https://maoyan.com/board/4?offset={offset}", headers=header)
    print(response.status_code)
    return response.text


item_title = []
list = []
body = getMovies("0")
soup = BeautifulSoup(body, "lxml")
if(soup.find('dl', class_="board-wrapper")):
    print("find")
    list = soup.find(class_="board_wrapper")
    print(list)
    for item in list:
        item_title = item.find(class_='title')
print(soup)
