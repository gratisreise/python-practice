# 1. 패키지란?

# 👉 폴더(디렉토리) = 패키지

# 즉:

# project/
#  ├── main.py
#  └── utils/
#       └── calculator.py

# 여기서 utils 폴더가 패키지다.

# 2. 패키지에서 import 하기
# from utils.calculator import add

# 👉 구조 해석:

# utils (패키지)
#  └── calculator (모듈)
#       └── add (함수)
# 3. 실제 예제
# (1) 구조
# project/
#  ├── main.py
#  └── utils/
#       └── calculator.py
# (2) calculator.py
# def add(a, b):
#     return a + b
# (3) main.py
# from utils.calculator import add

# print(add(3, 4))
# 4. 패키지 없이 import하면?
# import calculator  ❌

# 👉 안 된다 (다른 폴더니까)

# 반드시:

# from utils import calculator

# 또는

# from utils.calculator import add
# 5. 패키지 안에 여러 모듈
# project/
#  └── utils/
#       ├── calculator.py
#       ├── string_utils.py
#       └── file_utils.py

# 사용:

# from utils.calculator import add
# from utils.string_utils import to_upper
# 6. init.py (중요 개념)
# utils/
#  ├── __init__.py
#  └── calculator.py

# 👉 역할:

# 이 폴더를 “패키지”로 인식하게 함
# (요즘은 없어도 동작하지만 개념적으로 중요)
# init.py 활용 예
# # utils/__init__.py
# from .calculator import add

# 이렇게 하면:

# from utils import add

# 👉 바로 사용 가능

# 7. 실무 구조 느낌

# 너 스타일로 보면 이렇게 간다:

# project/
#  ├── user/
#  │    ├── controller.py
#  │    ├── service.py
#  │    └── repository.py
#  ├── order/
#  │    ├── controller.py
#  │    ├── service.py
#  │    └── repository.py
#  └── main.py

# 👉 이게 사실 전부 패키지 구조

# 8. import 경로 감각 (중요)
# from user.service import UserService

# 👉 읽는 법:

# user 패키지 → service 모듈 → UserService
# 9. 자주 하는 실수
# ❌ 상대 경로 착각
# from calculator import add  ❌

# 👉 다른 폴더면 안됨

# ❌ 경로 기준 헷갈림

# 👉 기준은 항상:

# “실행 파일 위치 기준”