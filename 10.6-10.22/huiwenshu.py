
def is_palindrome(n):
    return str(n)[::] == str(n)[::-1]     #变成字符串，进行判断,filter性质

output = filter(is_palindrome, range(1,1000))
print (list(output))
