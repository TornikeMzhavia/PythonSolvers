import sys
import math
import time

def SolveQuadratic(a,b,c):

    det=b**2-4*a*c

    if det < 0:
        print("There is no solution")
    elif det == 0:
        print("Solution is: ", (-b/(2*a)))
    else:
        print("Solution one is:", (-b+(det**0.5))/(2*a))
        print("Solution two is:", (-b-(det**0.5))/(2*a))

def SolveQuadraticString(equationString):

    equalIndex = equationString.index("=")

    separators = ["+","-","="]
    
    a=0.0
    b=0.0
    c=0.0

    symbol = 0
    while symbol < len(equationString):
        stopIndex = len(equationString)

        for separator in separators:
            if separator in equationString[symbol+1 : len(equationString)] and equationString.index(separator, symbol+1) < stopIndex:
                stopIndex = equationString.index(separator, symbol+1)

        character = equationString[symbol : stopIndex]

        if character[0] == "=":
            character = character[1 : len(character)]

        if "x2" in character:
            aString = character[0:character.index("x2")]

            if aString == "":
                aNumber = 1
            else:
                aNumber = float(aString)

            if symbol < equalIndex: 
                a += aNumber
            else: 
                a -= aNumber
        elif "x" in character:
            bString = character[0:character.index("x")]
            
            if bString == "":
                bNumber = 1
            else:
                bNumber = float(bString)

            if symbol < equalIndex: 
                b += bNumber
            else: 
                b -= bNumber
        elif character != "":
            if symbol < equalIndex: 
                c += float(character)
            else: 
                c -= float(character)

        symbol = stopIndex

    print("a=", a)
    print("b=", b)
    print("c=", c)

    SolveQuadratic(a,b,c)

#SolveQuadratic(2,5,3)
SolveQuadraticString("-2x2+5x+3=5-6x2")
#SolveQuadraticString(sys.argv[1])