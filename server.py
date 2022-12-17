import socket


def start_server():
    host = socket.gethostname()
    port = 6785
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    conn, address = server_socket.accept()

    print(f'Подключился математик: {address}')

    history = []

    while True:
        data = conn.recv(1024).decode()

        print("Принял уравнение: ", data)
        result = eval(data)
        conn.send(str(result).encode())

        h = str(data) + ' = ' + str(result)
        history.append(h)
        conn.send(str(history).encode())

        if not data:
            break


    conn.close()


if __name__ == '__main__':
    start_server()