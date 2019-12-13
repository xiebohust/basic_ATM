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
import json
import os


user_data = {
    'accound_id':None,
    'is_authed': False,
    'account_data':None
}


def save_to_file(user_account):
    account = json.dumps(user_account)
    file_path = user_account['username'] + '.json'
    with open(file_path, 'w') as f:
        f.write(account)
    print(user_account)

def read_file(username):
    file_path = username + '.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = f.read()
            account = json.loads(data)
    return account


def register():
    """1.注册（用户名，手机号，身份证号(18位)，密码（确认两次）（长度6位））
"""
    print('欢迎来到注册页面'.center(50, '*'))
    username = input('用户名：')
    password = input('密码：')
    confirm_password = input('确认密码：')
    if username and password == confirm_password:
        print('注册成功，欢迎 %s' %username)

        '用户账号信息'
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

    retry = 0
    while user_data['is_authed'] == False and retry < 3:

        username = input('用户名：')
        password = input('密码：')

        file_path = username + '.json'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data = f.read()
                account  = json.loads(data)
            print(account)
            if account['username'] == username and account['password'] == password:
                # user_data字典包含认证状态，子字典account_data有账号信息
                user_data['account_data'] = account
                user_data['is_authed'] = True
                user_data['accound_id'] = username
                print('user_data',user_data)
                return user_data
            else:
                print('账号密码错误')
                retry += 1
        else:
            print('账号没找到')
            retry += 1
    else:
        print('你错了3次了，拜拜')
        exit()

def login_auth(user):
    def wrapper(f):
        def inner(*args, **kwargs):
            if user['status']:
                return f(*args, **kwargs)
            else:
                login()
        return inner
    return wrapper


def query_account():
    if user_data['is_authed']:
        print('余额',user_data['account_data']['balance'])
    else:
        print('您未登录')

def withdraw():
    pass

def deposit():
    if user_data['is_authed']:
        money = float(input('输入您要存的金额：'))
        user_data['account_data']['balance'] += money
        save_to_file(user_data['account_data'])
    else:
        print('您未登录')


def transfer():
    pass



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
        """)

        actions = {
            '1':register,
            '2':query_account,
            '3':withdraw,
            '4':deposit,
            '5':transfer,
            '6':login
        }

        choice = input('输入你要进行的操作：')
        if choice in actions:
            actions[choice]()
        else:
            continue




if __name__ == '__main__':
    main()