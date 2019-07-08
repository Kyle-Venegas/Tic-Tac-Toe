import os

class Board:
    BOARD_SIZE = 3

    def __init__(self):
        self.grid = [["_" for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]

    def draw(self):
        print("\n    0    1    2")
        y = 0
        for row in self.grid:
           print(y, row)
           y += 1

    def make_move(self, player, row, col):
        if self.grid[row][col] != "_":
            return False
        self.grid[row][col] = playerLetter(player)
        return True

    def _all_same(self, check, player_letter):
        """Returns true if grid[i][j] = player_letter all i,j tuples in check.

        check - a list of tuples that correspond to coordinates in grid.

        Returns bool - True iff all coordinates in check have the same value.
        """
        return all(self.grid[x[0]][x[1]] == player_letter for x in check)

    def _check_col(self, col, player):
        """Returns true if all values in col are equal."""
        return self._all_same([(x, col) for x in range(self.BOARD_SIZE)], player)

    def _check_row(self, row, player):
        """Returns true if all values in row are equal."""
        return self._all_same([(row, x) for x in range(self.BOARD_SIZE)], player)

    def victory(self, player):
        size = self.BOARD_SIZE
        letter = playerLetter(player)
        for i in range(size):
            if self._check_col(i, letter):
                return True
            if self._check_row(i, letter):
                return True
        # left diagonal
        if self._all_same([(x, x) for x in range(size)], letter):
            return True
        #right diagonal
        return self._all_same([(x, size - 1 - x) for x in range(size)], letter)

def playerLetter(player):
    return "X" if player == 1 else "O"

def playTicTacToe():
    turn = 0
    player = 0
    game = Board()
    while True:
        os.system("clear")
        game.draw()
        while True:
            try:
                row = int(input("\nIn what row?: "))
                col = int(input("In what column?: "))
            except:
                print("Input must be a number.")
            if game.make_move(player, row, col):
                break
            else:
                print("Square already taken.")
        if game.victory(player):
            game.draw()
            print("\nPlayer {} wins".format(player))
            break
        turn += 1
        if turn == 9:
            game.draw()
            print("\nTie")
            break
        player = turn % 2

if __name__ == '__main__':
    playTicTacToe()
