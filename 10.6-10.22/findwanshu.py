for i in range(2,1001):
    
    s = i
    for j in range(1,i):
        if i % j == 0:
            s -= j        
    if s == 0:              #减完再看是否符合完数的定义
        print (i)
