import requests


def request(url, param):
    header = {'Accept': 'application/vnd.github.v3+json'}
    try:
        response = requests.get(url, params=param, headers=header)
        if response.status_code == 200:
            return response
        else:
            return None
    except requests.RequestException:
        return None


if __name__ == '__main__':
    params = {
        'q': 'python',
        'sort': 'stars',
        'order': 'desc'
    }
    response = request(
        'https://api.github.com/search/repositories', params).json()
    print(response["total_count"])
    print("一共有" + str(response["total_count"]) + "条结果")
    list = response["items"]
    for item in list:
        print("仓库名：%-30s\t" % str(item['name']), end=' ')
        print("Stars数：%10s" % str(item['forks_count']))
