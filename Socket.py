import socket
sp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sp.bind(socket.gethostname(), 1024)
sp.listen(5)

while True:
    dlt, bdr=sp.accept()
    print(f"Connection to {bdr} established")
    dlt.send(bytes("Socket Programming in Python","utf-8"))

