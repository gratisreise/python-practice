# ✅ 5단계: OrderedDict
# 🔹 1. OrderedDict란?

# collections.OrderedDict

# 👉 한 줄 정의
# “입력 순서를 유지하는 dict”

# 🔹 2. 근데 잠깐 (중요 포인트)
# 👉 Python 3.7+ 기준
# 일반 dict도 순서 유지함

d = {"a":1, "b":2, "c":3}
print(d)  # 순서 유지됨

# 👉 그래서 결론
# “요즘은 그냥 dict 써도 된다”

# 🔹 3. 그럼 왜 OrderedDict 쓰냐?
# 👉 차이점은 “기능”

# 🔹 4. 핵심 기능 (🔥 중요)
# 1️⃣ 순서 변경 가능
OrderedDict.move_to_end
from collections import OrderedDict

od = OrderedDict([("a",1), ("b",2), ("c",3)])

od.move_to_end("a")
# a가 뒤로 이동

# 2️⃣ 마지막/처음 제거
# OrderedDict.popitem
od.popitem()         # 마지막 제거
od.popitem(last=False)  # 처음 제거

# 👉 핵심

# “순서를 제어할 수 있다”

# 🔹 5. 실무 핵심 활용 (🔥 중요)
# 🔥 1. LRU Cache 구현
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# 👉 핵심
# 최근 사용 → 뒤로 이동
# 오래된 것 → 앞에서 제거

# 🔥 2. 순서 기반 로직
# 최근 요청 처리
# 캐시 eviction 정책
# 이벤트 순서 유지

# 🔹 6. dict vs OrderedDict
# 구분	dict	OrderedDict
# 순서 유지	✅	✅
# 순서 변경	❌	✅
# popitem 제어	❌	✅
# 추천	일반	특수 상황

# 🔹 7. 성능
# dict보다 약간 느림
# 대신 기능 제공

# 🔹 8. 면접용 한 줄
# “OrderedDict는 삽입 순서를 유지하면서 순서를 변경하거나 제어할 수 있는 dict로, LRU 캐시와 같은 순서 기반 로직에서 사용됩니다.”

# 🔹 9. 너 기준 핵심 포인트
# LRU Cache
# 캐시 eviction
# 순서 기반 데이터 처리

# 👉 특히
# “캐시 정책 구현할 때 핵심”