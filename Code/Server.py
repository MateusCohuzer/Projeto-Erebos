import socket
from threading import Thread


def accept_connections(clients_control=1):
    global name
    while True:
        client, client_address = SERVER.accept()
        name = f'Cliente-{clients_control}'
        clients_control += 1

        print(f'{name} está online.')
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")
        eccho(msg)


def send_to_all(sock, message):
    for socket in connected_list:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                connected_list.remove(socket)


clients = {}
addresses = {}

HOST = "127.0.0.1"
PORT = 33001
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Esperando conexões...")
    ACCEPT_THREAD = Thread(target=accept_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()

SERVER.close()
