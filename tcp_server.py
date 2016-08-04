
import socket
import datetime

HOST = ""
PORT = 8000

ADD = (HOST, PORT)
BUFFER_SIZE = 1024

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(ADD)
tcp_server_socket.listen(10)

tcp_client_socket, client_addr = tcp_server_socket.accept()

while True:
    data = tcp_client_socket.recv(BUFFER_SIZE)
    if data:
        current_time = datetime.datetime.now()
        current_time_formatted = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print "%s:%s" % (client_addr, current_time_formatted)


tcp_client_socket.close()
tcp_server_socket.close()

