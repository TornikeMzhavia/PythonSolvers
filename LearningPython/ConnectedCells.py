from collections import namedtuple
Element = namedtuple('Element', 'row column')

def get_region_size(matrix, row, column):
    region_size = 0
    stack = [Element(row,column)]
    
    while(len(stack) > 0):
        next_node = stack.pop()
        
        if(not matrix[next_node.row][next_node.column]):
            continue
        
        matrix[next_node.row][next_node.column] = False
        region_size += 1
        
        for i in range(max(0, next_node.row-1), min(len(matrix), next_node.row+2)):
            for j in range(max(0, next_node.column-1), min(len(matrix[0]), next_node.column+2)):
                if(matrix[i][j]):
                    stack.append(Element(i,j))
            
    return region_size

m = int(input())
n = int(input())
matrix = []
for i in range(m):
    matrix.append([element == '1' for element in input().split()])

max_region_size = 0
for i in range(m):
    for j in range(n):
        if(matrix[i][j]):
            current_region_size = get_region_size(matrix, i, j)
            if(current_region_size > max_region_size):
                max_region_size = current_region_size
print(max_region_size)          