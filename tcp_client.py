import socket
import datetime

HOST = "maytrue.net"
PORT = 8000
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)

tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_client.connect(ADDR)

data = 'hello server'
tcp_socket_client.send(data)

tcp_socket_client.close()