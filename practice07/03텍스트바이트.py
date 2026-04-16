# 3️⃣ 텍스트 파일 vs 바이너리 파일
# "텍스트는 문자열, 바이너리는 바이트"

# 1️⃣ 텍스트 파일 (Text)
# - 사람이 읽을 수 있음
# - 문자열(str)로 처리
# 예시 파일: .txt, .csv, .json

# 읽기
with open("test.txt", "r") as f:
    data = f.read()
    print(data)  # str
# 쓰기
with open("test.txt", "w") as f:
    f.write("Hello")

# 2️⃣ 바이너리 파일 (Binary)
# - 사람이 읽기 어려움
# - bytes 타입으로 처리
# 예시 파일: 이미지 (.png, .jpg), 영상 (.mp4), 실행파일 (.exe)

# 읽기
with open("image.png", "rb") as f:
    data = f.read()
    print(type(data))  # bytes
# 쓰기
with open("copy.png", "wb") as f:
    f.write(data)

# 3️⃣ 차이 핵심 비교
# 구분	텍스트	바이너리
# 모드	"r", "w" "rb", "wb"
# 데이터	str	bytes
# 가독성	O	X

# 4️⃣ 실무 핵심 예제 (진짜 중요)

# 👉 파일 복사
with open("image.png", "rb") as f:
    data = f.read()

with open("copy.png", "wb") as f:
    f.write(data)

# 👉 이미지, 파일 업로드 로직 전부 이 원리

# 5️⃣ 언제 뭘 쓰냐?
# 텍스트 처리 → "r", "w"
# 이미지/파일 → "rb", "wb"

# 👉 헷갈리면 "사람이 읽냐? → 텍스트"