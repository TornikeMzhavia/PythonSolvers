import sys
#sys.stdin = open('input05.txt', 'r')

def dfs_rec(tree, discovered, w, start):
    discovered[start-1] = True
    
    for el in tree[start]:
        if(not discovered[el-1]):
            w[start-1] += dfs_rec(tree, discovered, w, el)
            
    return w[start-1]

def dfs(tree, discovered, w, stack):
    while(len(stack) > 0):
        nextNode = stack.pop()
        
        discovered[nextNode-1] = True
        
        for neighbor in tree[nextNode]:
            if(not discovered[neighbor-1]):
                w[nextNode-1] += w[neighbor-1]
                stack.append(neighbor)

    return w[start-1]

n = int(input())
w = [int(weight) for weight in input().split()]

tree = {}
for i in range(n-1):
    pair = [int(node) for node in input().split()]   
    if(pair[0] in tree):
        tree[pair[0]].append(pair[1])  
    else:
        tree[pair[0]] = [pair[1]]  
    if(pair[1] in tree):
        tree[pair[1]].append(pair[0])  
    else:
        tree[pair[1]] = [pair[0]]

#middle = dfs(tree, [False]*n, w, 1)/2
middle = dfs_rec(tree, [False]*n, w, 1)/2
    
print(int(abs(middle - min(w, key = lambda sum: abs(sum-middle)))*2))