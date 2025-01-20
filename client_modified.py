# Лабораторная работа 4, ДПИ22-1, Ершова Юлия Д, 2025 г.
# Клиент с модификациями

import socket

# задаем хост и порт
host = 'localhost'
port = 52366


def client_tcp():
    # создаем сокет
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Соединение с сервером {host}:{port}....")
    try:
        # подключение к серверу
        client.connect((host, port))
        print(f"1. Соединение с сервером {host}:{port} установлено.")  # служебное сообщение I

        # message = input("Введите данные, которые хотите передать серверу: ")

        while True:
            message = input("Введите данные, которые хотите передать серверу: ")
            # если строка не пустая, отправляем данные серверу
            if message != '' and message != "exit":
                client.send(message.encode())
                print("3. Отправка данных серверу....")  # служебное сообщение III
                # принимаем данные от сервера порционно
                data = client.recv(1024)
                # служебное сообщение IV
                print(f"4. Приём данных от сервера прошел успешно. Сервер вернул сообщение: {data.decode()}")
                continue
            # если строка содержит exit, отключаем клиента
            if message.lower() == "exit":
                client.sendall(message.encode())
                print("Отправка команды 'exit'. Завершение работы клиента.")
                break
            # если строка пустая, выводим сообщение и запускаем цикл заново до тех пор, пока строка не будет
            # содержать какие-либо данные
            if message == '':
                print("\033[31m" + "Внимание! Данные для отправки серверу не были введены." + "\033[39m")
                continue
        # разрываем соединение
        print("2. Разрыв соединения с сервером.")  # служебное сообщение II
        client.close()
    # ошибка соединения, если клиент не может подключиться к серверу по каким-либо причинам
    except ConnectionRefusedError:
        print(f"Не удалось установить соединение с сервером {host}:{port}. Хост или порт являются недействительными.")
    # вызываем ошибку, если клиент прерывает соединение
    except KeyboardInterrupt:
        print(f"\nКлиент принудительно разорвал соединение с сервером.")


client_tcp()
