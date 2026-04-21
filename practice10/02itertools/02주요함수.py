# 🔷 1. permutations (순열)
# 👉 itertools.permutations
# 🔹 정의

# “순서를 고려한 모든 경우의 수”

# 🔹 예제
from itertools import permutations

list(permutations([1,2,3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# 🔹 핵심
# 순서 O
# nPr
# 👉 (1,2) ≠ (2,1)

# 🔹 언제 쓰냐
# 모든 경우 탐색
# 브루트포스
# 순서 중요한 조합

# 🔷 2. combinations (조합)
# 👉 itertools.combinations

# 🔹 정의
# “순서 없이 선택하는 경우의 수”

# 🔹 예제
from itertools import combinations

list(combinations([1,2,3], 2))
# [(1,2), (1,3), (2,3)]

# 🔹 핵심
# 순서 X
# nCr
# 👉 (1,2) == (2,1)

# 🔹 언제 쓰냐
# 팀 구성
# 추천 후보 생성
# 부분 집합

# 🔷 3. product (데카르트 곱)
# 👉 itertools.product
# 🔹 정의

# “모든 조합 (중복 허용)”

# 🔹 예제
from itertools import product

list(product([1,2], repeat=2))
# [(1,1), (1,2), (2,1), (2,2)]

# 🔹 핵심
# 중복 O
# 모든 경우 생성

# 🔹 언제 쓰냐
# 전체 경우 탐색
# 테스트 케이스 생성
# 좌표 생성

# 🔷 4. groupby
# 👉 itertools.groupby
# 🔹 정의

# “연속된 데이터를 그룹으로 묶음”

# 🔹 예제
from itertools import groupby

data = [1,1,2,2,3]

for key, group in groupby(data):
    print(key, list(group))

# 👉 결과

# 1 [1,1]
# 2 [2,2]
# 3 [3]

# 🔹 핵심 (🔥 중요)
# 👉 반드시 정렬 필요
data = sorted(data)

# 🔹 특징
# SQL GROUP BY ❌
# “연속된 것만 묶음”

# 🔹 언제 쓰냐
# 로그 압축
# 연속 데이터 처리

# 🔷 5. accumulate
# 👉 itertools.accumulate

# 🔹 정의
# “누적 계산”

# 🔹 예제
from itertools import accumulate

list(accumulate([1,2,3,4]))
# [1,3,6,10]

# 🔹 핵심
# prefix sum

# 🔹 커스터마이징
import operator
list(accumulate([1,2,3], operator.mul))
# [1,2,6]

# 🔹 언제 쓰냐
# 누적 합
# 통계 계산
# 로그 집계

# 🔷 6. chain
# 👉 itertools.chain

# 🔹 정의
# “여러 iterable을 하나로 연결”

# 🔹 예제
from itertools import chain
from itertools import chain

list(chain([1,2], [3,4]))
# [1,2,3,4]

# 🔹 핵심
# flatten 느낌
# 메모리 효율적

# 🔹 언제 쓰냐
# 리스트 합치기
# 스트림 처리

# 🔥 핵심 비교 정리 (진짜 중요)
# 함수	특징	핵심
# permutations	순서 O	nPr
# combinations	순서 X	nCr
# product	중복 O	모든 경우
# groupby	연속 그룹	정렬 필요
# accumulate	누적	prefix sum
# chain	연결	flatten

# 🔥 면접 한 줄 요약
# “itertools는 반복 데이터를 효율적으로 처리하기 위한 라이브러리로, permutations, combinations 등을 통해 경우의 수를 생성하고, accumulate와 groupby를 통해 데이터 집계 및 그룹화를 수행할 수 있습니다.”

# 🎯 너 기준 핵심 포인트
# 특히 중요:
# combinations → 추천 시스템
# product → 전체 경우 탐색
# groupby → 로그/데이터 묶기
# accumulate → 통계/누적값
# chain → 데이터 스트림 처리

# 👉 핵심
# “데이터 조작 + 경우의 수 + 성능 최적화”