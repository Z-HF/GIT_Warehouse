#!/usr/bin/python3.6.5
# -*- coding:UTF-8 -*-

PYTHONIOENCODING="UTF-8"  

__author__ = {
	"name": "ZhuHaifang",
	"mail": "11598778350@qq.com",
	"date": "2018-11-12 15:41:23",
	"object": "Python 翻译工具",
	"version": " V1.0"
}

#baidu = {"appid": "20181120000236966",
#		"key": "0RoAEI619PDaL93VXToR"}

API = {
	"百度": {"appid": "xxxxxxx",
			"key": "xxxxxxxxxx"},
	"有道": {"appid": "xxxxxxx",
			"key": "xxxxxxxxxx"},
	"谷歌": {"appid": "xxxxxxx",
			"key": "xxxxxxxxxx"}
}


'''
	思路：
		1、三个单选框选择翻译网站
		2、输入框输入要翻译的内容
		3、两个翻译语言选择控制（输入和输出）
		4、输出框输出翻译结果
'''
		
web_list = {"百度翻译": "http://api.fanyi.baidu.com/api/trans/vip/translate",
			"有道翻译": "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/",
			"谷歌翻译": "http://translate.google.cn"
			}	# 字典类型作为翻译网站索引
			
			
language = ('中文简体', 'English', '中文繁体', '粤语', '日本語', '한국어.', 'русский язык', 'Deutsch', 'Français')	# 元祖类型作为语言选择
baidu_type = ('zh', 'en', 'cht', 'yue', 'ja', 'kor', 'ru', 'de', 'fra')	
youdao_type = ('zh-CHS', 'en', 'cht', 'yue', 'ja', 'ko', 'ru', 'de', 'fr')
google_type = ('zh-CN', 'en', 'zh-TW', 'yue', 'ja', 'ko', 'ru', 'de', 'fr')	
			
from tkinter import *
import tkinter.messagebox
import requests
import string
import hashlib
import time
import json
import re
import urllib.parse, urllib.request
import urllib


def translate_baidu(i_type, o_type, i_text):	# 百度翻译

	o_text = '百度翻译'

	lower_case = list(string.ascii_lowercase)

	salt = str(time.time())[:10]

	final_sign = str(API["百度"]["appid"]) + i_text + salt + str(API["百度"]["key"])
	
	final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
	
	paramas = {
		'q': i_text,
		'from': baidu_type[i_type],
		'to': baidu_type[o_type],
		'appid': '%s'%API["百度"]["appid"],
		'salt': '%s'%salt,
		'sign': '%s'%final_sign
		}

	my_url = web_list["百度翻译"]+'?appid='+str(API["百度"]["appid"])+'&q='+i_text+'&from='+baidu_type[i_type]+'&to='+baidu_type[o_type]+'&salt='+salt+'&sign='+final_sign

	try:
		response = requests.get(web_list["百度翻译"], params=paramas).content

		content = str(response, encoding='utf-8')

		json_reads = json.loads(content)

		o_text = json_reads['trans_result'][0]['dst']

		return o_text

	except:
		o_text = translate_offline(i_type, o_type, i_text)

		return o_text
	
	
def translate_youdao(i_type, o_type, i_text):	# 有道翻译
	o_text = '有道翻译'
	dict = {}
	dict['type'] = youdao_type[i_type]+"2"+	youdao_type[o_type]#'AUTO'
	dict['doctype'] = 'json'
	dict['xmlVersion'] = '1.8'
	dict['keyfrom'] = 'fanyi.web'
	dict['ue'] = 'UTF-8'
	dict['action'] = 'FY_BY_CLICKBUTTON'
	dict['typoResult'] = 'true'
	dict['i'] = i_text
	try:
		data = urllib.parse.urlencode(dict).encode('utf-8')
		response = urllib.request.urlopen(web_list["有道翻译"], data)
		content = response.read().decode('utf-8')
		data = json.loads(content)
		o_text = data['translateResult'][0][0]['tgt']
		return o_text
	except:
		o_text = translate_offline(i_type, o_type, i_text)
		return o_text
	
	
