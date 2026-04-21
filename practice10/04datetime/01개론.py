# ✅ 10. 표준 라이브러리 - datetime (1단계)
# 🔹 1. datetime이란?

# datetime은
# 날짜 + 시간 + 시간 연산을 다루는 핵심 라이브러리

# 👉 한 줄 정의

# “시간을 생성하고, 계산하고, 포맷하는 도구”

# 🔹 2. 왜 중요하냐? (백엔드 핵심)

# 너 기준으로 보면 거의 필수다:

# 로그 시간 기록
# API 응답 timestamp
# 예약/스케줄링
# TTL / 만료 처리
# 통계 (일/주/월 집계)

# 👉 즉

# “시간 못 다루면 백엔드 못 한다”

# 🔹 3. 핵심 구성 4개
# 1️⃣ datetime.datetime
# 👉 날짜 + 시간

from datetime import datetime

now = datetime.now()
print(now)  # 2026-05-03 12:00:00

# 2️⃣ datetime.date
# 👉 날짜만

from datetime import date

today = date.today()
print(today)  # 2026-05-03

# 3️⃣ datetime.time
# 👉 시간만

from datetime import time

t = time(14, 30)
print(t)  # 14:30:00

# 4️⃣ datetime.timedelta
# 👉 시간 계산 (🔥 중요)

from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=1)

print(future)

# 👉 핵심
# “시간 연산은 timedelta로 한다”

# 🔹 4. 핵심 기능 (실무 필수)
# ✅ 현재 시간
datetime.now()
datetime.utcnow()

# ✅ 문자열 ↔ 날짜 변환 (🔥 중요)
# 1. 문자열 → datetime
# datetime.strptime
dt = datetime.strptime("2026-05-03", "%Y-%m-%d")
# 2. datetime → 문자열
# datetime.strftime
s = datetime.now().strftime("%Y-%m-%d")

# 🔹 5. 포맷 코드 (암기 핵심)
# 코드	의미
# %Y	년도
# %m	월
# %d	일
# %H	시
# %M	분
# %S	초

# 🔹 6. 백엔드 실무 포인트 (🔥 중요)
# 🔥 1. 만료 시간 처리
expire_at = datetime.now() + timedelta(minutes=30)

# 👉 JWT / 세션 TTL

# 🔥 2. 시간 비교
if datetime.now() > expire_at:
    print("만료")

# 🔥 3. 로그 포맷
log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🔥 4. UTC vs Local (중요)

# 👉 실무 규칙
# “서버는 UTC, 클라이언트에서 변환”

# 🔹 7. 핵심 요약 (면접용)
# 👉 한 줄 답변

# “datetime은 날짜와 시간을 표현하고 연산하기 위한 라이브러리로, timedelta를 활용한 시간 계산과 strftime/strptime을 통한 포맷 변환이 핵심입니다.”