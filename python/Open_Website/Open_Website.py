# !/usr/bin/python3.6.5
# -*- coding:UTF-8 -*-

__author = {
    "name": "ZhuHaifang",
    "email": "1159878350@qq.com",
    "date": "2018-11-2 22:16:30"
}

'''
Use Way:
    1. Copy Website in Entry
    2. Set the time to open Website
    3. Click the Confirm button
Design ideas:
    1. Use the tkinter GUI tools buy python to build a windows
    2. Make a Enter control input the Website
    3. Make three Enter control set time(hour, minute, second)
    4. Make a button to start program
        a). get Website and open time
        b). get system time and contrast open time
            if system time is open time ---> open Website
            else ---> program sleep one second
'''

from tkinter import *

from tkinter import messagebox

import datetime

import webbrowser

import threading

import re

def Check_Type(time, website):

    tim = re.compile(r'^(0?[0-9]|1[0-9]|2[0-3]):(0?[0-9]|[1-5][0-9]):(0?[0-9]|[1-5][0-9])$')

    web = re.compile(r'^(?:http|ftp)s?://')

    time_type = tim.search(time)

    web_type = web.search(website)

    print(time_type.group(), web_type.group())

    print(re.match(r'http', website), re.match(tim, time))

def Open_Website():

    web = website.get()

    time = opentime.get()

    # Check_Type(time, web)

    if web == '' or time == '':

        messagebox.showinfo('输入错误', '请输入正确的网址和时间！')

        return

    # elif Check_Type(time, web) == False:

        # messagebox.showinfo('格式错误', '请输入正确的网址和时间格式\n注意时间间隔为英文状态下的冒号！')

        # return

    else:

        systime = datetime.datetime.now().strftime('%H:%M:%S')

        if systime >= time:

            webbrowser.open(web)

            messagebox.showinfo('设定时间到', '设定时间已到，网址已打开')

            return

        else:

            sec = threading.Timer(1, Open_Website)

            sec.setDaemon(True)

            Label(MainWindows, text=systime).place(x=170, y=50)

            sec.start()

MainWindows = Tk()

website = StringVar()

opentime = StringVar()

MainWindows.geometry('340x85')     # set window size

MainWindows.title('网站闹钟')       # set window title

MainWindows.resizable(width=False, height=False)

# MainWindows.iconbitmap('logo.ico')    # set window icon

Label(MainWindows, text='目标网址：').place(x=10, y=10)

Entry(MainWindows, textvariable=website).place(x=75, y=10, width=250)

Label(MainWindows, text='打开时间：').place(x=10, y=50)

opentime.set('00:00:00')

Entry(MainWindows, textvariable=opentime).place(x=75, y=50, width=70)

Button(MainWindows, text='启动定时', command=Open_Website).place(x=265, y=45)

MainWindows.mainloop()

