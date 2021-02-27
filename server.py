import socket
import threading

class Client(threading.Thread):
    def __init__(self, sock: socket.socket, func = None) -> None:
        super().__init__(name = "Client#"+str(id(self)))
        sock.listen(1)
        self.func = func
        self.sock = sock
        self.conn, self.addr = sock.accept()
        print(f"Connected {self.addr}")
        self.start()

    def run(self):
        if self.func != None: self.func(self)

def client_handle(client: Client):
    i = 0
    while 1:
        i += 1
        inp = client.conn.recv(1024).decode()
        print(inp)
        client.conn.send(bytes(f"Got {i}-th message", "utf-8"))


sock = socket.socket()
sock.bind(('', 9191))
print(f"Server opened in {sock.getsockname()[0]}:{sock.getsockname()[1]}")
while 1:
    client = Client(sock, client_handle)

