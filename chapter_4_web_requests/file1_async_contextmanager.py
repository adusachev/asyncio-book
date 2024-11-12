import asyncio
import socket
from asyncio import AbstractEventLoop
from types import TracebackType
from typing import Optional, Type

class ConnectedSocket:
    def __init__(self, server_socket: socket):
        self.server_socket = server_socket
        self._connection = None
    
    async def __aenter__(self):
        print(f"Ожидание подключения")
        loop = asyncio.get_event_loop()
        connection, address = await loop.sock_accept(self.server_socket)
        connection.setblocking(False)
        self._connection = connection
        print("Подключение подтверждено")
        return self._connection

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_message: Optional[BaseException],
            traceback: Optional[TracebackType]):
        print("Закрытие подключения")
        self._connection.close()


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('0.0.0.0', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    loop = asyncio.get_event_loop()

    async with ConnectedSocket(server_socket) as conn:
        data = await loop.sock_recv(conn, 1024)
        # await loop.sock_sendall(conn, data)
        print(data)


asyncio.run(main())
