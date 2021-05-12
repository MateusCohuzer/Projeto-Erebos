import socket
import threading
import time

def aceitaClientes():
    global controle_thread, udp, limite_conexoes
    while True:
        if controle_thread < limite_conexoes:
            try:
                clientsocket, address = udp.accept()
            finally:
                controle_thread += 1
                print(f'Connection from {address} has been established!')
                clientsocket.send(bytes("Bem vindo ao Servidor!", 'utf-8'))
        else:
            print('O limite de conexões foi feito.')
            break


PORT = 5000
BUFFSIZE = 1024
controle_thread = 0
limite_conexoes = 3

udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (socket.gethostname(), PORT)
udp.bind(orig)
udp.listen(limite_conexoes)

thread_aceitaClientes = threading.Thread(target=aceitaClientes)
thread_aceitaClientes.start()

while limite_conexoes == 0:
    time.sleep(1)

while True:
    try:
        msg, cliente = udp.recvfrom(BUFFSIZE)
        msg.decode('utf-8')
        print(f'{cliente}: {msg}')
    except:
        break
udp.close()
