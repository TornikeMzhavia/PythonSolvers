n = 1000

chairs = [False] + [True] * (n-1)
counter = 1
eliminatedCount = 1
while (eliminatedCount < n-1):
    trueCounter = eliminatedCount+1

    while(trueCounter > 0):
        if(chairs[counter]):
            trueCounter -= 1
            if(trueCounter == 0):
                chairs[counter] = False

        counter += 1
        if(counter == n):
            counter = 0

    eliminatedCount += 1

print(chairs.index(True) + 1)
