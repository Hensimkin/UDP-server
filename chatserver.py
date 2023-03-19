import socket
import threading

# Step 1: Define an array of 5 ports
ports = [8000, 8001, 8002, 8003, 8004]

def accept_connections(port):
    """Thread function to accept incoming connections"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} accepted.")
        threading.Thread(target=handle_connection, args=(client_socket,)).start()

def handle_connection(client_socket):
    """Thread function to handle an incoming connection"""
    # Send a greeting message to the client
    client_socket.send(b"W")

    # Wait for the client to respond with "Hello"
    data = client_socket.recv(1024)
    if data == b"Hello":
        print(f"Received 'Hello' from {client_socket.getpeername()}")
        # Respond with "World"
        client_socket.send(b"World")
    else:
        print(f"Error: unexpected message received from {client_socket.getpeername()}")
    client_socket.close()

if __name__ == "__main__":
    # Step 2: Ask the user for an index and choose a port number from the array
    index = int(input("Enter an index between 0 and 4: "))
    port = ports[index]

    # Step 3: Start listening on the chosen port and create a new thread to accept connections
    threading.Thread(target=accept_connections, args=(port,)).start()

    # Step 4: Attempt to connect to all other ports and exchange messages
    for p in ports:
        if p != port:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(('127.0.0.1', p))
                client_socket.send(b"Hello")
                data = client_socket.recv(1024)
                if data == b"World":
                    print(f"Received 'World' from port {p}")
                else:
                    print(f"Error: unexpected message received from port {p}.")
                client_socket.close()
            except ConnectionRefusedError:
                print(f"Connection to port {p} refused.")
