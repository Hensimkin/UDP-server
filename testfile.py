import threading
import time


def respond_to_client(conn, address):
    # do something to respond to the client
    pass


# create a socket and bind it to a port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', portop))
sock.listen(1)

while True:
    # attempt to connect to other servers
    for i in range(len(ports)):
        if i != input:
            try:
                client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
                client_sock.connect(("127.0.0.1", ports[i]))
                print(f"Connected to {ports[i]}")

                # close the socket connection
                client_sock.close()
            except socket.error as e:
                # if connection is unsuccessful, print the error message
                print(f"Failed to connect to {ports[i]}: {e}")

    # wait for a certain amount of time before attempting to connect again
    time.sleep(60)

    # accept incoming connections
    conn, address = sock.accept()
    print('New connection from', address)

    # start a new thread to respond to the client
    threading.Thread(target=respond_to_client, args=(conn, address)).start()