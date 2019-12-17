import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='12345678', db='test',charset='utf8')

# 游标默认返回元组
# cursor = conn.cursor()

# 游标设置为字典，fetch返回字典格式
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


# 执行sql
cursor.execute("insert into account (username,password) values ('a','a')")

# 让改动更新到数据库
conn.commit()

# 获取数据
cursor.execute("select * from account")
data = cursor.fetchall()
print('移动前',data)

# 移动游标
cursor.scroll(0,'absolute') # 绝对位置
# cursor.scroll(1,'relative')   相对位置
data2 = cursor.fetchall()
print('移动后',data2)

# 获取自增id
cursor.execute("insert into account (username,password) values ('b','b')")
new_id = cursor.lastrowid
print('新id：',new_id)


# 关闭游标和数据库连接
cursor.close()
conn.close()

def add_account(username, password):
    """添加账号"""
    sql = "insert into account (username,password) values (%s,%s)"
    cursor.execute(sql,(username,password))
    conn.commit()
    data = cursor.fetchall()
    print(data)

def update_account(money,username):
    """修改账号"""
    sql = "update account set balance=%s where username=%s"
    cursor.execute(sql,(money,username))
    conn.commit()
    data = cursor.fetchone()
    print(data)

def get_account(username):
    """查询账号"""
    sql = "select * from account where username=%s"
    cursor.execute(sql,username)
    conn.commit()
    data = cursor.fetchone()
    cursor.scroll(0,'absolute')
    data2 = cursor.fetchall()
    print(data)
    print(data['username'])
    print('data2',data2)




