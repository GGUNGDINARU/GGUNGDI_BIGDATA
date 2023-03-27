# 다음 영화 순위 크롤링 하는 프로그램
import requests
from bs4 import BeautifulSoup

# 다음 영화 순위 페이지 URL
url = "https://movie.daum.net/ranking/reservation"

# HTTP 요청 보내기
response = requests.get(url)

# HTTP 요청이 성공했는지 확인하기
if response.status_code == 200:
    # HTML 파싱하기
    soup = BeautifulSoup(response.text, "html.parser")
    # 영화 순위 리스트 찾기
    rank = 0
    movie_list = soup.select(".tit_item")
    for tr in movie_list:
        a_tag = tr.select_one("a")
        rank = rank + 1
        print(f'{rank}위 {a_tag.text}')
else:
    print("HTTP 요청 실패")