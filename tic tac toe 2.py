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
    col = int(x)
    for y in range(0, len(grid)):
        if y == 0:
            if player == 1:
                value = "X"
            if player == 2:
                value = "O"
        elif value != grid[col][y] or grid[col][0] == "_":
            return False
    return True

def CheckRow(y, player):
    row = int(y)
    for x in range(0, len(grid)):
        if x == 0:
            if player == 1:
                value = "X"
            if player == 2:
                value = "O"
        elif value != grid[x][row] or grid[0][row] == "_":
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
        grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]):
        print("\nPlayer {} wins".format(player)) 
        return 1

import os

player = 1
turn = 1

while 1:
    os.system("clear")
    board() 
    if turn > 5:
        end = victory2(player)
        if end == 1:
            break

    player = who(turn)
    row = input("\nIn what row?: ")
    col = input("In what column?: ")
    makemove(player, row, col)
    turn += 1
