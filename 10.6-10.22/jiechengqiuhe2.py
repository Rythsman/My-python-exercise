s = 0
L = range(1,21)
def op(x):
    r = 1
    for i in range(1,x+1):
        r *= i
    return r
s = sum(map(op,L))
print ('1!+2!+...+20! = %d' % s)
    
