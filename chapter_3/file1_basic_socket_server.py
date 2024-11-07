import socket

# инициализация сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# назначение сокету IP адреса и порта
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)

# прослушивание запросов от клиентов
server_socket.listen()

# ожидание запроса на подключение
connection, client_address = server_socket.accept()
print(f'Получен запрос на подключение от {client_address}!')