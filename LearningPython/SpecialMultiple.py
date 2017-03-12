def int2b(i):
    s = ''
    while i:
        if i & 1:
            s = "9{}".format(s)
        else:
            s = "0{}".format(s)
        i=i>>1
    return s
    
T = int(input())

for case in range(T):
    n = int(input())
    
    for i in range(1,1<<31):
        candidate = int(int2b(i))
        if candidate % n == 0:
            print(candidate)
            break