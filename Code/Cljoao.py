# EXECUTAR COM UMA IDE DEDICADA (EX: VSCODE, PYCHARM, ATOM...) PARA VER OS NOMES COLORIDOS
import socket
import threading
from time import sleep
from random import randint
from cryptography.fernet import Fernet

def getIP():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) #IPv4
    return ip_address


def crypto_tolls(x):
    if x%2 == 0:
        key = b'n05rzNJNF-tU4H-oCneuEdDxR4_fCL_wAgsy9CmB7Jk='
    else:
        key = b'T2xPK9saUIDXn3yDRd5YxzhVu0_nlMwcz7jfnIelkes='
    fernet = Fernet(key)
    return fernet


def reciveMsg():
    global kill_bool, cont_server, crypto, msgBytes, BUFFSIZE
    while True:
        if cont_server == 0:
            msgBytes, serverIP = client.recvfrom(BUFFSIZE)
            crypto = crypto_tolls(msgBytes.decode('utf8'))
            cont_server += 1
        elif cont_server == 1:
            print('\n', msgBytes.decode('utf8'))
        msgBytes, serverIP = client.recvfrom(BUFFSIZE)
        print('\n', crypto.decrypt(msgBytes.decode('utf8')))
        if kill_bool:
            break


def clientSide(address):
    global cont_client, kill_var, kill_bool, crypto
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


cont_client = 0
cont_server = 0
kill_var = ' /exit'
kill_bool = False
#Local machine
HOST = getIP()
PORT = 12000  # Porta desejada
BUFFSIZE = 4096
ADDR = (HOST, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ClientSideThread = threading.Thread(target=clientSide, args=(ADDR,))
ClientReciveThread = threading.Thread(target=reciveMsg)
ClientSideThread.start()
while True:
    if cont_client != 0:
        ClientReciveThread.start()
        break
ClientSideThread.join()
