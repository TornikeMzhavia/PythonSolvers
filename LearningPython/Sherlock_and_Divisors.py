import math
import sys

sys.stdin = open('input07.txt', 'r')
T=int(input())

for case in range(T):
    n_string = input()
    
    if int(n_string[-1]) % 2 == 1:
        print(0)
        continue
        
    n = int(n_string)
    ans = 1
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            if i % 2 == 0:
                ans += 1
            if n // i % 2 == 0 and n // i != i:
                ans += 1
    print(ans)