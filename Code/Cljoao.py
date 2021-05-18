# EXECUTAR COM UMA IDE DEDICADA (EX: PYCHARM, VSCODE, ATOM...) PARA UM MELHOR FUNCIONAMENTO DO PROGRAMA
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
    global kill_bool, crypto, msgBytes, BUFFSIZE, escopo
    while True:
        msgBytes, clientIP = client.recvfrom(BUFFSIZE)
        msgBytes = msgBytes.decode('utf8')
        flag = msgBytes[0]
        if flag == '0':
            msgBytes = msgBytes[2:]
            msgBytes = msgBytes.replace("'", '')
            escopo = msgBytes.split()
            msgBytes = escopo[0]  # name
            escopo2 = escopo[1]  # msg
            msgBytes = bytes(msgBytes.encode('utf8'))
            escopo3 = crypto.decrypt(msgBytes)
            msgBytes = escopo3.decode('utf8') + ' ' + escopo2
            print(f'\n{msgBytes}')
        elif flag == '1':
            msgBytes = msgBytes[2:]
            msgBytes = msgBytes.replace("'", '')
            escopo = msgBytes.split()
            msgBytes = escopo[0]  # name
            escopo2 = escopo[1]  # msg
            escopo2 = escopo2[1:]
            escopo2 = escopo2.replace("'", '')
            msgBytes = bytes(msgBytes.encode('utf8'))
            escopo2 = bytes(escopo2.encode('utf8'))
            escopo3 = crypto.decrypt(msgBytes)
            escopo4 = crypto.decrypt(escopo2)
            msgBytes = str(escopo3.decode('utf8')) + ': ' + str(escopo4.decode('utf8'))
            print(f'\n{msgBytes}')
        elif flag == '2':
            msgBytes = msgBytes[1:]
            print('\n' + msgBytes)
        if kill_bool:
            break
    print('fim da thread de recebimento')


def clientSide(address):
    global cont_client, kill_var, kill_bool, crypto, start
    while True:
        if cont_client == 0:
            msgSend = input("Name: ")
            start = perf_counter()
            msgSend = f'\033[1;3{randint(1, 6)}m{msgSend}\033[m'
            msgSend = bytes(msgSend.encode('utf8'))
            msgSend = '0' + str(crypto.encrypt(msgSend))
        else:
            sleep(0.001)
            msgSend = input('MSG: ')
            if msgSend == kill_var:
                msgSend = '2' + f'\033[1;31mO USUÁRIO SE DESCONECTOU \033[m'
                print(msgSend[1:])
                kill_bool = True
            else:
                msgSend = f' {crypto.encrypt(bytes(msgSend.encode("utf8")))}'
        client.sendto(msgSend.encode("utf8"), address)
        cont_client += 1
        if kill_bool:
            break
    finish = perf_counter()
    print(f'\033[1:33m Você permaneceu {round(finish-start, 2)}s online no servidor!')


cont_client = 0
cont_server = 0
kill_var = '/exit'
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
