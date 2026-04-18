# 6️⃣ 함수형 프로그래밍 (map, filter, reduce)

# ✅ 한 줄 정의 (면접용)
# 함수를 값처럼 다루면서 데이터를 변환하는 방식

# ✅ 핵심 특징
# 함수를 변수처럼 사용
# 상태 변경 최소화
# 데이터 변환 중심

# 1️⃣ map
# ✅ 역할
# 모든 요소에 함수 적용

# ✅ 기본 사용
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)
print(list(result))

# 👉 결과
[2, 4, 6, 8]

# ✅ 리스트 컴프리헨션 비교
# [x * 2 for x in numbers]
# 👉 ✔️ 파이썬에서는 이게 더 많이 쓰임

# 👉 결론
# map ❌ (가독성 떨어짐)
# 리스트 컴프리헨션 ✅

# 2️⃣ filter
# ✅ 역할
# 조건에 맞는 것만 필터링

# ✅ 기본 사용
numbers = [1, 2, 3, 4]

result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

# 👉 결과
[2, 4]

# ✅ 리스트 컴프리헨션 비교
[x for x in numbers if x % 2 == 0]
# 👉 이것도 리스트 컴프리헨션이 더 많이 씀

# 3️⃣ reduce
# ✅ 역할
# 누적 계산

# ✅ 사용법
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda acc, x: acc + x, numbers, 0)
print(result)

# 👉 결과
# 10

# ✅ 동작 과정
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10

# ✅ 대체 가능
# sum(numbers)

# 👉 내장 함수가 더 좋다

# 🔥 실무 기준 핵심 정리

# 너 기준으로 정확하게 말해준다 👇
# ✅ map / filter 거의 안 쓴다

# 👉 이유
# 가독성 떨어짐
# lambda 남용됨

# ✅ 대신 이거 쓴다
# 👉 리스트 컴프리헨션
[x * 2 for x in numbers if x % 2 == 0]

# ✅ reduce는 더 안 쓴다
# 👉 대부분
# sum
# max
# min
# 으로 대체 가능

# 🔥 언제 쓰냐 (예외 케이스)
# ✔️ 함수 조합할 때
# map(func, data)
# ✔️ 파이프라인 스타일
# filter → map → reduce

# 👉 근데 이건
# 👉 제너레이터로 더 많이 해결함

# 🔥 너한테 중요한 포인트
# 리스트 컴프리헨션 > map/filter
# 제너레이터 > lazy 처리
# 클로저 + 데코레이터 > 구조 설계

# 👉 이 3개가 핵심이다

# 🔥 한 줄 정리 (면접용)

# "파이썬에서 함수형 프로그래밍은 map, filter, reduce 등을 통해 데이터를 변환하는 방식이지만, 실무에서는 가독성을 위해 리스트 컴프리헨션과 내장 함수를 더 많이 사용합니다."