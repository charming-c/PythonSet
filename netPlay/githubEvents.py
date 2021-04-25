import requests


def request(url):
    header = {'Accept': 'application/vnd.github.v3+json'}
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response
    except requests.RequestException:
        return None


responsebody = request(' https://api.github.com/events')
# print(responsebody.content)
print(responsebody.raw)
data = responsebody.json()
for item in data:
    print(item['id'])
# raw = {
#     'aa': "123"
# }
# print(raw['aa'])
print(responsebody.history)
