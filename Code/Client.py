import socket
import time
import threading


def sendMsg(controle='0'):
    while True:
            SERVER.connect(ADDR)
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

controle = '0'
HOST = "localhost"
PORT = 33001
if not PORT:
    PORT = 33001
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)
THREAD_SEND = threading.Thread(target=sendMsg(), args=(controle,))
THREAD_SEND.start()
THREAD_SEND.join()

SERVER.close()
