# 1️⃣ JSON 처리 (가장 먼저)

# 👉 API / 로그 / 설정파일 → 거의 다 JSON

# 핵심 개념
# JSON ↔ Python dict 변환
# 파일 읽기 / 쓰기
# 직렬화 / 역직렬화

# 기본 사용

import json

# dict → JSON 문자열
data = {"name": "kim", "age": 30}
json_str = json.dumps(data)

# JSON 문자열 → dict
parsed = json.loads(json_str)

# 파일 처리
# 쓰기
with open("data.json", "w") as f:
    json.dump(data, f)

# 읽기
with open("data.json", "r") as f:
    data = json.load(f)

# 실무 포인트
# API 응답 → 거의 json.loads()
# LLM 응답 → JSON 강제 파싱 (너 지금 하는 방식 그대로)
# 키 누락 대비 try/except 필수

# 2️⃣ CSV 처리

# 👉 엑셀 / 로그 / 데이터셋

# 기본 사용
import csv

# 쓰기
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["kim", 30])

# 읽기
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# dict 기반 (더 실무적)
# 쓰기
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "kim", "age": 30})

# 읽기
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
        
# 실무 포인트
# 데이터 마이그레이션
# 로그 export/import
# 하지만 → 대부분 pandas로 넘어감