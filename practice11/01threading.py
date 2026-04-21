# 1. threading이란?

# threading은 하나의 프로세스 안에서 여러 실행 흐름을 만드는 기능이다.

# 쉽게 말하면:

# 프로그램 1개
#  ├─ 스레드 1: 파일 읽기
#  ├─ 스레드 2: API 요청
#  └─ 스레드 3: 로그 출력

# 이렇게 여러 작업을 겹쳐서 실행할 수 있다.

# 2. 언제 쓰는가?

# threading은 주로 I/O 작업에 적합하다.

# 예를 들면:

# 네트워크 요청
# 파일 읽기/쓰기
# DB 요청
# 외부 API 호출
# 크롤링

# 이런 작업은 CPU가 계속 계산하는 게 아니라
# 응답을 기다리는 시간이 많다.

# 그래서 스레드를 쓰면 기다리는 동안 다른 작업을 처리할 수 있다.

# 3. 기본 예제
import threading

def task():
    print("작업 실행")

thread = threading.Thread(target=task)

thread.start()
thread.join()

print("메인 종료")

# 실행 흐름:

# 1. Thread 객체 생성
# 2. start() 호출 → 새 스레드에서 task 실행
# 3. join() 호출 → 스레드가 끝날 때까지 메인 스레드 대기
# 4. 메인 종료 출력
# 4. start()와 join()
# start()
# thread.start()

# 새 스레드를 시작한다.

# 주의할 점:

# thread.run()

# 이렇게 직접 호출하면 새 스레드가 아니라
# 그냥 일반 함수 호출처럼 실행된다.

# join()
# thread.join()

# 해당 스레드가 끝날 때까지 기다린다.

# join()이 없으면 메인 흐름이 먼저 끝날 수 있다.

# 핵심 정리
# threading = 하나의 프로세스 안에서 여러 작업 흐름을 만드는 것
# I/O 작업에 적합
# CPU 연산에는 적합하지 않음
# start() = 스레드 시작
# join() = 스레드 종료까지 대기