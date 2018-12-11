# !/usr/bin/python 3.6.5
# -*- coding:utf-8 -*-


__author__ = {
    "name": "ZhuHaifang",
    "email": "1159878350@qq.com",
    "data": "2018-12-11 23:03:30",
    "project": "Python 串口工具",
    "version": " V1.0"
}

'''
    python 串口通信示例代码
    可以正常收发数据
'''

import time
import _thread
import serial
import threading

class myserial:
    recdata = ""
    def __init__(self, port, baudrate, timeout):
        self.port = serial.Serial(port, baudrate)

        if(self.port.is_open):
            print("打开", self.port.portstr)
        else:
            print("打开端口失败")

    def recevemsg(self):
        while True:
            size = self.port.in_waiting

            if size:
                self.recdata = self.port.read_all().decode('utf-8')
                if self.recdata != "":
                    print("rec at", time.ctime(), '\n', str(self.recdata))
                    self.recdata = ""

    def sendmsg(self):
        while True:
            senddata = input("plz input:")
            senddata = senddata.encode('utf-8')
            self.port.write(senddata)


if __name__ == '__main__':

    print("starting")
    # 实例化
    myport = myserial('COM3', baudrate=9600, timeout=1)
    # 线程开启
    _thread.start_new_thread(myport.sendmsg, ())
    # _thread.start_new_thread(myport.recevemsg, ())
    print("here")
    while True:
        time.sleep(1)
        myport.recevemsg()


