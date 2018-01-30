
from selenium import webdriver
from selenium.webdriver.common.by import By #
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import threading
import os
import queue;


# q = queue.Queue(maxsize=10)



# def sss(ine):
# 	while True:
# 		print(q.get(),'线程',ine)
# 		time.sleep(3)


# i = 0;
# if __name__ == '__main__':
# 	for ine in range(3):
# 		w = threading.Thread(target=sss,args=(ine,));
# 		w.start();
# 	while True:
# 		try:
# 			q.put(i)
# 			# print(i)
# 			i += 1
# 		except Exception as e:
# 			print(e)
			

# driver = webdriver.Chrome()

# driver.get('https://www.baidu.com')

# inpuname = driver.find_elements(By.CSS_SELECTOR,'input')
# for u in inpuname:
# 	if u.get_attribute('name') == 'wd':
# 		# name = driver.find_element(By.CSS_SELECTOR,'#'+u.get_attribute('id'))
# 		u.send_keys('username')
# 	elif u.get_attribute('type') == 'submit':
# 		# butt = driver.find_element(By.CSS_SELECTOR,'#'+u.get_attribute('id'))
# 		u.click()

	# print(u.get_attribute('id'))
# inpuname.send_keys('username')

# driver.execute_script('window.open()')
# driver.execute_script('window.open()')

# # 获取打开的多个窗口句柄
# windows = driver.window_handles
# # 切换到当前最新打开的窗口
# driver.switch_to.window(windows[-1])

# driver.get('http://python.org')
# driver.switch_to.window(windows[-2])

# driver.get('http://localhost')
# driver.close()
# driver.switch_to.window(windows[-1])

# driver.close()
# driver.switch_to.window(windows[0])

# driver.get('http://www.test.com')



# def isamdin():
# 	try:
# 		lists2 = [5,6,7,8,9,10]
# 		lists = [1,2]
# 		for i in lists:
# 			if i in lists2:
# 				return '2222222222'
# 		return 'ssssss'
# 	except Exception as e:
# 		print('错误')
# 	else:
# 		print('正确')
# 	finally:
# 		print('--错--误--')

# print(isamdin())

print(os.getcwd())