from random import randint
class Player1:
    ships = []
    def add(self, ships):
        pass

class Player2():
    ships = []
    def add(self, ships):
        pass

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

player1 = Player1()
player1.add(patrol_boat("patrol"))
player1.add(patrol_boat("patrol"))
player1.add(battleships("battleship"))
player1.add(battleships("battleship"))
player1.add(submarine("submarine"))
player1.add(destroyer("destroyer"))
player1.add(carrier("carrier"))

player2 = Player2()
player2.add(patrol_boat("patrol"))
player2.add(patrol_boat("patrol"))
player2.add(battleships("battleship"))
player2.add(battleships("battleship"))
player2.add(submarine("submarine"))
player2.add(destroyer("destroyer"))
player2.add(carrier("carrier"))


game_board = []


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

ship_points = load_game(game_board)
#players will alternate turns:
def player_turns(total_turns):
    if total_turns % 2 == 0:
        total_turns += 1
        return player1
    return player2

players = [player1, player2]
def row_choice(players):
    return