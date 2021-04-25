import requests
from bs4 import BeautifulSoup
import re
import json


def getLeetcode(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
        'cookie': '_uab_collina=160795516618225197196951; gr_user_id=d7ea0187-8ead-4215-895f-7f9e0cd816b0; grwng_uid=8d5b0363-0d39-420a-b414-4c045cabd209; __auc=962da03517598838f9941d118f5; _ga=GA1.2.408268298.1604581560; a2873925c34ecbd2_gr_last_sent_cs1=charming-10; __atuvc=1%7C5; csrftoken=MydEh6ytBiHOXpqmJyYNsmN6nngvhsxouPg5D02NnbgosNT514tQjryxrRsQWFLg; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLyIsIl9hdXRoX3VzZXJfaWQiOiIxMjgyMDEyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4YWFlZDZjZDM4NTBjNjUyNDE2ZjU2NDE4MDk5NGU3NjMwZTZlZTA2N2MyNzg3NWEwNWQwNDNlMjUyZmY5MDMxIiwiaWQiOjEyODIwMTIsImVtYWlsIjoiY2hhcm1pbmctY2NAbWFpbHMuY2NudS5lZHUuY24iLCJ1c2VybmFtZSI6ImNoYXJtaW5nLTEwIiwidXNlcl9zbHVnIjoiY2hhcm1pbmctMTAiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy9jaGFybWluZy0xMC9hdmF0YXJfMTU4MjI5MzIxOC5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTYxODQxNDQ4MS45ODgxMTk4fQ.3E0aVDmvQjHXZPME8f_RhXZlgMBHLaKKuQCT8HNUUtQ; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1616940987,1617020379,1618414483; _gid=GA1.2.1216311299.1619316980; __asc=68f4bf2517907bf0c3411220a35; a2873925c34ecbd2_gr_session_id=e00a45c5-8891-49ce-aade-fe8eef4fd553; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=e00a45c5-8891-49ce-aade-fe8eef4fd553; a2873925c34ecbd2_gr_session_id_e00a45c5-8891-49ce-aade-fe8eef4fd553=true; _gat_gtag_UA_131851415_1=1; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1619332669; a2873925c34ecbd2_gr_cs1=charming-10'
    }
    try:
        res = requests.get(url, headers=header)
        if res.status_code == 200:
            return res.text
    except requests.RequestException:
        return None


if __name__ == '__main__':
    response = getLeetcode("https://leetcode-cn.com/problemset/all/")
    questions_json = json.loads(response)
    questions_list = questions_json['stat_status_pairs']
    print(questions_list)
    # list = soup.find_all('tr')
    # if soup.find(class_='reactable-data'):
    # list = soup.find(class_='reactable-data').find_all('tr')
    # print(list)
    # else:
    #     print(soup)n
    # print(list)
