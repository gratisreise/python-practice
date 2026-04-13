# 1️⃣ 캡슐화란? 👉 데이터를 숨기고, 필요한 것만 외부에 공개하는 것

# 3️⃣ 캡슐화 안 하면
class Account:
    def __init__(self, balance):
        self.balance = balance

acc = Account(1000)
acc.balance = -999999  # ❌ 문제 발생

# 4️⃣ 캡슐화 적용
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = Account(1000)
acc.deposit(500)

print(acc.get_balance())  # 1500

# 5️⃣ 접근 제한 (파이썬 스타일)
# | 표기       | 의미               |
# | -------- | ---------------- |
# | `name`   | public           |
# | `_name`  | 내부용 (관례)         |
# | `__name` | private (이름 변경됨) |

# 6️⃣ 진짜 중요한 포인트 🔥
self.__balance #👉 내부적으로 이렇게 바뀜
_Account__balance #👉 완전 막는 게 아니라 이름을 바꿔서 보호



class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value

acc = Account(1000)
acc.balance = 2000  # setter
print(acc.balance)  # getter

# 8️⃣ 실무 감각
# 👉 캡슐화는 이런 느낌
# 중요한 데이터는 직접 못 건드리게
# 반드시 메서드 통해서만 변경