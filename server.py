# Лабораторная работа 4, ДПИ22-1, Ершова Юлия Д, 2025 г.

import socket

# задаем хост и порт
host = ''
port = 52366


def server_tcp():
    # создаем сокет
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # привязываем сокет к хосту и порту
    server.bind((host, port))
    # прослушивание соединения
    server.listen(1)
    print(f"1. Сервер запустился на порту {port}....")  # служебное сообщение I
    print(f"2. Начало прослушивания входящих соединений на порту {port}....")  # служебное сообщение II
    # принимаем подключение
    client_socket, client_address = server.accept()
    print(f"3. Клиент {client_address} подключился к серверу.")  # служебное сообщение III
    while True:
        # принимаем клиентское сообщение
        data = client_socket.recv(1024)
        data_dec = data.decode('utf-8')
        if not data:
            break
        print("4. Получение данных от клиента прошло успешно.")  # служебное сообщение IV
        print(f"Полученные данные от клиента: {data_dec}")
        # видоизменяем возвращаемые данные
        up_data = data_dec.upper()  # переводим буквы в строке в верхний регистр
        repl_data = up_data.replace(' ', '__')  # делаем замену
        # отправляем видоизмененные данные клиенту
        print("5. Полученые данные были видоизменены сервером. Отправка данных клиенту....")  # служебное сообщение V
        client_socket.send(repl_data.encode())

    # закрываем соединение
    print(f"6. Отключение клиента {client_address} от сервера.")  # служебное сообщение VI
    client_socket.close()
    print("7. Остановка сервера.")  # служебное сообщение VI
    server.close()


server_tcp()
