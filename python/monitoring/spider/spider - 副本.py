
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
import pymysql


class Spider(object):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
	already = []
	datainfo = []
	DBconnect = pymysql.connect(host='localhost',user='root',passwd='',db='spider',charset='utf8',port=3306)
	DBcursor = DBconnect.cursor();#创建一个游标
	def __init__(self):
		pass

	def grab(self,url):
		try:
			#排除也抓取过的
			if url in self.already:
				sys.exit()
			else:
				self.already.append(url)


			print('正在抓取：'+url)
			try:
				htmlobj = requests.get(url,headers=self.headers)
				try:
					encoding = requests.utils.get_encodings_from_content(htmlobj.text)[0]
					if encoding:
						htmlobj.encoding = encoding
				except Exception as e:
					pass
				

			except Exception as e:
				print(url ,' 无法访问')
				sys.exit()
			#判断是否是dz论坛
			if htmlobj.status_code == 200:
				html = htmlobj.text.encode().decode('utf8')
				q = pyquery.PyQuery(html)
				title = q('title').text()

				if '错误' in title or '404' in title or '页面不存在' in title or '找不回' in title or '新闻' in title or '找不回' in title:
					sys.exit()

				try:
					#查询是否存在
					# selectsql = "select id from info where url = '%s'"%(url)
					# self.DBcursor.execute(selectsql);
					# data = self.DBcursor.fetchall()
					if url not in self.datainfo:
						# file.write(url+'\t'+title+'\n')
						if 'href="forum.php"' in html or "href='forum.php'" in html:
							self.datainfo.append([url, self.DBconnect.escape(title[0:100].replace("'",'_'))])

				except Exception as e:
					print(e)
					# time.sleep(10)
					# try:
					# 	self.DBconnect = pymysql.connect(host='localhost',user='root',passwd='',db='spider',charset='utf8',port=3306)
					# 	self.DBcursor = self.DBconnect.cursor();#创建一个游标
					# 	# self.datainfo.append([url,title])
					# 	time.sleep(10)
					# except Exception as e:
					# 	# print(e)
					# 	sys.exit(0)
					
					
				# while True:
				# 	try:
				# 		if not data:
				# 			sql = "insert into info(url,title) values('%s','%s')"%(url,title)
				# 			DBcursor.execute(sql.encode('utf8'));#执行sql
				# 			DBconnect.commit();#执行提交
				# 			break
				# 		else:
				# 			break
				# 	except Exception as e:
				# 		print(e)
				# 		time.sleep(10)
				# 		pass
					
			else:
				sys.exit()
			time.sleep(1)
			#匹配所有觉得连接
			pattern = re.compile(r'.*?(http:\/\/[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+).*?',re.S)
			urls = list(set(re.findall(pattern,html)))
			# print(urls)
			for u in list(urls):
				#排除子域名 防止站群
				myurl = url.split('.')[1] #切割当前访问的连接
				uurl = u.split('.')[1]
				if url not in u and 'w3.org' not in u and 'qq.com' not in u and 'cnzz.com' not in u and 'baidu.com' not in u and '0455xx.cn' not in u and myurl != uurl:
					myqueue.append(u)
			print('抓取结束：'+url)
			sys.exit()
		except Exception as e:
			# print(e)
			sys.exit()

	def main(self,initurl):
		
		# print(dir(threading))
		# print(threading.stack_size())
		# exit()
		# global file
		# file = open('dz.txt','a',encoding='utf8')
		global myqueue
		myqueue = []
		myqueue.append(initurl)

		# DBconnect2 = pymysql.connect(host='localhost',user='root',passwd='',db='vip',charset='utf8',port=3306)
		# DBcursor2 = DBconnect2.cursor();#创建一个游标
		# sql = "select url from info"
		# DBcursor2.execute(sql);
		# data = DBcursor2.fetchall()
		# for i in data:
		# 	myqueue.append(i[0])

		wlist = []
		while True:
			if len(self.datainfo) > 50:
				try:
					print('写入数据库')
					sql = "insert into info(url,title) values"
					for row in self.datainfo:
						sql += '("%s","%s")'%(row[0],row[1])+","
					print(sql)
					sql = sql[0:-1]
					self.DBcursor.execute(sql.encode('utf8'));#执行sql
					self.DBconnect.commit();#执行提交
					self.datainfo = []
					pass
				except Exception as e:
					try:
						# self.DBconnect.close()
						self.DBconnect = pymysql.connect(host='localhost',user='root',passwd='',db='spider',charset='utf8',port=3306)
						self.DBcursor = self.DBconnect.cursor();#创建一个游标
						time.sleep(10)
					except Exception as e:
						sys.exit()
				

			if (threading.active_count()) < 100:
				if len(myqueue) >= 1:
					print(threading.active_count(),'个线程正在运行',)
					print(self.datainfo)
					print('等待抓取的个数 ',len(myqueue))
					url = myqueue.pop()
					w = threading.Thread(target=self.grab,args=(url,))
					w.start()
					wlist.append(w)
			else:
				time.sleep(1)
			# if threading.active_count() <= 0:
			# 	exit()


if __name__ == '__main__':
	
	Spider().main('http://www.500dh.us/')
	
	