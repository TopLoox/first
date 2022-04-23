from Chess_pieces.Pawn import Pawn
from Chess_pieces.Horse import Horse
from Chess_pieces.Elephant import Elephant
from Chess_pieces.Castle import Castle
from Chess_pieces.Queen import Queen
from Chess_pieces.King import King


# Списки для фигур
black_pawn = [0] * 8
white_pawn = [0] * 8
black_castle = [0] * 2
white_castle = [0] * 2
black_horse = [0] * 2
white_horse = [0] * 2
black_el = [0] * 2
white_el = [0] * 2

# Пешки
for i in range(8):
    white_pawn[i] = Pawn(i, 6, 'White')
    black_pawn[i] = Pawn(i, 1, 'Black')
white_pawn = {'wp1': white_pawn[0], 'wp2': white_pawn[1], 'wp3': white_pawn[2], 'wp4': white_pawn[3],
              'wp5': white_pawn[4], 'wp6': white_pawn[5], 'wp7': white_pawn[6], 'wp8': white_pawn[7]}
black_pawn = {'bp1': black_pawn[0], 'bp2': black_pawn[1], 'bp3': black_pawn[2], 'bp4': black_pawn[3],
              'bp5': black_pawn[4], 'bp6': black_pawn[5], 'bp7': black_pawn[6], 'bp8': black_pawn[7]}

# Ладьи
white_castle = {'wc1': Castle(0, 7, 'White'), 'wc2': Castle(7, 7, 'White')}
black_castle = {'bc1': Castle(0, 0, 'Black'), 'bc2': Castle(7, 0, 'Black')}

# Кони
white_horse = {'wh1': Horse(1, 7, 'White'), 'wh2': Horse(6, 7, 'White')}
black_horse = {'bh1': Horse(1, 0, 'Black'), 'bh2': Horse(6, 0, 'Black')}

# Слоны
white_el = {'we1': Elephant(2, 7, 'White'), 'we2': Elephant(5, 7, 'White')}
black_el = {'be1': Elephant(2, 0, 'Black'), 'be2': Elephant(5, 0, 'Black')}

# Короли и Ферзи
white_queen = {'wq': Queen(3, 7, 'White')}
black_queen = {'bq': Queen(3, 0, 'Black')}
white_king = {'wk': King(4, 7, 'White')}
black_king = {'bk': King(4, 0, 'Black')}

# Все существующие фигуры

White = [white_castle, white_el, white_horse, white_king, white_queen, white_pawn]
Black = [black_castle, black_el, black_horse, black_king, black_queen, black_pawn]
Figures = [white_castle, white_el, white_horse, white_king, white_queen, white_pawn, black_castle, black_el,
           black_horse, black_king, black_queen, black_pawn]
