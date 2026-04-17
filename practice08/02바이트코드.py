# 1️⃣ 바이트코드란?

# 👉 한 줄 정의

# “Python이 실행하기 위해 만든 중간 코드 (PVM이 이해하는 코드)”

# 2️⃣ 왜 바이트코드를 쓰는가?

# 이거 3개로 정리하면 끝이다 👇

# ✔ 1. 플랫폼 독립성
# OS / CPU 상관없이 동일 실행
# ✔ 2. 실행 속도 개선
# 매번 파싱 안 함 → .pyc 재사용
# ✔ 3. 인터프리터 단순화
# PVM은 바이트코드만 해석하면 됨
# 3️⃣ 실제 흐름 다시 연결
# Python 코드
#    ↓
# 컴파일
#    ↓
# 바이트코드 (.pyc)
#    ↓
# PVM 실행

# 👉 여기서
# 👉 “PVM이 직접 실행하는 게 바이트코드”

# 4️⃣ 바이트코드 직접 확인 (중요 🔥)

# 파이썬에서는 직접 볼 수 있다

# import dis

# def hello():
#     print("hi")

# dis.dis(hello)
# 출력 예시:
#   2           0 LOAD_GLOBAL              0 (print)
#               2 LOAD_CONST               1 ('hi')
#               4 CALL_FUNCTION            1
#               6 RETURN_VALUE
# 5️⃣ 이게 의미하는 것

# 👉 Python은 이렇게 실행된다

# print("hi")

# 👇 실제로는

# LOAD_GLOBAL (print)
# LOAD_CONST ("hi")
# CALL_FUNCTION
# RETURN_VALUE

# 👉 즉

# 👉 고수준 코드 → 저수준 명령어로 쪼개짐

# 6️⃣ 특징 (면접 핵심 포인트)
# ✔ 스택 기반 VM
# 값 push/pop 하면서 실행
# ✔ CPU가 아니라 PVM이 실행
# JVM이 bytecode 실행하는 것과 유사
# ✔ 사람이 읽기 어렵지만 규칙적
# 디버깅 / 최적화 힌트 가능
# 7️⃣ .pyc 파일 정리

# 👉 자동 생성됨

# __pycache__/

# 👉 특징

# 캐시용
# 없어도 실행됨 (다시 생성됨)
# Python 버전 종속
# 8️⃣ 실무에서 중요한 포인트

# 너 기준으로 중요한 연결 👇

# ✔ 성능 분석
# 불필요한 연산 → 바이트코드 증가
# ✔ 함수 호출 비용 이해
# CALL_FUNCTION 자체가 비용
# ✔ 최적화 방향
# 반복문 / 함수 호출 줄이기