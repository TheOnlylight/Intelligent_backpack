import pymysql
def dbInit():
    db = pymysql.connect(host="localhost",user="testuser",password="test123",database="TODO" )
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS TAGS")
    # 使用预理语句创建表
    sql = """CREATE TABLE TAGS (
                OBJNAME  CHAR(20) NOT NULL,
                OBJID json, )"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS LOGS")
    # 使用预理语句创建表
    sql = """CREATE TABLE LOGS (
                OBJNAME  CHAR(20) NOT NULL,
                ACT_TIME JSON,
                ACT int )"""
    cursor.execute(sql)
    
    cursor.execute("DROP TABLE IF EXISTS WITHIN")
    # 使用预理语句创建表
    sql = """CREATE TABLE LOGS (
                OBJNAME  CHAR(20) NOT NULL,
                TIME JSON,
                SEX CHAR(1),
                INCOME FLOAT )"""
    cursor.execute(sql)
    
dbInit()