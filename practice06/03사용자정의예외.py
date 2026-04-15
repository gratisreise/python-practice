# 1. 왜 사용자 정의 예외를 쓰냐
# 기본 예외는 한계가 있다.

ValueError
TypeError

# 👉 이걸로는 비즈니스 상황 표현이 안 된다
# - 잔액 부족
# - 권한 없음
# - 이미 존재하는 사용자
# 👉 이런 건 직접 만들어야 한다

# 2. 기본 문법
# 👉 Exception을 상속하면 끝

class MyError(Exception):
    pass

# 3. 간단한 사용
class MyError(Exception):
    pass

try:
    raise MyError("내가 만든 에러")
except MyError as e:
    print(e)
# 출력:내가 만든 에러

# 4. 실전 예제 (중요)
# ❌ 기본 예외만 쓴 경우
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("출금 불가")

# 👉 뭐가 문제냐? → 의미가 애매함

# ✅ 사용자 정의 예외
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("잔액 부족")

# 👉 훨씬 명확함

# 5. 예외에 정보 x담기 (중요)
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"잔액:{balance}, 요청:{amount}")

try:
    raise InsufficientBalanceError(1000, 5000)
except InsufficientBalanceError as e:
    print(e)

# 6. 계층 구조 설계 (실무 핵심)
# 👉 예외도 “설계”한다

class AppError(Exception):
    pass

class AuthError(AppError):
    pass

class PermissionError(AuthError):
    pass

# 👉 이런 구조의 장점:
# except AuthError:
    # 인증 관련 전체 처리