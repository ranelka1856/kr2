import socket


def start_client():
    host = socket.gethostname()
    port = 6785

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Введи значения. Пример: 2+2. Напиши 'Thanks' чтобы завершить.")
    message = input('-> ')

    while message != 'Thanks':

        client_socket.send(message.encode())
        result = client_socket.recv(1024).decode()

        print('Ответ: ', result)

        print("Введи значения. Пример: 2+2. Напиши 'Thanks' чтобы завершить.")
        message = input('-> ')

        if message == 'History':
            history = client_socket.recv(1024).decode()
            print(history)


    client_socket.close()


if __name__ == '__main__':
    start_client()