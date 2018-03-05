from wxpy import *
import requests

TULING_TOKEN = '8b31ab81e746489083f6fc426b5cb98a'
bot = Bot()

tuling = Tuling(api_key=TULING_TOKEN)
@bot.register(msg_types=TEXT)

def auto_reply_all(msg):
    tuling.do_reply(msg)

embed()
