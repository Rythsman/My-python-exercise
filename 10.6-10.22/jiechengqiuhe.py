from functools import reduce
L = []
sum = 0
for i in range(1,21):
    for j in range(1,i+1):
        L.append(j)
    s = reduce(lambda x,y:x*y, L)
    sum += s
print (sum)
    
