import math as m
def ExponentialSteps(n):
    foundExps = [1]
    highestKnown = 1
    while(highestKnown != n):
        if(n - highestKnown in foundExps):
            break

        nextStep = 1
        if(IsPrime(n)):
            if(highestKnown * 2 > n):
                for i in range(1, len(foundExps)):
                    if(highestKnown + foundExps[len(foundExps) - i - 1] < n):
                        nextStep = foundExps[len(foundExps) - i - 1]
                        break
            else:
                nextStep = highestKnown
        else:
            for i in range(0, len(foundExps)):
                if(n % foundExps[len(foundExps) - i - 1] == 0 and highestKnown + foundExps[len(foundExps) - i - 1] < n):
                    nextStep = foundExps[len(foundExps) - i - 1]
                    break

        highestKnown = highestKnown + nextStep
        foundExps.append(highestKnown)

    return len(foundExps)

def IsPrime(n):
    if(n % 2 == 0):
        return False
    sq = int(m.sqrt(n))
    for i in range(3, sq):
        if(n % i == 0):
            return False
    return True

k = 200
sum = 0
for i in range(2, k + 1):
    print(i, ExponentialSteps(i))
    #sum += ExponentialSteps(i)
#print(sum)

#print(ExponentialSteps(13))