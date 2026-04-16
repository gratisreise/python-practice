# with open (핵심)
# "파일을 자동으로 닫아주는 안전한 방식"

# 1️⃣ 기본 구조
with open("test.txt", "r") as f:
    data = f.read()
    print(data)

# 2️⃣ 왜 쓰냐? (중요)
# 기존 방식:
f = open("test.txt", "r")
data = f.read()
f.close()

# 👉 문제
# close() 까먹으면?
# 에러 발생하면 close 안됨

# ✔️ with open의 장점
# 자동 close
# 예외 발생해도 안전
# 코드 더 깔끔
# 👉 그래서 실무에서는 무조건 with 사용

# 3️⃣ 읽기 예제
with open("test.txt", "r") as f:
    for line in f:
        print(line)
# 👉 실무에서 가장 많이 쓰    는 패턴

# 4️⃣ 쓰기 예제
with open("test.txt", "w") as f:
    f.write("Hello\n")
    f.write("World")
# 5️⃣ 추가 모드 예제
with open("test.txt", "a") as f:
    f.write("\n추가 내용")

# 7️⃣ 내부 동작 (조금 깊게)
with open(...) as f:

# 👉 사실은
# f = open(...)
# try:
#     ...
# finally:
#     f.close()

# 👉 이걸 자동으로 해주는 문법