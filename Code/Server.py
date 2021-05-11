import socket

HOST = '127.0.0.1'
PORT = 5000

buffsize = 1024
udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(buffsize)
    msg.decode('utf-8')
    print(cliente, msg)
