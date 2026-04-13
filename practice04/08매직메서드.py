# 8. 매직 메서드 (Magic Method)
# 1️⃣ 매직 메서드란?
# 👉 파이썬이 자동으로 호출해주는 특수 메서드
# __ (더블 언더스코어)로 시작/끝
# 우리가 직접 호출 안 해도 실행됨

# 2️⃣ 대표 3개 (무조건 알아야 함🔥)
# ✔ __str__ → 사용자용 출력
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"이름: {self.name}"
p = Person("철수")
print(p)

# ✔ __repr__ → 개발자용 출력
class Person:
    def __repr__(self):
        return "Person 객체"

# ✔ __eq__ → 객체 비교
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("철수")
p2 = Person("철수")

print(p1 == p2)  # True

# 메서드	역할
# __init__	생성자
# __str__	사용자 출력
# __repr__	디버깅
# __eq__	비교
# __len__	길이
# __add__	+ 연산
# __getitem__	인덱싱


# 실전예제
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"책 제목: {self.title}"

    def __eq__(self, other):
        return self.title == other.title

b1 = Book("파이썬")
b2 = Book("파이썬")

print(b1)          # 책 제목: 파이썬
print(b1 == b2)    # True
