import pn532uid

import flask,json
from flask import request

'''

flask: seb using the decorator @server.route()
to transfer normal func into server login

'''
import pymysql

server = flask.Flask(__name__)

@server.route('/getThingOut',methods=['GET','post'])

def login():
    InputLanguage = request.values.get('Input')
    id = pn532uid()
    cursor = db.cursor()
 
# SQL 删除语句
    sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
    try:
    # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
    # 发生错误时回滚
        db.rollback()
    return True

server.run(debug=True,port=8801,host='0.0.0.0')
