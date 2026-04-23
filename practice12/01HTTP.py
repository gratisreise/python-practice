# 1. HTTP 요청 기본 개념
# ✔ 한 줄 정의

# HTTP는 클라이언트가 서버에 요청(Request)을 보내고 응답(Response)을 받는 통신 프로토콜

# 2. Python에서 HTTP 요청 → requests
# 설치
# pip install requests
# 3. 가장 기본: GET 요청
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)  # 상태 코드
print(response.text)         # 문자열 응답
print(response.json())       # JSON → dict
# 4. 핵심 구조 (무조건 외워라)
# ✔ 요청
# URL
# Method (GET, POST 등)
# Headers
# Body
# ✔ 응답
# status_code
# headers
# body (text / json)

# 5. 주요 HTTP 메서드
# 메서드	의미	사용
# GET	조회	데이터 가져오기
# POST	생성	데이터 생성
# PUT	전체 수정	전체 업데이트
# PATCH	부분 수정	일부 업데이트
# DELETE	삭제	데이터 삭제

# 6. POST 요청 (실무 핵심)
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "hello",
    "body": "world",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

# 👉 json= 쓰면 자동으로 Content-Type: application/json

# 7. Query Parameter (GET에서 중요)
params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(response.url)  # 실제 요청 URL 확인

# 👉 결과:

# ...?userId=1
# 8. Header 설정 (인증에서 핵심)
headers = {
    "Authorization": "Bearer access_token",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

# 👉 너 JWT 구조랑 100% 연결됨

# 9. 에러 처리 (실무 필수)
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("에러 발생:", response.status_code)

# 또는

response.raise_for_status()

# 10. Timeout (실무에서 반드시 넣는다)
requests.get(url, timeout=3)

# 👉 안 넣으면 장애 난다 (진짜로)

# 11. 세션 (Connection 재사용 → 성능)
session = requests.Session()

session.get(url)
session.post(url, json=data)

# 👉 내부적으로 keep-alive → 성능 개선

# 12. 너 기준 실무 연결 (중요)

# 너가 하던 거랑 연결해보면:

# OpenFeign → requests 역할
# 외부 API 호출 (Gemini) → 동일 개념
# Header → JWT / API Key
# JSON contract → response.json()

# 👉 즉

# Python requests = Java RestTemplate / Feign의 축소판

# 13. 면접 1분 답변

# HTTP 요청은 클라이언트가 서버에 요청을 보내고 응답을 받는 구조이며, Python에서는 requests 라이브러리를 통해 간단하게 HTTP 통신을 수행할 수 있습니다. GET, POST 등의 메서드를 사용해 데이터를 조회하거나 생성할 수 있고, Header를 통해 인증 정보를 전달하거나 JSON 형태의 데이터를 주고받을 수 있습니다. 또한 timeout 설정과 예외 처리를 통해 안정적인 외부 API 호출을 구현할 수 있습니다.