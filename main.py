import logging
import traceback

# 导入发消息方法
from wxbot import send_message

def main():
    try:
        # 给用户名为小李的用户发送消息
        send_message('hello world', '小李')
    except Exception as e:
        logging.error('# 任务运行出错: ' + repr(e))
        traceback.print_exc()

if __name__ == '__main__':
    main()