def translate_google(i_type, o_type, i_text):	# 谷歌翻译

	o_text = '谷歌翻译'

	reg_text = re.compile(r'(?<=TRANSLATED_TEXT=).*?;')

	user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 r'Chrome/44.0.2403.157 Safari/537.36'

	values = {'hl': 'zh-cn', 'ie': 'utf-8', 'text': i_text, 'langpair': '%s|%s' % (google_type[i_type], google_type[o_type])}

	value = urllib.parse.urlencode(values)

	req = urllib.request.Request(web_list["谷歌翻译"] + '?' + value)

	req.add_header('User-Agent', user_agent)
	
	try:
		response = urllib.request.urlopen(req)

		content = response.read().decode('utf-8')

		data = reg_text.search(content)

		o_text = data.group(0).strip(';').strip('\'')

		return o_text

	except:
		o_text = translate_offline(i_type, o_type, i_text)

		return o_text
	
	
def translate_offline(i_type, o_type, i_text):	# 离线翻译
	o_text = '离线翻译'
	try:	
		return o_text
	except:
		return 'offline translate error!'
	
	
def show_help():

	msg = '''
帮助文档：
    1. 到对应官网申请你的API，方法可百度
    2. 将你的API在菜单“API”中填入
    3. 点击“确定”，确认输入你的API
    4. 输入完成后即可使用翻译小工具
	'''
	
	tkinter.messagebox.showinfo(title="帮助", message=msg)

def call_author():

	msg = __author__["name"]+'\n\n'+__author__["mail"]+'\n\n'+__author__["date"]
	
	tkinter.messagebox.showinfo(title="作者", message=msg)

pyticon = False

user_api = False

def open_apifile_icon():
	
	try:		# 检测图标是否存在
		with open(r"pyt.ico", "r") as ico:
			u_ico = True
	except:
		u_ico = False
		
	try:		# 检测API是否存在
		with open(r"API.api", "r") as api:
			i_api = eval(api.read())	# 将API读取为字典
			u_api = True
	except:
		i_api = API
		u_api = False

	return u_ico, u_api, i_api


