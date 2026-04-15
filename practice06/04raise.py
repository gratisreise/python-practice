# 1. raise란?
# 👉 "강제로 예외를 발생시키는 키워드"
# 즉, “여기서 일부러 에러 터뜨릴게”

# 2. 기본 사용
raise Exception("에러 발생")

# 예제
try:
    raise Exception("강제 에러")
except Exception as e:
    print(e)

# 출력:
# 강제 에러

# 3. 왜 쓰냐 (핵심)
# 👉 조건 검증 (validation) 때문

# 예제
def withdraw(balance, amount):
    if amount > balance:
        raise Exception("잔액 부족")

    return balance - amount

# 👉 조건 위반 시 바로 중단

# 4. 사용자 정의 예외와 함께 (진짜 중요)
# 👉 실무에서는 무조건 이 조합

class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("잔액 부족")

# 5. 예외 다시 던지기 (re-raise)
# 👉 기존 예외를 그대로 다시 던짐
try:
    x = int("abc")
except ValueError:
    print("로그 남김")
    raise

# 👉 흐름:
# - 에러 발생
# - 로그 찍음
# - 다시 예외 던짐 → 상위로 전달

# 6. 예외 변환 (실무 핵심)
# 👉 내부 예외 → 의미 있는 예외로 변경

try:
    x = int("abc")
except ValueError:
    raise Exception("입력값이 잘못되었습니다")

# 👉 더 좋은 방식

class InvalidInputError(Exception):
    pass

try:
    x = int("abc")
except ValueError:
    raise InvalidInputError("잘못된 입력")

# 7. finally + raise 흐름
try:
    raise Exception("에러")
finally:
    print("무조건 실행")

# 출력:
# - 무조건 실행
# - Traceback ...
# 👉 finally는 raise보다 먼저 실행됨