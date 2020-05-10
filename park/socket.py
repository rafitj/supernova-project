import socket


class Connection:
    def __init___(PORT = 5005)
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = PORT
        self.BUFFER_SIZE = 20
    def connect():
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((socket.gethostname(), self.TCP_PORT))
        s.listen(self.BUFFER_SIZE)
        while True:
            clientSocket, address = s.accept()
            print(f"Connection from {address} has been established")
            clientSocket.send(bytes('Welcome', 'utf-8'))