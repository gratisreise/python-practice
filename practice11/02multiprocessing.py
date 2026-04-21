# 1. multiprocessing이란?

# multiprocessing은
# 프로세스를 여러 개 만들어서 작업을 병렬로 처리하는 방식이다.

# 프로세스 1 (메모리 독립)
# 프로세스 2 (메모리 독립)
# 프로세스 3 (메모리 독립)

# 👉 각각 완전히 별개라서 진짜 병렬 처리 가능

# 2. 왜 필요한가?

# 파이썬에는
# Global Interpreter Lock 이 있어서

# threading → CPU 병렬 처리 ❌
# multiprocessing → CPU 병렬 처리 ⭕

# 👉 그래서 CPU 많이 쓰는 작업은 무조건 multiprocessing이다

# 3. 언제 쓰는가?

# 👉 CPU 연산-heavy 작업

# 예시:

# 이미지 처리
# 데이터 분석
# AI 계산
# 대량 수학 연산
# 4. 기본 예제
from multiprocessing import Process

def task():
    print("프로세스 실행")

p = Process(target=task)

p.start()
p.join()

# 5. 실행 흐름
# 1. Process 객체 생성
# 2. start() → 새로운 프로세스 생성
# 3. task 함수 실행
# 4. join() → 프로세스 종료까지 대기

# 6. threading vs multiprocessing 핵심 차이
# 구분	threading	multiprocessing
# 실행 단위	스레드	프로세스
# 메모리	공유	독립
# 속도	가벼움	무거움
# 병렬 처리	❌ (GIL)	⭕
# 사용 목적	I/O	CPU

# 7. 중요한 포인트 (실무)
# 1) 메모리 공유 안됨
# # 안됨
# global_var = 0

# 👉 프로세스끼리는 값 공유 안된다

# 2) 값 공유하려면?
from multiprocessing import Value

counter = Value('i', 0)

# 또는

from multiprocessing import Queue

# 👉 IPC(프로세스 간 통신) 필요

# 3) main 필수
if __name__ == "__main__":
# 👉 이거 안 쓰면 무한 프로세스 생성됨 (특히 Windows)

# 핵심 정리
# multiprocessing = 여러 프로세스로 진짜 병렬 처리
# CPU 작업에 사용
# 메모리 공유 안됨 → IPC 필요
# threading보다 무겁지만 강력함