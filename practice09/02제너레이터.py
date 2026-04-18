# 2️⃣ 제너레이터 (Generator, yield)
# ✅ 한 줄 정의 (면접용)
# 값을 한 번에 다 만들지 않고, 필요할 때 하나씩 생성하는 객체

# ✅ 왜 필요하냐 (핵심)

# 리스트:

[x for x in range(100000000)]

# 👉 메모리 한 방에 다 잡아먹음

# 제너레이터:
# (x for x in range(100000000))
# 👉 필요할 때 하나씩 생성 (lazy evaluation)

# ✅ 기본 개념
# 🔹 일반 함수 vs 제너레이터 함수
# 일반 함수
def func():
    return 1
# 제너레이터 함수
def gen():
    yield 1

# 👉 return → 종료
# 👉 yield → 값을 반환하고 상태 유지

# ✅ 동작 방식 (중요)
def gen():
    yield 1
    yield 2
    yield 3

g = gen()

print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

# 👉 함수가 멈췄다가 다시 이어서 실행됨

# ✅ for문에서 사용
def gen():
    yield 1
    yield 2
    yield 3

for x in gen():
    print(x)

# 👉 내부적으로 next() 계속 호출됨

# ✅ 제너레이터 표현식 (리스트 컴프리헨션과 비교)
# 리스트
lst = [x * 2 for x in range(5)]

# 제너레이터
gen = (x * 2 for x in range(5))

# 👉 [] vs ()

# ✅ 언제 쓰냐 (실무 관점)
# 1. 대용량 데이터 처리
def read_file():
    with open("big.txt") as f:
        for line in f:
            yield line

# 👉 파일 전체 안 올리고 한 줄씩 처리

# 2. 스트리밍 처리
def infinite():
    i = 0
    while True:
        yield i
        i += 1

# 👉 무한 데이터도 가능

# 3. 파이프라인 처리
def double(nums):
    for n in nums:
        yield n * 2

def even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

nums = range(10)
result = even(double(nums))

for r in result:
    print(r)

# 👉 데이터 흐름 기반 처리

# ⚠️ 주의
# ❌ 한 번만 순회 가능
g = (x for x in range(3))

list(g)  # [0,1,2]
list(g)  # []

# 👉 이미 다 써버림

# ❌ 인덱싱 안됨
# g[0]  # ❌
# 🔥 핵심 비교 (중요)
# 구분	리스트	제너레이터
# 메모리	많이 사용	적게 사용
# 실행	즉시 생성	지연 생성
# 재사용	가능	불가능
# 속도	빠름	상황에 따라
# 🔥 한 줄 정리 (면접용)

# "제너레이터는 yield를 사용하여 값을 하나씩 생성하는 이터레이터로, 메모리 효율적인 데이터 처리를 위해 사용됩니다."