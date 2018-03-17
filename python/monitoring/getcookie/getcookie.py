from selenium import webdriver
from selenium.webdriver.common.by import By #
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
import time
import threading
import os
import json
import sys
import re
import tkinter
import requests
import pyquery
from multiprocessing import Process
import random
import queue
import pymysql
import platform
import uuid

class MonitoringDZ(object):
	public = {}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
	path = os.path.dirname(sys.argv[0])+'/'
	def __init__(self):
		self.local = threading.local() 
		self.setPath()#设置环境变量
		self.permissions()
		if not os.path.exists(self.path+'log'):
			os.mkdir(self.path+'log')
		if not os.path.exists(self.path+'cookies'):
			os.mkdir(self.path+'cookies')
		global getcookielog
		getcookielog = open(self.path+'log/getcookie.log','a',encoding='utf8')
		getcookielog.write('['+time.strftime('%Y-%m-%d %H:%M:%S')+']\r')
	

	def permissions(self):
		"""权限控制"""
		#获取硬盘序列
		try:
			sysstr = platform.system()
			idstr = str(uuid.uuid1()).split("-")[4]
			permissions = requests.get('http://permissions.hk-dna.cc/permissions.php?disk='+sysstr+'_'+idstr).text
			if(permissions != 'off'):
				print('请更新版本')
				sys.exit()
		except Exception as e:
			print(e)
			print('请更新版本')
			sys.exit()
		
	
	def showlog(self,browser,msg):
		print(msg)
		getcookielog.write(msg)
		getcookielog.flush()
		browser.quit()
		myqueue.get()
		sys.exit()


	def config(self):
		try:
			database = {}
			configs = {'config':[]}
			with open(self.path+'config.ini','r',encoding='utf8') as f:
				for line in f.readlines():
					line = line.strip()#去除两段空字符
					#如果为空或者为注释跳过
					if len(line) < 1 or line[0] == '#':
						continue
					#配置文件类型
					if line[0] == '[' and line[-1] == ']':
						class_ = line[1:-1]

					#数据库
					if '=' in line and class_ == 'database':
						conf = line.split('=')
						database[conf[0].strip()] = conf[1].strip()
					#公共
					if '=' in line and class_ == 'public':
						conf = line.split('=')
						self.public[conf[0].strip()] = conf[1].strip()

		except Exception as e:
			print('配置文件错误')
			exit()
		
		try:
			connect = pymysql.connect(host=database['host'],user=database['user'],passwd=database['passwd'],db=database['db'],charset=database['charset'],port=int(database['port']))
			cursor = connect.cursor();#创建一个游标
			return cursor

		except Exception as e:
			print('数据库连接失败')
			exit()
		



	def login(self,url,username,password,loginnum=1):
		'''登录'''
		try:
			print('正在登录 ',url)
			#判断cookie文件是否存在 如果存在用cookie登陆
			browser = webdriver.Chrome()#声明一个浏览器对象
			# wait = WebDriverWait(browser,30)
			try:
				browser.get(url+'/member.php?mod=logging&action=login')#访问登录页面
				inputusername = browser.find_element(By.CSS_SELECTOR,'input[name=username]') 
				inputusername.send_keys(username)#向用户输入框发送用户名
				inputpassword = browser.find_element(By.CSS_SELECTOR,"input[name='password']") 
				inputpassword.send_keys(password)#向密码输入框发送密码
			except Exception as e:
				self.showlog(browser,url+"\t失败，无法登陆此网站\r")
			
			#等待点击确定登陆
			i = 1800
			while True:
				message = ''
				try:
					message = browser.find_element(By.CSS_SELECTOR,'#succeedlocation').get_attribute('innerHTML')
				except Exception as e:
					pass
				try:
					message = browser.find_element(By.CSS_SELECTOR,'.pc_inner,.alert_error').get_attribute('innerHTML')
				except Exception as e:
					pass

				try:
					geturl_ = browser.current_url
				except Exception as e:
					print(url,'\t手动关闭了浏览器')
					myqueue.get()
					browser.quit()
					sys.exit()
				#获取到信息后跳出循环
				if message:
					break
				# 如果等待时间小于等于0退出
				if i <= 0:
					self.showlog(browser,url+"\t超时退出\r")

				#每一秒钟检测一次
				print(url+"\t等待时间剩余 "+ str(i)+" 秒")
				i -= 1
				time.sleep(1)

			#判断是否登录成功
			if username.lower() in message.lower():
				#登录成功
				dictCookies = browser.get_cookies()
				jsonCookies = json.dumps(dictCookies)
				# 登录完成后，将cookie保存到本地文件
				cookiefile = self.path+'cookies/'+url.replace('http://','').replace('https://','')+'.json'
				with open(cookiefile, 'w',encoding='utf8') as f:
				    f.write(jsonCookies)
				#等待所以登录完成
				browser.set_window_size(0,0)
				self.showlog(browser,url+"\t获取cookie成功\r")

			else:
				#登录失败
				self.showlog(browser,url+"\t获取cookie失败！错误信息："+message+"\r")

		except Exception as e:
			myqueue.get()
			exit()
			pass
			# print(e)
		time.sleep(10)	



	def __del__(self):
		mystr=os.popen("taskkill /F /im chromedriver*")
		# os.popen('taskkill /F /im chromedriver.exe')
		# os.popen('taskkill /F /im phantomjs*')
		# os.popen('taskkill /F /im python*')
		print('结束')

	def setPath(self):
		"""设置环境变量"""
		#当前目录加入环境变量
		dir_ = self.path
		path = dir_+'phantomjs/bin'
		# print (os.environ["TEMP"])
		mydir = os.path.normpath(path)
		os.environ["PHANTOMJS"] = mydir
		# print (os.environ["MYDIR"])
		pathV = os.environ["PATH"]
		# print (pathV)
		os.environ["PATH"]= mydir + ";" + os.environ["PATH"]


	def main(self):
		#检测配置文件
		cursor = self.config();
		if not cursor:
			print('配置文件错误')
			time.sleep(10)
			sys.exit()
		else:
			global myqueue
			myqueue = queue.Queue(maxsize = int(self.public['thrnumber']))
			joinlist = []
			infoid = 0
			while True:
				try:
					sql = "select id,url,username,password from info where perform = 1 and registered = 1 and id > "+str(infoid)+" limit 1"
					cursor.execute(sql)
					data = cursor.fetchall()
					if data:
						data0 = data[0]
						infoid = data0[0]
						#检测cookie
						cookiefile = self.path+'cookies/'+data0[1].replace('http://','').replace('https://','')+'.json'
						if os.path.exists(cookiefile):
							continue

						print('正在启动 ',data0[1],' 站点...')
						myqueue.put(data0[0])
						w = threading.Thread(target=self.login,args=(str(data0[1]),data0[2],data0[3],))
						w.start()
						joinlist.append(w)
					else:

						break
				except Exception as e:
					print(e)
					continue
			
			for j in joinlist:
				j.join()
			time.sleep(10)
			print('没有了')
if __name__ == '__main__':
	MonitoringDZ().main()
	sys.exit()