# ✅ 2단계: defaultdict

# 🔹 1. defaultdict란?
# collections.defaultdict
# 👉 한 줄 정의
# “key가 없을 때 자동으로 기본값을 생성해주는 dict”

# 🔹 2. 왜 쓰냐?

# 일반 dict 문제 👇
d = {}
d["a"] += 1   # ❌ KeyError, 존재하지 않는 키에 대해 접근시 에러 발생

# 👉 해결하려면
if "a" not in d:
    d["a"] = 0
d["a"] += 1

# 👉 defaultdict
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1   # 자동으로 0 생성

# 👉 핵심
# “초기화 코드 제거”

# 🔹 3. 기본 사용
# 1️⃣ 기본값 int (0)
d = defaultdict(int)
d["x"] += 1

print(d)  # {'x': 1}

# 2️⃣ 기본값 list
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)

print(d)  # {'a': [1, 2]}

# 3️⃣ 기본값 set
d = defaultdict(set)
d["a"].add(1)
d["a"].add(1)

print(d)  # {'a': {1}}

# 🔹 4. 핵심 구조 이해 (중요)
defaultdict(기본값_생성함수)

# 👉 예:
# int → 0
# list → []
# set → {}

# 👉 포인트
# “값이 아니라 ‘함수’를 넣는다”

# 🔹 5. 실무에서 진짜 많이 쓰는 패턴
# 🔥 1. 그룹핑 (★★★★★)
data = [
    ("user1", "A"),
    ("user1", "B"),
    ("user2", "A"),
]

d = defaultdict(list)

for user, item in data:
    d[user].append(item)

# 👉 결과
{
  "user1": ["A", "B"],
  "user2": ["A"]
}

# 👉 SQL 느낌
# GROUP BY

# 🔥 2. 카운팅
d = defaultdict(int)

for x in ["a","b","a"]:
    d[x] += 1

# 👉 Counter 대체 가능 (단순한 경우)

# 🔥 3. 그래프 (코테/알고리즘)
graph = defaultdict(list)

graph[1].append(2)
graph[1].append(3)

# 🔥 4. 중첩 구조
d = defaultdict(lambda: defaultdict(int))
d["user"]["count"] += 1

# 👉 JSON-like 구조

# 🔹 6. 성능 / 장점
# 조건문 제거 → 코드 간결
# KeyError 방지
# 반복 로직에서 매우 강력

# 🔹 7. 주의할 점 (🔥 중요)
# 👉 존재하지 않는 key 접근하면 자동 생성됨
d = defaultdict(int)
print(d["not_exist"])  # 0 생성됨

# 👉 문제
# “의도하지 않은 key 증가”

# 🔹 8. Counter vs defaultdict
# 구분	Counter	defaultdict
# 목적	카운팅 특화	범용
# 편의성	더 간단	더 유연
# 추천	단순 카운트	그룹핑

# 🔹 9. 면접용 한 줄
# “defaultdict는 존재하지 않는 key 접근 시 기본값을 자동 생성해주는 dict로, 그룹핑이나 누적 연산에서 조건문 없이 간결한 코드 작성이 가능합니다.”

# 🔹 10. 너 기준 핵심 포인트
# GROUP BY 구현
# 유저별 데이터 묶기
# JSON 구조 만들기
# 이벤트 집계

# 👉 특히
# “데이터 구조 만들 때 거의 무조건 씀”