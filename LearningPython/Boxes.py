def PrintBox(number, length, x, y, symbol):
    box = ''
    for line in range(0, 1 + number*(length+1)):
        if(line % (length + 1) == 0): 
            filler = '-'
            edge = '+'
        else:
            filler = ' '
            edge = 'I'

        for column in range(0, 1 + number*(length+1)):
            if(line == x and column == y):
                    box += symbol
            else:
                if(column % (length + 1) == 0):
                    box += edge
                else:
                    box += filler
        box += '\n'

    print(box)

PrintBox(3,5, 15, 15, '*')