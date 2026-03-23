#1. for문 (가장 많이 씀)
for i in range(5):
    print(i)

#range()
range(5)        # 0 ~ 4
range(1, 5)     # 1 ~ 4
range(1, 10, 2) # 1,3,5,7,9

#리스트 반복
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#문자열 반복
for ch in "python":
    print(ch)

#2. while문
i = 0

while i < 5:
    print(i)
    i += 1

#3. 반복문 + 조건문
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 4. 중첩 반복문
for i in range(3):
    for j in range(2):
        print(i, j)

#5. 반복문에서 자주 쓰는 패턴
total = 0

for i in range(1, 6):
    total += i

print(total)

#최대값 찾기
nums = [3, 7, 2, 9, 5]
max_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n

print(max_val)