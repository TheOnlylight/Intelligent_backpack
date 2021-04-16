import pymysql

db = pymysql.connect(host="localhost",user="testuser",password="test123",database="TODO" )


cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预理语句创建表
sql = """CREATE TABLE EMPLOYEE (
            FIRST_NAME  CHAR(20) NOT NULL,
            LAST_NAME  CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT )"""
cursor.execute(sql)


# how to  take the desired data from the DB
sql = "SELECT * FROM EMPLOYEE \WHERE INCOME > %s" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                (fname, lname, age, sex, income ))
except:
    print ("Error: unable to fetch data")