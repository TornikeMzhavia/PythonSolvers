with open("C:\\Users\\Tornike\\Desktop\\input.txt") as f:
    s = 0
    for line in f.readlines():
        inputs = line.split('x')
        numbers = [int(inputs[0]), int(inputs[1]), int(inputs[2])]

        #areas = [numbers[0] * numbers[1], numbers[0] * numbers[2], numbers[1] * numbers[2]]
        #s = s + 2*sum(areas) + min(areas)

        numbers.sort()
        s=s+2*(numbers[0]+numbers[1]) + numbers[0]*numbers[1]*numbers[2]
    print(s)