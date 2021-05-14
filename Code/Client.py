import socket
import time


def sendMsg():
    while True:
        try:
            SERVER.connect(ADDR)
        finally:
            start = time.perf_counter()
            print('Client conectado ao servidor!')
            break

    print(f'Para sair digite: {controle}\n')

    while True:
        msg = input().encode('utf-8')
        SERVER.sendto(msg, ADDR)
        if msg.decode('utf-8') == controle:
            break
    SERVER.close()

    finish = time.perf_counter()
    print(f'\033[1;33mCliente desconectado\n-> O cliente ficou conectado por {round(finish-start, 2)} segundos.')
    print('Fim do processo')

HOST = "127.0.0.1"
PORT = 5001
ADDR = (HOST, PORT)
controle = '0'

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)
sendMsg()
