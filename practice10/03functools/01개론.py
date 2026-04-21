# ✅ 10. 표준 라이브러리 - functools (1단계)
# 🔹 1. functools란?

# functools는
# “함수를 더 강력하게 다루기 위한 도구 모음”

# 👉 한 줄 정의

# “함수를 조합하고, 캐싱하고, 확장하는 유틸리티 라이브러리”

# 🔹 2. 왜 쓰냐? (핵심)

# 일반 코드에서는 이런 문제가 있음:

# 같은 계산 반복됨 (비효율)
# 함수 인자 고정하기 번거로움
# 정렬 기준 커스터마이징 어려움

# 👉 functools가 해결

# 🔹 3. 핵심 기능 4개 (중요)
# 1️⃣ 캐싱 (🔥 실무 중요)
# functools.lru_cache

# 👉 동일 입력 → 결과 재사용

# from functools import lru_cache

# @lru_cache(maxsize=128)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# 👉 효과

# 성능 폭발적으로 개선 (특히 재귀)
# 2️⃣ 함수 인자 고정
# functools.partial
# from functools import partial

# def add(a, b):
#     return a + b

# add_10 = partial(add, 10)
# print(add_10(5))  # 15

# 👉 한 줄 정의

# “함수를 미리 설정된 버전으로 만드는 것”

# 3️⃣ 정렬 커스터마이징
# functools.cmp_to_key
# from functools import cmp_to_key

# def compare(a, b):
#     return a - b

# sorted_list = sorted([3,1,2], key=cmp_to_key(compare))

# 👉 기존 comparator → key 방식 변환

# 4️⃣ 데코레이터 도우미
# functools.wraps
# from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         return func()
#     return wrapper

# 👉 역할

# 원래 함수 정보 유지 (name, docstring)
# 🔹 4. 백엔드 관점 연결 (중요)

# 너 기준으로 보면:

# 🔥 실무에서 진짜 쓰는 것
# lru_cache
# → API 결과 캐싱 / 연산 캐싱
# → Redis 쓰기 전에 로컬 캐시로 활용 가능
# partial
# → 설정값 고정된 함수 생성 (ex. 특정 옵션)
# wraps
# → 로깅 / 트랜잭션 / 인증 데코레이터 만들 때 필수

# 👉 핵심

# “functools = 함수 기반 구조를 확장하는 핵심 도구”

# 🔹 5. 핵심 요약 (면접용)

# 👉 한 줄 답변

# “functools는 함수형 프로그래밍을 지원하는 라이브러리로, 캐싱, 부분 적용, 데코레이터 보조 기능 등을 통해 코드 재사용성과 성능을 개선할 수 있습니다.”