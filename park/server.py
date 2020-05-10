import asyncio
import datetime
import random
from connection import Connection

socket = Connection()


async def function(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

server = socket.server(function)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
