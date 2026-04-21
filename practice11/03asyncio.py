# 1. asyncio란?

# asyncio는
# 이벤트 루프 기반 비동기 처리 방식이다.

# 👉 스레드/프로세스 없이
# 👉 한 개의 스레드로 수천 개 작업을 처리

# 2. 핵심 개념 (중요)
# 동기(sync)
# → 하나 끝나야 다음 실행

# 비동기(async)
# → 기다리는 동안 다른 작업 실행
# 3. 동기 vs 비동기 비교
# ❌ 동기 코드
# import time

# def task():
#     time.sleep(1)
#     print("끝")

# task()
# task()
# task()

# 👉 3초 걸림

# ✅ 비동기 코드
import asyncio

async def task():
    await asyncio.sleep(1)
    print("끝")

async def main():
    await asyncio.gather(
        task(),
        task(),
        task()
    )

asyncio.run(main())

# 👉 1초 걸림 (동시에 처리)

# 4. async / await 의미
# async
# async def task():

# 👉 이 함수는 코루틴 (coroutine) 이다

# await
# await something()

# 👉 기다리는 동안
# 👉 다른 작업 실행 가능

# 5. 이벤트 루프 (핵심 개념)
# [이벤트 루프]
#  ├─ task1 실행
#  ├─ await 만나면 → 잠시 멈춤
#  ├─ task2 실행
#  ├─ task3 실행
#  └─ 다시 돌아와서 이어서 실행

# 👉 CPU를 낭비하지 않고 계속 돌린다

# 6. 언제 쓰는가?

# 👉 I/O 작업 + 고성능 서버

# 예시:

# API 서버 (예: FastAPI)
# 웹 크롤링
# DB 요청
# LLM API 호출 (Gemini, GPT 등)
# 7. threading vs asyncio 차이
# 구분	threading	asyncio
# 방식	여러 스레드	이벤트 루프
# 비용	높음	낮음
# 성능	중간	매우 높음
# 사용	일반 I/O	대량 I/O
# 8. 중요한 실수 포인트 (실무 핵심)
# ❌ blocking 코드 쓰면 의미 없음
import time

async def task():
    time.sleep(1)  # ❌ async 의미 없음

# 👉 반드시 비동기 함수 써야 한다

# await asyncio.sleep(1)  # ⭕
# ❌ await 안 쓰면 실행 안됨
# task()  # ❌ 그냥 객체

# 👉 반드시

# await task()
# 9. gather (동시 실행 핵심)
# await asyncio.gather(
#     task1(),
#     task2(),
#     task3()
# )

# 👉 여러 작업을 동시에 실행

# 핵심 정리 (면접용 한 줄)
# asyncio는 이벤트 루프 기반 비동기 처리 방식으로,
# I/O 작업에서 높은 동시성을 확보하기 위해 사용됩니다.
# 너 기준 (백엔드 관점 핵심)

# 너가 하는 것들 기준으로 보면:

# Gemini API 호출
# → asyncio

# 외부 API 연동
# → asyncio

# SSE / 스트리밍
# → asyncio

# FastAPI
# → asyncio 기반

# 👉 결론:
# “요즘 백엔드는 threading보다 asyncio가 기본이다”