from selenium import webdriver
from selenium.webdriver.common.by import By #
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import threading;
import queue;
import os

# AVQ群696643608   abc1666549728
# domain = input('请输入网址(格式:http://www.ssss.com):').strip();
# username = input('请输入用户名:').strip();
# password = input('请输入密码:').strip();
# msg = input('请输入要发送的信息:').strip();
# id_ = input('请输入开始ID(一个整型数字):');
print('请输入所需信息用英文逗号隔开:(格式：网址,用户名,密码,申请好友时所发送的信息,起始ID) 例:  http://www.test.com,testuser,userpassword,您好我是某某,10')
parameter = input('请输入：').strip()
domain,username,password,msg,id_ = parameter.split(',')
# print(domain,username,password,msg,id_)
successlog = domain.replace('://','-')+'_success.log'
errorlog = domain.replace('://','-')+'_error.log'
success = open(successlog,'w',encoding='utf8')
error   = open(errorlog,'w',encoding='utf8')
success.write(parameter+"\r\n")
error.write(parameter+"\r\n")

def sends(q,ine):
	try:
		browser = webdriver.PhantomJS()#声明一个浏览器对象
		#执行登录
		browser.get(domain)
		ls_username = browser.find_element_by_id('ls_username');
		ls_username.send_keys(username)
		ls_password = browser.find_element_by_id('ls_password')
		ls_password.send_keys(password)
		logobutton = browser.input_first = browser.find_element(By.CSS_SELECTOR,'.fastlg_l button')
		logobutton.click()
		wait = WebDriverWait(browser,30)
		inputs = wait.until(EC.presence_of_element_located((By.ID,'flk')))
		time.sleep(10)
	except Exception as e:
		exit()
	
	while True:
		try:
			uid = q.get()
			browser.get(domain+'/home.php?mod=spacecp&ac=friend&op=add&uid='+str(uid))
			inputs = browser.find_element_by_class_name('px')#找到kw这个id
			inputs.send_keys(msg)#像id为kw这个input中输入一个pathon
			buttom = browser.find_element_by_id('addsubmit_btn')
			buttom.click()
			print('uid   ',uid,'   好友申请发送成功')
			success.write(domain+'/home.php?mod=spacecp&ac=friend&op=add&uid='+str(uid)+" 好友申请发送成功 \r\n")

		except Exception as e:
			print('uid   ',uid,'  用户不存在或者以发送过请求！')
			error.write(domain+'/home.php?mod=spacecp&ac=friend&op=add&uid='+str(uid)+" 用户不存在或者以发送过请求！ \r\n")
		success.flush()# 刷新到文件
		error.flush()# 刷新到文件




if __name__ == '__main__':
	q = queue.Queue(maxsize=20);
	i = int(id_)
	for ine in range(20):
		print('线程 ',ine,' 正在登录请稍后...')
		w = threading.Thread(target=sends,args=(q,ine,));
		w.start();
	while True:
		try:
			q.put(i)
			i += 1
		except Exception as e:
			print(e)
			success.close()
			error.close()
			exit()
	

