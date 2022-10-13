from requests import get #모듈 불러오기
from bs4 import BeautifulSoup
#베이스 URL과 검색어 입력받기
base_url = input("스크래핑할 사이트의 베이스 URL을 입력하세요 (예시:https://weworkremotely.com/remote-jobs/search?&term=) : ")

search_term = input("스크래핑하고싶은 검색어를 입력하세요 (예시: Full Stack, front end, python, node.js) :")

response = get(f"{base_url}{search_term}")
if response.status_code != 200: #에러 확인
    print("사이트를 불러올수없습니다.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all('section', class_="jobs"))

    #에러가 아니라면 프린트