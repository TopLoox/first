import socket
import threading

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(("localhost", 12346))  # 192.168.1.78

server.listen(5)

print("<< Server have started >>")

users = []

part = 0


def send_all(data):
    print(part)
    dates = data.decode('utf-8').split(' ')
    if (len(users) == 2) and (len(dates) == 2):
        if part % 2 == 1:
            users[1].send(data)
        else:
            users[0].send(data)
    elif (len(users) == 2) and (len(dates) != 2):
        users[1].send(data)
        users[0].send(data)


def server_chat(user, room_number):
    global part
    while True:
        data = user.recv(2048)
        dates = data.decode('utf-8').split(' ')
        if len(dates) == 4:
            part = int(dates[3])
        if dates == ['f', '0', '0', '0']:
            send_all('White 1'.encode('utf-8'))
            part = 1
            send_all('Black 1'.encode('utf-8'))
        else:
            send_all(data)


def server_start():
    while True:
        user_socket, address = server.accept()
        room_number = user_socket.recv(2048).decode("utf-8")

        print(f"\033[31m{'-' * 30}\n\033[0m<< User {address[0]} has join at {room_number} room >>\033[31m\n{'-' * 30}")

        users.append(user_socket)

        server_listen = threading.Thread(
            target=server_chat,
            args=(user_socket, room_number)
        )

        server_listen.start()


if __name__ == '__main__':
    server_start()