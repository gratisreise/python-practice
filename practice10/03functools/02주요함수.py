# 🔷 1. lru_cache (🔥 제일 중요)
# 👉 functools.lru_cache

# 🔹 정의
# “최근 사용 결과를 캐싱해서 재사용하는 데코레이터”
# (LRU = Least Recently Used)

# 🔹 기본 사용
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# 🔹 핵심 효과
# 동일 입력 → 함수 실행 ❌ → 캐시 반환
# 성능 폭발적으로 개선

# 🔹 내부 동작
# 👉 key = 함수 인자
# 👉 value = 결과

# 🔹 실무 포인트
# 반복 계산 많은 로직
# API 결과 캐싱 (간단한 경우)
# DB 조회 캐싱 (짧은 TTL 느낌)

# 🔹 주의 (🔥 중요)
# mutable 인자 ❌ (list, dict)
# 메모리 사용 증가
# 최신 데이터 필요할 때 부적합

# 🔹 면접 한 줄
# “lru_cache는 함수 호출 결과를 캐싱하여 동일 입력에 대한 중복 연산을 제거하는 데코레이터입니다.”

# 🔷 2. partial
# 👉 functools.partial

# 🔹 정의
# “일부 인자를 고정한 새로운 함수 생성”

# 🔹 예제
from functools import partial

def add(a, b):
    return a + b

add10 = partial(add, 10)
add10(5)  # 15

# 🔹 핵심
# 👉 함수 커스터마이징

# 🔹 실무 포인트
# 설정값 고정 함수 생성
# callback 전달
# 옵션 미리 지정

# 🔹 면접 한 줄
# “partial은 함수의 일부 인자를 미리 고정하여 새로운 함수를 생성하는 도구입니다.”

# 🔷 3. wraps
# 👉 functools.wraps

# 🔹 정의
# “데코레이터에서 원래 함수 정보를 유지”

# 🔹 문제 상황
def deco(func):
    def wrapper():
        return func()
    return wrapper
# 👉 name, docstring 사라짐

# 🔹 해결
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper

# 🔹 핵심
# 👉 metadata 유지

# 🔹 실무 포인트
# 로깅 데코레이터
# 인증/인가
# 트랜잭션 처리

# 👉 데코레이터 만들 때 필수

# 🔹 면접 한 줄

# “wraps는 데코레이터 사용 시 원래 함수의 메타데이터를 유지하기 위해 사용됩니다.”

# 🔷 4. cmp_to_key
# 👉 functools.cmp_to_key

# 🔹 정의
# “비교 함수(comparator)를 key 함수로 변환”

# 🔹 예제
from functools import cmp_to_key

def compare(a, b):
    return a - b

sorted([3,1,2], key=cmp_to_key(compare))

# 🔹 핵심
# 👉 Python 정렬은 기본적으로 key 기반
# 👉 comparator → key로 변환 필요

# 🔹 실무 포인트
# 복잡한 정렬 조건
# 우선순위 비교 로직

# 🔹 면접 한 줄
# “cmp_to_key는 comparator 함수를 key 함수로 변환하여 Python의 정렬 함수에서 사용할 수 있게 합니다.”

# 🔥 전체 핵심 비교
# 기능	역할	핵심
# lru_cache	캐싱	성능 최적화
# partial	함수 생성	인자 고정
# wraps	데코레이터	metadata 유지
# cmp_to_key	정렬	comparator 변환

# 🎯 너 기준 핵심 포인트
# 진짜 중요한 것만 보면:
# 👉 1순위
# lru_cache → 성능
# 👉 2순위
# wraps → 데코레이터 필수
# 👉 3순위
# partial → 구조 설계
# 👉 4순위
# cmp_to_key → 알고리즘

# 🔥 최종 한 줄 (면접용)
# “functools는 함수형 프로그래밍을 지원하는 라이브러리로, lru_cache를 통한 캐싱, partial을 통한 함수 생성, wraps를 통한 데코레이터 보조, cmp_to_key를 통한 정렬 확장을 제공합니다.”