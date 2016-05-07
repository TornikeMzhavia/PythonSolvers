def calc(s):
    operrands = ['+', '-', '/', '*', '(', ')']
    operrandMet = False;
    firstNumber = 0.0

    for i in range(len(s)):
        character = s[i]
        if character not in operrands:
            j = i+1
            while(j < len(s) and s[j] not in operrands):
                j+=1
            firstNumber = calc(s[i:j])
        else:
            operrandMet = True;
            if character == '+':
                return firstNumber + calc(s[i+1:])
            elif character == '-':
                return firstNumber - calc(s[i+1:])
            elif character == '*':
                return firstNumber * calc(s[i+1:])
            elif character == '/':
                return firstNumber / calc(s[i+1:])
            elif character == '(':
                bracketCounter = 1
                j = i + 1
                while(bracketCounter != 0):
                    if s[j] == '(':
                        bracketCount += 1
                    elif s[j] == ')':
                        bracketCounter -= 1
                    j+=1
                firstNumber = calc(s[i+1:j-1])

    if not operrandMet:
        return firstNumber

print(calc("(3*5)+2"))
        