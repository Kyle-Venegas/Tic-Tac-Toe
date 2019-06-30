import os

grid = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
        ]

def who(turn):
    if turn % 2 == 0:
        return 2
    else:
        return 1

def board():
    print("    0    1    2")
    y = 0
    for row in grid:
       print(y, row)   #after printing row, it goes to the next line
       y += 1

def playerLetter(player):
    return "X" if player == 1 else "O"

def makemove(player, row, col):
    x = int(row)
    y = int(col)
    grid[x][y] = playerLetter(player)

def CheckCol(x, player):
    x = int(x)
    for i in range(0, len(grid)):
        if i == 0:
            value = grid[i][x]
        elif value != grid[i][x] or grid[i][x] == "_":
            return False
    return True

def CheckRow(y, player):
    y = int(y)
    for i in range(0, len(grid)):
        if i == 0:
            value = grid[y][i]
        elif value != grid[y][i] or grid[y][i] == "_":
                return False
    return True

def victory2(player):
    for i in range(3):
        if CheckCol(i, player):
            return True
        if CheckRow(i, player):
            return True
    # left diagonal
    if (grid[0][0] == grid[1][1] == grid[2][2] == playerLetter(player)):
        return True
    #right diagonal
    if (grid[0][2] == grid[1][1] == grid[2][0] == playerLetter(player)):
        return True
    return False

def playTicTacToe():
    turn = 1
    player = 1
    while True:
        os.system("clear")
        board()
        player = who(turn)
        row = input("\nIn what row?: ")
        col = input("In what column?: ")
        if check_(player, row, col):
            continue
        makemove(player, row, col)
        if victory2(player):
            board()
            print("\nPlayer {} wins".format(player))
            break
        turn += 1


if __name__ == '__main__':
    playTicTacToe()
