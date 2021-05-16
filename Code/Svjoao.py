import socket
import threading


def username(msganswer):
    name = ''
    for i in range(1, len(msganswer)):
        name += msganswer[i]
    return name


def format(msg, names, ipA, ipB, clientIP):
    msgFormat = ''
    for i in range(0,len(names),1):
        if ipA[i] == clientIP[0] and ipB[i] == clientIP[1]:
            msgFormat += names[i] + ': '
            break
    for i in range(1,len(msg),1):
        if i != 0:
            msgFormat += msg[i]
    print(msgFormat)
    return msgFormat


def serverSide():
    global names, ipA, ipB, msgFormat
    while True:
        msgBytes, clientIP = server.recvfrom(2048)
        msgAnswer = msgBytes.decode('utf8')
        msgFormat = ''

        if msgAnswer[0] == '0':
            names.append(username(msgAnswer))
            ipA.append(clientIP[0])
            ipB.append(clientIP[1])
            name = username(msgAnswer) + " entrou"
            print(name)
            server.sendto(name.encode('utf8'), (ipA[0], ipB[0]))
        else:
            for i in range(0, len(ipA)):
                print(ipA[i], ipB[i])
                msgFormat = format(msgAnswer, names, ipA, ipB, clientIP)
                server.sendto(msgFormat.encode('utf8'), (ipA[i], ipB[i]))


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
