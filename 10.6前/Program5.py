#整数顺序排列问题简述：任意三个整数类型，x、y、z
#提问：要求把这三个数，按照由小到大的顺序输出
#重点是如何检测到输入的这三个数

L = []
for i in range(3):
    a = int (input('请输入一个数（共三次）：'))
    L.append(a)
L.sort()
print (L)
