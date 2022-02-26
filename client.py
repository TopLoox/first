import socket
import threading
from data import part
from Chess_pieces.Figurestype import Figures

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(('localhost', 12347))


def server_listen(room):
    global part
    while True:
        data = client.recv(2048).decode("utf-8").split(' ')
        print(data)
        for i in Figures:
            if data[0] in i:
                i[data[0]].motion(int(data[1]), int(data[2]))
        part = int(data[3])


def createpotok():
    room = 'server'
    client.send(room.encode("utf-8"))

    start_client = threading.Thread(
        target=server_listen,
        args=(room,)
    )

    start_client.start()

    send_server('f 0 0 0')


def send_server(data):
    client.send(data.encode("utf-8"))


if __name__ == '__main__':
    send_server()
