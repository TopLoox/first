from pickle import TRUE
import socket
import threading
from Chess_pieces.Figurestype import Figures, black_king, white_king, White, Black
from Chess_pieces.Pawn import Pawn
from Chess_pieces.Elephant import Elephant
from Chess_pieces.Queen import Queen
from Chess_pieces.Horse import Horse
from Chess_pieces.Castle import Castle
from Chess_pieces.figcon import con,shahcon

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(('localhost', 12346))  # 192.168.1.78

part, Serb, shah, outClr, shah_fig, ph, fin = [0 for i in range(7)]
Clr, Choose_condition, Choose_Color = 'White', False, ''


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

def getPh():
    return ph

def getPhFig():
    return phantom

def getFin():
    return fin

def getChcd():
    return Choose_condition

def getChClr():
    return Choose_Color

def server_listen(room):
    global part, Clr, Serb, shah, outClr, shah_fig, shah_coord, ph, phantom, fin, Choose_condition, Choose_Color, check_change
    while True:
        data = client.recv(2048).decode("utf-8").split(' ')
        print(data)
        TEST = True
        check_change = 0
        if len(data) == 4:
            for i in Figures:
                if data[0] in i:
                    if (type(i[data[0]]) == Pawn):
                        phantom_coord = i[data[0]].coord()
                        if  abs(phantom_coord[1] - int(data[2])) == 2:
                            if i[data[0]].coloured() == 'White':
                                y = int(data[2]) + 1
                            else:
                                y = int(data[2]) - 1
                            phantom = Pawn(int(data[1]),y, i[data[0]].coloured())
                            ph = 1 
                        else:
                            phantom = Pawn(-10000,-10000,'NoColor')
                            ph = 0
                    else:
                        phantom = Pawn(-10000,-10000,'NoColor')
                        ph = 0
                    i[data[0]].motion(int(data[1]), int(data[2]))
                    if type(i[data[0]]) == Pawn:
                        i[data[0]].eat(int(data[1]), int(data[2]))
                    for figs in Figures:
                        for m in figs.values():
                            cord2 = m.coord()
                            if cord2 == [int(data[1]), int(data[2])] and m != i[data[0]]:
                                m.eated()
                                TEST = False
                    for figs in Figures:
                        for m in figs.values():
                            cord2 = m.coord()
                            if TEST == True and type(i[data[0]]) == Pawn:
                                if i[data[0]].coloured() == 'White':
                                    if cord2 == [int(data[1]), int(data[2])+1]:
                                        m.eated()   
                                else:
                                    if cord2 == [int(data[1]), int(data[2])-1]:
                                        m.eated() 
                    if (Clr != i[data[0]].coloured()):
                        if Clr == 'White':
                            shah_coord = white_king['wk'].coord()
                        else:
                            shah_coord = black_king['bk'].coord()
                        if con(i[data[0]], shah_coord[0], shah_coord[1], outClr,phantom):
                            shah = 1
                            shah_fig = i[data[0]]
                        else:
                            shah = 0
                        if shah == 1:
                            L = False
                            if Clr == 'White':
                                for figs in White:
                                    for m in figs.values():
                                        for y1 in range(8):
                                            for x1 in range(8):
                                                if shahcon(shah_fig, shah_coord[0], shah_coord[1], m, x1, y1, Clr, phantom):
                                                    L = True
                            else:
                                for figs in Black:
                                    for m in figs.values():
                                        for y1 in range(8):
                                            for x1 in range(8):
                                                if shahcon(shah_fig, shah_coord[0], shah_coord[1], m, x1, y1, Clr, phantom):
                                                    L = True
                            if L == False:
                                fin = 1
            part = int(data[3])

        elif len(data) == 2:
            Clr = data[0]
            Serb = int(data[1])
            if Clr == 'White':
                outClr = 'Black'
            else:
                outClr = 'White'

        elif len(data) == 5:
            key = data[0]
            x = int(data[1])
            y = int(data[2])
            figs = data[3]
            for dicts in Figures:
                if key in dicts:
                    if figs == 'Horse':
                        dicts[key] = Horse(x, y, data[4])
                    elif figs == 'Castle':
                        dicts[key] = Castle(x, y, data[4])
                    elif figs == 'Elephant':
                        dicts[key] = Elephant(x, y, data[4])
                    elif figs =='Queen':
                        dicts[key] = Queen(x, y, data[4])
                    check_change = 1
                    Choose_condition = 0
                    

        elif len(data) == 3:
            Choose_condition = data[0]
            Choose_Color = data[1]
        



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
