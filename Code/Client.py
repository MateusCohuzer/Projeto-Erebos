import socket
import time

PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (socket.gethostname(), PORT)
controle = '0'

while True:
    try:
        udp.connect(dest)
    finally:
        start = time.perf_counter()
        print('Client conectado ao servidor!')
        break

print(f'Para sair digite: {controle}\n')
msg = input().encode('utf-8')

while True:
    if msg.decode('utf-8') == controle:
        break
    udp.sendto(msg, dest)
    msg = input().encode('utf-8')
udp.close()

finish = time.perf_counter()
print(f'\033[1;33mCliente desconectado\n-> O cliente ficou conectado por {round(finish-start, 2)} segundos.')
print('Fim do processo')