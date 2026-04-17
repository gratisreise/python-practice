# 1️⃣ Global Interpreter Lock (GIL)

# 👉 한 줄 정의

# “한 번에 하나의 스레드만 Python 바이트코드를 실행하도록 막는 락”

# 2️⃣ 왜 존재하는가?

# 결론부터 말하면 👇

# 👉 메모리 관리 쉽게 하려고

# Python은 내부적으로
# 👉 Reference Counting (참조 카운트) 사용

# 이게 문제다 👇

# 객체 A 참조 수 += 1
# 객체 A 참조 수 -= 1

# 👉 멀티스레드에서 동시에 접근하면?

# 👉 race condition 발생 (데이터 깨짐)

# 그래서 해결책

# 👉 “그냥 한 번에 하나만 실행하자” → GIL

# 3️⃣ 동작 방식
# Thread 1  ─── 실행
# Thread 2  ─── 대기
# Thread 3  ─── 대기

# 👉 일정 시간 지나면

# Thread 2 실행
# Thread 1 대기

# 👉 즉

# 👉 멀티스레드지만 실제론 싱글스레드처럼 동작

# 4️⃣ 중요한 오해 (이거 틀리면 안됨)

# ❌ “Python은 멀티스레드가 안 된다”
# 👉 틀림

# ✔ I/O 작업에서는 잘 동작

# 왜?

# 👉 GIL은 이런 상황에서 풀린다

# 파일 읽기
# 네트워크 요청
# DB 호출

# 👉 즉

# 👉 I/O 대기 동안 다른 스레드 실행 가능

# 5️⃣ 언제 문제냐 (핵심)
# ❗ CPU-bound 작업
# for i in range(100000000):
#     x += i

# 👉 이런 거

# 👉 스레드 10개 써도 의미 없음

# 👉 GIL 때문에 하나씩 실행

# 6️⃣ 해결 방법
# ✔ 1. 멀티프로세싱
# from multiprocessing import Process

# 👉 프로세스는 GIL 공유 안 함

# 👉 진짜 병렬 가능

# ✔ 2. C 확장 사용
# numpy
# pandas

# 👉 내부는 C → GIL 우회

# ✔ 3. asyncio (I/O 최적화)

# 👉 비동기 처리

# 7️⃣ 실무 감각으로 정리

# 너 기준으로 이렇게 이해하면 된다 👇

# ✔ API 서버
# I/O 많음 → GIL 문제 거의 없음
# ✔ 데이터 처리 / 연산
# CPU-bound → GIL 병목 발생
# 8️⃣ 한 줄 면접 답변

# 👉
# “Python의 GIL은 메모리 관리를 단순화하기 위해 한 번에 하나의 스레드만 바이트코드를 실행하도록 제한하는 락이며, CPU-bound 작업에서는 병목이 되지만 I/O 작업에서는 큰 문제가 되지 않습니다.”

# 9️⃣ 너 수준에서 가져가야 할 포인트
# 왜 GIL이 존재하는지 (reference counting 때문)
# 언제 문제 되는지 (CPU-bound)
# 언제 괜찮은지 (I/O-bound)
# 어떻게 해결하는지 (multiprocessing / async / C 확장)