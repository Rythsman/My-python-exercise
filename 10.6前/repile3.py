'''
pachong
@author haowang

'''
import requests
try:
    kv = {'wd':'porn'}
    r = requests.get('http://www.baidu.com/s', params=kv)
    print(r.request.url)      #模块名是requests,中的函数名是request
    r.raise_for_status()
    print(r.text[1000:2000])
    r.encoding = r.apparent_encoding #无需加()
except:
    print ('爬取失败')
    

