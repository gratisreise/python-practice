# 🔷 1. math
# 🔹 1. math란?

# math는
# 수학 계산을 위한 함수 모음 (고속, C 기반)

# 👉 한 줄 정의

# “정확하고 빠른 수학 연산 라이브러리”

# 🔹 2. 왜 쓰냐?
# 기본 연산: + - * / → 한계 있음
# math → 더 다양한 연산 제공

# 🔹 3. 핵심 함수 (실무 + 코테 필수)

# 1️⃣ 올림 / 내림
# math.ceil
# math.floor
import math

math.ceil(2.3)   # 3
math.floor(2.7)  # 2

# 2️⃣ 제곱 / 루트
# math.sqrt
# math.pow
math.sqrt(16)  # 4
math.pow(2, 3) # 8

# 3️⃣ 절대값 / 팩토리얼
# math.fabs
# math.factorial
math.fabs(-10)      # 10.0
math.factorial(5)   # 120

# 4️⃣ 로그 / 상수
# math.log
# math.pi
# math.e

# 🔹 4. 실무 포인트
# ceil → 페이징 처리 (페이지 수 계산)
# sqrt → 거리 계산
# log → 데이터 분석 / 확률
# factorial → 조합 계산

# 🔷 2. random
# 🔹 1. random이란?

# random은
# 난수를 생성하는 라이브러리

# 👉 한 줄 정의
# “랜덤 데이터 생성 도구”

# 🔹 2. 핵심 함수 (🔥 중요)
# 1️⃣ 기본 난수
# random.random
import random
random.random()  # 0 ~ 1 사이

# 2️⃣ 범위 랜덤
# random.randint
random.randint(1, 10)  # 1~10

# 3️⃣ 리스트 랜덤
# random.choice
# random.shuffle
# random.sample
lst = [1,2,3]

random.choice(lst)   # 하나 선택
random.shuffle(lst)  # 섞기
random.sample(lst, 2) # 2개 뽑기

# 🔹 3. 핵심 차이 (중요)
# 함수	특징
# choice	1개
# sample	여러 개 (중복 X)
# shuffle	순서 섞기

# 🔹 4. 실무 포인트
# 너 기준으로 보면:

# random.sample → 추천 시스템 (랜덤 후보)
# shuffle → A/B 테스트
# randint → 테스트 데이터 생성

# 🔹 5. 주의 (🔥 중요)

# 👉 random은
# “보안용 아님”

# → 인증 토큰 / 비밀번호 생성 ❌
# 👉 이런 경우:

# secrets 모듈 사용
# 🔹 6. 핵심 요약 (면접용)
# 👉 한 줄 답변
# “math는 수학 연산을 위한 라이브러리이고, random은 난수 생성을 위한 라이브러리로, 각각 계산 처리와 랜덤 데이터 생성에 활용됩니다.”