class Windows:

	def __init__(self, master):		# 菜单及控件初始化

		menu = Menu(master)
	
		api_menu = Menu(menu, tearoff=0)

		api_menu.add_command(label="百度", command=self.baidu_api)
		
		api_menu.add_command(label="有道", command=self.youdao_api)

		api_menu.add_command(label="谷歌", command=self.google_api)

		menu.add_cascade(label="API", menu=api_menu)

		
		help_menu = Menu(menu, tearoff=0)

		help_menu.add_command(label="帮助文档", command=show_help)

		help_menu.add_command(label="联系作者", command=call_author)

		menu.add_cascade(label="帮助", menu=help_menu)

		master.config(menu=menu)

		
		self.baidu_button = Radiobutton(master, text='百度翻译', variable = translate_channel, value = 0)
		
		self.baidu_button.place(x=10, y=10)
		
		self.youdao_button = Radiobutton(master, text='有道翻译', variable = translate_channel, value = 1)
		
		self.youdao_button.place(x=180, y=10)
		
		self.google_button = Radiobutton(master, text='谷歌翻译', variable = translate_channel, value = 2)
		
		self.google_button.place(x=350, y=10)
		
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
		
		

	def baidu_api(self):

		global API_baidu, baidu_appid, baidu_passw
		
		API_baidu = Tk()

		API_baidu.title("输入百度 API")

		API_baidu.geometry("280x90")

		API_baidu.resizable(width=False, height=False)

		appid_label = Label(API_baidu, text="APP ID:")
	
		appid_label.place(x=10, y=20)

		baidu_appid = Entry(API_baidu)

		baidu_appid.place(x=60, y=20)

		passw_label = Label(API_baidu, text="KEY: ")

		passw_label.place(x=10, y=50)

		baidu_passw = Entry(API_baidu)

		baidu_passw.place(x=60, y=50)

		baidu_button = Button(API_baidu, text="确定", command=self.quit_baidu_api)

		baidu_button.place(x=220, y=30)

		API_baidu.mainloop()

	def quit_baidu_api(self):

		API["百度"]["appid"] = baidu_appid.get()

		API["百度"]["key"] = baidu_passw.get()

		api = open(".\\API.api", "w")

		api.write(str(API))

		api.close()

		print(API["百度"]["appid"], API["百度"]["key"])
		
		API_baidu.destroy()


	def youdao_api(self):

		global API_youdao, youdao_appid, youdao_passw
		
		API_youdao = Tk()

		API_youdao.title("输入有道 API")

		API_youdao.geometry("280x90")

		API_youdao.resizable(width=False, height=False)

		appid_label = Label(API_youdao, text="APP ID:")
	
		appid_label.place(x=10, y=20)

		youdao_appid = Entry(API_youdao)

		youdao_appid.place(x=60, y=20)

		passw_label = Label(API_youdao, text="KEY: ")

		passw_label.place(x=10, y=50)

		youdao_passw = Entry(API_youdao)

		youdao_passw.place(x=60, y=50)

		baidu_button = Button(API_youdao, text="确定", command=self.quit_youdao_api)

		baidu_button.place(x=220, y=30)

		API_youdao.mainloop()

	def quit_youdao_api(self):

		API["有道"]["appid"] = youdao_appid.get()

		API["有道"]["key"] = youdao_passw.get()

		api = open(".\\API.api", "w")

		api.write(str(API))

		api.close()

		print(youdao_appid.get(), youdao_passw.get())
		
		API_youdao.destroy()


	def google_api(self):

		global API_google, google_appid, google_passw
		
		API_google = Tk()

		API_google.title("输入谷歌 API")

		API_google.geometry("280x90")

		API_google.resizable(width=False, height=False)

		appid_label = Label(API_google, text="APP ID:")
	
		appid_label.place(x=10, y=20)

		google_appid = Entry(API_google)

		google_appid.place(x=60, y=20)

		passw_label = Label(API_google, text="KEY: ")

		passw_label.place(x=10, y=50)

		google_passw = Entry(API_google)

		google_passw.place(x=60, y=50)

		baidu_button = Button(API_google, text="确定", command=self.quit_google_api)

		baidu_button.place(x=220, y=30)

		API_google.mainloop()

	def quit_google_api(self):

		API["谷歌"]["appid"] = google_appid.get()

		API["谷歌"]["key"] = google_passw.get()

		api = open(".\\API.api", "w")

		api.write(str(API))

		api.close()

		print(google_appid.get(), google_passw.get())
		
		API_google.destroy()

	
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
		
		if use_website == 0 and user_api == True:
		
			#print(str(use_website) , web_list['百度翻译'])
			
			out_text = translate_baidu(in_type, out_type, in_text)
			
			self.output_entry.delete(0, END)
			
			self.output_entry.insert(0, out_text)
		
		elif use_website == 1 and user_api == True:
		
			#print(str(use_website) , web_list['有道翻译'])
			
			out_text = translate_youdao(in_type, out_type, in_text)
			
			self.output_entry.delete(0, END)
			
			self.output_entry.insert (0, out_text)
			
		elif use_website == 2:
		
			#print(str(use_website) , web_list['谷歌翻译'])
			
			out_text = translate_google(in_type, out_type, in_text)
			
			self.output_entry.delete(0, END)
			
			self.output_entry.insert (0, out_text)

		else:

			#print("translate offline")
			
			out_text = translate_offline(in_type, out_type, in_text)
			
			self.output_entry.delete(0, END)
			
			self.output_entry.insert (0, out_text)
			
pyticon, user_api, API = open_apifile_icon()	# 检测图标和API，并读入API

MainWindows = Tk()	# 窗体初始化及设置

translate_channel = StringVar()

input_text = StringVar()

output_text = StringVar()

input_type = StringVar()

input_type.set('0')

output_type = StringVar()

output_type.set('1')

MainWindows.title(__author__['object']+__author__['version'])

MainWindows.resizable(width=False, height=False)

if pyticon:
	MainWindows.iconbitmap(".\\pyt.ico")
	MainWindows.geometry('440x190')
else:
	MainWindows.geometry('440x170')

app = Windows(MainWindows)

MainWindows.mainloop()









