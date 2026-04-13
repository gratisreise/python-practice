# 4. 메서드 (instance / class / static)

# 1️⃣ 인스턴스 메서드
# 👉 객체를 통해 호출되는 기본 메서드
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"안녕하세요, 저는 {self.name}입니다.")
p = Person("철수")
p.greet()
# 👉 포인트
# self 필수
# 객체 데이터(self.name) 사용 가능


# 2️⃣ 클래스 메서드
# 👉 클래스를 대상으로 동작하는 메서드

class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# 👉 포인트
# @classmethod 사용
# cls → 클래스 자체
# 클래스 변수 접근/수정

print(Person.get_count())


# 3️⃣ 정적 메서드 (static)
# 👉 클래스와 관련은 있지만 상태를 안 쓰는 함수

class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b
print(MathUtil.add(3, 5))

# 👉 포인트
# self, cls 없음
# 그냥 함수 느낌


class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    def introduce(self):  # 인스턴스 메서드
        print(f"나는 {self.name}")

    @classmethod
    def get_count(cls):  # 클래스 메서드
        return cls.count

    @staticmethod
    def is_valid_name(name):  # 정적 메서드
        return len(name) > 1