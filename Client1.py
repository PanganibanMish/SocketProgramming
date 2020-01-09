import socket
sp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sp.connect((socket.gethostname(), 1024))
while True:
    msg=sp.recv(7)
    print(msg.decode("utf-8"))
