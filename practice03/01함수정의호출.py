# 1. 함수란? 👉 특정 작업을 묶어서 재사용하는 코드 블록
print("hello")
print("hello")
print("hello")

# def 함수이름():
#     실행할 코드


def say_hello():
    print("hello")


def greet():
    print("안녕하세요")
# ✔ 핵심 포인트

# def : 함수 선언 키워드
# greet : 함수 이름
# () : 입력 받을 자리 (지금은 없음)
# : : 함수 시작
# 들여쓰기 된 부분 = 함수 몸체

# 함수 호출
greet()


# 실행흐름
def greet():
    print("A")

print("B")
greet()
print("C")

# 위에서부터 읽음
# def는 실행이 아니라 "등록"
# greet() 만났을 때 실행됨


# 함수 여러 번 호출
def hello():
    print("hi")

hello()
hello()
hello()