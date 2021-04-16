import flask,json
from flask import request
from TimeNormalizer import TimeNormalizer # 引入包

tn = TimeNormalizer()

'''

flask: seb using the decorator @server.route()
to transfer normal func into server login

'''

server0 = flask.Flask(__name__)

@server0.route('/getTimeFrom',methods=['GET','post'])

def login():
    InputLanguage = request.values.get('Input')
    res = tn.parse(InputLanguage)
    return res

server0.run(debug=True,port=8888,host='0.0.0.0')

server1 = flask.Flask(__name__)

@server1.route('/getTimeFrom',methods=['GET','post'])

def login0():
    InputLanguage = request.values.get('Input')
    res = tn.parse(InputLanguage)
    return res

server1.run(debug=True,port=8848,host='0.0.0.0')
