import requests
import re
from bs4 import BeautifulSoup
import json


def getFilms(url, header, page):
    try:
        response = requests.get(
            url+'?start=' + str(page*25)+'&filter=', headers=header)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


'''有的api为了反爬虫。就会给api加一个header去确认浏览器访问，这里就拿到浏览器信息就好'''
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
base_url = 'https://movie.douban.com/top250'
for i in range(0, 11):
    html = getFilms(base_url, header, i)
    soup = BeautifulSoup(html, 'lxml')
    if soup.find(class_='grid_view'):
        list = soup.find(class_='grid_view').find_all('li')

        fileName = 'films.json'
        with open(fileName, 'a') as f:

            for item in list:
                item_name = item.find(class_='title').string
                item_img = item.find('a').find('img').get('src')
                item_index = item.find(class_='').string
                item_score = item.find(class_='rating_num').string
                item_author = item.find('p').text
                if item.find(class_='inq'):

                    item_intr = item.find(class_='inq').string
                    print('爬取电影：' + item_index + ' | ' + item_name +
                          ' | ' + item_score + ' | ' + item_intr)
                    f.write(str('爬取电影：' + item_index + ' | ' + item_name +
                                ' | ' + item_score + ' | ' + item_intr+'\n'))

                else:
                    f.writelines('爬取电影：' + item_index + ' | ' + item_name +
                                 ' | ' + item_score + ' | '+'None'+'\n')
                    print('爬取电影：' + item_index + ' | ' + item_name +
                          ' | ' + item_score + ' | '+'None')
                    # print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_img + ' | '
                    #       + item_score + ' | ' + item_author + ' | ''' + item_intr)
