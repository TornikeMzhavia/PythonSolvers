def tower(small, big, height):
    return height - min(big,height//5)*5 - small <= 0


#def tower(small, big, height):
#    a = big // 1
#    b = small // 1 
#    x = height % 5
   
#    if height < 5 and height // small <= height or height > 5 and a * 5 >=  height and x // b <= height:
#        return True
#    elif height < 5 and height // b == height or height > 5 and a * 5 >= height and x // b == height:
#        return True
#    else:
#        return False

print(tower(3, 1, 4))