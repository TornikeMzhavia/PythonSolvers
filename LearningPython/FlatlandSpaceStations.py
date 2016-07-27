import sys
import bisect


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

if(n==m):
    print(0)
else:
    c = sorted(int(c_temp) for c_temp in input().strip().split(' '))

    #print(max(min(abs(i-city) for city in c) if i not in c else 0 for i in range(n)))
    def get_dist():
        for i in range(n):
            ci = max(0, bisect.bisect(c,i)-1)
            yield min(abs(i-c[ci]), (c[ci+1]-i) if ci < len(c)-1 else n)
            
            #while((i+j) not in c and (i-j) not in c):
            #    j += 1
            #yield j
            
    print(max(get_dist()))