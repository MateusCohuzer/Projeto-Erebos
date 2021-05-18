import socket
import threading


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
            msgFormat += names[i]
            break
    msgFormat = msgFormat + msg[0:len(msg)]
    return msgFormat


def serverSide():
    global names, ipA, ipB, msgFormat
    while True:
        if len(ipA) == 0:
            print('Aguardando conexões...')
        while True:
            try:
                msgBytes, clientIP = server.recvfrom(BUFFSIZE)
                break
            except:
                pass

        msgAnswer = msgBytes.decode('utf8')
        msgFormat = ''

        if msgAnswer[0] == '0':
            names.append(username(msgAnswer))
            ipA.append(clientIP[0])
            ipB.append(clientIP[1])
            name = '0' + username(msgAnswer) + " entrou"
            print(name)
            for i in range(0, len(ipA)):
                server.sendto(name.encode('utf8'), (ipA[i], ipB[i]))

        elif msgAnswer[0] == '2':
            for i in range(0, len(ipA)):
                if ipA[i] == clientIP[0] and ipB[i] == clientIP[1]:
                    msgFormat = f'\033[1;31m O USUÁRIO {names[i]}'+msgAnswer[18:]
                    del names[i]
                    del ipA[i]
                    del ipB[i]
                    print(msgFormat)
                    msgFormat = '2' + msgFormat
                    print('\033[31;mUsuário removido com sucesso')
                    if len(ipA) > 1:
                        for j in range(0, len(ipA)):
                            server.sendto(msgFormat.encode('utf8'), (ipA[i], ipB[i]))
                    break
        else:
            for i in range(0, len(ipA)):
                print(ipA[i], ipB[i])
                msgFormat = format(msgAnswer, names, ipA, ipB, clientIP)
                msgFormat = '1' + msgFormat
                print(msgFormat)
                server.sendto(msgFormat.encode('utf8'), (ipA[i], ipB[i]))



names = []
ipA = [] #IPv4
ipB = [] #Port
#Local Machine
HOST = getIP()
PORT = 12000
BUFFSIZE = 10240
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)
ServerSideThread = threading.Thread(target=serverSide())
ServerSideThread.start()
ServerSideThread.join()
