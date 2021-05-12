import socket
import threading


def aceitaClientes():
    while True:
        clientsocket, address = udp.accept()
        print(f'Connection from {address} has been established!')
        clientsocket.send(bytes("Bem vindo ao Servidor!", 'utf-8'))


PORT = 5000
BUFFSIZE = 1024

udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (socket.gethostname(), PORT)
udp.bind(orig)
udp.listen(3)

while True:
    try:
        msg, cliente = udp.recvfrom(BUFFSIZE)
        msg.decode('utf-8')
        print(f'{cliente}: {msg}')
    except:
        break
udp.close()
