line = input()
h = int(line.split(':')[0])
m = line.split(':')[1]
s = line.split(':')[2][:2]
ampm = line.split(':')[2][2:4]

if(ampm == "PM" and h != 12):
    h += 12
if(ampm == "AM" and h == 12):
    h -= 12 
if(h < 10):
    h = '0'+str(h)
print(str(h)+':'+m+':'+s)