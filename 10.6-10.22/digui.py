def digui(n):
    if n == 0:
        a = 1
    else:
        a = n * digui(n-1)
    return a
for n in range(10):
    print ('%d! = %d' % (n, digui(n)))
