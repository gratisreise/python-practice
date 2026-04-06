# 힙은 가장 작은 값(또는 큰 값)을 빠르게 꺼내기 위한 자료구조다.


import heapq

heap = []

# 값 추가(push)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heap)  # [1, 3, 2]

# 값 꺼내기
print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 2
print(heapq.heappop(heap))  # 3

# 최소값 확인(pop 없이)
heap[0]


# 최대 힙 만들기: 음수 트릭을 사용한다.
heap = []

heapq.heappush(heap, -3)
heapq.heappush(heap, -1)
heapq.heappush(heap, -2)

print(-heapq.heappop(heap))  # 3


# 한번에 힙 만들기 
arr = [3, 1, 2]

heapq.heapify(arr)

print(arr)  # [1, 3, 2]

# 우선순위큐 
import heapq

heap = []

heapq.heappush(heap, (1, "작업A"))
heapq.heappush(heap, (3, "작업C"))
heapq.heappush(heap, (2, "작업B"))

print(heapq.heappop(heap))  # (1, "작업A")


# k번째 작은 값
import heapq

arr = [5, 1, 9, 3]

heapq.heapify(arr)

for _ in range(k-1):
    heapq.heappop(arr)

print(heapq.heappop(arr))