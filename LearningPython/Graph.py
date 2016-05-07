def Search(pointA, pointB):
    path = []

    if(pointB in graph[pointA]):
        return [pointA, pointB]
    else:
        searched.append(pointA)

    paths = []
    for node in graph[pointA]:
        if(node not in searched):
            s = Search(node, pointB)
            if(len(s) > 0):
                paths.append(s)
    
    if(len(paths) > 0):
        minLen = len(paths[0])
        path = paths[0]
        for p in paths:
            if(len(p) < minLen):
                path = p
                minLne = len(p)

    if(len(path) > 0):
        path = [pointA] + path

    return path

def Travel(startPoint, count):
    sum = 0
    visited[startPoint] += 1

    for i in range(0, count):
        maxDist = max(distanceMatrix[startPoint])
        candidates = []
        for j in range(0, len(distanceMatrix[startPoint])):
            if(distanceMatrix[startPoint][j] == maxDist):
                candidates.append(j)
        
        minVisits = []

        minValue = visited[candidates[0]]
        for c in candidates:
            if(visited[c] < minValue):
                minValue = visited[c]

        for c in candidates:
            if(visited[c] == minValue):
                minVisits.append(c)

        startPoint = minVisits[0]
        sum += maxDist
        visited[startPoint] += 1
    return sum


testCounts = input()
testCases = int(testCounts.split(' ')[0])
questions = int(testCounts.split(' ')[1])

graph = {}
searched = []
distanceMatrix = [[0 for x in range(testCases)] for x in range(testCases)] 
visited = []

for i in range(0, testCases):
    visited.append(0)

for i in range(0, testCases - 1):
    numbers = input().split(' ')
    node1 = int(numbers[0]) - 1
    node2 = int(numbers[1]) - 1

    if(node1 in graph):
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]
    
    if(node2 in graph):
        graph[node2].append(node1)
    else:
        graph[node2] = [node1]

for i in range(0, len(distanceMatrix)):
    for j in range(0, len(distanceMatrix[i])):
        if(i == j):
            distanceMatrix[i][j] = 0
        elif(j > i):
            distanceMatrix[i][j] = len(Search(i, j)) - 1
            searched = []
        else:
            distanceMatrix[i][j] = distanceMatrix[j][i]

for i in range(0, questions):
    #print(','.join(map(str, sorted(graph[int(input())]))))

    inp = input().split(' ')
    pointA = int(inp[0]) - 1
    count = int(inp[1])

    print(Travel(pointA, count))
    
    visited = []
    for i in range(0, testCases):
        visited.append(0)