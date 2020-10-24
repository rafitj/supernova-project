import asyncio
import threading
import websockets
import json

class Connection(threading.Thread):
    def __init__(self, port=5015):
        super(Connection, self).__init__()
        self.host = '127.0.0.1'
        self.port = port
        self.output_stack = []
        self.input_stack = []
        self.lock = threading.Condition()
        self.loop = asyncio.new_event_loop()

    def run(self):
        server = websockets.serve(self.handler, self.host, self.port, loop=self.loop)
        print("Connection Started")
        self.loop.run_until_complete(server)
        self.loop.run_forever()

    async def poll_input(self, websocket):
        with self.lock:
            input_msg = await websocket.recv()
            print(input_msg)
            self.input_stack.append(input_msg)

    async def poll_output(self,websocket):
        if self.output_stack:
            with self.lock:
                await websocket.send(json.dumps(self.output_stack.pop(0)))

    async def handler(self, websocket, path):
        while True:
            try:
                await asyncio.wait_for(self.poll_input(websocket), timeout=0.01)
            except asyncio.TimeoutError:
                await self.poll_output(websocket)



connection = Connection()
connection.start()

def sendData(type, data):
    with connection.lock:
        connection.output_stack.append({type: data})