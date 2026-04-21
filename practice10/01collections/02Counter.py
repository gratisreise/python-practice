# ✅ 1단계: Counter (핵심 중 핵심)
# 🔹 1. Counter란?
# collections.Counter

# 👉 한 줄 정의
# “데이터의 개수를 자동으로 세주는 dict”

# 🔹 2. 왜 쓰냐?
# 일반 방식 👇

d = {}
for x in ["a", "b", "a"]:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

# 👉 Counter

from collections import Counter

Counter(["a", "b", "a"])
# {'a': 2, 'b': 1}

# 👉 핵심
# “카운팅 로직 제거”

# 🔹 3. 기본 사용
from collections import Counter

c = Counter("banana")
print(c)
# {'a': 3, 'n': 2, 'b': 1}

# 🔹 4. 핵심 기능 (🔥 중요)
# 1️⃣ 개수 조회
c["a"]  # 3

# 2️⃣ 가장 많이 나온 것
# Counter.most_common
c.most_common(2)
# [('a', 3), ('n', 2)]

# 👉 TOP-N 구할 때 핵심

# 3️⃣ 합치기 / 빼기
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)  # 합
print(c1 - c2)  # 차

# 4️⃣ 요소 반복 생성
list(c.elements())
# ['a','a','a','n','n','b']

# 🔹 5. 실무에서 진짜 쓰는 패턴
# 🔥 1. 로그 집계
logs = ["INFO", "ERROR", "INFO"]
Counter(logs)

# 🔥 2. Top N 조회
Counter(data).most_common(10)
# 👉 인기 검색어 / 추천 시스템

# 🔥 3. 문자열 분석
Counter(text)
# 👉 NLP 기초

# 🔹 6. 성능 포인트
# 내부적으로 C 최적화
# dict보다 빠르고 간결

# 👉 한 줄
# “성능 + 가독성 둘 다 잡음”

# 🔹 7. 면접용 한 줄
# “Counter는 iterable의 요소 개수를 자동으로 계산해주는 자료구조로, most_common을 통해 빈도 기반 데이터를 쉽게 처리할 수 있습니다.”

# 🔹 8. 너 기준 핵심 포인트
# (백엔드 연결)
# Redis 쓰기 전 간단 카운팅
# 인기 데이터 집계
# 로그 분석
# 추천 후보 선정

# 👉 특히
# “Top-K 문제 해결용”