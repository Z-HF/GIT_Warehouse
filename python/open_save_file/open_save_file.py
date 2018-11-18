# !/usr/bin/python3.6.5
# -*- coding:UTF-8 -*-

__author__ = {
    "name": "ZhuHaifang",
    "email": "1159878350@qq.com",
    "date": "2018-11-18 20:16:23",
    "Project": "打开保存文件",
    "Version": " V 1.0"
}

from tkinter import *

import win32ui

import win32con

file_type = 'All File(*.*)|*.*|' \
            'Html File(*.html)|*.html|' \
            'Image File(*.bmp .jpg .png)|*.png;*.jpg;*.bmp|' \
            'python File(*.py .pyc)|*.py;*.pyc|' \
            '|'

API_flag = win32con.OFN_OVERWRITEPROMPT | win32con.OFN_FILEMUSTEXIST

def Win_Open_File():

    print("Open File\n")

    dlg = win32ui.CreateFileDialog(1, None, None, API_flag, file_type)     # 指定为打开文件窗口

    dlg.SetOFNInitialDir("C:")

    dlg.DoModal()

    path = dlg.GetPathName()

    print(path)

def Win_Save_File():        # 保存文件时，文件后缀需要另处理

    print("Save File\n")

    dlg = win32ui.CreateFileDialog(0, None, None, API_flag, file_type)     # 指定为保存文件窗口

    dlg.SetOFNInitialDir('C:')     # 默认打开的位置

    dlg.DoModal()

    path = dlg.GetPathName()         # 获取打开的路径

    print(path)

MainWindows = Tk()  # 主窗体

MainWindows.title(__author__["Project"]+__author__["Version"])

MainWindows.geometry("500x300")

Button(text='WIN 打开文件', command=Win_Open_File).pack()

Button(text='WIN 保存文件', command=Win_Save_File).pack()

MainWindows.mainloop()

