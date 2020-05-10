import asyncio
import websockets


class Connection:
    def __init__(self, port=5015):
        self.host = '127.0.0.1'
        self.port = port

    def server(self, function):
        return websockets.serve(function, self.host, self.port)
