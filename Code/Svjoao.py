import socket
import threading
from random import randint
from time import sleep


def getIP():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) #IPv4
    return ip_address


def username(msganswer):
    name = ''
    for i in range(1, len(msganswer)):
        name += msganswer[i]
    return name


def format(msg, names, ipA, ipB, clientIP):
    msgFormat = ''
    for i in range(0, len(names)):
        if ipA[i] == clientIP[0] and ipB[i] == clientIP[1]:
            msgFormat += names[i] + ': '
            break
    msgFormat = msgFormat + msg[0:len(msg)]
    return msgFormat


def serverSide():
    global names, ipA, ipB, msgFormat, x
    while True:
        if len(ipA) == 0:
            print('Aguardando conexões...')
            x = randint(1, 10000)
            x = bytes(x)
        while True:
            try:
                msgBytes, clientIP = server.recvfrom(2048)
                break
            except:
                pass

        msgAnswer = msgBytes.decode('utf8')
        msgFormat = ''

        if msgAnswer[0] == '0':
            names.append(username(msgAnswer))
            ipA.append(clientIP[0])
            ipB.append(clientIP[1])
            name = username(msgAnswer) + " entrou"
            print(name)
            server.sendto(x, clientIP)
            sleep(0.1)
            for i in range(0, len(ipA)):
                server.sendto(name.encode('utf8'), (ipA[i], ipB[i]))

        else:
            for i in range(0, len(ipA)):
                print(ipA[i], ipB[i])
                msgFormat = format(msgAnswer, names, ipA, ipB, clientIP)
                print(msgFormat)
                server.sendto(msgFormat.encode('utf8'), (ipA[i], ipB[i]))

            if msgAnswer == ' ' + '\033[1;31m>>USUÁRIO SE DESCONECTOU \033[m':
                for i in range(0, len(ipA)):
                    if ipA[i] == clientIP[0] and ipB[i] == clientIP[1]:
                        del names[i]
                        del ipA[i]
                        del ipB[i]
                        print(msgFormat)
                        print('Usuário desconectado com sucesso')
                        break


names = []
ipA = [] #IPv4
ipB = [] #Port
#Local Machine
HOST = getIP()
PORT = 12000
BUFFSIZE = 4096
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)
ServerSideThread = threading.Thread(target=serverSide())
ServerSideThread.start()
ServerSideThread.join()
