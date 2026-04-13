# 3. 인스턴스 변수 / 클래스 변수

# 1️⃣ 인스턴스 변수
# 👉 객체마다 따로 가지는 변수
class Person:
    def __init__(self, name):
        self.name = name  # 인스턴스 변수

p1 = Person("철수")
p2 = Person("영희")

print(p1.name)  # 철수
print(p2.name)  # 영희

# 👉 포인트
# self.name
# 객체마다 값 다름

# 2️⃣ 클래스 변수
# 👉 모든 객체가 공유하는 변수
class Person:
    country = "Korea"

p1 = Person()
p2 = Person()

print(p1.country)  # Korea
print(p2.country)  # Korea

# 👉 포인트
# 클래스에 직접 정의
# 모든 객체가 같은 값 사용

# 헷갈리는 포인트(중요🔥)
class Person:
    country = "Korea"

p1 = Person()
p1.country = "USA"

print(p1.country)        # USA
print(Person.country)    # Korea

# 클래스 변수 진짜 변경 방법
Person.country = "USA"


class User:
    user_count = 0 #클래스 변수
    
    def __init__(self, name):
        self.name = name #인스턴스 변수
        User.user_count += 1 #클래스 변수 접근
u1 = User("철수")
u2 = User("영희")

print(User.user_count) # 2