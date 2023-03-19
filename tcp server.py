import socket
import threading
import time
"""""
ports=[2000,2001,2002,2003,2004]
option=int(input("enter option"))
portop=ports[option]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('127.0.0.1', portop))
sock.listen(1)

def connection():
    for i in range(len(ports)):
        if i != option:
            try:
                client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
                client_sock.connect(("127.0.0.1", ports[i]))
                print(f"Connected to {ports[i]}")
                #client_sock.close()
            except ConnectionRefusedError:
                # if connection is unsuccessful, print the error message
                print(f"Failed to connect to {ports[i]}:")


def respond_to_client(conn_socket, client_address):
    print('start listening from', client_address)
    conn_socket.send(('hello from port port 2').encode())



def listening(portop):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('127.0.0.1', portop))
    sock.listen(1)
    threading.Thread(target=respond_to_client, args=(conn, address)).start()
"""""
def connectionhandshake(client_socket):
    #client_socket.send(b"Hello")
    data = client_socket.recv(1024)
    if data == b"Hello":
        print(f"Received 'Hello' from {client_socket.getpeername()}")
        client_socket.send(b"World")
    elif data==b"World":
        print(f"Received 'World' from {client_socket.getpeername()}")
    else:
        print(f"Error: unexpected message received from {client_socket.getpeername()}")
        client_socket.close()




def buildconnection(portop):#socket build and start listening to other servers
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('127.0.0.1', portop))
    sock.listen(1)

    while True:
        client_socket, client_address = sock.accept()
        print(f"Connection from {client_address} accepted.")
        data = client_socket.recv(1024)
        if data == b"Hello":
            print(f"Received 'Hello' from {client_socket.getpeername()}")
            client_socket.send(b"World")
        elif data == b"World":
            print(f"Received 'World' from {client_socket.getpeername()}")
        else:
            print(f"Error: unexpected message received from {client_socket.getpeername()}")
            client_socket.close()



        #threading.Thread(target=connectionhandshake, args=(client_socket, client_address,)).start()





def main():
    ports = [2000, 2001, 2002, 2003, 2004]
    option = int(input("enter option 0-4"))
    portop = ports[option]
    threading.Thread(target=buildconnection, args=(portop,)).start()

    for i in range(len(ports)):
        if i != option:
            try:
                client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
                client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                client_sock.connect(("127.0.0.1", ports[i]))
                print(f"Connected to {ports[i]}")
                client_sock.send(b"Hello")
                data = client_sock.recv(1024)
                if data == b"World":
                    print(f"Received 'World' from port {ports[i]}")
                else:
                    print(f"Error: unexpected message received from port {ports[i]}.")
                client_sock.close()
            except ConnectionRefusedError:
                # if connection is unsuccessful, print the error message
                print(f"Failed to connect to {ports[i]}:")



if __name__ == '__main__':
    main()
