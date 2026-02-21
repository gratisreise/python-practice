
# 큰/작따옴표 둘다 가능
a = "Hello, World!"
b = 'Hello, World!'

# 여러 문자열 
text = """이것은 
예술입니다."""

# 문자열 더하기
a = "Hello, "
b = "World!"
print(a + " " + b)


# 문자열 반복
print("hi" * 3)


# 문자열 인덱싱
text = "python"
print(text[0])  # 'p'
print(text[1])  # 'y'
print(text[-1])  # 'n'

# 문자열 슬라이싱
text = "python"

print(text[0:2])   # py
print(text[2:5])   # tho
print(text[:3])    # pyt
print(text[3:])    # hon

#문자열 길이
text = "hello"
print(len(text))



# 문자열 함수
text = "hello"

print(text.upper())  # HELLO
print(text.lower())  # hello

# 공백제거
text = "  hello  "

print(text.strip())   # "hello"

# 문자열 찾기
text = "hello"

print(text.find("e"))   # 1
print(text.find("l"))   # 2
print(text.find("z"))   # -1 (찾지 못했을 때)

# 문자열 교체
text = "hello"

print(text.replace("h", "j"))

# 문자열 나누기
text = "a,b,c"

print(text.split(","))


# 문자열 포매팅

# f-string (Python 3.6 이상)
name = "철수"
age = 20

print(f"이름은 {name}, 나이는 {age}")

# format() 메서드
print("이름은 {}, 나이는 {}".format(name, age))


