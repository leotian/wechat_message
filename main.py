import logging
import traceback

from wxbot import send_message

def main():
    try:
        send_message('hello world', '小李')
    except Exception as e:
        logging.error('# 任务运行出错: ' + repr(e))
        traceback.print_exc()

if __name__ == '__main__':
    main()