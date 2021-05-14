import socket
import time
import threading


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
        SERVER.send(bytes("", "utf8") + msg)
        if msg.decode('utf-8') == controle:
            break
    SERVER.close()

    finish = time.perf_counter()
    print(f'\033[1;33mCliente desconectado\n-> O cliente ficou conectado por {round(finish - start, 2)} segundos.')
    print('Fim do processo')


HOST = ""
PORT = 3301
ADDR = (HOST, PORT)
controle = '0'

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)
THREAD_SEND = threading.Thread(target=sendMsg())
THREAD_SEND.start()
THREAD_SEND.join()

SERVER.close()
