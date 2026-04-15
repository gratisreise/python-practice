#전체 구조
try:
    pass
except:
    pass
finally:
    pass


#실행 흐름 (핵심)

#케이스 1: 에러 발생
try:
    x = int("abc")  # 에러
except:
    print("에러 처리")
finally:
    print("무조건 실행")

#결과
# 에러 처리
# 무조건 실행

#케이스 2: 에러 없음
try:
    x = int("10")  # 정상
except:
    print("에러 처리")
finally:
    print("무조건 실행")

#결과
# 무조건 실행


# finally는 왜 쓰냐 (실무 핵심)
# 👉 “정리 작업” 때문에 쓴다
# - 파일 닫기
# - DB 연결 종료
# - 네트워크 연결 해제
# - 리소스 반환

try:
    f = open("test.txt", "r")
    data = f.read()
except:
    print("파일 오류")
finally:
    f.close()
    print("파일 닫음")