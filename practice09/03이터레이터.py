# 3️⃣ Iterable / Iterator
# ✅ 한 줄 정의 (면접용)
# Iterable

# 반복 가능한 객체 (for문 돌릴 수 있는 것)

# Iterator

# 실제로 값을 하나씩 꺼내는 객체 (next() 가능)

# ✅ 직관적으로 이해

# 👉 리스트는 Iterable이다
# 👉 근데 리스트 자체는 Iterator가 아니다

lst = [1, 2, 3]

for x in lst:
    print(x)

# 이게 되는 이유는 👇

# Iterable → Iterator → next() 호출
# ✅ 내부 동작 (진짜 중요)
lst = [1, 2, 3]

it = iter(lst)  # Iterator 생성

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# 👉 for문은 내부적으로 이걸 자동으로 해준다

# ✅ 구조 정리
# 개념	역할
# Iterable	반복 가능한 객체 (__iter__)
# Iterator	값을 하나씩 반환 (__next__)

# ✅ Iterable 조건

# 👉 이거 하나면 된다
__iter__()

# ✅ Iterator 조건

# 👉 두 개 필요
__iter__()
__next__()

# ✅ 직접 만들어보기 (핵심)
class MyIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > 3:
            raise StopIteration
        return self.current
it = MyIterator()

for x in it:
    print(x)

# 👉 결과

1
2
3

# ✅ 왜 중요하냐 (실무 관점)

# 너 기준으로 중요 포인트만 말해준다 👇

# 1. for문의 본질 이해
# for x in something:

# 👉 내부적으로는

# it = iter(something)
# while True:
#     try:
#         x = next(it)
#     except StopIteration:
#         break

# 👉 이걸 알아야 제너레이터 / 커스텀 객체 설계 가능

# 2. 제너레이터 = Iterator
def gen():
    yield 1

# 👉 얘는 사실

# Iterator를 자동으로 만들어주는 문법 설탕

# 3. 데이터 흐름 설계

# 너 스타일 기준 👇

# 스트리밍 처리
# Batch 처리
# 파이프라인

# 👉 전부 Iterator 기반 사고

# ⚠️ 많이 틀리는 포인트
# ❌ Iterable == Iterator 아니다
lst = [1,2,3]

iter(lst)  # Iterator 생성됨

# 👉 리스트는 "반복 가능"일 뿐
# 👉 실제 반복은 Iterator가 한다

# ❌ Iterator는 소모된다
it = iter([1,2,3])

list(it)  # [1,2,3]
list(it)  # []
# 🔥 한 줄 정리 (면접용)

# "Iterable은 반복 가능한 객체이고, Iterator는 next()를 통해 값을 하나씩 반환하는 객체입니다. for문은 내부적으로 Iterable을 Iterator로 변환하여 순회합니다."

# 🔥 연결 구조 (중요)
# Iterable → iter() → Iterator → next()
#                     ↑
#                 yield (Generator)

# 👉 이 구조 머리에 박아라