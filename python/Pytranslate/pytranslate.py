#!/usr/bin/python3.6.5
# -*- coding:UTF-8 -*-

#PYTHONIOENCODING = "UTF-8"

__author__ = {
	"name": "ZhuHaifang",
	"mail": "11598778350@qq.com",
	"date": "2018-11-12 15:41:23",
	"object": "Python 翻译工具",
	"version": " V1.0"
}


'''
	思路：
		1、三个单选框选择翻译网站
		2、输入框输入要翻译的内容
		3、两个翻译语言选择控制（输入和输出）
		4、输出框输出翻译结果
		---------------------------------------------
		|	Python 翻译工具							|
		|											|
		|	百度翻译	有道翻译	谷歌翻译		|
		|											|
		|		输入语言			输出语言		|
		|											|
		| 要翻译的内容：________________________	|
		|											|
		| 翻译结果：	________________________	|
		|											|
		---------------------------------------------
'''
		
web_list = {"百度翻译": "http://fanyi.baidu.com/v2transapi",
			"有道翻译": "http://fanyi.youdao.com/",
			"谷歌翻译": "https://translate.google.cn/"
			}	# 字典类型作为翻译网站索引
			
			
language = ('中文简体', 'English', '中文繁体', '日本語', '한국어.', 'русский язык')	# 元祖类型作为语言选择
			

from tkinter import *


def translate_baidu(i_type, o_type, i_text):	# 百度翻译
	o_text = 'baidu'
	try:
		return o_text
	except:
		o_text = translate_offline()
		return o_text
	
	
def translate_youdao(i_type, o_type, i_text):	# 有道翻译
	o_text = 'youdao'
	try:
		
		return o_text
	except:
		o_text = translate_offline()
		return o_text
	
	
def translate_google(i_type, o_type, i_text):	# 谷歌翻译
	o_text = 'google'
	try:
		return o_text
	except:
		o_text = translate_offline()
		return o_text
	
	
def translate_offline(i_type, o_type, i_text):	# 离线翻译
	o_text = 'offline'
	try:	
		return o_text
	except:
		return 'offline translate error!'
	
	

class Windows:

	def __init__(self, master):		# 菜单及控件初始化
		
		self.baidu_button = Radiobutton(master, text='百度翻译', variable = translate_channel, value = 0)
		
		self.baidu_button.place(x=10, y=10)
		
		self.youdao_button = Radiobutton(master, text='有道翻译', variable = translate_channel, value = 1)
		
		self.youdao_button.place(x=180, y=10)
		
		self.guge_button = Radiobutton(master, text='谷歌翻译', variable = translate_channel, value = 2)
		
		self.guge_button.place(x=350, y=10)
		
		translate_channel.set('0')

		
		input_language=language[int(input_type.get())]	# 选择输入语言按钮
		
		self.input_button = Menubutton(master, text=input_language, relief=RAISED)
		
		self.input_button.place(x=10, y=50, width=200)
		
		input_menu = Menu(self.input_button, tearoff=False)
		
		for i in range(0, len(language)):
		
			input_menu.add_radiobutton(label=language[i], variable=input_type, value=i, command=self.set_input_text)
		
		self.input_button.config(menu=input_menu)
		
		
		output_language = language[int(output_type.get())]	# 选择输出语言按钮
		
		self.output_button = Menubutton(master, text=output_language, relief=RAISED)
		
		self.output_button.place(x=230, y=50, width=200)
		
		output_menu = Menu(self.output_button, tearoff=False)
		
		for j in range(0, len(language)):
		
			output_menu.add_radiobutton(label=language[j], variable=output_type, value=j, command=self.set_output_text)
			
		self.output_button.config(menu=output_menu)
		
		
		input_text.set('输入要翻译的内容：')
		
		self.input_entry = Entry(master, textvariable=input_text, width=28, xscrollcommand=self.translate_text)
		
		self.input_entry.place(x=10, y=100, height=50)
		
		
		output_text.set('翻译结果为：')
		
		self.output_entry = Entry(master, textvariable=output_text, width=28)
		
		self.output_entry.place(x=230, y=100, height=50)
		
		
		
	def set_input_text(self):
		
		self.input_button['text'] = language[int(input_type.get())]
		
		
	def set_output_text(self):
	
		self.output_button['text'] = language[int(output_type.get())]
		
			
	def translate_text(self, a, b):	# Entry控件回调函数有三个输入参数，可不调用
	
		# print(self, a, b)
		
		use_website = int(translate_channel.get())	# 选择的翻译网站
		
		in_type = int(input_type.get())				# 输入语种
		
		out_type = int(output_type.get())			# 输出语种
		
		in_text = input_text.get()					# 输入的内容
		
		if use_website == 0:
		
			print(str(use_website) , web_list['百度翻译'])
			
			out_text = translate_baidu(in_type, out_type, in_text)
			
			self.output_entry.delete(0, END)
			
			self.output_entry.insert (0, out_text)
		
		elif use_website == 1:
		
			print(str(use_website) , web_list['有道翻译'])
			
			out_text = translate_youdao(in_type, out_type, in_text)
			
			self.output_entry.delete(0, END)
			
			self.output_entry.insert (0, out_text)
			
		else:
		
			print(str(use_website) , web_list['谷歌翻译'])
			
			out_text = translate_google(in_type, out_type, in_text)
			
			self.output_entry.delete(0, END)
			
			self.output_entry.insert (0, out_text)			
			
			

MainWindows = Tk()	# 窗体初始化及设置

translate_channel = StringVar()

input_text = StringVar()

output_text = StringVar()

input_type = StringVar()

input_type.set('0')

output_type = StringVar()

output_type.set('1')

MainWindows.title(__author__['object']+__author__['version'])

MainWindows.geometry('440x170')

MainWindows.resizable(width=False, height=False)

app = Windows(MainWindows)

MainWindows.mainloop()









