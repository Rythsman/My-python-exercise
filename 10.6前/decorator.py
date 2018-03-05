import functools

def log(text):
    print(id(text))
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print ("%s begin call %s()" % (text,func.__name__))
            ret = func(*args,**kw)
            print ("%s end call %s()" % (text,func.__name__))
            return ret
        return wrapper
    
    if isinstance(text,str) or isinstance(text,int):
        print('1')
        return decorator     #按照装饰器的格式来，返回一个函数，并将一个函数作为参数，为3层调用
    else :
        f = text
        print('2')
        #text = ''
        print(f)
        return decorator(text)   #就是两层调用
    

@log
def f():
    print ('123')
print(id(f()))
