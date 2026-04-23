# 1. 소켓 한 줄 정의

# 소켓(Socket) = 네트워크에서 데이터를 주고받기 위한 통신 endpoint (IP + Port)

# 2. 구조 먼저 이해 (중요)
# [클라이언트]  →  [서버]
#     socket        socket

# 👉 둘 다 소켓을 생성하고 연결해서 통신함

# 3. 프로토콜 종류
# 종류	설명	특징
# TCP	연결 기반	신뢰성 높음 (HTTP, DB)
# UDP	비연결	빠름, 대신 손실 가능

# 👉 우리가 먼저 할 건 TCP (실무 99%)

# 4. 서버 만들기 (핵심)
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 8080))
server_socket.listen()

print("서버 대기 중...")

conn, addr = server_socket.accept()

print("클라이언트 연결:", addr)

data = conn.recv(1024)
print("받은 데이터:", data.decode())

conn.sendall("응답 완료".encode())

conn.close()
server_socket.close()

# 5. 클라이언트 만들기
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("localhost", 8080))

client_socket.sendall("Hello Server".encode())

data = client_socket.recv(1024)

print("서버 응답:", data.decode())

client_socket.close()

# 6. 흐름 (무조건 외워라)
# 서버
# socket 생성
# bind (IP + Port)
# listen (대기)
# accept (연결 수락)
# recv / send
# close
# 클라이언트
# socket 생성
# connect
# send / recv
# close

# 7. 핵심 메서드 정리
# 함수	역할
# socket()	소켓 생성
# bind()	주소 할당
# listen()	연결 대기
# accept()	연결 수락
# connect()	서버 연결
# send / sendall	데이터 전송
# recv	데이터 수신
# close	종료

# 8. 왜 중요한가 (진짜 핵심)

# 👉 우리가 쓰던 것들 전부 이 위에 있음

# HTTP → TCP 위에서 동작
# WebSocket → 소켓 기반
# DB 연결 → TCP

# 👉 즉

# 소켓 = 네트워크의 가장 기본 레벨

# 9. HTTP랑 비교
# 구분	소켓	HTTP
# 레벨	Low	High
# 구조	자유	규격 있음
# 데이터	raw bytes	JSON, text
# 편의성	낮음	높음

# 👉 HTTP는 “소켓 위에 만들어진 규칙”

# 10. 멀티 클라이언트 처리 (실무 중요)

# 기본 코드는 한 명만 처리 가능

# 👉 해결: threading

import threading

def handle_client(conn):
    data = conn.recv(1024)
    conn.sendall("ok".encode())
    conn.close()

while True:
    conn, addr = server_socket.accept()
    threading.Thread(target=handle_client, args=(conn,)).start()
    
# 11. 너 기준 실무 연결

# 너가 했던 것들이랑 연결해보면:

# WebSocket → 소켓 기반 (실시간 채팅)
# SSE → HTTP지만 내부적으로 지속 연결
# Gateway → TCP 레벨 위에서 동작
# Redis Pub/Sub → 내부적으로 네트워크 소켓

# 👉 즉

# “나는 소켓 위에서 동작하는 구조를 설계해봤다”
# 이렇게 말할 수 있음

# 12. 면접 1분 답변

# 소켓은 네트워크 통신의 가장 기본 단위로, IP와 Port를 기반으로 클라이언트와 서버 간 데이터를 주고받는 endpoint입니다. Python에서는 socket 라이브러리를 통해 TCP 또는 UDP 기반 통신을 구현할 수 있으며, 서버는 bind와 listen으로 연결을 대기하고 accept로 연결을 수락한 뒤 데이터를 송수신합니다. HTTP나 WebSocket 같은 고수준 프로토콜도 내부적으로는 소켓 위에서 동작합니다.