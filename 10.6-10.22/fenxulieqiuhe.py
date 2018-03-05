from functools import reduce  #Python3.0后将reduce移除built-in函数
a = 2.0
b = 1.0
l = []
for n in range(1,21):
    l.append(a / b)
    b,a = a,a + b
    
print (reduce(lambda x,y: x + y, l))
#reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用
