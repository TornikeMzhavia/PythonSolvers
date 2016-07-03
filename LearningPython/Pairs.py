import sys
import time
import numpy as np

sys.stdin = open('input10.txt', 'r')

def pairs(a,k):
    #return sum(map(lambda number: number-k in a, a))
    return sum([1 for number in a if number-k in a])
    #return len(list(filter(lambda el: el-k in a, a)))
    #return sum(number-k in a for number in a)
    #return np.sum(number-k in a for number in a)

# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = set(map(int, b.split(' ')))
    #b=np.unique(list(map(int, b.split(' '))))

    timer = time.clock();
    print(pairs(b,_k))
    print(time.clock()-timer)
