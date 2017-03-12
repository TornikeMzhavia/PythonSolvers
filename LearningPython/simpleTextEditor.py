history = ['']
q = int(input())

for i in range(q):
    t,*w = input().split()

    if(len(w) > 0):
        w = w[0]
    
    if(t=='1'):
        history.append(''.join([history[-1], w]))
    elif(t=='2'):
        history.append(history[-1][:-int(w)])
    elif(t=='3'):
        print(history[-1][int(w)-1])
    elif(t=='4'):
        del history[-1]