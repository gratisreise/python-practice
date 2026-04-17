# 1️⃣ Python 메모리 관리 개요

# 👉 한 줄 정의

# “Python은 Reference Counting + Garbage Collection으로 메모리를 관리한다”

# 2️⃣ Reference Counting (핵심)
# ✔ 개념

# 👉 객체가 몇 개의 변수에서 참조되는지 카운트

# a = [1, 2, 3]  # 참조 수 1
# b = a          # 참조 수 2

# 👉 내부 상태

# [1,2,3] → ref_count = 2
# ✔ 참조 감소
# del a

# 👉

# ref_count = 1
# ✔ 0이 되는 순간
# del b

# 👉

# ref_count = 0 → 즉시 메모리 해제
# ✔ 특징
# 매우 빠름 (즉시 해제)
# 구현 단순
# 대부분의 객체 처리 담당
# 3️⃣ 문제: 순환 참조 (🔥 중요)

# 이게 핵심 문제다

# a = []
# b = []

# a.append(b)
# b.append(a)

# 👉 구조

# a → b
# b → a

# 👉 결과

# ref_count = 1 (서로 참조)

# 👉 하지만 실제로는 아무도 안 씀

# 👉 ❗ 메모리 해제 안 됨 (메모리 누수)

# 4️⃣ Garbage Collector (GC)

# 👉 이 문제 해결용

# 👉 Python은 GC도 같이 사용

# ✔ 역할

# 👉 순환 참조 탐지 후 제거

# ✔ 동작 방식 (간단)
# 객체 그래프 탐색
# 도달 불가능 객체 찾기
# 제거
# ✔ 자동 실행

# 👉 개발자가 직접 안 해도 됨

# 하지만 가능은 함:

# import gc
# gc.collect()
# 5️⃣ GIL과 연결 (🔥 중요)

# 이제 퍼즐 완성이다

# ✔ 왜 GIL이 필요한가?

# 👉 Reference Counting 때문

# ref_count += 1
# ref_count -= 1

# 👉 이게 여러 스레드에서 동시에 실행되면?

# 👉 ❗ 데이터 깨짐

# 그래서

# 👉 GIL = ref_count 보호용 락

# 6️⃣ 메모리 구조 (추가 이해)

# Python 메모리는 이렇게 나뉜다

# ✔ Stack
# 함수 호출
# 지역 변수
# ✔ Heap
# 객체 저장
# 리스트, dict 등

# 👉 Reference Counting은 Heap 객체 기준

# 7️⃣ 실무에서 중요한 포인트

# 너 기준으로 중요한 것만 뽑는다 👇

# ✔ 메모리 누수 원인
# 순환 참조
# 큰 객체 계속 유지
# ✔ 성능 이슈
# GC 타이밍 → 지연 발생 가능
# ✔ 객체 관리 전략
# 불필요한 참조 제거
# 큰 객체 scope 줄이기
# 8️⃣ 한 줄 면접 답변

# 👉
# “Python은 Reference Counting으로 대부분의 메모리를 즉시 해제하고, 순환 참조 문제는 Garbage Collector가 보완하는 구조이며, 이러한 참조 카운트의 안전성을 위해 GIL이 필요합니다.”