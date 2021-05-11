import socket

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('Para sair use CTRL+X\n')
msg = input().encode('utf-8')

while(msg != ('\x18')):
    udp.sendto (msg, dest)
    msg = input().encode('utf-8')
udp.close()
