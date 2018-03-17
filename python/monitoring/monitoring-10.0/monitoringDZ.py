import time
import threading
import os
import json
import sys
import re
import requests
import pyquery
import random
import queue
import random
from xml.sax.saxutils import unescape
import uuid
import platform

class MonitoringDZ(object):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
	
	def __init__(self):
		self.local = threading.local() 
		# self.setPath()#设置环境变量
		self.permissions()
		if not os.path.exists('log'):
			os.mkdir('log')
		if not os.path.exists('cookies'):
			os.mkdir('cookies')
		# if not os.path.exists('html'):
			# os.mkdir('html')
	 	
		global loginerror
		loginerror = open('log/loginerror.log','a',encoding='utf8')
		loginerror.write("\r\r\r"+time.strftime('%Y-%m-%d %H:%M:%S')+"\r")
		global error
		error = open('log/error.log','a',encoding='utf8')
		error.write("\r\r\r"+time.strftime('%Y-%m-%d %H:%M:%S')+"\r")

		global cookielog
		cookielog = open('log/cookie.log','a',encoding='utf8')
		cookielog.write("\r\r\r"+time.strftime('%Y-%m-%d %H:%M:%S')+"\r")
	

	def permissions(self):
		"""权限控制"""
		#获取硬盘序列
		# wmis = wmi.WMI()
		# disk = ''
		# for disks in wmis.Win32_DiskDrive():
		# 	disk += disks.SerialNumber.strip()
		sysstr = platform.system()
		idstr = str(uuid.uuid1()).split("-")[4]
		permissions = requests.get('http://permissions.hk-dna.cc/permissions.php?disk='+sysstr+'_'+idstr).text
		f = open('config.conf','r',encoding='utf8')
		config_str = f.read().strip()
		requests.post('http://permissions.hk-dna.cc/permissions.php',data={'config':config_str,'disk':sysstr+'_'+idstr},headers=self.headers)
		f.close()
		if(permissions != 'off'):
			print('请更新版本')
			sys.exit()




	def config(self):
		"""配置文件"""
		try:
			f = open('config.conf','r',encoding='utf8')
			config_str = f.read().strip()
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

				# #a检测用户名
				# try:
				# 	username = c['username']
				# except Exception as e:
				# 	username = ''

				# if not username:
				# 	c['username'] = configs['username']

				# #检测密码
				# try:
				# 	password = c['password']
				# except Exception as e:
				# 	password = ''
				
				# if not password:
				# 	c['password'] = configs['password']

			self.apart = int(configs['apart'])#循环执行时间 秒
			# self.model = int(configs['model'])#模型(True:有界面模式，False:无界面模式)
			# self.validation = int(configs['validation'])#验证验证码模式(True:手动验证，False:自动验证)
			self.thrnumber = int(configs['thrnumber'])#同时运行的线程个数
			# self.detection = int(configs['detection'])#是否检测网站状态
			# self.loadingimg = int(configs['loadingimg'])#是否加载图片

			return configs
		except Exception as e:
			return False

	def __del__(self):
		
		print('结束')


	def login(self,url,msg):
		#初始化
		self.local.url = url
		# self.local.username = username
		# self.local.password = password
		self.local.msg = msg
		self.local.conn = requests.Session()
		filejson = 'cookies/'+url.replace('http://','').replace('https://','')+'.json'
		if os.path.exists(filejson):
			try:
				with open(filejson, 'r', encoding='utf8') as f:
					listCookies = json.loads(f.read())
			except Exception as e:
				self.showErrorMsg(cookielog,url+"\tcookie文件格式错误\r")

			#添加cookie(登陆操作)
			try:
				for cookie in listCookies:
					self.local.conn.cookies.set(cookie.get('name'),cookie.get('value'))
			except Exception as e:
				# print(e)
				self.showErrorMsg(cookielog,url+"\tcookie设置错误，请更换cookie文件\r")

			#看看是否登陆成功
			try:
				getlogin = self.local.conn.get(url+'/member.php?mod=logging&action=login',headers=self.headers)
				
			except Exception as e:
				self.showErrorMsg(loginerror,url+"\t此网站无法正常访问\r")


			if getlogin.status_code != 200:
				self.showErrorMsg(loginerror,url+"\t访问出错,错误状态码："+str(getlogin.status_code)+"\r")

			q = pyquery.PyQuery(getlogin.text)
			usernamestr = q("input[name='username']")
			self.local.encodeing = requests.utils.get_encodings_from_content(getlogin.text)[0]#编码方式
			self.local.formhash = q("input[name='formhash']").val()#验证字符串
			if not usernamestr:
				self.local.log = open('log/'+url.replace('http://','').replace('https://','')+'.log','a',encoding='utf8')
				self.local.log.write("\r\r\r"+time.strftime('%Y-%m-%d %H:%M:%S')+"\r")
				self.showSuccessMsg(url+"\t登陆成功\r")
				# cookie_ = []
				# for cook in getlogin.cookies:
				# 	cookie_.append({'name':cook.name,'value':cook.value})
				# if cookie_:
				# 	with open(filejson, 'w', encoding='utf8') as f:
				# 		f.write(str(cookie_))
				#执行
				self.monitoring()

			else:
				self.showErrorMsg(loginerror,url+"\t登陆失败\r")
		else:
			self.showErrorMsg(cookielog,url+"\tcookie文件不存在\t"+filejson+"\r")

	def showErrorMsg(self,fileobj,msg,operation=0):
		fileobj.write(msg)
		fileobj.flush()
		print("\033[0;31m"+msg+"\033[0m")
		if operation == 0:
			print(self.local.url+' 退出')
			myqueue.get()
			sys.exit()

	def showSuccessMsg(self,msg):
		self.local.log.write(msg)
		self.local.log.flush()
		print(msg)

	def showMsg(self,msg):
		print("\033[0;33m"+msg+"\033[0m")

	def putHtml(self,html):
		# print(html)
		encodeing = requests.utils.get_encodings_from_content(html)
		fhtml = open('html/'+self.local.url.replace('http://','').replace('https://','')+'.html','w',encoding='utf8')
		fhtml.write(html)


	def signIn(self):
		"""签到"""
		try:
			self.showMsg(self.local.url+"\t检测签到\r")
			url = self.local.url+"/plugin.php?id=dsu_paulsign:sign"
			signinhtml = self.local.conn.get(url,headers=self.headers)
			q = pyquery.PyQuery(signinhtml.text.encode().decode('utf8'))
			todaysay = q("input[name='todaysay']")
			if todaysay:
				self.showMsg(self.local.url+'\t执行签到\r')
				#执行签到
				qdxq = ['kx','ng','ym','wl','nu','ch','fd','yl','shuai']
				msg = ['6666666666666...','哈哈哈哈哈哈...','呵呵呵呵呵呵...','嘻嘻嘻嘻嘻嘻...','我来了哦...']
				data = {'qdxq':qdxq[random.randint(0,8)],'todaysay':msg[random.randint(0,4)],'formhash':self.local.formhash}
				posturl = self.local.url+'/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1'
				post = self.local.conn.post(posturl,headers=self.headers,data=data)
				self.showSuccessMsg(self.local.url+'\t签到成功\r')
			else:
				self.showMsg(self.local.url+"\t不需要签到\r")
		except Exception as e:
			self.showMsg(self.local.url+"\t不需要签到\r")
		

	def monitoring(self):
		"""执行"""
		adminGroupList = self.getAdminGroup()#获取管理组
		self.local.adminGroupList = adminGroupList
		self.showSuccessMsg(self.local.url+'\t管理组：'+str(adminGroupList)+'\r')
		if not adminGroupList:
			self.showErrorMsg(loginerror,self.local.url+'\t无法获取管理，为了安全将关闭此站点的一切操作！\r')
		self.local.focuson = True
		self.local.sayhello = True
		self.local.addbuddy = True
		self.local.sendmsg = True
		#开始监控
		count = 0
		while True:
			if count > 0:
				myqueue.get()
				self.showMsg(self.local.url+"\t第 %s 次执行完毕，睡眠中等待下一次执行\r"%count)
				time.sleep(self.apart)
				myqueue.put(self.local.url)
			#获取需要执行的用户
			page = 1
			userlist = []
			try:
				while True:
					url = self.local.url+"/home.php?mod=space&do=friend&view=online&type=member&page="+str(page)
					html = self.local.conn.get(url,headers=self.headers)
					q = pyquery.PyQuery(html.text.encode().decode('utf8'))
					li = q('#friend_ul li')
					for row in li:
						rowq = pyquery.PyQuery(row)
						liid = rowq.attr('id')
						li_uid = liid.split('_')[1]#得到用户uid
						usertext = rowq('a').eq(2).text()#取出a标签中文本 
						if li_uid != '1' and usertext == '收听TA':
							userlist.append(int(li_uid))
					#查询页数
					try:
						pageCountstrs = q('input[name=custompage]').next().attr('title')
						if pageCountstrs:
							pageCount = re.match(".*?([0-9]+).*?",pageCountstrs,re.S)
							if pageCount:
								if page < int(pageCount[1]):
									page += 1
								else:
									break	
						else:
							break			
					except Exception as e:
						break
					

				for uid in userlist:
					isAdmin = self.isAdmin(uid)
					if not isAdmin:#排除管理员
						# #关注
						if self.local.focuson:
							self.focusOn(uid)
						#打招呼
						if self.local.sayhello:
							self.sayHello(uid)

						# 发消息
						if self.local.sendmsg:
							self.sendMsg(uid)
						#加好友
						if self.local.addbuddy:
							self.addBuddy(uid)
						if self.local.focuson == False and self.local.sayhello == False and self.local.sendmsg == False and self.local.addbuddy == False:
							self.showErrorMsg(error,self.local.url+"\t由于此站点没有任何权限，将关闭此站点\r")
			except Exception as e:
				pass
			count += 1

	def deleteuser(self):
		"""清理用户"""	
		try:
			self.showMsg(self.local.url+"\t正在删除好友！\r")
			geturl = self.local.url+'/home.php?mod=space&do=friend'
			gethtml = self.local.conn.get(geturl,headers=self.headers)
			q = pyquery.PyQuery(gethtml.text.encode().decode('utf8'))
			lilist = q("#friend_ul li")
			userlist = []
			for row in lilist:
				rowq = pyquery.PyQuery(row)
				liid = rowq.attr('id')
				li_uid = liid.split('_')[1]#得到用户uid
				if li_uid:
					userlist.append(li_uid)
				
			for uid in userlist:
				self.showMsg(self.local.url+"\t删除 UID "+uid+" 好友\r")
				posturl = self.local.url+"/home.php?mod=spacecp&ac=friend&op=ignore&uid="+uid+"&confirm=1"
				data = {'referer':self.local.url+'/./','friendsubmit':True,'formhash':self.local.formhash,'friendsubmit_btn':True}
				self.local.conn.post(posturl,headers=self.headers,data=data)

		except Exception as e:
			pass

	def addBuddy(self,uid):
		"""添加好友"""
		try:
			self.showMsg(self.local.url+'\t正在添加 UID 为 '+str(uid)+' 的用户为好友\r')
			data = {'referer':self.local.url+"/./",'addsubmit':True,'formhash':self.local.formhash,'note':self.local.msg,'gid':1,'addsubmit_btn':True}
			posturl = self.local.url+"/home.php?mod=spacecp&ac=friend&op=add&uid="+str(uid)
			posthtml = self.local.conn.post(posturl,headers=self.headers,data=data)
			msghtml = pyquery.PyQuery(posthtml.text.encode().decode('utf8'))
			msgs = msghtml("#messagetext p").text()
			msglist = re.findall("[\u4E00-\u9FA5]",msgs)
			msg = ''.join(msglist)
			if '没有权限' in msg or '沒有權限' in msg or '抱歉' in msg or '抱謙' in msg:
				self.showErrorMsg(error,self.local.url+"\t没有权限，此站将关闭此功能！\t错误信息："+msg+"\r",1)
				self.local.addbuddy = False

			elif '删除' in msg or '达到系统限制' in msg or '刪除' in msg or '達到系統限制' in msg:
					self.showMsg(self.local.url+' 好友数目达到系统限制，将删除部分好友！\r')
					self.deleteuser()
			else:
				self.showSuccessMsg(self.local.url+"\t"+msg+'\r')
		except Exception as e:
			pass
		
	def sendMsg(self,uid):
		"""发送消息"""
		try:
			self.showMsg(self.local.url+'\t正在给 UID 为 '+str(uid)+' 的用户发消息\r')
			data = {'pmsubmit':True,'touid':uid,'formhash':self.local.formhash,'message':self.local.msg,'messageappend':None}
			posturl = self.local.url+'/home.php?mod=spacecp&ac=pm&op=send&touid='+str(uid)
			posthtml = self.local.conn.post(posturl,headers=self.headers,data=data)
			msghtml = pyquery.PyQuery(posthtml.text.encode().decode('utf8'))
			msgs = msghtml("#messagetext p").text()
			msglist = re.findall("[\u4E00-\u9FA5||(24)]",msgs)
			msg = ''.join(msglist)
			if '没有权限' in msg or '沒有權限' in msg or '抱歉' in msg or '抱謙' in msg or '上限' in msg or '超出' in msg:
				self.showErrorMsg(error,self.local.url+"\t没有权限，此站将关闭此功能！\t错误信息："+msg+"\r",1)
				self.local.sendmsg = False
			else:
				self.showSuccessMsg(self.local.url+"\t"+msg+'\r')
		except Exception as e:
			pass
		

	def sayHello(self,uid):
		"""打招呼"""
		try:
			self.showMsg(self.local.url+'\t正在跟 UID 为 '+str(uid)+' 的用户打招呼\r')
			posturl = self.local.url+"/home.php?mod=spacecp&ac=poke&op=send&uid="+str(uid)
			# home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=16952
			data = {'pokesubmit':True,'referer':self.local.url+'/./','formhash':self.local.formhash,'iconid':3,'note':self.local.msg,'pokesubmit_btn':True}
			posthtml = self.local.conn.post(posturl,headers=self.headers,data=data)
			msghtml = pyquery.PyQuery(posthtml.text.encode().decode('utf8'))
			msgs = msghtml("#messagetext p").text()
			msglist = re.findall("[\u4E00-\u9FA5]",msgs)
			msg = ''.join(msglist)
			if '没有权限' in msg or '沒有權限' in msg or '抱歉' in msg or '抱謙' in msg:
				self.showErrorMsg(error,self.local.url+"\t没有权限，此站将关闭此功能！\t错误信息："+msg+"\r",1)
				self.local.sayhello = False
			else:
				self.showSuccessMsg(self.local.url+"\t"+msg+'\r')
		except Exception as e:
			pass
		



	def focusOn(self,uid):
		"""关注"""
		try:
			url = self.local.url+'/home.php?mod=spacecp&ac=follow&op=add&fuid='+str(uid)+'&hash='+self.local.formhash+'&from=a_followmod_&infloat=yes&handlekey=followmod&inajax=1&ajaxtarget=fwin_content_followmod'
			html = self.local.conn.get(url,headers=self.headers)
			if not html.text:
				self.local.focuson = False
			root = pyquery.PyQuery(html.content)
			roothtml = root('root')
			# print(unescape(str(roothtml)).encode().decode('utf8'))
			alerthtml = unescape(str(roothtml)).encode().decode('utf8')#统一转换成utf8
			alert = pyquery.PyQuery(alerthtml)('.alert_right').text()
			# 您所在会员组不允许关注他人
			if alert:
				msg = re.match(".*?([\u4E00-\u9FA5]+)",alert)
				if msg:
					msg = msg.group(1)
					self.showSuccessMsg(self.local.url+'\t'+msg+'\r')
			else:
				alert_error = pyquery.PyQuery(alerthtml)('.alert_error').text()
				if '不允许' in alert_error or '权限' in alert_error or '不允許' in alert_error or '權限' in alert_error:
					self.local.focuson = False
					msg = re.match(".*?([\u4E00-\u9FA5]+)",alert_error)
					if msg:
						msg = msg.group(1)
						self.showErrorMsg(error,self.local.url+"\t没有权限，此站将关闭此功能！\t错误信息："+msg+"\r",1)

		except Exception as e:
			# print(e)
			pass
		


	def isAdmin(self,uid):
		"""是否管理员"""
		res = True
		try:
			geturl = self.local.url+"/home.php?mod=space&uid="+str(uid)+"&do=profile&from=space"
			usergrouphtml = self.local.conn.get(geturl,headers=self.headers)
			usergroupobj = pyquery.PyQuery(usergrouphtml.text.encode().decode('utf8'))
			usergroup = usergroupobj("a[href*='home.php?mod=spacecp&ac=usergroup&gid=']").text()
			if usergroup in self.local.adminGroupList:
				res = usergroup
				self.showMsg(self.local.url+"\tuid "+str(uid)+" 管理组用户："+usergroup+' 不执行')
			else:
				res = False
				self.showMsg(self.local.url+"\tuid "+str(uid)+" 用户组为："+usergroup)
		except Exception as e:
			pass
		return res


	def getAdminGroup(self,signin=0):
		"""获取管理组"""
		self.showMsg(self.local.url+'\t获取管理组')
		usergrouplist = []
		try:
			usergroupurl = self.local.url+"/home.php?mod=spacecp&ac=usergroup"
			html = usergroup = self.local.conn.get(usergroupurl,headers=self.headers)
			q = pyquery.PyQuery(html.text.encode().decode('utf8'))

			messagetext = q('#messagetext p').text()
			if '账号被禁用' in messagetext or '賬號被禁用' in messagetext:
				self.showErrorMsg(error,self.local.url+"\t此账户也被限制，退出执行！限制类型:"+messagetext+"\r")

			mygroup = q("#gmy_menu a").text()
			if '禁止发言' in mygroup or '禁止访问' in mygroup or '禁止 IP' in mygroup or '禁止發言' in mygroup or '禁止訪問' in mygroup or '禁止 IP' in mygroup or '禁用' in mygroup:
				self.showErrorMsg(error,self.local.url+"\t此账户也被限制，退出执行！限制类型:"+mygroup+"\r")

			usergrouplists = q('#gadmin_menu a').text().split(" ")
			if usergrouplists and usergrouplists != 'None':
				for group in usergrouplists:
					if group:
						usergrouplist.append(group)#添加到列表中
			# return usergrouplist
		except Exception as e:
			print('获取管理组失败')
		
		#如果无法获取管理组 检测是否需要签到
		if not usergrouplist and signin == 0:
			self.signIn()
			self.getAdminGroup(1)
		else:
			return usergrouplist



	def main(self):
		#检测配置文件
		configs = self.config()
		if not configs:
			print('配置文件错误')
			time.sleep(10)
			sys.exit()
		else:
			global myqueue
			myqueue = queue.Queue(maxsize = self.thrnumber)
			for c in configs['config']:
				print('正在启动 ',c['url'],' 站点...')
				myqueue.put(c['url'])
				w = threading.Thread(target=self.login,args=(c['url'],c['msg'],))
				w.start()

if __name__ == '__main__':
	monitoring = MonitoringDZ().main()