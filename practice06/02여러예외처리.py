# 1. 왜 여러 예외 처리가 필요하냐

# 👉 에러는 종류가 다르다
# - 숫자 변환 실패 → ValueError
# - 0으로 나누기 → ZeroDivisionError
# - 파일 없음 → FileNotFoundError

# 👉 근데 다 똑같이 처리하면?
# → 디버깅 지옥

# 2. 기본 형태 (여러 except)
try:
    x = int(input("숫자 입력: "))
    y = 10 / x
except ValueError:
    print("숫자를 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
# 실행 흐름
# 입력: abc → ValueError
# 입력: 0 → ZeroDivisionError

# 👉 각 상황에 맞게 다르게 처리 가능

# 3. except에 변수 받기 (중요)

# 👉 에러 내용을 직접 확인 가능

try:
    x = int("abc")
except ValueError as e:
    print(e)

# 출력: invalid literal for int() with base 10: 'abc'
# 👉 실무에서는 로그 찍을 때 필수

# 4. 여러 예외를 한 번에 처리
try:
    x = int("abc")
except (ValueError, TypeError):
    print("값 또는 타입 에러")

# 👉 같은 방식으로 처리할 때만 사용

# 5. Exception (모든 예외 잡기)
try:
    x = int("abc")
except Exception as e:
    print("모든 에러 처리:", e)
# ⚠️ 중요한 포인트
# 👉 Exception은 최후의 보루

# 왜냐하면:
# - 모든 에러를 잡아버림
# - 버그 숨길 수 있음

# 6. 올바른 순서 (이거 중요)
try:
    ...
except ValueError:
    ...
except Exception:
    ...
# 👉 구체적인 것 → 일반적인 것 순서

# ❌ 잘못된 코드
try:
    ...
except Exception:
    ...
except ValueError:
    ...
# 👉 ValueError 절대 안 들어옴

# 7. 실무 스타일 예시 (너 스타일)
try:
    result = external_api_call()
except TimeoutError:
    print("API 타임아웃")
except ValueError as e:
    print("데이터 파싱 오류:", e)
except Exception as e:
    print("알 수 없는 에러:", e)

# 👉 이게 진짜 백엔드 스타일
# 8. 한 줄 핵심 (면접용)
# 👉"여러 예외 처리는 각각의 예외 타입에 따라 다른 대응을 하기 위해 사용하며, 구체적인 예외부터 순서대로 처리해야 합니다."