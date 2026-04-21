# ✅ 3단계: deque
# 🔹 1. deque란?

# collections.deque

# 👉 한 줄 정의

# “양쪽에서 빠르게 삽입/삭제 가능한 큐 자료구조”
# (deque = double-ended queue)

# 🔹 2. 왜 쓰냐?
# ❌ list의 문제
lst = [1,2,3]
lst.insert(0, 0)   # 느림 (O(n))
lst.pop(0)         # 느림 (O(n))
# 👉 앞에서 작업하면 전체 이동 발생

# ✅ deque
from collections import deque

dq = deque([1,2,3])
dq.appendleft(0)   # 빠름 (O(1))
dq.popleft()       # 빠름 (O(1))

# 👉 핵심
# “앞/뒤 작업 모두 O(1)”

# 🔹 3. 기본 사용
from collections import deque

dq = deque([1,2,3])

dq.append(4)       # 오른쪽 추가
dq.appendleft(0)   # 왼쪽 추가

dq.pop()           # 오른쪽 제거
dq.popleft()       # 왼쪽 제거

# 🔹 4. 핵심 기능 (🔥 중요)
# 1️⃣ 양쪽 삽입/삭제
# 기능	메서드
# 오른쪽 추가	append
# 왼쪽 추가	appendleft
# 오른쪽 제거	pop
# 왼쪽 제거	popleft

# 2️⃣ 회전 (rotate)
dq = deque([1,2,3,4])
dq.rotate(1)
# [4,1,2,3]
# 👉 오른쪽으로 밀기

# 3️⃣ 최대 길이 제한 (🔥 실무)
dq = deque(maxlen=3)

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)

# print(dq)  # [2,3,4]

# 👉 자동으로 오래된 값 제거

# 🔹 5. 실무에서 진짜 쓰는 패턴
# 🔥 1. 큐 (FIFO)
dq = deque()

dq.append("task1")
dq.append("task2")

dq.popleft()  # task1
# 👉 작업 처리 / 이벤트 큐

# 🔥 2. 스택 (LIFO)
dq = deque()

dq.append(1)
dq.append(2)

dq.pop()  # 2

# 🔥 3. Sliding Window (★★★★★)
dq = deque(maxlen=3)

for i in [1,2,3,4,5]:
    dq.append(i)
    print(list(dq))
# 👉 최근 N개 유지

# 🔥 4. BFS (알고리즘 핵심)
from collections import deque

queue = deque([start])

while queue:
    node = queue.popleft()

# 🔹 6. 성능 비교 (중요)
# 작업	list	deque
# append	O(1)	O(1)
# pop	O(1)	  O(1)
# insert(0)	O(n) 	O(1)
# pop(0)	O(n) 	O(1)

# 👉 핵심
# “앞에서 작업하면 무조건 deque”

# 🔹 7. 주의할 점
# 중간 인덱스 접근은 list가 더 빠름 => 랜덤액세스가 가능 하니깐
# deque는 순차 처리용

# 🔹 8. 면접용 한 줄
# “deque는 양쪽 끝에서 O(1)로 삽입과 삭제가 가능한 자료구조로, 큐, 스택, sliding window 등의 상황에서 list보다 효율적으로 사용할 수 있습니다.”

# 🔹 9. 너 기준 핵심 포인트
# Redis Queue 개념 이해
# 이벤트 처리 구조
# Sliding Window (로그/트래픽)
# 비동기 큐 구조

# 👉 특히
# “실시간 데이터 흐름 처리에 핵심”