# ✅ 1. datetime vs timestamp
# 🔹 개념
# datetime.datetime

# 👉 사람이 읽는 시간

# 2026-05-03 12:00:00
# timestamp (Unix time)

# 👉 기준: Unix Epoch

# 1714700000  # 초 단위 숫자

# 🔹 변환 (🔥 필수)
# datetime → timestamp
from datetime import datetime

dt = datetime.now()
ts = dt.timestamp()

# timestamp → datetime
datetime.fromtimestamp(ts)     # local

# 🔹 핵심 차이
# 구분	datetime	timestamp
# 형태	객체	숫자
# 가독성	좋음	나쁨
# 연산	직관적	빠름
# 저장	비효율	효율

# 🔹 실무 규칙 (🔥 중요)
# 👉 DB 저장
# timestamp (UTC)

# 👉 API 응답
# ISO datetime

# 👉 핵심
# “저장은 timestamp, 보여줄 때 datetime”

# ✅ 2. strftime / strptime (깊게)
# 🔹 datetime.strftime
# 👉 datetime → 문자열
datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🔹 datetime.strptime
# 👉 문자열 → datetime
datetime.strptime("2026-05-03", "%Y-%m-%d")

# 🔹 포맷 핵심 (암기)
# 코드	의미
# %Y	4자리 년
# %m	월
# %d	일
# %H	시
# %M	분
# %S	초

# 🔹 실무 포인트
# 🔥 API 파싱
dt = datetime.strptime(request_time, "%Y-%m-%dT%H:%M:%S")

# 🔥 로그 포맷
log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🔹 주의
# 👉 포맷 안 맞으면 바로 에러
# 👉 핵심
# “입력 형식 정확히 맞춰야 한다”

# ✅ 3. timedelta 심화
# 🔹 datetime.timedelta
# 👉 시간 연산 전용 객체

# 🔹 기본
from datetime import timedelta

timedelta(days=1)
timedelta(hours=2)
timedelta(minutes=30)

# 🔹 연산
now + timedelta(days=1)
now - timedelta(hours=3)

# 🔹 비교
if now > expire_time:
    print("만료")

# 🔹 실무 핵심
# 🔥 TTL 처리
expire = now + timedelta(minutes=30)

# 🔥 기간 계산
# diff = end - start
# diff.days
# diff.seconds

# 🔥 sliding window
if now - event_time < timedelta(minutes=5):
    print("유효")
# 🔹 핵심 포인트

# 👉 datetime끼리 빼면 timedelta 나옴

# 👉 핵심

# “시간 연산은 무조건 timedelta”

# ✅ 4. timezone (🔥 실무 핵심)
# 이거 제대로 모르면 서비스 터진다.

# 🔹 naive vs aware
# naive
datetime.now()

# 👉 시간대 없음

# aware
# from datetime import timezone

# datetime.now(timezone.utc)

# 👉 시간대 포함

# 🔹 왜 중요하냐

# 👉 서버 / 사용자 / DB 시간 다 다름

# 🔹 핵심 규칙 (🔥 필수 암기)

# ✅ 서버 저장 = UTC
# ✅ DB 저장 = UTC
# ❌ local time 저장 금지

# 🔹 변환
from datetime import timezone

dt_utc = datetime.now(timezone.utc)
dt_local = dt_utc.astimezone()

# 🔹 실무 패턴
# 🔥 API 응답
datetime.now(timezone.utc).isoformat()
# 🔥 파싱
datetime.fromisoformat("2026-05-03T12:00:00+00:00")

# 🔹 핵심 요약
# 개념	의미
# naive	timezone 없음
# aware	timezone 있음
# UTC	표준 시간
# local	사용자 시간

# 👉 핵심
# “시간은 항상 UTC 기준으로 다뤄라”
# 🔥 최종 핵심 요약 (면접용)

# “datetime은 사람이 읽기 위한 시간 표현이고 timestamp는 저장을 위한 숫자형 시간입니다. 시간 연산은 timedelta를 사용하며, 문자열 변환은 strftime/strptime으로 처리합니다. 실무에서는 timezone 문제를 방지하기 위해 UTC 기반의 aware datetime을 사용하는 것이 중요합니다.”

# 🎯 너 기준 핵심 포인트

# 진짜 중요한 것만:

# timestamp ↔ datetime 변환
# strptime (API 파싱)
# timedelta (TTL / 만료)
# timezone (UTC 강제)

# 👉 특히

# “timezone 모르면 장애 난다”