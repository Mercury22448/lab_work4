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
        message = input("Введите данные, которые хотите передать серверу: ")

        # при отправке пустого сообщения сервер находится в бесконечном ожидании данных
        # поэтому делаем проверку строки
        def check_message(m):
            # если строка пустая, выводим сообщение и запускаем функцию заново до тех пор, пока строка не будет
            # содержать какие-либо данные
            if m == '':
                print("\033[31m" + "Внимание! Данные для отправки серверу не были введены." + "\033[39m")
                m = input("Введите данные, которые бы хотели отправить серверу, отправка пустой строки невозможна: ")
                check_message(m)
            # если строка не пустая, отправляем данные серверу
            elif m != '':
                client.send(m.encode())
                print("3. Отправка данных серверу....")  # служебное сообщение III
                # принимаем данные от сервера порционно
                data = client.recv(1024)
                # служебное сообщение IV
                print(f"4. Приём данных от сервера прошел успешно. Сервер вернул сообщение: {data.decode()}")
                # разрываем соединение
                print("2. Разрыв соединения с сервером.")  # служебное сообщение II
                client.close()

            else:
                # разрываем соединение
                print("2. Разрыв соединения с сервером.")  # служебное сообщение II
                client.close()
        # вызов функции проверки строки
        check_message(message)
    # ошибка соединения, если клиент не может подключиться к серверу по каким-либо причинам
    except ConnectionRefusedError:
        print(f"Не удалось установить соединение с сервером {host}:{port}. Хост или порт являются недействительными.")
    # вызываем ошибку, если клиент прерывает соединение
    except KeyboardInterrupt:
        print(f"\nКлиент принудительно разорвал соединение с сервером.")


client_tcp()
