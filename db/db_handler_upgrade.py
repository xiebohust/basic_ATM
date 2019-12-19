import pymysql


def account_operation(action,username,password=None,money=None):
    if action == 'add':
        sql = "insert into account (username,password) values (%s,%s)"
        cursor.execute(sql, (username, password))

    elif action == 'update':
        """修改账号"""
        sql = "update account set balance=%s where username=%s"
        cursor.execute(sql, (money, username))

    elif action == 'get':
        """查询账号"""
        sql = "select * from account where username=%s"
        cursor.execute(sql, username)
        data = cursor.fetchone()
        print(data)
    conn.commit()


if __name__ == "__main__":
    # 连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='12345678', db='test', charset='utf8')

    # 游标设置为字典，fetch返回字典格式
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    account_operation('add','ab','2')
    account_operation('get','a','1','1')
    account_operation('update','a',money=12)
    account_operation('get','a')

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()

