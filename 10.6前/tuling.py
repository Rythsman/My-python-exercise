from wxpy import *
import requests

TULING_TOKEN = '8b31ab81e746489083f6fc426b5cb98a'
bot = Bot()

@bot.register(Group, TEXT) # 这里注册了群聊中的文字消息，测试时可以设置为自己(上篇中提到过)
def group_msg(msg):
    if msg.is_at:
        url_api = 'http://www.tuling123.com/openapi/api'
        data = {
            'key'    : TULING_TOKEN,
            'info'   : msg.text, # 收到消息的文字内容
        }

        s = requests.post(url_api, data=data).json()
        print (s) # 打印所获得的json查看如何使用

        if s['code'] == 100000:
            print (s['text']) # 查看回复消息的内容，可省略
            msg.reply(s['text']) # 回复消息
        
embed()