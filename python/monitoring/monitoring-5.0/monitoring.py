
import os
import sys
import requests
import pyquery
import time
import json
import threading
import tkinter
from PIL import Image as MyImages, ImageTk
import re
import wmi



class Monitoring(object):


	def __init__(self):
		if not os.path.exists('log/'):
			os.mkdir('log/')
		self.ErrorLog = open('log/error.log','w',encoding='utf8')#登录错误日志
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
		# self.setPath()#设置环境变量
		# self.permissions()
	

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
			# headers = {
			#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36',
			# }
			# requests.post('http://permissions.hk-dna.cc/permissions.php',data={'config':config_str},headers=headers)
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
			print(e)
			return False
	# def login(self,url,username,password,msg):
	# 	conn = requests.Session()


	# 	url = url+'/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&fastloginfield=username&username='+username+'&password='+password+'&quickforward=yes&handlekey=ls'
	# 	print(url)
	# 	getresponse = conn.get(url,headers=self.headers)
	# 	print(getresponse.text)



	def login(self,url,username,password,msg,loginnum=1):
		'''登录'''
		print(url ,' 正在登录...')
		conn = requests.Session()
		#访问第一个页面获取用于登录的数据
		try:
			getresponse = conn.get(url+'/member.php?mod=logging&action=login&infloat=yes&frommessage&inajax=1&ajaxtarget=messagelogin',headers=self.headers)
		except Exception as e:
			print(url,' 此站点无法正常访问！')
			errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+'登录失败！错误信息：此站点无法正常访问！'
			self.ErrorLog.write(errormsg+"\r\r")
			self.ErrorLog.flush()
			sys.exit()
		
		#判断是否正常访问
		if getresponse.status_code == 200:
			#构造登录表单
			gethtml = getresponse.text
			getq = pyquery.PyQuery(gethtml)
			formhash = getq('input[name=formhash]').val()
			posturl = getq("form[name='login']").attr('action')
			referer = getq("input[name='referer']").val()
			if not formhash:
				getq = pyquery.PyQuery(gethtml.encode('gbk'))
				formhash = getq('input[name=formhash]').val()
				posturl = getq("form[name='login']").attr('action')
				referer = getq("input[name='referer']").val()
			data = {
					'formhash':formhash,
					'referer':referer,
					'loginfield':'username',
					'username':username,
					'password':password,
					'questionid':0,
					'answer':'',
					'loginsubmit':True
					}
			print(data)
		else:
			print(getresponse.status_code)
		print(posturl)

		#执行登录
		# conn.get()
		login = conn.post(url+'/'+posturl,headers=self.headers,data=data)
		print(login.text)
		if login.status_code != 200:
			print(url,' 登录失败！')
			errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+'登录失败！错误信息：'+login.text+"\r\r"
			self.ErrorLog.write(errormsg+"\r\r")
			self.ErrorLog.flush()
			sys.exit()

		else:
			msglist = re.findall("[\u4e00-\u9fa5].*?[\u4e00-\u9fa5]",login.text)
			if msglist:
				msgstr = ''.join(msglist)
				if '欢迎您回来' in msgstr or '歡迎您回來' in msgstr:
					print(url,' 登录成功')
					exit()
					# time.sleep(1000)

					#获取管理组
					self.monitoring(conn,url,msg)
				else:
					print(url,' 登录失败！')
					errormsg = time.strftime('%Y-%m-%d %H:%M:%S')+' '+url+'登录失败！错误信息：'+login.text+"\r\r"
					self.ErrorLog.write(errormsg+"\r\r")
					self.ErrorLog.flush()
					sys.exit()








	def monitoring(self,conn,url,msg):
		# http://www.smdywlt.com/home.php?mod=space&do=friend&view=online&type=member
		#日志
		logfile = url.replace('://','-')+'.log'
		log = open('log/'+logfile,'a',encoding='utf8')
		
		adminGroupList = self.getAdminGroup(conn,url)#获取管理组 返回一个列表
		print(adminGroupList)

		log.write(time.strftime('%Y-%m-%d %H:%M:%S')+"\r")
		log.write('管理组：'+str(adminGroupList)+"\r")
		log.flush()
		#开启监控
		# 开始监控 打招呼 发消息 加好友
		number = 1#执行次数
		while True:
			page = 1#分页
			userListId = []
			if number > 1:
				time.sleep(self.apart)
			while True:
				try:
					monitoringurl = url+"/home.php?mod=space&do=friend&view=online&type=member&page="+str(page)
					html = conn.get(monitoringurl,headers=self.headers)
				except Exception as e:
					print(url+monitoringurl,' 访问出错')
					self.ErrorLog.write(self.usr+monitoringurl+' 访问出错，错误信息：'+html.text)
					sys.exit()


				usersobj = pyquery.PyQuery(html.text)#查找所有用户li 获取到li的id
				users = usersobj('#friend_ul li')
				for u in users:
					liid = pyquery.PyQuery(u).attr('id')
					li_uid = liid.split('_')[1]#uid+
					if not li_uid:
						continue
					if li_uid == '1':#排除自己和超级管理员
						continue
					userListId.append(li_uid)


				#查询页数
				pageCountstrs = usersobj('input[name=custompage]').next().attr('title')
				if pageCountstrs:
					pageCount = re.match(".*?([0-9]+).*?",pageCountstrs,re.S)
					if pageCount:
						if page < int(pageCount[1]):
							page += 1
						else:
							break

			#执行关注 打招呼 加好友 发信息
			for row in userListId:
				isAdmin = self.isAdmin(conn,adminGroupList,url,row)#检测是否是管理员
				if isAdmin:
					print('%s uid \033[0;31m %s \033[0m 用户为 %s 不做任何操作'%(url,row,isAdmin,))
					continue
				else:

					log.write(url+'   '+row+"\r")
					log.flush()
					print(isAdmin)
			print(url+'第 \033[0;31m %d \033[0m 次执行完毕'%(number,))
			number += 1
			
	def isAdmin(self,conn,adminGroupList,url,uid):
		try:
			geturl = url+"/home.php?mod=space&uid="+uid+"&do=profile&from=space"
			usergrouphtml = conn.get(geturl,headers=self.headers)
			usergroupobj = pyquery.PyQuery(usergrouphtml.text)
			usergroup = usergroupobj("a[href^='"+url+"/home.php?mod=spacecp&ac=usergroup&gid=']").text()
			res = False
			if usergroup in adminGroupList:
				res = usergroup
			else:
				res = False
				print('%s uid \033[0;31m %s \033[0m 用户组为 \033[0;31m %s \033[0m'%(url,uid,usergroup))
		except Exception as e:
			pass
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

	def getAdminGroup(self,conn,url):
		"""获取管理组"""
		print(url,' 获取管理组')
		try:
			usergroupurl = url+"/home.php?mod=spacecp&ac=usergroup"
			html = usergroup = conn.get(usergroupurl,headers=self.headers)
			q = pyquery.PyQuery(html.text)
			usergrouplists = q('#gadmin_menu a').text().split(" ")
			usergrouplist = []
			for group in usergrouplists:
				usergrouplist.append(group)#添加到列表中
			return usergrouplist
		except Exception as e:
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
				time.sleep(3)
				w = threading.Thread(target=self.login,args=(c['url'],c['username'],c['password'],c['msg'],))
				w.start()
if __name__ == '__main__':
	monitoring = Monitoring().main()
