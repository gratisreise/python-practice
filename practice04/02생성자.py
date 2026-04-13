# 생성자 (__init__)
# 1️⃣ 생성자란?

# 👉 객체가 생성될 때 자동으로 실행되는 함수

class Person:
    def __init__(self):
        print("생성됨")
p = Person()

# 2️⃣ 왜 필요하냐?
# 👉 객체마다 초기값 세팅하려고

# ❌ 생성자 없으면
class Person:
    pass

p = Person()
p.name = "철수"
p.age = 10

# ✅ 생성자 사용
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("철수", 10)
p2 = Person("영희", 12)

# 3️⃣ self 뭐냐 (중요🔥)
# 👉 "자기 자신 객체"를 가리킴
self.name = name
# self.name → 객체 안에 저장
# name → 전달받은 값


# 핵심구조
class 클래스명:
    def __init__(self, 파라미터들):
        self.변수 = 값

# 5️⃣ 실습 예제
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

c1 = Car("BMW", 5000)
c2 = Car("KIA", 3000)

print(c1.brand)  # BMW
print(c2.price)  # 3000