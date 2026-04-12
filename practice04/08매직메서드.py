# 1. 클래스 / 객체 (핵심 개념)

# ✔ 클래스 (Class)
# 👉 설계도 / 틀
# “이런 데이터와 기능을 가진 객체를 만들겠다” 라는 정의
# 붕어빵 틀 같은 개념

class Person:
    pass


# ✔ 객체 (Object, Instance)
# 👉 클래스를 기반으로 만들어진 실제 데이터
# 붕어빵 틀 → 클래스
# 실제 만들어진 붕어빵 → 객체
p1 = Person()  # p1이라는 객체(인스턴스) 생성


# 바로 감 잡는 예제
class Dog:
    pass
dog1 = Dog()
dog2 = Dog()


# 파이썬 특징 (중요 포인트)

# 파이썬은 모든 게 객체다

# x = 10
# print(type(x))  # <class 'int'>

# 👉 int도 클래스임
# 👉 10도 객체임


class Car:
    pass
c1 = Car()
c2 = Car()
print(type(c1))
print(type(c2))