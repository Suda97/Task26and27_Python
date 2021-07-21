import os

## Checking for 3 same numbers in the row
def check(gamelist):
    if gamelist[0][0] == gamelist[0][1] == gamelist[0][2] == 1:
        return 1
    elif gamelist[0][0] == gamelist[0][1] == gamelist[0][2] == 2:
        return 2

    if gamelist[1][0] == gamelist[1][1] == gamelist[1][2] == 1:
        return 1
    elif gamelist[1][0] == gamelist[1][1] == gamelist[1][2] == 2:
        return 2

    if gamelist[2][0] == gamelist[2][1] == gamelist[2][2] == 1:
        return 1
    elif gamelist[2][0] == gamelist[2][1] == gamelist[2][2] == 2:
        return 2

    if gamelist[0][0] == gamelist[1][0] == gamelist[2][0] == 1:
        return 1
    elif gamelist[0][0] == gamelist[1][0] == gamelist[2][0] == 2:
        return 2

    if gamelist[0][1] == gamelist[1][1] == gamelist[2][1] == 1:
        return 1
    elif gamelist[0][1] == gamelist[1][1] == gamelist[2][1] == 2:
        return 2

    if gamelist[0][2] == gamelist[1][2] == gamelist[2][2] == 1:
        return 1
    elif gamelist[0][2] == gamelist[1][2] == gamelist[2][2] == 2:
        return 2

    if gamelist[0][0] == gamelist[1][1] == gamelist[2][2] == 1:
        return 1
    elif gamelist[0][0] == gamelist[1][1] == gamelist[2][2] == 2:
        return 2

    if gamelist[0][2] == gamelist[1][1] == gamelist[2][0] == 1:
        return 1
    elif gamelist[0][2] == gamelist[1][1] == gamelist[2][0] == 2:
        return 2

## Printing whole game board
def printGame(gamelist):
    for i in range(0, 3):
        print(*gamelist[i])

## Player one round
def playerOneRound(gamelist):
    while True:
        x = int(input("Player ONE turn!\nX cord: ")) - 1
        y = int(input("Y cord: ")) - 1
        if gamelist[x][y] == 0:     ## checking if the field is taken if not then change number
            gamelist[x][y] = 1
            break
        else:
            os.system('clear')
            print("Place taken! Choose another")
            printGame(gamelist)
    os.system('clear')
    return gamelist

## Player two round
def playerTwoRound(gamelist):
    while True:
        x = int(input("Player TWO turn!\nX cord: ")) - 1
        y = int(input("Y cord: ")) - 1
        if gamelist[x][y] == 0:
            gamelist[x][y] = 2
            break
        else:
            os.system('clear')
            print("Place taken! Choose another")
            printGame(gamelist)
    os.system('clear')
    return gamelist

## Whole game script
def game(gamelist):
    count = 0
    while True:
        printGame(gamelist)
        gamelist = playerOneRound(gamelist)
        count += 1
        if check(gamelist) == 1:
            printGame(gamelist)
            print("PLAYER ONE WINS!")
            break
        if count == 5:
            print("TIE!")
            return 0
        printGame(gamelist)
        gamelist = playerTwoRound(gamelist)
        if check(gamelist) == 2:
            printGame(gamelist)
            print("PLAYER TWO WINS!")
            break


if __name__ == '__main__':
    gamelist = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game(gamelist)
