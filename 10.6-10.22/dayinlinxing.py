#根据已经给出的一个菱形图案，用python方法完成一样效果的输出。
from sys import stdout
for i in range(4):
    for j in range(3-i):
        stdout.write (' ')
    for k in range(2*i+1):
        stdout.write ('*')
    print ('\n')
 
for i in range(3):
    for j in range(i+1):
        stdout.write(' ')
    for k in range(5-2*i):
        stdout.write('*')
    print ('\n')               
    
#很明显了，stdout.write()输出不换行而print()输出自己会换行。。。。
#我在命令行中写程序时，却发现stdout.write并不能换行，还输出了很奇怪的东西。
from sys import stdout
for i in range(5):
	stdout.write('*')

*1
*1
*1
*1
*1
