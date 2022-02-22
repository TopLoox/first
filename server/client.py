import socket
import threading

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(("192.168.1.78", 12345))


def server_listen(room):
    while True:
        data = client.recv(2048).decode("utf-8").split(chr(123456))
        data_user, data_room = [i[2:-1] for i in data]
        if data_room == room:
            print(f">> {data_user}")


def send_server():
    room = 'server'
    client.send(room.encode("utf-8"))

    start_client = threading.Thread(
        target=server_listen,
        args=(room,)
    )

    start_client.start()

    client.send('GO'.encode("utf-8"))

    while True:
        client.send(input().encode("utf-8"))


if __name__ == '__main__':
    send_server()
