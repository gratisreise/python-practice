# 리스트: 여러 개의 값을 순서대로 저장하는 자료구조
numbers = [10, 20, 30, 40]
names = ["kim", "lee", "park"]
mixed = [1, "hello", True]
# 1. 순서가 있다
# 2. 값 변경이 가능하다
# 3. 중복 저장이 가능하다

# 리스트 생성
arr = []
arr = [1, 2, 3]
arr = list()

# 인덱스 접근
arr = [10, 20, 30]

print(arr[0])  # 10
print(arr[1])  # 20
print(arr[2])  # 30

# 뒤에서부터 접근
print(arr[-1])  # 30
print(arr[-2])  # 20


# 값 변경
arr = [10, 20, 30]

arr[1] = 99

print(arr)  # [10, 99, 30]

# 값 추가
arr = [1, 2, 3]

arr.append(4)

print(arr)  # [1, 2, 3, 4]

arr.insert(1, 99)

print(arr)  # [1, 99, 2, 3, 4]

# 값 삭제
arr = [1, 2, 3, 4]

arr.pop()

print(arr)  # [1, 2, 3]

arr.remove(3)

print(arr)  # [1]

# 값 확인
arr = [10, 20, 30]

print(len(arr))  # 3

# 반복문 + 리스트
arr = [10, 20, 30]

for num in arr:
    print(num)

# 인덱스와 값 동시에 접근
for i in range(len(arr)):
    print(i, arr[i])

for i, value in enumerate(arr):
    print(i, value)

# 포함여부
arr = [1, 2, 3]

print(2 in arr)      # True
print(5 in arr)      # False
print(5 not in arr)  # True

# 코딩테스트에서 자주 쓰는 형태
arr = list(map(int, input().split()))