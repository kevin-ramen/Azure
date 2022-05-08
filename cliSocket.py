# echo-client.py
import socket

HOST = "20.228.243.120"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))
    server.sendall(b"Hello, world!")
    data = server.recv(1024)
    print(f"Received: {data}")
except Exception as e:
    print(e)
