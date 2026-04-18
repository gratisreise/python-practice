# 1️⃣ 리스트 컴프리헨션 (List Comprehension)
# ✅ 정의 (한 줄 요약)

# 반복문 + 조건문을 한 줄로 리스트 생성하는 문법

# ✅ 기본 구조
# [표현식 for 변수 in iterable]
# [표현식 for 변수 in iterable if 조건]

# ✅ 예제 1: 기본 반복
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers]
print(result)

# 👉 결과
# [2, 4, 6, 8, 10]

# ✅ 예제 2: 조건 추가
numbers = [1, 2, 3, 4, 5]

result = [x for x in numbers if x % 2 == 0]
print(result)

# 👉 결과
[2, 4]

# ✅ 예제 3: 조건 + 변형
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers if x % 2 == 0]
print(result)

# 👉 결과
[4, 8]

# ✅ 예제 4: if-else 포함
numbers = [1, 2, 3, 4, 5]

result = [x if x % 2 == 0 else 0 for x in numbers]
print(result)

# 👉 결과
[0, 2, 0, 4, 0]

# ✅ 기존 for문 vs 리스트 컴프리헨션
# 🔹 일반 for문
result = []
for x in range(5):
    result.append(x * 2)

# 🔹 리스트 컴프리헨션
result = [x * 2 for x in range(5)]

# 👉 훨씬 짧고 파이썬스럽다

# ✅ 실무 관점 핵심 포인트

# 너 기준으로 중요한 부분만 짚는다 👇

# 1. 데이터 변환
# DTO 변환 느낌
names = ["kim", "lee", "park"]
upper_names = [name.upper() for name in names]

# 2. 필터링
# 조건 기반 조회 느낌
users = [user for user in users if user.is_active]

# 3. 중첩 루프 (주의)
matrix = [[1,2], [3,4]]

flatten = [num for row in matrix for num in row]

# 👉 이건 가독성 떨어지니까 남용 금지

# ⚠️ 주의 (중요)
# ❌ 너무 복잡하게 쓰지 마라
# 이런건 면접에서 까인다
[x*2 if x%2==0 else x+1 for x in nums if x > 3]

# 👉 복잡하면 그냥 for문 써라

# 🔥 한 줄 정리 (면접용)

# "리스트 컴프리헨션은 반복문과 조건문을 한 줄로 표현하여 리스트를 생성하는 문법으로, 코드의 간결성과 가독성을 높이기 위해 사용합니다."