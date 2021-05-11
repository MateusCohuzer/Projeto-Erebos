import socket

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

controle = '%STOP%'
print(f'Para sair digite {controle}\n')
msg = input().encode('utf-8')

while(msg != controle):
    udp.sendto (msg, dest)
    msg = input().encode('utf-8')
udp.close()
