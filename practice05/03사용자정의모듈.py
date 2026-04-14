import calculator

print(calculator.add(3, 2))
print(calculator.sub(5, 1))


from calculator import add

print(add(10, 5))


from calculator import add, sub

print(add(1, 2))
print(sub(5, 3))


import calculator as calc

print(calc.add(2, 3))


# 6. ⭐ 핵심 포인트 (중요)
# 같은 폴더에 있어야 한다
# project/
#  ├── calculator.py
#  └── main.py

# 다른 폴더에 있으면?
from folder.calculator import add


# 9. 자주 나오는 실수
# ❌ 파일 이름 잘못 짓기
# math.py

# 👉 위험

# 왜냐면:

# import math

# 하면 내 파일 vs 표준 라이브러리 충돌

# ❌ 실행 파일 안에서 import 꼬임

# 순환참조:

# A → B import
# B → A import

# 👉 터짐 따라서 표준라이브러리와 같은 이름을 사용하지 말자