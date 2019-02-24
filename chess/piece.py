
class Piece(object):

    def __init__(self, name='king', loc='e4'):
        # translation for coordinate
        self.translate = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        # pieces with score
        self.pieces = {'king':10000, 'queen':9, 'bishop':3, 'knight':3, 'rook':5, 'pawn':1}

        # info about piece
        self.loc = self.chess_to_coord(loc)
        self.piece = name

    """Coordinate in form 'e5' to (4, 3)"""
    def chess_to_coord(coord):
        x = int(self.translate[coord[0])
        y = 8 - int(coord[1])
        return (x, y)