from Chess_pieces.Pawn import Pawn
from Chess_pieces.Horse import Horse
from Chess_pieces.Elephant import Elephant
from Chess_pieces.Castle import Castle
from Chess_pieces.Queen import Queen
from Chess_pieces.King import King

from Chess_pieces.Figurestype import Figures, Black, White, black_castle, white_castle, white_king, black_king

def getCastlin():
    return castlin

def getMoveing():
    return moveing

def con(fig, x, y, Clr):
    global castlin, moveing
    if type(fig) == Horse:
        if fig.testmotion(x, y) == 0:
            return False
        for figs in Figures:
            for m in figs.values():
                cord2 = m.coord()
                if m.coloured() == Clr and (cord2 == [x, y]):
                    return False
        return True
    elif type(fig) == Castle:
        cord = fig.coord()
        for figs in Figures:
            for m in figs.values():
                cord2 = m.coord()
                if (type(m) != King) and (m.coloured != Clr):
                    if cord[0] == x:
                        if m.coloured() == Clr:
                            if ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)) and (cord[0] == cord2[0]):
                                return False
                        else:
                            if ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)) and (cord[0] == cord2[0]):
                                return False

                    elif cord[1] == y:
                        if m.coloured() == Clr:
                            if ((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and (cord[1] == cord2[1]):
                                return False
                        else:
                            if ((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and (cord[1] == cord2[1]):
                                return False
                    else:
                        return False
        return True
    elif type(fig) == Elephant:
        cord = fig.coord()
        for figs in Figures:
            for m in figs.values():
                cord2 = m.coord()
                if (type(m) != King) and (m.coloured != Clr):
                    if m.coloured() == Clr:
                        if (abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and \
                                (((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and
                                ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y))) or (abs(cord[0]-x) == 0) \
                                            or (abs(cord[0] - x) != abs(cord[1] - y)):
                            return False
                    else:
                        if (abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and \
                                (((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and
                                ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y))) or (abs(cord[0]-x) == 0) \
                                            or (abs(cord[0] - x) != abs(cord[1] - y)):
                            return False
        return True

    elif type(fig) == King:
        cord = fig.coord()
        if Clr == 'White':
            for p in white_castle.values():
                if (cord[1] == y) and (fig.getCount() == 0) and (p.getCount() == 0):
                    cord2 = p.coord()
                    if (cord[0] - x == 2) and (cord2[0] - x == -2) and (con(p, x + 1, y, Clr)):
                        castlin = p
                        moveing = x + 1
                        return True
                    elif (cord2[0] - x == 1) and (x - cord[0] == 2) and (con(p, x - 1, y, Clr)):
                        castlin = p
                        moveing = x - 1
                        return True
        else:
            for p in black_castle.values():
                if (cord[1] == y) and (fig.getCount() == 0) and (p.getCount() == 0):
                    cord2 = p.coord()
                    if (cord[0] - x == 2) and (cord2[0] - x == -2) and (con(p, x + 1, y, Clr)):
                        castlin = p
                        moveing = x + 1
                        return True
                    elif (cord2[0] - x == 1) and (x - cord[0] == 2) and (con(p, x - 1, y, Clr)):
                        castlin = p
                        moveing = x - 1
                        return True
        outing = False
        for figs in Figures:
            for m in figs.values():
                cord2 = m.coord()
                if m.coloured() == Clr:
                    if (cord2 == [x, y]) or (abs(cord[0]-x) > 1) or (abs(cord[1]-y) > 1):
                        return False
                    elif Clr == 'White':
                        for figs2 in Black:
                            for p in figs2.values():
                                if (type(p) != King) and (type(p) != Pawn):
                                    outing = con(p, x, y, Clr)
                                    if outing == True:
                                        return False
                                elif type(p) == King:
                                    cord3 = p.coord()
                                    if (abs(cord3[0] - x) <= 1) and (abs(cord3[1] - y) <= 1):
                                        return False
                                elif type(p) == Pawn:
                                    cord3 = p.coord()
                                    if (abs(cord3[0] - x) == 1) and (y - cord3[1] == 1):
                                        return False
                    elif Clr == 'Black':
                        for figs2 in White:
                            for p in figs2.values():
                                if (type(p) != King) and (type(p) != Pawn):
                                    outing = con(p, x, y, Clr)
                                    if outing == True:
                                        return False
                                elif type(p) == King:
                                    cord3 = p.coord()
                                    if (abs(cord3[0] - x) <= 1) and (abs(cord3[1] - y) <= 1):
                                        return False
                                elif type(p) == Pawn:
                                    cord3 = p.coord()
                                    if (abs(cord3[0] - x) == 1) and (cord3[1] - y == 1):
                                        return False
        return True

    elif type(fig) == Queen:
        cord = fig.coord()
        for figs in Figures:
            for m in figs.values():
                cord2 = m.coord()
                if (type(m) != King) and (m.coloured != Clr):
                    if m.coloured() == Clr:
                        if ((abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and
                            (((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and
                            ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)))) or \
                                ((cord[0] == x) and ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)) and
                                (cord[0] == cord2[0])) or ((cord[1] == y) and ((cord[0] < cord2[0] <= x) or
                                (cord[0] > cord2[0] >= x)) and (cord[1] == cord2[1])) or not(((abs(cord[0] - x) == abs(cord[1] - y)) or
                                ((cord[1] == y) or (cord[0] == x))) and not((cord[1] == y) and (cord[0] == x))):
                            return False
                    else:
                        if ((abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and
                            (((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and
                            ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)))) or \
                                ((cord[0] == x) and ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)) and
                                (cord[0] == cord2[0])) or ((cord[1] == y) and ((cord[0] < cord2[0] < x) or
                                (cord[0] > cord2[0] > x)) and (cord[1] == cord2[1])) or not(((abs(cord[0] - x) == abs(cord[1] - y)) or
                                ((cord[1] == y) or (cord[0] == x))) and not((cord[1] == y) and (cord[0] == x))):
                            return False
        return True
    elif type(fig) == Pawn:
        if Clr == 'White':
            cord = fig.coord()
            for figs in Black:
                for m in figs.values():
                    cord2 = m.coord()

                    if (abs(cord[0] - cord2[0]) == 1) and (cord[1] - cord2[1] == 1) and (cord2 == [x, y]):
                        return True

            for figs in Figures:
                for m in figs.values():
                    cord2 = m.coord()
                    if ((cord[1] > cord2[1] >= y) and cord[0] == cord2[0]) or (x != cord[0]) or \
                                ((fig.getCount() == 0) and ((cord[1] - y) > 2)) or ((fig.getCount() > 0) and ((cord[1] - y) > 1)) or ((y - cord[1]) >= 0):
                        return False
            return True

        else:
            cord = fig.coord()
            for figs in White:
                for m in figs.values():
                    cord2 = m.coord()

                    if (abs(cord[0] - cord2[0]) == 1) and (cord2[1] - cord[1] == 1) and (cord2 == [x, y]):
                        return True

            for figs in Figures:
                for m in figs.values():
                    cord2 = m.coord()

                    if ((cord[1] < cord2[1] <= y) and cord[0] == cord2[0]) or (x != cord[0]) or \
                                ((fig.getCount() == 0) and ((y - cord[1]) > 2)) or ((fig.getCount() > 0) and ((y - cord[1]) > 1)) or ((cord[1] - y) >= 0):
                        return False
            return True


def shahcon(shahfig, king_x, king_y, fig, x, y, Clr):
    shah_coord = shahfig.coord()
    if type(shahfig) == Pawn or type(shahfig) == Horse:
        if shah_coord == [x, y] and con(fig, x, y, Clr) and type(fig) != King:
            return True
        elif type(fig) == King:
            return con(fig, x, y, Clr) 
        else:
            return False

    elif type(shahfig) == Castle:
        if shah_coord == [x, y] and con(fig, x, y, Clr) and type(fig) != King:
            return True
        elif type(fig) == King:
            return con(fig, x, y, Clr)
        elif x == king_x == shah_coord[0]:
            if shah_coord[1] < king_y:
                if shah_coord[1] < y < king_y and con(fig, x, y, Clr):
                    return True
            else:
                if shah_coord[1] > y > king_y and con(fig, x, y, Clr):
                    return True
        elif y == king_y == shah_coord[1]:
            if shah_coord[0] < king_x:
                if shah_coord[0] < x < king_x and con(fig, x, y, Clr):
                    return True
            else:
                if shah_coord[0] > x > king_x and con(fig, x, y, Clr):
                    return True
        else:
            return False
    
    elif type(shahfig) == Elephant:
        if shah_coord == [x, y] and con(fig, x, y, Clr) and type(fig) != King:
            return True
        elif type(fig) == King:
            return con(fig, x, y, Clr)
        elif shah_coord[0] < king_x:
            if shah_coord[1] < king_y:
                if (shah_coord[0] < x < king_x) and (shah_coord[1] < y < king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
            elif shah_coord[1] > king_y:
                if (shah_coord[0] < x < king_x) and (shah_coord[1] > y > king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
        elif shah_coord[0] > king_x:
            if shah_coord[1] < king_y:
                if (shah_coord[0] > x > king_x) and (shah_coord[1] < y < king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
            elif shah_coord[1] > king_y:
                if (shah_coord[0] > x > king_x) and (shah_coord[1] > y > king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
        else:
            return False

    elif type(shahfig) == Queen: 
        if shah_coord == [x, y] and con(fig, x, y, Clr) and type(fig) != King:
            return True
        elif type(fig) == King:
            return con(fig, x, y, Clr)
        elif shah_coord[0] < king_x:
            if shah_coord[1] < king_y:
                if (shah_coord[0] < x < king_x) and (shah_coord[1] < y < king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
            elif shah_coord[1] > king_y:
                if (shah_coord[0] < x < king_x) and (shah_coord[1] > y > king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
        elif shah_coord[0] > king_x:
            if shah_coord[1] < king_y:
                if (shah_coord[0] > x > king_x) and (shah_coord[1] < y < king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
            elif shah_coord[1] > king_y:
                if (shah_coord[0] > x > king_x) and (shah_coord[1] > y > king_y) and con(fig, x, y, Clr) and (abs(x - king_x) == abs(y - king_y)):
                    return True
        elif x == king_x == shah_coord[0]:
            if shah_coord[1] < king_y:
                if shah_coord[1] < y < king_y and con(fig, x, y, Clr):
                    return True
            else:
                if shah_coord[1] > y > king_y and con(fig, x, y, Clr):
                    return True
        elif y == king_y == shah_coord[1]:
            if shah_coord[0] < king_x:
                if shah_coord[0] < x < king_x and con(fig, x, y, Clr):
                    return True
            else:
                if shah_coord[0] > x > king_x and con(fig, x, y, Clr):
                    return True
        else:
            return False  

    return False