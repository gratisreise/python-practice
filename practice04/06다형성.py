# 1️⃣ 다형성이란? 👉 같은 이름의 메서드가 다른 동작을 하는 것

class Dog:
    def speak(self):
        print("멍멍")

class Cat:
    def speak(self):
        print("야옹")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

# 상속 + 다형성
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("멍멍")

class Cat(Animal):
    def speak(self):
        print("야옹")

# 파이썬 특징(Duck Typing)
class Bird:
    def speak(self):
        print("짹짹")

class Human:
    def speak(self):
        print("안녕하세요")

for obj in [Bird(), Human()]:
    obj.speak()

# 7️⃣ 실무 감각

# 👉 다형성 쓰는 이유

# 확장성 (새 클래스 추가 쉬움)
# 유지보수 (조건문 제거)
# 인터페이스 통일