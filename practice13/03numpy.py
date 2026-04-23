# 4️⃣ numpy (🔥 성능 담당)

# 👉 “빠른 계산용 라이브러리”

# 기본
import numpy as np

arr = np.array([1, 2, 3])

# 연산
arr + 1
arr * 2

# 행렬
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

np.dot(a, b)

# 실무 포인트
# ML / AI 전처리
# 벡터 연산 (너 pgvector 쓰니까 감각 중요)
# pandas 내부도 numpy 기반