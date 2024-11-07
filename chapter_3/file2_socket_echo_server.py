import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('0.0.0.0', 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'Получен запрос на подключение от {client_address}!')

    buffer = b''
    while buffer[-2:] != b'\r\n':  # критерий окончания сообщения - Enter
        data = connection.recv(2)  # читаем данные по 2 байта за раз

        if not data:
            break
        else:
            print(f"Получены данные: {data}")
            buffer += data
    print(f"Все данные: {buffer}")
    connection.sendall(buffer)  # отправка данных обратно клиенту
finally:
    server_socket.close()
 