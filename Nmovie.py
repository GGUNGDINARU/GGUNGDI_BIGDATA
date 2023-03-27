import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
# 내가 원하는 위치에 있는 데이터 가져오기
'''
여기는 여러줄로 설명할수 있어요
또 써도 되요
'''
#title = soup.select_one('#old_content > table > tbody > tr:nth-child(6) > td.title > div > a')
#print(title.text)

# #old_content > table > tbody > tr

trs = soup.select("#old_content > table > tbody > tr")
# print(trs)
# 랭킹을 달아주기 위한 변수
rank = 0
for tr in trs:
    a_tag = tr.select_one("td.title > div > a")
    # 만약에 a_tag 가 None이 아니면 text를 출력
    if a_tag is not None:
        rank = rank + 1
        print(rank, a_tag.text)