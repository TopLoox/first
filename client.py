import socket
import threading
from Chess_pieces.Figurestype import Figures, black_king, white_king
from Chess_pieces.Pawn import Pawn
from Chess_pieces.figcon import con

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(('localhost', 12346))  #192.168.1.78

part = 0 
Clr = 'White'
Serb = 0
shah = 0
outClr = 0
shah_fig = 0  

def getShah():
    return shah

def getClr():
    return Clr

def getSerb():
    return Serb

def getPart():
    return part

def getShahfig():
    return shah_fig

def getShahCoord():
    return shah_coord

def server_listen(room):
    global part, Clr, Serb, shah, outClr, shah_fig, shah_coord 
    while True:
        data = client.recv(2048).decode("utf-8").split(' ')
        print(data)
        if len(data) != 2:
            for i in Figures:
                if data[0] in i:
                    i[data[0]].motion(int(data[1]), int(data[2]))
                    if type(i[data[0]]) == Pawn:
                        i[data[0]].eat(int(data[1]), int(data[2]))
                    for figs in Figures:
                        for m in figs.values():
                            cord2 = m.coord()
                            if cord2 == [int(data[1]), int(data[2])] and m != i[data[0]]:
                                m.eated()
                    if (Clr != i[data[0]].coloured()):
                        if Clr == 'White':
                            shah_coord = white_king['wk'].coord()
                        else:
                            shah_coord = black_king['bk'].coord()
                        if con(i[data[0]], shah_coord[0], shah_coord[1], outClr):
                            shah = 1
                            shah_fig = i[data[0]]
                        else:
                            shah = 0
            part = int(data[3])

        else:
            Clr = data[0]
            Serb = int(data[1])
            if Clr == 'White':
                outClr = 'Black'
            else:
                outClr = 'White'


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
