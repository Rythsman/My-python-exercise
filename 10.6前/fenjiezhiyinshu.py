#从2开始做除数，不需要先找出质数。递归
from math import *

#num = int(input('请输入一个数：'))
L = []

def getnum(num):
    iszhishu = 1
    for x in range(2, int(sqrt(num+1))+1):
        if num % x == 0:
            L.append(x)
            iszhishu = 0
            getnum(num // x)
            break
    if iszhishu == 1:
        L.append(num)

getnum(123124324324134334 )
print (L)
