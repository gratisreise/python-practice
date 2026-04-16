# 1️⃣ 파일 열기 기본 구조
f = open("파일경로", "모드")
# 모드 종류
# "r" → 읽기 (기본값)
# "w" → 쓰기 (기존 내용 삭제)
# "a" → 추가 (뒤에 이어쓰기)

# 2️⃣ 파일 읽기
# (1) 전체 읽기
f = open("test.txt", "r")

data = f.read()
print(data)

f.close()

# 👉 파일 전체를 문자열로 가져옴
# (2) 한 줄씩 읽기
f = open("test.txt", "r")

line = f.readline()
print(line)

f.close()

# 👉 한 줄만 읽음
# (3) 여러 줄 리스트로 읽기
f = open("test.txt", "r")

lines = f.readlines()
print(lines)

f.close()

# 👉 결과: 리스트 형태

["첫줄\n", "둘째줄\n"]

# (4) 반복문으로 읽기 (실무 핵심)
f = open("test.txt", "r")

for line in f:
    print(line)

f.close()

# 👉 메모리 효율 좋음 (실무에서 많이 씀)

# 3️⃣ 파일 쓰기
# (1) 새로 쓰기 (덮어쓰기)
f = open("test.txt", "w")

f.write("Hello\n")
f.write("World")

f.close()

# 👉 기존 내용 다 날아감
# (2) 이어쓰기
f = open("test.txt", "a")

f.write("\n추가 내용")

f.close()

# 👉 기존 내용 유지 + 뒤에 추가

# 4️⃣ 중요한 포인트 (면접 & 실무 핵심)
# 1. close() 꼭 해야 함 안 하면 메모리/파일 잠금 문제 발생 가능
# 2. read vs readline vs readlines
# 함수	특징
# read()	전체
# readline()	한 줄
# readlines()	리스트

# 3. 반복문이 제일 중요
for line in f:
    pass
# 👉 대용량 파일 처리 시 필수 패턴