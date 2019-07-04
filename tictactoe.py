import os

BOARD_SIZE = 3

class board:

    def __init__(self):
        self.grid = [["_" for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def draw(self):
        print("    0    1    2")
        y = 0
        for row in self.grid:
           print(y, row)
           y += 1
 
    def makemove(self, player, row, col):
        x = int(row)
        y = int(col)
        self.grid[x][y] = playerLetter(player)
 
    def victory(self, player):
        for i in range(BOARD_SIZE):
            if CheckCol(i, player):
                return True
            if CheckRow(i, player):
                return True
        # left diagonal
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == playerLetter(player)):
            return True
        #right diagonal
        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == playerLetter(player)):
            return True
        return False

game = board()

def who(turn):
    if turn % 2 == 0:
        return 2
    else:
        return 1

def playerLetter(player):
    return "X" if player == 1 else "O"

def CheckCol(x, player):
    x = int(x)
    for i in range(0, len(game.grid)):
        if i == 0:
            value = game.grid[i][x]
        elif value != game.grid[i][x] or game.grid[i][x] == "_":
            return False
    return True

def CheckRow(y, player):
    y = int(y)
    for i in range(0, len(game.grid)):
        if i == 0:
            value = game.grid[y][i]
        elif value != game.grid[y][i] or game.grid[y][i] == "_":
                return False
    return True

def check_(player, row, col):
    row = int(row)
    col = int(col)
    if game.grid[row][col] == "X" or game.grid[row][col] == "O":
        return True
    return False

def playTicTacToe():
    turn = 1
    player = 1
    while True:
        os.system("clear")
        game.draw()
        player = who(turn)
        row = input("\nIn what row?: ")
        col = input("In what column?: ")
        if check_(player, row, col):
            continue
        game.makemove(player, row, col)
        if game.victory(player):
            game.draw()
            print("\nPlayer {} wins".format(player))
            break
        if turn == 9:
            game.draw()
            print("\nTie")
            break
        turn += 1

if __name__ == '__main__':
    playTicTacToe()
