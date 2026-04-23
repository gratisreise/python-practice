# 3️⃣ pandas (🔥 핵심)

# 👉 “데이터 처리 = pandas”라고 보면 됨

# 핵심 구조
# DataFrame (테이블)
# Series (컬럼)
# 기본 사용
import pandas as pd

df = pd.DataFrame({
    "name": ["kim", "lee"],
    "age": [30, 25]
})

print(df)

# CSV 읽기
df = pd.read_csv("data.csv")

# 주요 기능
df.head()        # 상위 데이터
df.describe()    # 통계
df["age"]        # 컬럼 선택
df[df["age"] > 20]  # 조건 필터

# 컬럼 추가
df["age_plus"] = df["age"] + 1

# 그룹화 (🔥 중요)
df.groupby("name")["age"].mean()

# 실무 포인트 (너랑 연결)
# 로그 분석
# 추천 데이터 전처리
# Batch 작업 (Spring Batch 느낌으로 데이터 처리)