import socket
import threading


def reciveMsg():
    while True:
        msgBytes, serverIP = client.recvfrom(2048)
        print('\n' + msgBytes.decode('utf8'))


def clientSide(address):
    global cont
    while True:
        if cont == 0:
            msgSend = input("Name: ").capitalize()
        else:
            msgSend = input("\nMSG: ").capitalize()

        msgSend = str(cont) + msgSend
        client.sendto(msgSend.encode('utf8'), address)
        cont += 1


cont = 0
HOST = "192.168.0.106"
PORT = 12000
ADDR = (HOST, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ClientSideThread = threading.Thread(target=clientSide, args=(ADDR,))
ClientReciveThread = threading.Thread(target=reciveMsg)
ClientSideThread.start()
while True:
    if cont != 0:
        ClientReciveThread.start()
        break
ClientSideThread.join()
