# 1. 이게 뭐냐?
if __name__ == "__main__":
    print("실행됨")

# 👉 의미:
# “이 파일을 직접 실행했을 때만 실행해라”

# 2. 핵심 개념: __name__
# 파이썬 파일은 실행 방식에 따라 __name__ 값이 달라진다.

# (1) 직접 실행하면
# python main.py
# __name__ == "__main__"

# (2) import 되면
# import main
# __name__ == "main"
# 👉 파일 이름이 들어간다

# 3. 왜 필요하냐?
# 이거 없으면 문제 생긴다.

# ❌ 문제 상황
# calculator.py
def add(a, b):
    return a + b

print("테스트 코드 실행")

# main.py
import calculator

# 👉 결과:
# 테스트 코드 실행

# ❗ import 했는데도 실행됨 → 문제

# 4. 해결 방법
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("테스트 코드 실행")

# main.py
import calculator

# 👉 결과:
# (아무것도 안 나옴)

# 5. 직접 실행하면?
# python calculator.py

# 👉 결과:
# 테스트 코드 실행

# 6. 정리하면
# 상황	name 값	실행 여부
# 직접 실행	"main"	실행됨
# import	파일이름	실행 안됨

# 7. 언제 쓰냐? (실무 기준)
# 1) 테스트 코드
# if __name__ == "__main__":
#     print(add(1, 2))

# 2) 실행 진입점 (entry point)
# def main():
#     print("프로그램 시작")
# if __name__ == "__main__":
#     main()
# 👉 Java의 main() 느낌

# 8. 실무 감각 포인트 (중요)
# 👉 “이 파일이 라이브러리냐? 실행 파일이냐?”
# 라이브러리 → import만 됨
# 실행 파일 → 직접 실행됨
# 이걸 분리하는 장치가:

# 👉 if __name__ == "__main__"

# 9. 자주 하는 실수
# ❌ 테스트 코드 그냥 위에 작성
# print(add(1, 2))

# 👉 import하면 같이 실행됨 (문제)
# ❌ main 함수 안 만들고 난잡하게 작성

# 👉 유지보수 힘들어짐
# 10. 정리
# __name__은 파일의 실행 상태를 나타냄
# "__main__"이면 직접 실행된 것
# import될 때는 실행되지 않게 막는 용도