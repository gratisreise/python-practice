# 1. 표준 라이브러리란?
# 파이썬을 설치하면 기본으로 제공되는 기능 모음
# 즉, 추가 설치 없이 바로 쓸 수 있는 모듈들이다.

import math
import random
import datetime

# 2. 왜 중요한가?
# 실무에서 생각보다 직접 구현 안 한다.
# 랜덤 값 → 직접 구현 ❌ → random 사용
# 날짜 계산 → 직접 구현 ❌ → datetime 사용
# 파일 읽기 → 직접 구현 ❌ → open() 사용

# 3. 대표 표준 라이브러리
# (1) math → 수학 계산
import math
print(math.sqrt(16))   # 제곱근
print(math.pi)         # 원주율

# (2) random → 랜덤 값
import random
print(random.randint(1, 10))  # 1~10 랜덤 숫자
print(random.choice(['a', 'b', 'c']))

# (3) datetime → 날짜 / 시간
import datetime
now = datetime.datetime.now()
print(now)

# (4) os → 운영체제 관련
import os
print(os.getcwd())  # 현재 경로

# (5) sys → 파이썬 실행 환경
import sys
print(sys.version)

# (6) collections → 자료구조 확장
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
print(dq)

# 👉 큐/스택 구현할 때 많이 씀

# 4. import 방식 복습 (실전 연결)
import random
print(random.randint(1, 10))

from random import randint
print(randint(1, 10))

# 5. 표준 라이브러리 vs 외부 라이브러리
# 표준 라이브러리
import math

# ✔ 설치 필요 없음

# 외부 라이브러리
# pip install requests
import requests

# ✔ 따로 설치 필요

# 6. 실무 감각 포인트 (중요)
# 이거 하나 기억해라:
# 👉 “필요한 기능이 있으면 먼저 표준 라이브러리부터 찾아라”

# 예:
# 문자열 처리 → re
# JSON 처리 → json
# 파일 압축 → zipfile
# 멀티스레드 → threading