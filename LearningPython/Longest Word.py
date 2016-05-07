import sys

def LongestWord(line):
    words = line.split(' ')
    longestLength = 0
    for word in words:
        if(len(word) > longestLength):
            longestLength = len(word)

    for word in words:
        if(len(word) == longestLength):
            return word

def SumOfPrimes(limit):
    sum = 2
    counter = 0
    i = 3
    while(counter < limit):
        if(IsPrime(i)):
            sum += i
            counter += 1
        i += 2
    return sum

def IsPrime(number):
    for i in range(2, number):
        if(number % i == 0):
            return False
    return True

def Bats(wireLength, distance, batsCount, coordinates):
    batCount = 0

    if((batsCount > 0 and coordinates[0] >= 6 + distance) or wireLength > 12):
        batCount += 1

    if((batsCount > 0 and wireLength - coordinates[-1] - 6 >= distance) or wireLength > 12 + distance):
        batCount += 1

    #wireLength -= 12 
    coordinates.append(wireLength - 6)
    lastBat = 6
    for coordinate in coordinates:
        batCount += ((coordinate - lastBat) // distance) - 1
        lastBat = coordinate

    return batCount

def GetMaxChains(words):
    chain = []
    maxChainLength = 1
        
    for word in words:
        wordsCopy = words[:]

        chain.append(word)
        lastChar = word[-1]
        wordsCopy.remove(word)

        while(len(wordsCopy) > 0):
            nextWord = ''

            for candidate in wordsCopy:
                if(candidate[0] == lastChar):
                    nextWord = candidate
                    break

            if(nextWord == ''):
                break

            chain.append(nextWord)
            lastChar = nextWord[-1]
            wordsCopy.remove(nextWord)

        if(len(chain) > maxChainLength):
            maxChainLength = len(chain)
        chain = []

    return maxChainLength

#while(True):
#    line = input('Enter line:')
#    print(LongestWord(line))
#test = 'cjz,tojiv,sgxf,awonm,fcv'
#inputs = test.split(',')
#wireLength = int(inputs[0])
#distance = int(inputs[1])
#batsCount = int(inputs[2])
#coordinates = [ int(x) for x in inputs[3:] ]
#print(Bats(wireLength, distance , batsCount ,coordinates ))
#maxChains = GetMaxChains(inputs)
#if(maxChains > 1):
#    print(maxChains)
#else:
#    print('None')

#test = '3; 1:[1, 3, 2], 2:[1], 3:[1]'
with open('data.txt') as f:
    for line in f.readlines():
        test = line.strip('\n')
        if(test == ''):
            continue

        n = test.split(';')[0]
        newTest = test.split(';')[1]
        distincts = []

        for t in newTest.split(']'):
            if(t == ''):
                break

            seatsText = t.split('[')[1]
            newLists = []

            for seatText in seatsText.split(','):
                seatNumber = int(seatText)

                if(len(distincts) > 0):
                    for d in distincts:
                        if(seatNumber not in d):
                            newLists.append(d.copy())
                            newLists[-1].add(seatNumber)
                else:
                    newLists.append({seatNumber})

            distincts = newLists

        if(len(distincts) > 0):
            print('Yes')
        else:
            print('No')