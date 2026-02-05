# 변수: 값을 저장하는 공간
a = 10
name = "철수"


# 자료형
a = 10        # 정수형
b = 3.14      # 실수형
c = "Hello"   # 문자열형
d = True      # 불린형

# 자료형 확인

age = 25 
print(type(age))

print(type(10))       # int
print(type(3.14))     # float
print(type("hello"))  # str
print(type(True))     # bool


# 변수이름규칙

# 가능
name = "kim"
age = 20
user_name = "jung" #보통 언더바로 구분

# 1name = "kim"   # 숫자로 시작 불가
# user-name = "kim"  # - 사용 불가
# class = "A"     # 예약어 사용 불가


# 변수값 변경: 나중에 다른 값으로 변경 가능
age = 25
print(age)
age = 10
print(age)

# 자료형 변환
a = "10"
b = int(a)
print(b + 5)

# 자주쓰는 형변환
int("10")      # 문자열 → 정수
float("3.14")  # 문자열 → 실수
str(100)       # 숫자 → 문자열
bool(1)        # 숫자 → 불리언 (0은 False, 나머지는 True)
bool(0)       # 숫자 → 불리언 (0은 False, 나머지는 True)