# 1. 모듈이란? 모듈은 쉽게 말하면 파이썬 파일 하나다.
# math.py
# user.py
# order.py
# calculator.py
# 이런 .py 파일 하나하나가 모듈이다.

# 다른 파일에 있는 기능을 가져와서 쓰고 싶을 때 import를 사용한다.


import 모듈명

import math

print(math.sqrt(16))


# 3. import를 쓰면 왜 math.을 붙일까?
import math
# 이렇게 가져오면 math 모듈 전체를 가져오는 것이다.
# 그래서 그 안에 있는 기능을 쓸 때는:

math.sqrt()
math.pi
math.floor()
# 처럼 모듈명.기능명 형태로 사용한다.

import math

print(math.pi)
print(math.floor(3.8))


# 4. from import 기본 형태
from 모듈명 import 기능명
from math import sqrt
print(sqrt(16))


# 이 방식은 math.sqrt()가 아니라 바로 sqrt()로 사용할 수 있다.
# 5. import vs from import 차이
import math
print(math.sqrt(16))

# 모듈명.기능명
# 형태로 사용한다.
# 장점은 어디서 온 기능인지 명확하다.

from math import sqrt
print(sqrt(16))

# 기능명 만으로 바로 사용한다.
# 장점은 코드가 짧아진다.
# 단점은 기능 이름만 보면 어디서 온 함수인지 덜 명확할 수 있다.

# 6. 여러 개 가져오기
from math import sqrt, floor, pi

print(sqrt(25))
print(floor(3.9))
print(pi)


# 7. 별칭 사용하기: as 모듈명이나 함수명이 길 때 별칭을 줄 수 있다.

import math as m
print(m.sqrt(16))

from math import sqrt as s
print(s(16))


# 8. 실무적으로 더 추천되는 방식

import math
print(math.sqrt(16))

math.sqrt()

# “아, sqrt는 math 모듈에서 온 거구나”라고 바로 알 수 있다.