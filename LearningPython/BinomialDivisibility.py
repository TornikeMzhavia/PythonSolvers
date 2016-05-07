def conbinatoricFactor2(n, k, d):
    for i in range(max(k, n-k) + 1, n + 1):
      if(i % d == 0):
        print('1')
        return
    print('0')

conbinatoricFactor2(1000,500,200)