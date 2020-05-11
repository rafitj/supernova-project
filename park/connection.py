import asyncio
import threading
import websockets


class Connection(threading.Thread):
    def __init__(self, port=5015):
        super(Connection, self).__init__()
        self.host = '127.0.0.1'
        self.port = port
        self.stack = []
        self.lock = threading.Condition()
        self.loop = asyncio.new_event_loop()

    def run(self):
        server = websockets.serve(self.handler, self.host, self.port, loop=self.loop)
        self.loop.run_until_complete(server)
        self.loop.run_forever()

    async def handler(self, websocket, path):
        while True:
            if self.stack:
                with self.lock:
                    await websocket.send(self.stack.pop(0))
