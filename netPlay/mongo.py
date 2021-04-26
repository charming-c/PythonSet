from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup


def getFilms(baseurl, start):

    param = {
        'start': str(start * 25),
        'filter': ''
    }
    proxy = {
        'http': 'http://127.0.0.1:51837'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    try:
        response = requests.get(baseUrl, params=param,
                                headers=header)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


if __name__ == '__main__':
    baseUrl = 'https://movie.douban.com/top250/'

    conn = MongoClient("mongodb://localhost:27017/")
    db = conn.films

    for i in range(0, 10):
        body = getFilms(baseUrl, i)
        soup = BeautifulSoup(body, 'lxml')
        if soup.find(class_="grid_view"):
            list = soup.find(class_='grid_view').find_all('li')
            for item in list:
                map = {}
                map['No'] = item.find(class_='').string
                map['Name'] = item.find(class_='title').string
                map['Score'] = item.find(class_='rating_num').string
                # map['Script'] = item.find('p', class_='').get_text(strip=True)
                if item.find(class_='inq'):
                    map['Quote'] = item.find(class_='inq').string
                else:
                    map['Quote'] = None
                db.col.insert_one(map)
    for item in db.col.find():
        print(item)
# conn = MongoClient('mongodb://localhost:27017/')
# db = conn.films
# # db.col.insert_one({'No': 3, 'Name': "肖生克的救赎",
# #                   'score': '9.7', 'quote': '希望让人自由。'})
# # db.col.insert_many([
# #     {'No': 1, 'Name': "肖生克的救赎",
# #      'score': '9.7', 'quote': '希望让人自由。'},
# #     {'No': 2, 'Name': "肖生克的救赎",
# #         'score': '9.7', 'quote': '希望让人自由。'}
# # ])

# for item in db.col.find():
#     print(item)
