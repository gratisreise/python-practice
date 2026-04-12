# 왜 필요한가 👉 매개변수 개수를 모를 때 사용
# 이런 상황
# 숫자 2개 받을 수도 있고
# 3개 받을 수도 있고
# 10개 받을 수도 있음

# *args (가변 위치 인자) 👉 여러 값을 tuple로 받는다
def add(*args):
    print(args)
add(1, 2, 3)

# 활용예시
def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)

add(1, 2, 3)       # 6
add(10, 20, 30)    # 60

# **kwargs (가변 키워드 인자) 👉 여러 값을 dict로 받는다
def print_user(**kwargs):
    print(kwargs)

print_user(name="정호", age=30)

# 활용예시
def print_user(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_user(name="정호", age=30)


# 같이 쓰기
def func(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

func(1, 2, 3, name="정호", age=30)

# def func(일반, *args, **kwargs):
# 순서중요
# 일반 파라미터
# *args
# **kwargs

# 실무느낌
def create_user(name, **options):
    print("name:", name)
    print("옵션:", options)

create_user("정호", age=30, job="backend")