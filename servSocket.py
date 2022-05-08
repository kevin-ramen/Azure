#Socket module provides an interface to the Berkeley sockets API
"""
The primary socket API functions an methods are:
socket()
.bind()
.listen()
.accept()
.connect()
.connect_ex()
.send()
.recv()
.close()
"""
# echo-server.py

import socket

HOST = ""  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
except Exception as e:
    print(e)
