from requests import get #모듈 불러오기

#베이스 URL과 검색어 입력받기
base_url = input("스크래핑할 사이트의 베이스 URL을 입력하세요 (예시:https://search.daum.net/search?q=) : ")

search_term = input("스크래핑하고싶은 검색어를 입력하세요 (예시: python, C++, USD환율 ) :")

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("사이트를 불러올수없습니다.")
else:
    print(response.text)
    #프린트