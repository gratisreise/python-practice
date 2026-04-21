# ✅ 10. 표준 라이브러리 - collections (1단계)
# 🔹 1. collections란?

# collections는
# 기본 자료구조(list, dict, set)를 “확장/보완”한 라이브러리

# 👉 한 줄 정의

# “더 효율적이고, 더 의도가 명확한 자료구조 모음”

# 🔹 2. 왜 쓰냐? (핵심 포인트)

# 기본 자료구조는 한계가 있음

# 문제	해결
# dict 초기값 처리 귀찮음	defaultdict
# key 카운팅 직접 해야함	Counter
# 양쪽 삽입 느림(list)	deque
# 튜플인데 이름 없음	namedtuple

# 👉 즉

# “코드 줄이고 + 성능 + 가독성 개선”

# 🔹 3. 주요 구성 (오늘 전체 맵만 잡자)

# collections 핵심 5개:

# collections.Counter
# collections.defaultdict
# collections.deque
# collections.namedtuple
# collections.OrderedDict
# 🔹 4. 언제 뭐 쓰는지 감 잡기 (중요)
# 상황	쓰는 것
# 개수 세기	Counter
# key 없을 때 자동 생성	defaultdict
# 큐/스택	deque
# 구조체 느낌	namedtuple
# 순서 유지 dict	OrderedDict
# 🔹 5. 백엔드 관점 연결 (중요)

# 너 기준으로 보면:

# Counter → 로그 집계 / 트래픽 카운트
# defaultdict → 그룹핑 (ex. 유저별 데이터)
# deque → 이벤트 큐 / BFS / 작업 처리
# namedtuple → DTO 간단 버전
# OrderedDict → 캐시 정책 (LRU)

# 👉 실무 포인트

# “자료구조 선택 = 성능 + 코드 품질”