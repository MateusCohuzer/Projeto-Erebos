import socket
import threading


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
    for i in range(1, len(msg)):
        if i != 0:
            msgFormat += msg[i]
    return msgFormat


def serverSide():
    global names, ipA, ipB, msgFormat
    while True:
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
                        print('Usuário removido com sucesso')
                        break


names = []
ipA = []
ipB = []
HOST = ''
PORT = 12000
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)
print('Aguardando conexões...')
ServerSideThread = threading.Thread(target=serverSide())
ServerSideThread.start()
ServerSideThread.join()