# 5️⃣ 클로저 (Closure)

# ✅ 한 줄 정의 (면접용)
# 외부 함수의 변수를 내부 함수가 계속 참조하는 구조

# ✅ 핵심 먼저
# 👉 함수 안에 함수
# 👉 내부 함수가 외부 변수 기억

# ✅ 기본 예제
def outer():
    x = 10

    def inner():
        print(x)

    return inner
f = outer()
f()

# 👉 결과
10
# ❗ 중요한 포인트

# 👉 outer()는 끝났는데
# 👉 x는 살아있다

# 👉 이게 클로저

# ✅ 왜 가능하냐

# 파이썬은 함수 객체 안에
# 👉 외부 변수 상태를 같이 저장한다

# ✅ 상태 유지 예제 (핵심)
def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc
c = counter()

print(c())  # 1
print(c())  # 2
print(c())  # 3

# 👉 함수인데 상태를 기억함
# 👉 객체처럼 동작

# ✅ nonlocal 키워드
# 👉 외부 함수 변수 수정할 때 필요

# nonlocal count
# ✅ 왜 쓰냐 (실무 관점)

# 너 기준 핵심만 딱 말한다 👇

# 1. 상태 유지 (객체 대신)
def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print(double(5))  # 10

# 👉 설정값 기억하는 함수

# 2. 데코레이터의 본질
def decorator(func):
    def wrapper():
        return func()
    return wrapper

# 👉 wrapper가 func 기억함
# 👉 이게 클로저

# 3. 설정 캡슐화
def logger(prefix):
    def log(msg):
        print(prefix, msg)
    return log
debug_log = logger("[DEBUG]")
debug_log("test")
# 🔥 너한테 중요한 연결
# 클로저 → 데코레이터 → AOP

# 👉 이 흐름 이해하면 끝

# ⚠️ 주의
# ❌ mutable 공유 문제
def outer():
    lst = []

    def inner():
        lst.append(1)
        return lst

    return inner

# 👉 상태 공유됨 (의도인지 확인 필요)

# 🔥 한 줄 정리 (면접용)
# "클로저는 내부 함수가 외부 함수의 변수를 참조하고 유지하는 구조로, 함수에 상태를 부여할 때 사용됩니다."

# 🔥 핵심 요약
# 함수 안 함수
# 외부 변수 기억
# 상태 유지 가능
# 데코레이터의 기반