import time
import binascii

from pn532pi import Pn532, pn532
from pn532pi import Pn532I2c
from pn532pi import Pn532Spi
from pn532pi import Pn532Hsu

import flask,json
from flask import request
from TimeNormalizer import TimeNormalizer # 引入包

'''

flask: seb using the decorator @server.route()
to transfer normal func into server login

'''

server = flask.Flask(__name__)

@server.route('/getIDFrom',methods=['GET','post'])

def login():
    InputLanguage = request.values.get('Input')
    PN532_I2C = Pn532I2c(1)
    nfc = Pn532(PN532_I2C)
    nfc.begin()
    versiondata = nfc.getFirmwareVersion()
    if (not versiondata):
        print("Didn't find PN53x board")
        raise RuntimeError("Didn't find PN53x board")  # halt

    #  Got ok data, print it out!
    print("Found chip PN5 {:#x} Firmware ver. {:d}.{:d}".format((versiondata >> 24) & 0xFF, (versiondata >> 16) & 0xFF,
                                                                (versiondata >> 8) & 0xFF))

    #  configure board to read RFID tags
    nfc.SAMConfig()
    success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
    res = format(binascii.hexlify(uid))
    return res

server.run(debug=True,port=8848,host='0.0.0.0')
