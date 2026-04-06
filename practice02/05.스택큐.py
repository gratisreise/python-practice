# 스택과 큐는 데이터를 넣고 빼는 방식이 정해진 구조다.
#파이썬에서는 보통 **collections.deque**로 구현한다.

from collections import deque

dq = deque()

#스택 append() + pop()
stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())  # 3
print(stack.pop())  # 2

#큐 append() + popleft()
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())  # 1
print(queue.popleft())  # 2

# 양쪽 삽입 / 삭제
dq = deque([1, 2, 3])

dq.appendleft(0)   # 왼쪽 추가
dq.append(4)       # 오른쪽 추가

dq.popleft()       # 왼쪽 제거
dq.pop()           # 오른쪽 제거

# 왜 deque 쓰냐?
arr = [1, 2, 3]
arr.pop(0)  # ❌ 느림 (O(n))
