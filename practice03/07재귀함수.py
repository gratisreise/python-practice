# 재귀 함수란 👉 자기 자신을 호출하는 함수
# def 함수():
#     함수()  # 자기 자신 호출

# 2. 왜 쓰는가?

# 👉 반복문으로도 가능하지만
# 👉 문제를 더 “구조적으로” 표현할 수 있음

# 대표 예:

# 팩토리얼
# 트리 탐색
# DFS
# 종료 조건(base case)이 반드시 있어야 한다

# 팩토리열
def factorial(n):
    if n == 1:          # 종료 조건
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# factorial(5)
# → 5 * factorial(4)
# → 5 * 4 * factorial(3)
# → 5 * 4 * 3 * factorial(2)
# → 5 * 4 * 3 * 2 * factorial(1)
# → 5 * 4 * 3 * 2 * 1

