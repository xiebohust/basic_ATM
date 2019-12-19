#!/usr/bin/env python3

"""
一、基础阶段项目要求
1.ATM自动存取款系统的程序
1.注册（用户名，手机号，身份证号(18位)，密码（确认两次）（长度6位））
2.查询（账号（必须存在），密码（确认3次，不对就锁卡））
3.取款（账号（必须存在），密码（确认3次，不对就锁卡））
4.存款（账号（必须存在），金额不能低于0，存款的金额必须是纯数字）
5.转账（你的账号，被转的账号（都必须存在），你的密码（确认3次，不对就锁卡），转账的金额不得超过你的余额，必须是纯数字）
6.登录
"""
from core.file_operation import read_file, save_to_file
from core.logger import get_logger
from conf import setting

# 设置用户账号初始值
user_data = {
    'account_id':None,
    'is_authed': False,
    'account_data':None
}

# 创建logger对象
trans_log = get_logger('transaction')
access_log = get_logger('access')

def register():
    """1.注册（用户名，密码，确认密码）
"""
    print('欢迎来到注册页面'.center(50, '*'))
    username = input('用户名：')
    password = input('密码：')
    confirm_password = input('确认密码：')
    if username and password == confirm_password:
        print('注册成功，欢迎 %s' %username)
        access_log.info('注册成功，欢迎 %s' %username)

        """用户账号信息"""
        user_account = {
            'username':username,
            'password':password,
            'balance':0

        }
        save_to_file(user_account)


def login():
    """登录
    """
    print('欢迎来到登录页面'.center(50, '*'))

    # retry = 0
    while not user_data['is_authed']:

        username = input('用户名：')
        password = input('密码：')
        account = read_file(username)  #调用read_file 寻找数据库里的账号
        if account:
            if account['username'] == username and account['password'] == password:
                # user_data字典包含认证状态，子字典account_data有账号信息
                user_data['account_data'] = account
                user_data['is_authed'] = True
                user_data['account_id'] = username
                # print ('%s,你已登录成功' %user_data['account_id'])
                access_log.info('%s,你已登录成功' %user_data['account_id'])
                # print('user_data',user_data)
                return user_data
            else:
                print('账号密码错误')
                # retry += 1
        else:
            print('账号没找到')
            # retry += 1

    else:
        print('%s 你已经登录了' %user_data['account_id'])
        return user_data


def logout():
    # print('%s，你已经退出成功' %user_data['account_id'])
    user_data['account_id'] = None
    user_data['is_authed'] = False
    user_data['account_data'] = {}
    access_log.info('%s已经退出成功' %user_data['account_id'])



def make_transaction(user_account,transaction,money=0,**kwargs):
    old_balance = user_account['account_data']['balance']

    if transaction in setting.transaction_type:
        fee = setting.transaction_type[transaction]['fee']
        if setting.transaction_type[transaction]['action'] == 'minus':
            new_balance = old_balance - money - fee
        elif setting.transaction_type[transaction]['action'] == 'plus':
            new_balance = old_balance + money + fee
        else:
            new_balance = old_balance

        if new_balance >= 0:
            user_account['account_data']['balance'] = new_balance
            trans_log.info('交易类型 %s，交易金额%.2f，交易账号%s' %(transaction,money,user_account['account_id']))
            save_to_file(user_account['account_data'])
        else:
            print('余额不足，不能完成操作')
    else:
        print('错误交易类型')
        return


def auth(f):
    """
    判断是否登录的装饰器
    :param f:
    :return:
    """

    def wrapper(*args,**kwargs):
        if user_data['is_authed']:
           return f(*args,**kwargs)
        else:
            print('您未登录')
    return wrapper

@auth
def query():
    """查询余额"""
    make_transaction(user_data, 'query',0)
    print('查询余额为：%.2f' %user_data['account_data']['balance'])


@auth
def withdraw():

    money = float(input('输入您要取出的金额：'))
    make_transaction(user_data,'withdraw',money)

@auth
def deposit():
    """存钱"""
    money = float(input('输入您要存的金额：'))
    make_transaction(user_data, 'deposit',money)


@auth
def transfer():
    money = float(input('输入您要转出的金额：'))
    username = input('输入对方的账号：')
    other_user = {}
    account = read_file(username)
    if account:
        other_user['account_data'] = account
        other_user['account_id'] = username
        other_user['is_authed'] = False

        make_transaction(user_data, 'withdraw', money)
        make_transaction(other_user, 'deposit', money)






def main():
    while True:
        print("""
欢迎来到ATM自动存取款系统的程序
1.注册
2.查询
3.取款
4.存款
5.转账
6.登录
7.退出
        """)

        actions = {
            '1':register,
            '2':query,
            '3':withdraw,
            '4':deposit,
            '5':transfer,
            '6':login,
            '7':logout
        }

        choice = input('输入你要进行的操作：')
        if choice in actions:
            actions[choice]()
        else:
            continue




if __name__ == '__main__':
    main()