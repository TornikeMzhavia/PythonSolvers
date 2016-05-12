import sys
import time

def armstrong(n):    
    counter = 0
    i = 10
    while counter < n:
        sum = 0
        digs = len(str(i))-1
        temp = i
        while (temp > 0):
            sum += powerMatrix[temp%10][digs]
            temp //= 10
            if sum > i:
                break
        if i == sum:
            counter += 1
            print(i)
        i += 1

startTime = time.perf_counter()

n = int(sys.argv[1])
powerMatrix = []
for i in range(10):
    powerMatrix.append([])
    for j in range(15):
        element = 1
        if j > 0:
            element = powerMatrix[i][j-1]
        powerMatrix[i].append(i*element)

armstrong(n)

print(time.perf_counter() - startTime)