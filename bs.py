# 필요한 라이브러리를 가져옵니다.
import requests
from bs4 import BeautifulSoup

# 연관 검색어를 가져올 웹사이트 주소를 변수에 저장합니다.
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

# requests 라이브러리를 사용하여 해당 웹사이트의 내용을 가져옵니다.
response = requests.get(url)

# 가져온 웹사이트 내용을 BeautifulSoup을 사용하여 HTML로 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 웹사이트에서 연관 검색어 부분의 HTML 구조를 분석하여, 연관 검색어가 있는 태그들을 모두 찾습니다.
# 현재 연관 검색어는 <a> 태그의 "keyword" 클래스에 들어있습니다.
related_keywords = soup.select('.lst_related_srch a.keyword')

# 찾아낸 연관 검색어들을 반복문을 통해 출력합니다.
for keyword in related_keywords:
    print(keyword.get_text())  # 각 태그에서 텍스트 부분만 가져와서 출력합니다.
