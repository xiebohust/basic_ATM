import json
import os
from conf.setting import BaseDir



# 保存账号到文件
def save_to_file(user_account):
    account = json.dumps(user_account)
    file_path = BaseDir +'/account_db/' +user_account['username'] + '.json'
    with open(file_path, 'w') as f:
        f.write(account)
    print(user_account)

# 加载文件账号到内存
def read_file(username):
    file_path = BaseDir + '/account_db/' + username + '.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = f.read()
            account = json.loads(data)
            return account



if __name__ == "__main__":
    save_to_file({'username':'111'})
    print(read_file('111'))