from selenium import webdriver
from selenium.webdriver.common.by import By #
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import threading
import os
import config#配置文件
conf = config.config

def sayHello(url,browser,msg,uid):
	"""打招呼"""
	print('正在跟 UID 为',uid,' 的用户打招呼')
	try:
		windows = browser.window_handles
		# uid = sayHello_q.get()
		browser.switch_to.window(windows[-1])
		url = url+"/home.php?mod=spacecp&ac=poke&op=send&uid="+uid
		browser.get(url)
		inputs = browser.find_elements(By.CSS_SELECTOR,'input,button')#查找所有input框
		for inp in inputs:
			if inp.get_attribute('name') == 'note':
				inp.send_keys(msg)
				time.sleep(5)
			elif inp.get_attribute('name') == 'pokesubmit_btn':
				inp.click()
				time.sleep(5)

	except Exception as e:
		pass
	else:
		pass
	finally:
		browser.switch_to.window(windows[0])

def sendMsg(url,browser,msg,uid):
	"""发消息"""
	print('正在给 UID 为',uid,' 的用户发消息')
	try:
		windows = browser.window_handles
		# uid = sendMsg_q.get()
		browser.switch_to.window(windows[-1])
		url = url+"/home.php?mod=spacecp&ac=pm&op=showmsg&handlekey=showmsg_"+uid+"&touid="+uid+"&pmid=0&daterange=2"
		browser.get(url)
		textarea = browser.find_element(By.CSS_SELECTOR,'textarea')
		textarea.send_keys(msg)
		time.sleep(5)

		button = browser.find_element(By.CSS_SELECTOR,'form div button')
		button.click()
		time.sleep(5)

	except Exception as e:
		pass
	else:
		pass
	finally:
		browser.switch_to.window(windows[0])


def addBuddy(url,browser,msg,uid):
	"""加好友"""
	print('正在添加 UID ',uid,' 的用户为好友')
	try:
		windows = browser.window_handles
		browser.switch_to.window(windows[-1])
		url = url+"/home.php?mod=spacecp&ac=friend&op=add&uid="+uid
		browser.get(url)
		inputs = browser.find_element_by_class_name('px')#找到kw这个id
		inputs.send_keys(msg)#像id为kw这个input中输入一个pathon
		time.sleep(5)

		buttom = browser.find_element_by_id('addsubmit_btn')
		buttom.click()
		time.sleep(5)

	except Exception as e:
		pass
	else:
		pass
	finally:
		browser.switch_to.window(windows[0])
# http://www.smdywlt.com/home.php?mod=spacecp&ac=usergroup&gid=10
def isAdmin(url, browser,usergrouplist,uid):
	try:
		windows = browser.window_handles
		uid = isAdmin_q.get()
		browser.switch_to.window(windows[-1])
		url = url+"/home.php?mod=space&uid="+uid+"&do=profile&from=space"
		browser.get(url)
		usergroup = find_elements(By.CSS_SELECTOR,'li a')
		for ug in usergroup:
			href = ug.get_attribute('href')
			if href in usergrouplist:
				return True

		return False
	except Exception as e:
		pass
	else:
		pass
	finally:
		browser.switch_to.window(windows[0])
		

def perform(url,uid,username,password,msg):
	try:
		browser = webdriver.PhantomJS()#声明一个浏览器对象
		# browser = webdriver.Chrome()#声明一个浏览器对象

		#执行登录
		browser.get(url+'/member.php?mod=logging&action=login')#访问登录页面
		inputs = browser.find_elements(By.CSS_SELECTOR,'input,button')#查找所有input框
		#循环判断
		for inp in inputs:
			if inp.get_attribute('name') == 'username':#如果这个input的name等于 username 为用户名输入框
				inp.send_keys(username)#向用户输入框发送用户名
			elif inp.get_attribute('name') == 'password':#如果这个input的等于 password 为密码输入框
				inp.send_keys(password)#向密码输入框发送密码
			elif inp.get_attribute('name') == 'loginsubmit':
				inp.click()
		
		time.sleep(10)
	except Exception as e:
		pass
	time.sleep(10)
	#开启
	browser.execute_script('window.open()')

	#获取管理组
	try:
		usergroupurl = url+"/home.php?mod=spacecp&ac=usergroup"
		browser.get(usergroupurl)
		print('获取管理组')
		time.sleep(10)
		usergroup = browser.find_elements(By.CSS_SELECTOR,'#gadmin_menu a')
		usergrouplist = []
		for group in usergroup:
			usergrouplist.append(group.get_attribute('href'))#添加到列表中 
	except Exception as e:
		pass
	

	# print(usergrouplist)  

	#打开日志文件
	logfile = url.replace('://','-')+'.log'
	log = open(logfile,'w',encoding='utf8')

	# 开始监控 打招呼 发消息 加好友
	tag = 0
	i = 0
	while True:
		if tag == 1:
			print('睡眠中等待下一次执行')
			time.sleep(config.apart)#检测相隔时间
			i = 1
			tag = 0
		else:
			i = i + 1
		try:
			monitoringurl = url+'/home.php?mod=space&uid='+uid+'&do=friend&view=online&type=member&page='+str(i)
			browser.get(monitoringurl)
			users = browser.find_elements(By.CSS_SELECTOR,'#friend_ul li')#查找所有用户li 获取到li的id

			for u in users:
				try:
					li_id = u.get_attribute('id')#li的id
					li_uid = li_id.split('_')[1]#uid+
					if li_uid == uid or li_id == '1':#排除自己和超级管理员
						continue
					listen = browser.find_element(By.CSS_SELECTOR,'#a_followmod_'+li_uid)#收听
					if listen.text == '收听TA':
						isadmin = isAdmin(url, browser,usergrouplist,li_uid)#判断是否是管理组
						if isadmin:
							continue
						print('正在关注 UID 为',li_uid,' 的用户')
						log.write(li_uid+"\r\n")
						log.flush()
						listen.click()#点击收听
						time.sleep(5)

					
					#打招呼
						# sayHello_q.put(li_uid)
						sayHello(url,browser,msg,li_uid)

					# 发消息
						# sendMsg_q.put(li_uid)
						sendMsg(url,browser,msg,li_uid)

					#加好友
						# addBuddy_q.put(li_uid)
						addBuddy(url,browser,msg,li_uid)
					
					# print(listen.get_attribute('id'))
				except Exception as e:
					continue;
				
				
			tag = 1
			# time.sleep(3)
			# if i == 3:
			# 	tag = 1
		except Exception as e:
			# print(e)
			tag = 1#如果报错 跳出当次 等待执行下一次
		




if __name__ == '__main__':
	for c in conf:
		time.sleep(config.apart)
		w = threading.Thread(target=perform,args=(c['url'],c['uid'],c['username'],c['password'],c['msg'],))
		w.start()


