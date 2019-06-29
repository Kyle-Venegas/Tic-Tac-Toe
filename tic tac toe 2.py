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

def makemove(player, row, col):
    x = int(row)
    y = int(col)
    if player == 1:
        letter = "X"
    if player == 2:
        letter = "O"
    grid[x][y] = letter

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
            if player == 1:
                value = "X"
            if player == 2:
                value = "O"
        elif value != grid[y][i] or grid[y][i] == "_":
                return False
    return True

def victory2(player):
    won1 = CheckCol(0, player)
    won2 = CheckCol(1, player)
    won3 = CheckCol(2, player)
    won4 = CheckRow(0, player)
    won5 = CheckRow(1, player)
    won6 = CheckRow(2, player)
    if (won1 or won2 or won3 or won4 or won5 or won6 or            #for diagonals
        grid[0][0] == grid[1][1] == grid[2][2] == "X" or grid[0][2] == grid[1][1] == grid[2][0] == "X" or
        grid[0][0] == grid[1][1] == grid[2][2] == "O" or grid[0][2] == grid[1][1] == grid[2][0] == "O"):
        print("\nPlayer {} wins".format(player)) 
        return True
    return False

import os

turn = 1
player = 1

while 1:
    os.system("clear")
    board() 
    end = victory2(player)
    if end:
        break

    player = who(turn)
    row = input("\nIn what row?: ")
    col = input("In what column?: ")
    makemove(player, row, col)
    turn += 1
