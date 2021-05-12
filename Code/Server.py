import socket
import threading


def aceitaClientes():
    global controle_thread, udp
    while True:
        try:
            clientsocket, address = udp.accept()
            global clientsocket, address
        finally:
            controle_thread += 1
            print(f'Connection from {address} has been established!')
            clientsocket.send(bytes("Bem vindo ao Servidor!", 'utf-8'))


PORT = 5000
BUFFSIZE = 1024
controle_thread = 0

udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (socket.gethostname(), PORT)
udp.bind(orig)
udp.listen(3)

thread_aceitaClientes = threading.Thread(target=aceitaClientes)
thread_aceitaClientes.start()

while True:
    try:
        msg, cliente = udp.recvfrom(BUFFSIZE)
        msg.decode('utf-8')
        print(f'{cliente}: {msg}')
    except:
        break
udp.close()
