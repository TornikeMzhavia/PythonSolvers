from random import randint

def CreateMines(count):
    while(count > 0):
        randI = randint(0, height - 1)
        randJ = randint(0, width - 1)

        if(mineMap[randI][randJ] == 0):
            mineMap[randI][randJ] = 1
        else:
            continue

        count -= 1

def PrintMap():
    print('  ', end = '')
    for i in range(0, width):
        print(i, end = '')
    print()
    print()

    for i in range(0, height):
        print(i, end = ' ')
        for c in map[i]:
            print(c, end = '')
        print('',i)

    print()
    print('  ', end = '')
    for i in range(0, width):
        print(i, end = '')
    print()
    print()

def PrintMineMap():
    print('  ', end = '')
    for i in range(0, width):
        print(i, end = '')
    print()
    print()

    for i in range(0, height):
        print(i, end = ' ')
        for c in mineMap[i]:
            if(c == 0):
                print('-', end = '')
            else:
                print('*', end = '')

        print('',i)

    print()
    print('  ', end = '')
    for i in range(0, width):
        print(i, end = '')
    print()
    print()

def GetNumber(x, y):
    n = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if(i >= 0 and i < len(mineMap) and j >= 0 and j < len(mineMap[i])):
                n += mineMap[i][j]
    return n

def OpenMap(x, y):
    n = GetNumber(x, y)
    c = str(n)
    if(n == 0):
        c = ' '

    map[x][y] = c
    revealed[x][y] = 1
    
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if(i >= 0 and i < len(mineMap) and j >= 0 and j < len(mineMap[i]) and mineMap[i][j] != 1):
                if(i != x or j != y):
                    newN = GetNumber(i,j)
                    newC = str(newN)
                    if(newN == 0):
                        newC = ' '
                    map[i][j] = newC
                    if(newN == 0 and revealed[i][j] == 0):
                        OpenMap(i, j)
                    
def StartGame():
    gameWon = False
    minesLeft = minesCount
    while(gameWon == False):
        print('Mines left:', minesLeft)
        inputString = input('Enter coordinates x y:')
        inputs = inputString.split(' ')
        x = int(inputs[0])
        y = int(inputs[1])

        if(len(inputs) == 3 and inputs[2] == 'F'):
            if(map[x][y] == inputs[2]):
                map[x][y] = 'X'
            else:
                map[x][y] = inputs[2]
                minesLeft -= 1
            PrintMap()
            continue

        if(mineMap[x][y] == 1):
            print('Game over')
            PrintMineMap()
            break
        else:
            OpenMap(x, y)
            PrintMap()

            undiscoveredCount = 0
            for row in map:
                for c in row:
                    if(c == 'X' or c == 'F'):
                        undiscoveredCount += 1

            if(undiscoveredCount == minesCount):
                print('You have won!')
                gameWon = True

width = 9
height = 9
minesCount = 10
map = [['X' for x in range(width)] for x in range(height)] 
mineMap = [[0 for x in range(width)] for x in range(height)] 
revealed = [[0 for x in range(width)] for x in range(height)] 

CreateMines(minesCount)

PrintMap()

StartGame()