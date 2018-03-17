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
	registered_ = {}
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
		getcookielog = open(self.path+'log/getcookieone.log','a',encoding='utf8')
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
		
	
	def showlog(self,browser,msg,quit=0):
		print(msg)
		getcookielog.write(msg)
		getcookielog.flush()

		if int(self.registered_['exit']) or quit == 0:
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
					#注册配置
					if '=' in line and class_ == 'registered':
						conf2 = line.split('=')
						self.registered_[conf2[0].strip()] = conf2[1].strip()

		except Exception as e:
			# print(e)
			print('配置文件错误')
			exit()
		
		try:
			global connect
			connect = pymysql.connect(host=database['host'],user=database['user'],passwd=database['passwd'],db=database['db'],charset=database['charset'],port=int(database['port']))
			global cursor
			cursor = connect.cursor();#创建一个游标
			return cursor

		except Exception as e:
			print('数据库连接失败')
			exit()
		



	def registered(self,id_,url,username,password,email,loginnum=1,browser=0):
		'''注册'''
		try:
			if loginnum == 1:
				print('正在注册 ',url)
				#判断cookie文件是否存在 如果存在用cookie登陆
				browser = webdriver.Chrome()#声明一个浏览器对象
				# wait = WebDriverWait(browser,30)
			try:
				if loginnum == 1:
					browser.get(url+'/member.php?mod=register')#访问注册页面
				try:
					geturl_one = browser.current_url
				except Exception as e:
					print(url,'\t手动关闭了浏览器')
					myqueue.get()
					browser.quit()
					sys.exit()
				#查找input框
				inputs = browser.find_elements(By.CSS_SELECTOR,'#reginfo_a th')
				password__ = False
				confirmpassword__ = False
				for inp in inputs:
					text = inp.get_attribute('textContent')
					if '用户名' in text or '用戶名' in text:
						name = inp.find_element(By.CSS_SELECTOR,"label").get_attribute('for')
						inputusername = browser.find_element(By.CSS_SELECTOR,"input[name='"+name+"']") 
						inputusername.send_keys(username)#向用户输入框发送用户名


					if ('密码' in text or '密碼' in text) and not password__:
						password__ = True
						password_ = inp.find_element(By.CSS_SELECTOR,"label").get_attribute('for')
						inputpassword = browser.find_element(By.CSS_SELECTOR,"input[name='"+password_+"']") 
						inputpassword.send_keys(password)

					if ('确认密码' in text or '確認密碼' in text) and not confirmpassword__:
						confirmpassword__ = True
						confirmpassword = inp.find_element(By.CSS_SELECTOR,"label").get_attribute('for')
						inputconfirmpassword = browser.find_element(By.CSS_SELECTOR,"input[name='"+confirmpassword+"']") 
						inputconfirmpassword.send_keys(password)

					if 'email' in text.lower() or '邮箱' in text or '郵箱' in text:
						email_ = inp.find_element(By.CSS_SELECTOR,"label").get_attribute('for')
						inputemail = browser.find_element(By.CSS_SELECTOR,"input[name='"+email_+"']") 
						inputemail.send_keys(email)
					
					
				
			except Exception as e:
				# self.showlog(browser,url+"\t失败，无法注册此网站\r")
				print(url+'\t无法识别此网站,请尝试手动注册')
			
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
			if '完善资料' in message or '逛逛' in message or '完善資料' in message:
				time.sleep(3)
				self.setstatus(id_)
				#登录成功
				dictCookies = browser.get_cookies()
				jsonCookies = json.dumps(dictCookies)
				# 登录完成后，将cookie保存到本地文件
				cookiefile = self.path+'cookies/'+url.replace('http://','').replace('https://','')+'.json'
				with open(cookiefile, 'w',encoding='utf8') as f:
				    f.write(jsonCookies)
				#等待所以登录完成
				# browser.set_window_size(0,0)
				self.showlog(browser,url+"\t获取cookie成功\r",1)
				#修改资料
				self.updatedata(browser,url)

				# if self.registered_['exit']:
				# 	self.showlog(browser,url+"\t获取cookie成功\r")
				# else:
				# 	self.showlog(browser,url+"\t获取cookie成功\r",1)

				# 	print(url,'\t请进行其它操作，操作完毕请手动关闭浏览器')


				
				while True:
					time.sleep(1)
					try:
						geturl_ = browser.current_url
					except Exception as e:
						print(url,'\t手动关闭了浏览器')
						myqueue.get()
						browser.quit()
						sys.exit()

			else:
				#登录失败
				# self.showlog(browser,url+"\t获取cookie失败！错误信息："+message+"\r")
				try:
					print(url+'\t无法完成注册，请尝试手动点击注册页面，或关闭浏览器！')
					while True:
						time.sleep(1)
						try:
							geturl_ = browser.current_url
						except Exception as e:
							print(url,'\t手动关闭了浏览器')
							myqueue.get()
							browser.quit()
							sys.exit()
						if geturl_ != geturl_one:
							self.registered(id_,url,username,password,email,2,browser)
							break
					pass
				except Exception as e:
					pass

				

		except Exception as e:
			print(url,'\t关闭')
			myqueue.get()
			browser.quit()
			sys.exit()
			pass
			# print(e)
		time.sleep(10)	
	def updatedata(self,browser,url):

		try:
			geturl = url+'/home.php?mod=spacecp'
			browser.get(geturl)

			try:
				realname = browser.find_element(By.CSS_SELECTOR,"input[name='realname']")
				realname.send_keys(self.registered_['realname'])
			except Exception as e:
				print(browser,url+'\t没有找到 真实姓名输入框 \r',1)

			time.sleep(1)

			try:
				lookingfor = browser.find_element(By.CSS_SELECTOR,"input[name='lookingfor']")
				lookingfor.send_keys(self.registered_['purpose'])
			except Exception as e:
				print(browser,url+'\t没有找到 交友目的输入框\r',1)
			time.sleep(1)
				
			try:
				profilesubmitbtn = browser.find_element(By.CSS_SELECTOR,"button[name='profilesubmitbtn']")
				profilesubmitbtn.click()
			except Exception as e:
				pass
				# print(browser,url+'\t没有找到 交友目的输入框\r',1)
			
			#个人主页
			try:
				browser.get(url+'/home.php?mod=spacecp&ac=profile&op=info')
				site = browser.find_element(By.CSS_SELECTOR,"input[name='site']")
				site.send_keys(self.registered_['site'])
				profilesubmitbtn = browser.find_element(By.CSS_SELECTOR,"button[name='profilesubmitbtn']")
				profilesubmitbtn.click()
			except Exception as e:
				pass
			

			geturl = url+'/home.php?mod=spacecp&ac=avatar'
			browser.get(geturl)



		except Exception as e:
			pass
			self.showlog(browser,url+'\t无法修改资料\r')
		




		# http://www.kaixin65.com/home.php?mod=spacecp 修改资料
					# http://www.kaixin65.com/home.php?mod=spacecp&ac=avatar 上传头像


	def setstatus(self,id_):
		try:
			cursor.execute("update info set seal = 0,registered = 1 where id = "+str(id_))
			connect.commit();#执行提交
		except Exception as e:
			pass
		

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
					sql = "select id,url,username,password,email from info where perform = 1 and (seal = 1 or registered = 0) and id > "+str(infoid)+" limit 1"
					cursor.execute(sql)
					data = cursor.fetchall()
					if data:
						data0 = data[0]
						infoid = data0[0]
						
						print('正在启动 ',data0[1],' 站点...')
						myqueue.put(data0[0])
						w = threading.Thread(target=self.registered,args=(data0[0],data0[1],data0[2],data0[3],data0[4],))
						w.start()
						joinlist.append(w)
					else:

						break
				except Exception as e:
					continue
			
			for j in joinlist:
				j.join()
			time.sleep(10)
			print('没有了')
if __name__ == '__main__':
	MonitoringDZ().main()
	sys.exit()