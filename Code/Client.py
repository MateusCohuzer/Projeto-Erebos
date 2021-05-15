import socket
import time
import threading


def sendMsg(controle='0'):

    start = time.perf_counter()
    print('Client conectado ao servidor!')

    print(f'Para sair digite: {controle}\n')

    while True:
        msg = input().encode('utf-8')
        CLIENT.sendto(msg, ADDR)
        if msg.decode('utf-8') == controle:
            break
    CLIENT.close()

    finish = time.perf_counter()
    print(f'\033[1;33mCliente desconectado\n-> O cliente ficou conectado por {round(finish-start, 2)} segundos.')
    print('Fim do processo')


def recMsg():
    while True:
        try:
            msg = CLIENT.recv(BUFSIZ).decode("utf8")
            print(msg)
        except OSError:
            break


controle = '0'
HOST = "localhost"
PORT = 33001
if not PORT:
    PORT = 33001
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect(ADDR)
THREAD_SEND = threading.Thread(target=sendMsg(), args=(controle,))
THREAD_REC = threading.Thread(target=recMsg())
THREAD_SEND.start()
THREAD_REC.start()
THREAD_SEND.join()
