# 1. REST API 한 줄 정의

# REST API = HTTP를 기반으로 자원을 URI로 표현하고, HTTP Method로 행위를 표현하는 API 설계 방식

# 2. 핵심 개념 3개 (이거 무조건 잡아라)
# ✔ 1. Resource (자원)
# /users
# /posts/1
# /orders/100

# 👉 “명사”로 표현

# ✔ 2. Method (행위)
# Method	의미
# GET	조회
# POST	생성
# PUT	전체 수정
# PATCH	부분 수정
# DELETE	삭제
# ✔ 3. Representation (표현)

# 👉 보통 JSON

{
  "id": 1,
  "name": "JungHo"
}
# 3. Python에서 REST API 호출 (실전)
# ✔ GET 요청 (조회)
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()
print(data["title"])

# ✔ POST 요청 (생성)
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

# ✔ PUT / PATCH (수정)
# requests.put(url, json=data)    # 전체 수정
# requests.patch(url, json=data)  # 부분 수정

# ✔ DELETE
# requests.delete(url)

# 4. REST API 호출 구조 (실무 기준)
import requests

url = "https://api.example.com/users/1"

headers = {
    "Authorization": "Bearer access_token"
}

response = requests.get(url, headers=headers, timeout=3)

response.raise_for_status()

data = response.json()

# 5. 상태 코드 (면접 핵심)
# 코드	의미
# 200	성공
# 201	생성 성공
# 400	잘못된 요청
# 401	인증 실패
# 403	권한 없음
# 404	없음
# 500	서버 오류

# 6. REST 설계 규칙 (중요)
# ✔ URI는 명사
# /getUsers ❌
# /users    ✅
# ✔ 행위는 Method로
# POST /users → 생성
# GET  /users → 조회
# ✔ 계층 구조 표현
# /users/1/orders

# 7. 실무 포인트 (진짜 중요)
# 1. 인증
# headers = {
#     "Authorization": "Bearer JWT"
# }

# 👉 너가 하던 JWT 구조 그대로

# 2. 예외 처리
# try:
#     response = requests.get(url, timeout=3)
#     response.raise_for_status()
# except requests.exceptions.RequestException as e:
#     print("에러:", e)

# 3. 재시도 / 안정성
# timeout 필수
# retry 필요
# circuit breaker (MSA)

# 👉 너 MSA 경험이랑 바로 연결됨

# 8. 너 기준 실무 연결 (핵심)

# 너가 했던 거 그대로다:

# OpenFeign → REST API 호출 자동화
# Gateway → API 진입점
# AuthService → JWT 검증
# 외부 API (Gemini) → REST 호출

# 👉 즉

# REST API 호출 = 너가 매일 하던 것

# 9. 한 단계 더 깊게 (차별화 포인트)

# 면접에서 이거 말하면 레벨 올라간다:

# Idempotency
# GET, PUT → 여러 번 호출해도 결과 동일
# Stateless
# 서버는 상태 저장 안함
# Cacheable
# 응답 캐싱 가능
# 10. 면접 1분 답변

# REST API는 HTTP 기반으로 자원을 URI로 표현하고, HTTP Method를 통해 행위를 정의하는 방식입니다. 클라이언트는 requests 같은 라이브러리를 통해 GET, POST 등의 요청을 보내고 JSON 형태로 데이터를 주고받습니다. 실무에서는 Authorization 헤더를 통한 인증, timeout 설정, 예외 처리 등을 통해 안정적인 API 호출을 구현하며, MSA 환경에서는 OpenFeign이나 Gateway를 통해 REST 통신을 표준화합니다.