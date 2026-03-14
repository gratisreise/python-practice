# 출력
print("hello")
print(10)

# 여러개 출력 
name = "철수"
age = 20

print(name, age)

# 구분자 변경
print("a", "b", "c", sep="-")

# 줄끝 변경
print("hello", end=" ")
print("world")


#입력 input
name = input()
print(name)


# 안내와 함께 입력 받기
name = input("이름을 입력하세요: ")
print(name)

#input은 무조건 문자열
age = input("나이 입력: ")
print(type(age))

#숫자로 바꾸기 형변환
age = int(input("나이 입력: "))
print(age + 1)

#실수 입력
height = float(input("키 입력: "))

# 여러값 입력받기
a, b = input("두 수 입력: ").split()
print(a, b)

# 숫자로 바로 받기
a, b = map(int, input().split())
print(a + b)


#실전예제 
name = input("이름: ")
age = int(input("나이: "))

print(f"{name}님의 나이는 {age}입니다")