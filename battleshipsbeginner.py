from random import randint
class ships:
    def __init__(self,row_size):
        self.row_size = row_size
class patrol_boat(ships):
    def __init__(self, column_size):
        ships.__init__(self,1)
        self.column_size = 2

class battleships(ships):
    def __init__(self, column_size):
        ships.__init__(self,1)
        self.column_size = 3


class submarine(ships):
    def __init__(self, column_size):
        ships.__init__(self, 1)
        self.column_size = 3


class destroyer(ships):
    def __init__(self, column_size):
        ships.__init__(self, 1)
        self.column_size = 4


class carrier(ships):
    def __init__(self, column_size):
        ships.__init__(self, 1)
        self.column_size = 5


game_board = []
player1 = {"name": "Player 1",
            "wins": 0,}
player2 = {"name": "Player 2",
            "wins": 0,}

def build_game_board(board):
    for item in range(5):
        board.append(["O"] * 5)

def show_board(board):
    for row in board:
        print(" ".join(row))

def load_game(board):
    print("WELCOME TO BATTLESHIP!")
    print("Find and sink the ships!")
    del board[:]
    build_game_board(board)
    show_board(board)
    ship_col = randint(1, len(board))
    ship_row = randint(1, len(board[0]))
    return {
        'ship_col': ship_col,
        'ship_row': ship_row,
    }
ship_points = load_game(game_board)
