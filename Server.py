import socket
names={}
UDP_IP='0.0.0.0'
UDP_PORT=9999


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
sock.bind((UDP_IP,UDP_PORT))

while True:
    message = ""
    data, addr = sock.recvfrom(1024)
    words = [word.strip() for word in data.decode().split()]
    if len(words)==1:
        if data not in names:
            names[data.decode()] = addr
    if len(words)>1:
        if words[0] in names:
            for i in range(1,len(words),1):
                message=message+words[i]+" "
            sock.sendto(message.encode(), names[words[0]])
        else:
            sock.sendto("No client".encode(), addr)
    print('received message:', data.decode())
    print(names)
    words.clear()