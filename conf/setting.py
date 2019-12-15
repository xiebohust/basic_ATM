import time
import os

# 项目根目录
BaseDir = os.path.dirname(os.path.dirname(__file__))


# 获取当前日期，如20191115
def current_date():
    today = time.strftime('%Y%m%d')
    return today