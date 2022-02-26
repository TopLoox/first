import socket
import threading

from Chess_pieces.Figurestype import Figures, Black, White

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(("localhost", 12347))   # 192.168.1.78

server.listen(5)

print("<< Server have started >>")

users = []


def send_all(data):
    for user in users:
        user[0].send(data)


def server_chat(user, room_number):
    while True:
        data = user.recv(2048)
        send_all(data)


def server_start():

    while True:
        user_socket, address = server.accept()
        room_number = user_socket.recv(2048).decode("utf-8")
        
        print(f"\033[31m{'-'*30}\n\033[0m<< User {address[0]} has join at {room_number} room >>\033[31m\n{'-'*30}")

        users.append([user_socket, room_number])

        server_listen = threading.Thread(
            target=server_chat,
            args=(user_socket, room_number)
        )

        server_listen.start()


if __name__ == '__main__':
    server_start()
