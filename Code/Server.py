import socket
import threading


def aceitaClientes():
    global controle_thread, tcp, limite_conexoes, clientsocket, address
    while True:
        if controle_thread < limite_conexoes:
            try:
                clientsocket, address = tcp.accept()
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

clientsocket = ''
address = ''

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (socket.gethostname(), PORT)
tcp.bind(orig)
tcp.listen(limite_conexoes)

thread_aceitaClientes = threading.Thread(target=aceitaClientes)
thread_aceitaClientes.start()

while True:
    try:
        msg, cliente = tcp.recvfrom(BUFFSIZE)
        msg.decode('utf-8')
        print(f'{cliente}: {msg}')
    except:
        break
tcp.close()
