# ✅ 10. 표준 라이브러리 - itertools (1단계)
# 🔹 1. itertools란?

# itertools는
# “반복(iteration)을 효율적으로 처리하기 위한 도구 모음”

# 👉 한 줄 정의

# “메모리 낭비 없이, 조합/순열/반복 처리를 해주는 라이브러리”

# 🔹 2. 왜 쓰냐? (핵심)

# 일반 코드 vs itertools

# # 일반
# result = []
# for i in range(3):
#     for j in range(3):
#         result.append((i, j))

# # itertools
# from itertools import product
# result = list(product(range(3), range(3)))

# 👉 핵심 차이

# 코드 짧아짐
# 성능 좋음 (lazy evaluation)
# 의도 명확
# 🔹 3. 핵심 개념 (중요)
# ✅ Lazy Evaluation (지연 평가)
# from itertools import count

# c = count(1)
# print(next(c))  # 1
# print(next(c))  # 2

# 👉 특징

# 미리 다 만들지 않음
# 필요할 때 하나씩 생성

# 👉 한 줄 정의

# “필요한 순간에만 값을 만드는 방식”

# 🔹 4. itertools 핵심 3분류
# 1️⃣ 무한 반복
# itertools.count
# itertools.cycle
# itertools.repeat

# 👉 특징: 끝 없음 (주의해서 사용)

# 2️⃣ 조합/순열 (🔥 핵심)
# itertools.permutations
# itertools.combinations
# itertools.product

# 👉 이건 코테 + 백엔드 로직에서 자주 등장

# 3️⃣ 데이터 처리
# itertools.groupby
# itertools.accumulate
# itertools.chain
# 🔹 5. 백엔드 관점 연결

# 너 기준으로 보면:

# 🔥 실제 쓰는 포인트
# combinations → 추천 시스템 후보 생성
# product → 모든 경우의 수 테스트
# groupby → 데이터 그룹핑 (SQL group by 느낌)
# chain → 여러 리스트 합치기
# accumulate → 누적값 (통계, 로그)
# 🔹 6. 핵심 요약 (면접용)

# 👉 한 줄 답변

# “itertools는 반복 처리를 효율적으로 수행하기 위한 라이브러리로, 지연 평가를 통해 메모리를 절약하면서 조합, 순열, 그룹핑 등의 연산을 간결하게 처리할 수 있습니다.”