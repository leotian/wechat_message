# 导入模块
from wxpy import *

# 初始化机器人，扫码登录
def send_message(message):
    bot = Bot(console_qr=True, cache_path=True)
    # 查找昵称为'田彦博'的好友
    my_friend = bot.friends().search(u'田彦博')[0]
    # 发送文本
    my_friend.send(message)
    return
