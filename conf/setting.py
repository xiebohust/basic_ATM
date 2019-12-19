import time
import os

# 项目根目录
BaseDir = os.path.dirname(os.path.dirname(__file__))


transaction_type = {
    'deposit':{
        'action':'plus',
        'fee':0.05},
    'withdraw':{
        'action':'minus',
        'fee':0.05},
    'transfer':{
        'action':'minus',
        'fee':'0.01'
    },
    'query':{
        'action':None,
        'fee':0
    }
}

# 获取当前日期，如20191115
def current_date():
    today = time.strftime('%Y%m%d')
    return today