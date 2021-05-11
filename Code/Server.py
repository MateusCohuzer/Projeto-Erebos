import socket

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    msg.decode('utf-8')
    print(cliente, msg)
