import socket

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

controle = '0'
print(f'Para sair digite: {controle}\n')
msg = input().encode('utf-8')

while True:
    if msg == controle:
        break
    udp.sendto (msg, dest)
    msg = input().encode('utf-8')
print('Fechando Cliente')
udp.close()
print('Fim do processo')
