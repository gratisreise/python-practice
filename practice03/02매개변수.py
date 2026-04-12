# def 함수이름(매개변수):
#     코드

#positional argument (위치 기반): 순서대로 전달
def greet(name):
    print(name, "님 안녕하세요")

greet("정호")


def introduce(name, age):
    print(name, age)

introduce("정호", 30)

# keyword argument (키워드 기반): 매개변수 이름으로 전달
def introduce(name, age):
    print(name, age)

introduce(age=30, name="정호")
# ✔ 순서 안 중요
# ✔ 가독성 좋음

#positional + keyword 혼합
def introduce(name, age):
    print(name, age)

introduce("정호", age=30)

# introduce(name="정호", 30)  # ❌ positional argument는 keyword argument보다 앞에 와야 함


def create_user(name, age, is_admin):
    print(name, age, is_admin)

create_user("정호", 30, True)   # ❌ 의미 파악 어려움
create_user(name="정호", age=30, is_admin=True)  # ✅