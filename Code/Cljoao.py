# EXECUTAR COM UMA IDE DEDICADA (EX: VSCODE, PYCHARM, ATOM...) PARA VER OS NOMES COLORIDOS
import socket
import threading
from time import sleep, perf_counter
from random import randint
from cryptography.fernet import Fernet

def getIP():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) #IPv4
    return ip_address


def crypto_tolls():
    key = b'n05rzNJNF-tU4H-oCneuEdDxR4_fCL_wAgsy9CmB7Jk='
    fernet = Fernet(key)
    return fernet


def reciveMsg():
    global kill_bool, cont_server, crypto, msgBytes, BUFFSIZE
    while True:
        msgBytes, serverIP = client.recvfrom(BUFFSIZE)
        msgBytes = bytes(msgBytes)
        msgBytes = crypto.decrypt(msgBytes)
        print('\n', msgBytes)
        if kill_bool:
            break


def clientSide(address):
    global cont_client, kill_var, kill_bool, crypto
    start = perf_counter()
    while True:
        if cont_client == 0:
            msgSend = input("Name: ")
            msgSend = '0' + f'\033[1;3{randint(1, 6)}m{msgSend}\033[m'
        else:
            sleep(0.001)
            msgSend = input('MSG: ')
            msgSend = f' {crypto.encrypt(bytes(msgSend.encode("utf8")))}'
            if msgSend == kill_var:
                msgSend = ' ' + f'\033[1;31m>>USUÁRIO SE DESCONECTOU \033[m'
                kill_bool = True
        client.sendto(msgSend.encode("utf8"), address)
        cont_client += 1
        if kill_bool:
            break
    finish = perf_counter()
    print(f'\033[1:33m Você permaneceu {round(finish-start, 2)}s online no servidor!')


cont_client = 0
cont_server = 0
kill_var = ' /exit'
kill_bool = False
#Local machine
HOST = getIP()
PORT = 12000  # Porta desejada
BUFFSIZE = 10240
ADDR = (HOST, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ClientSideThread = threading.Thread(target=clientSide, args=(ADDR,))
ClientReciveThread = threading.Thread(target=reciveMsg)
crypto = crypto_tolls()
ClientSideThread.start()
while True:
    if cont_client != 0:
        ClientReciveThread.start()
        break
ClientSideThread.join()
