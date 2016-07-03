#import time

def CycleElimination(n):
    chairs = [False] + [True] * (n-1)
    shift = 0
    for eliminatedCount in range(1,n-1):
        trueIndeces = [i for i, el in enumerate(chairs) if el]
    
        chairs[trueIndeces[(eliminatedCount + shift) % len(trueIndeces)]] = False

        shift = (eliminatedCount + shift) % len(trueIndeces)

    return chairs.index(True) + 1

def lastSurvivor(skip, count, chairs):
    if (len(chairs) == 1):
        return chairs[0]

    del chairs[skip]
    skip = (skip + 1 + count) % len(chairs)
    count+=1

    return lastSurvivor(skip, count, chairs)

def lastSurvivor2(chairs, skip):
    skip += 1;
    if (chairs == 1):
        return 1
    else:
        return ((lastSurvivor2(chairs - 1, skip) + skip - 1) % chairs) + 1

def lastSurvivor3(chairs, skip):
    count = 0
    while (len(chairs) > 1):
        del chairs[skip]
        skip = (skip + 1 + count) % len(chairs)
        count += 1
    return chairs[0]

def best(chairs, skip):
    for count in range(len(chairs) - 1):
        del chairs[skip]
        skip = (skip + count + 1) % len(chairs)
    return chairs[0]

#timer = time.clock()

#print(CycleElimination(100))
#print(lastSurvivor(0,0,list(range(1,101))))
#print(lastSurvivor2(100,0))
#print(lastSurvivor3(list(range(1,101)),0))
print(best(list(range(1,101)),0))

#print(time.clock() - timer)