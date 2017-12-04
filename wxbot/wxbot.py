# 导入模块
from wxpy import *

# 初始化机器人，扫码登录
def send_message(message, username):
    bot = Bot(console_qr=True, cache_path=True)
    # 查找昵称为'username'的好友
    my_friend = ensure_one(bot.friends().search(username))
    # 发送文本
    my_friend.send(message)
    return
