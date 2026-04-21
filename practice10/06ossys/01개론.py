# 🔷 1. os
# 🔹 1. os란?

# os는
# 운영체제(OS)와 상호작용하는 라이브러리

# 👉 한 줄 정의

# “파일, 디렉토리, 환경변수 등 OS 기능을 다루는 도구”

# 🔹 2. 핵심 기능
# 1️⃣ 현재 경로
# os.getcwd
# import os
# os.getcwd()  # 현재 디렉토리
# 2️⃣ 파일 / 디렉토리 조작
# os.listdir
# os.mkdir
# os.remove
# os.listdir()        # 파일 목록
# os.mkdir("test")    # 폴더 생성
# os.remove("a.txt")  # 파일 삭제
# 3️⃣ 경로 처리 (🔥 중요)
# os.path.join
# os.path.exists
# path = os.path.join("folder", "file.txt")
# os.path.exists(path)

# 👉 핵심

# “경로는 문자열 더하기 ❌ → join 사용”

# 4️⃣ 환경 변수 (🔥 실무 핵심)
# os.getenv
# db_url = os.getenv("DB_URL")

# 👉 백엔드 핵심

# DB 정보
# API KEY
# JWT secret
# 🔹 3. 실무 포인트

# 너 기준 핵심:

# 환경 변수 → 설정 분리 (dev / prod)
# 경로 처리 → OS 호환성
# 파일 처리 → 로그 / 업로드
# 🔷 2. sys
# 🔹 1. sys란?

# sys는
# 파이썬 실행 환경 자체를 제어하는 라이브러리

# 👉 한 줄 정의

# “프로그램 실행 상태와 입출력을 제어하는 도구”

# 🔹 2. 핵심 기능
# 1️⃣ 프로그램 종료
# sys.exit
# import sys
# sys.exit()
# 2️⃣ 입력 (표준 입력)
# sys.stdin
# import sys
# input = sys.stdin.readline

# 👉 코테에서 필수 (빠른 입력)

# 3️⃣ 출력 (표준 출력)
# sys.stdout
# 4️⃣ 실행 인자
# sys.argv
# import sys
# print(sys.argv)

# 👉 CLI 프로그램 만들 때 사용

# 🔹 3. 실무 포인트
# sys.stdin → 대용량 입력 처리
# sys.argv → 실행 옵션 전달
# sys.exit → 프로세스 종료 제어
# 🔥 os vs sys 차이 (면접 핵심)
# 구분	os	sys
# 역할	OS 기능	파이썬 실행 제어
# 대상	파일, 경로, 환경변수	입력, 출력, 인자
# 사용 시점	시스템 자원 접근	프로그램 흐름 제어
# 🔹 4. 백엔드 관점 핵심 정리

# 👉 진짜 중요한 것만 뽑으면:

# os.getenv → 설정 관리 (🔥 필수)
# os.path.join → 경로 안정성
# sys.argv → 배치 / CLI 옵션
# sys.stdin → 성능 입력 처리
# 🔹 5. 최종 요약 (면접용)

# 👉 한 줄 답변

# “os는 파일, 경로, 환경 변수 등 운영체제와 상호작용하기 위한 라이브러리이고, sys는 프로그램 실행 환경과 입출력을 제어하기 위한 라이브러리입니다.”