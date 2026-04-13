# 5. 상속 (Inheritance)
# 1️⃣ 상속이란?
# 👉 기존 클래스의 기능을 물려받는 것
# 부모 클래스 (superclass)
# 자식 클래스 (subclass)

# 2️⃣ 기본 구조
class 부모클래스:
    ...

class 자식클래스(부모클래스):
    ...

# 3️⃣ 바로 감 잡는 예제
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다")

class Dog(Animal):
    pass

class Animal:
    def speak(self):
        print("동물이 소리를 냅니다")

class Dog(Animal):
    pass
dog = Dog()
dog.speak()
# 👉 포인트
# 👉 Dog는 speak를 안 만들었는데도 사용 가능

# 4️⃣ 왜 쓰냐?
class Dog:
    def eat(self):
        print("먹는다")

class Cat:
    def eat(self):
        print("먹는다")

class Animal:
    def eat(self):
        print("먹는다")

class Dog(Animal):
    pass

class Cat(Animal):
    pass


#5️⃣ 기능 확장 (중요🔥)
class Animal:
    def speak(self):
        print("동물 소리")

class Dog(Animal):
    def bark(self):
        print("멍멍")
dog = Dog()
dog.speak()
dog.bark()

#6️⃣ 오버라이딩 (진짜 중요🔥🔥)
class Animal:
    def speak(self):
        print("동물 소리")

class Dog(Animal):
    def speak(self):
        print("멍멍")
dog = Dog()
dog.speak()

# 7️⃣ 부모 메서드 호출 (super())
class Animal:
    def speak(self):
        print("동물 소리")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("멍멍")

# 8️⃣ 실무 감각

# 👉 상속은 이런 데서 씀

# 공통 기능 묶기 (User, Admin, Guest)
# 기본 로직 + 커스터마이징
# 프레임워크 확장 (Spring도 내부적으로 다 상속 구조)
