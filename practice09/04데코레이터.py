# 4️⃣ 데코레이터 (Decorator)
# ✅ 한 줄 정의 (면접용)
# 함수를 수정하지 않고 기능을 추가하는 문법 (함수를 감싸는 구조)

# ✅ 핵심 개념 먼저
# 👉 함수도 객체다 (이게 핵심)

def hello():
    print("hello")

f = hello
f()

# 👉 함수도 변수에 담고 전달 가능

# ✅ 기본 구조
def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
# ✅ 사용 방법
def hello():
    print("hello")

hello = decorator(hello)

hello()

# 👉 결과
before
hello
after

# ✅ @ 문법 (문법 설탕)
@decorator
def hello():
    print("hello")

# 👉 이건 내부적으로

hello = decorator(hello)

# 이거랑 동일

# ✅ 인자 있는 함수 처리 (중요)
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

# ✅ 예제
@decorator
def add(a, b):
    return a + b

print(add(1, 2))

# 👉 결과
before
after
3

# ✅ 왜 쓰냐 (실무 관점 핵심)

# 너 기준으로 딱 이 4개만 기억해라 👇

# 1. 로깅
def log(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 실행")
        return func(*args, **kwargs)
    return wrapper

# 2. 권한 체크
def auth(func):
    def wrapper(*args, **kwargs):
        if not is_login:
            raise Exception("로그인 필요")
        return func(*args, **kwargs)
    return wrapper

# 3. 실행 시간 측정
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper

# 4. 캐싱
def cache(func):
    memo = {}
    def wrapper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return wrapper

# 🔥 너한테 중요한 포인트 (핵심)

# 👉 이거 그냥
# Spring AOP랑 100% 동일한 개념

# 🔹 비교
# Python	Spring
# decorator	AOP
# wrapper	advice
# func	target method

# 👉 즉
# 공통 로직 분리
# 비즈니스 로직 침투 없이 기능 추가
# 완전히 같은 철학

# ⚠️ 주의
# ❌ 메타데이터 깨짐
print(add.__name__)  # wrapper 나옴

# 👉 해결

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
🔥 한 줄 정리 (면접용)

# "데코레이터는 함수를 감싸서 기존 코드를 수정하지 않고 공통 기능을 추가하는 구조로, AOP와 유사한 역할을 합니다."