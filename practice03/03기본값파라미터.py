# 기본값 파라미터란? 값을 안 넣으면 기본값을 사용하는 매개변수
# def 함수(매개변수=기본값):
#     코드

# 기본 예제
def greet(name="손님"):
    print(name, "님 안녕하세요")

greet()
greet("정호")

# ✔ 값 안 넣으면 → 기본값 사용
# ✔ 값 넣으면 → 그 값으로 덮어씀

# 여러 개 기본값
def introduce(name="익명", age=0):
    print(name, age)

introduce()
introduce("정호")
introduce("정호", 30)


# positional  + default 혼합
def introduce(name, age=0):
    print(name, age)

introduce("정호")
introduce("정호", 30)

# ❗ 중요한 규칙 (면접 단골)
# 👉 기본값 파라미터는 뒤에 와야 한다
# def introduce(name="익명", age):
#     pass
def introduce(name, age=0):
    pass

# keyword와 같이 사용
def introduce(name, age=0):
    print(name, age)

introduce(name="정호")
introduce(name="정호", age=30)

# 실무 포인트
def create_user(name, age, is_admin=False):
    print(name, age, is_admin)

create_user("정호", 30)             # 일반 유저
create_user("관리자", 40, True)     # 관리자