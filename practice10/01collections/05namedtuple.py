# ✅ 4단계: namedtuple
# 🔹 1. namedtuple이란?
# collections.namedtuple

# 👉 한 줄 정의
# “이름이 붙은 튜플 (필드 접근 가능한 튜플)”

# 🔹 2. 왜 쓰냐?
# 일반 tuple 👇

user = ("kim", 30)

print(user[0])  # kim

# 👉 문제
# 가독성 최악
# index 기억해야 함

# 👉 namedtuple

# from collections import namedtuple

# User = namedtuple("User", ["name", "age"])

# u = User("kim", 30)
# print(u.name)  # kim

# 👉 핵심
# “tuple인데 객체처럼 사용 가능”

# 🔹 3. 기본 구조
namedtuple("클래스명", ["필드1", "필드2"])

# 🔹 4. 핵심 특징
# 1️⃣ immutable (불변)
u.name = "lee"  # ❌ 에러

# 👉 tuple이기 때문

# 2️⃣ 인덱스 + 이름 둘 다 가능
u[0]      # kim
u.name    # kim

# 3️⃣ dict처럼 변환
u._asdict()
# {'name': 'kim', 'age': 30}

# 4️⃣ 값 변경 (새 객체 생성)
u2 = u._replace(age=31)
# 👉 기존 수정 ❌ → 새로 생성

# 🔹 5. 실무에서 쓰는 패턴
# 🔥 1. 간단 DTO
User = namedtuple("User", ["id", "name"])
# 👉 클래스 만들기 귀찮을 때

# 🔥 2. DB 결과 매핑
row = User(1, "kim")

# 🔥 3. 좌표 / 데이터 구조
Point = namedtuple("Point", ["x", "y"])

# 🔹 6. dataclass와 차이 (🔥 중요)
# 구분	namedtuple	dataclass
# 변경 가능	❌	✅
# 성능	빠름	보통
# 기능	단순	다양
# 추천	가벼운 구조	실무 객체

# 👉 요즘 실무

# dataclass 더 많이 씀

# 🔹 7. 언제 쓰냐?
# 👉 쓰는 상황
# 읽기 전용 데이터
# 가벼운 구조
# 성능 중요한 경우

# 👉 안 쓰는 상황
# 값 변경 필요
# 복잡한 로직

# 🔹 8. 면접용 한 줄
# “namedtuple은 필드 이름으로 접근 가능한 튜플로, 가볍고 불변인 데이터 구조를 표현할 때 사용됩니다.”

# 🔹 9. 너 기준 핵심 포인트
# DTO 간단 구현
# DB 결과 구조화
# immutable 객체 설계

# 👉 특히
# “읽기 전용 데이터 모델”