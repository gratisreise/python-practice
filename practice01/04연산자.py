# 1. 산술 연산자
a = 10
b = 3

print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # 나눗셈 (결과는 실수)
print(a // b) # 몫 (결과는 정수)
print(a % b)  # 나머지
print(a ** b) # 거듭제곱


# 2. 비교 연산자
a = 10
b = 20
print(a == b)  # 같음
print(a != b)  # 다름
print(a > b)   # 큼
print(a < b)   # 작음
print(a >= b)  # 크거나 같음
print(a <= b)  # 작거나 같음

# 3. 논리 연산자

age = 20

print(age > 10 and age < 30)  # True
print(age < 10 or age > 15)   # True
print(not age > 10)           # False

# 4. 복합 연산자
a = 10

a += 5   # a = a + 5
a -= 3   # a = a - 3
a *= 2   # a = a * 2
a /= 4   # a = a / 4
a //= 2  # a = a // 2
a %= 3   # a = a % 3
a **= 2  # a = a ** 2

# 5. 문자열에서도 연산 가능
print("hi" + "hello")   # 연결
print("a" * 3)          # 반복

# 6. 연산자 우선순위

print(2 + 3 * 4)  # 14