import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(
        connection: socket,
        loop: AbstractEventLoop
) -> None:
    """
    В бесконечном цикле ожидаем данных от клиента.
    Получив данные, отправляем их обратно клиенту.
    """
    while data := await loop.sock_recv(connection, 1024):
        await loop.sock_sendall(connection, data)


async def listen_for_connection(
        server_socket: socket,
        loop: AbstractEventLoop
):
    """
    Принимает запросы клиентов на подключение.
    Для каждого клиента создает отдельный клиентский сокет.
    Создает задачу echo, которая принимает и возвращает данные.
    """
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {address}")
        asyncio.create_task(echo(connection, loop))


async def main():
    """
    Создает основной серверный сокет.
    Ждет запросов клиентов
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('0.0.0.0', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
