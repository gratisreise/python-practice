# 11-4. concurrent.futures
# 1. 이게 뭐냐?

# concurrent.futures는

# 👉 threading / multiprocessing을 쉽게 쓰게 해주는 추상화 API

# 직접 Thread / Process 관리 ❌
# → Executor가 대신 관리 ⭕
# 2. 핵심 구조
# Executor
#  ├─ ThreadPoolExecutor  → 스레드 기반
#  └─ ProcessPoolExecutor → 프로세스 기반
# 3. ThreadPoolExecutor

# 👉 I/O 작업용

# 예제
from concurrent.futures import ThreadPoolExecutor

def task(x):
    return x * 2

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4])

# print(list(results))
# 4. ProcessPoolExecutor

# 👉 CPU 작업용

# 예제
from concurrent.futures import ProcessPoolExecutor

def task(x):
    return x * x

with ProcessPoolExecutor() as executor:
    results = executor.map(task, [1, 2, 3, 4])

print(list(results))

# 5. submit vs map
# map (간단한 경우)
executor.map(task, data)
# 👉 순서 보장
# 👉 간단

# submit (고급)
future = executor.submit(task, 10)
print(future.result())
# 👉 개별 작업 컨트롤 가능
# 👉 비동기 결과 처리 가능

# 6. Future 객체 (핵심)
# future = executor.submit(task, 10)
# 👉 미래에 결과가 나올 객체

# future.result()
# 👉 결과 가져오기 (blocking)

# 7. asyncio랑 같이 쓰는 핵심 패턴 (🔥 중요)
# 이거 실무 핵심이다.
# 👉 async 코드 안에서 blocking 코드 실행할 때

import asyncio
from concurrent.futures import ThreadPoolExecutor

def blocking_task():
    import time
    time.sleep(2)
    return "done"

async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_task)

    print(result)

# asyncio.run(main())
# 왜 필요하냐?
# asyncio = 비동기 I/O 잘함
# BUT
# blocking 코드 만나면 전체 멈춤

# 👉 해결:

# blocking 코드 → ThreadPoolExecutor로 분리
# 8. 언제 쓰는가 (실무 기준)
# 외부 라이브러리가 async 지원 안함
# → executor 사용

# CPU 작업
# → ProcessPoolExecutor

# 간단한 병렬 처리
# → ThreadPoolExecutor
# 최종 정리 (이 파트 핵심)
# threading        → I/O
# multiprocessing  → CPU
# asyncio          → 고성능 I/O (핵심)
# concurrent.futures → 위 3개 쉽게 쓰는 도구
# 면접 한 방 정리
# concurrent.futures는 ThreadPoolExecutor와 ProcessPoolExecutor를 통해
# 멀티스레딩과 멀티프로세싱을 추상화하여 쉽게 병렬 처리를 구현할 수 있게 해주는 라이브러리입니다.