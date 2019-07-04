import os

BOARD_SIZE = 3

class Board:
    def __init__(self):
        self.grid = [["_" for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def draw(self):
        print("\n    0    1    2")
        y = 0
        for row in self.grid:
           print(y, row)
           y += 1

    def make_move(self, player, row, col):
        x = int(row)
        y = int(col)
        self.grid[x][y] = playerLetter(player)

    def check_col(self, x, player):
        x = int(x)
        for i in range(0, len(self.grid)):
            if i == 0:
                value = self.grid[i][x]
            elif value != self.grid[i][x] or self.grid[i][x] == "_":
                return False
        return True

    def check_row(self, y, player):
        y = int(y)
        for i in range(0, len(self.grid)):
            if i == 0:
                value = self.grid[y][i]
            elif value != self.grid[y][i] or self.grid[y][i] == "_":
                return False
        return True

    def check_empty_square(self, player, row, col):
        row = int(row)
        col = int(col)
        return self.grid[row][col] == "X" or self.grid[row][col] == "O"

    def victory(self, player):
        for i in range(BOARD_SIZE):
            if self.check_col(i, player):
                return True
            if self.check_row(i, player):
                return True
        # left diagonal
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == playerLetter(player)):
            return True
        #right diagonal
        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == playerLetter(player)):
            return True
        return False

def who(turn):
    return 2 if (turn % 2 == 0) else 1

def playerLetter(player):
    return "X" if player == 1 else "O"

def playTicTacToe():
    turn = 1
    player = 1
    game = Board()
    while True:
        os.system("clear")
        game.draw()
        player = who(turn)
        row = input("\nIn what row?: ")
        col = input("In what column?: ")
        if game.check_empty_square(player, row, col):
            continue
        game.make_move(player, row, col)
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
