import socket
sp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sp.connect((socket.gethostname(), 1024))
msg=sp.recv(1024)
print(msg.decode("utf-8"))
