
import time
import threading
import os
import json
import sys
import re
import requests


class Spider(object):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
	already = []#已经抓取
	urllist = []#等待抓取
	f = open('spider.txt','a',encoding='utf8')

	def __init__(self):
		pass

	def grab(self,url):
		try:
			print('正在抓取 ',url)
			#判断是否已经抓取过
			if url in self.already:
				sys.exit()
			else:
				self.already.append(url)

			try:
				htmlobj = requests.get(url,headers=self.headers)
				try:
					try:
						encoding = requests.utils.get_encodings_from_content(htmlobj.text)[0]
					except Exception as e:
						encoding = 'utf8'
					if encoding:
						htmlobj.encoding = encoding
				except Exception as e:
					print(url ,e,0)
			except Exception as e:
				print('无法访问',url)
				print(url ,e,' 2')
				sys.exit()
			
			try:
				if htmlobj.status_code == 200:
					html = htmlobj.text.encode().decode('utf8')
					pattern1 = re.compile(r'.*?<title>(.*?)</title>.*?',re.S)
					title = re.findall(pattern1,html)[0].strip()
					print(title)

					if '错误' in title or '404' in title or '页面不存在' in title or '找不回' in title or '新闻' in title or '找不回' in title:
						sys.exit()
				else:
					sys.exit()
			except Exception as e:
				print(url ,e,' 3')
			

			try:
				self.f.write(url+'\t'+title+'\n')
				self.f.flush()
			except Exception as e:
				print(url ,e,' 1')


			try:
				#匹配所有觉得连接
				pattern = re.compile(r'.*?(http:\/\/[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+).*?',re.S)
				urls = list(set(re.findall(pattern,html)))
				# print(urls)
				for u in list(urls):
					#排除子域名 防止站群
					try:
						myurl = url.split('.')[1] #切割当前访问的连接
						uurl = u.split('.')[1]
						if url not in u and 'w3.org' not in u and 'qq.com' not in u and 'cnzz.com' not in u and 'baidu.com' not in u and '0455xx.cn' not in u and myurl != uurl:
							self.urllist.append(u)
					except Exception as e:
						print(url ,e,7)
						self.urllist.append(u)
					

			except Exception as e:
				print(url ,e,' 4')
			

		except Exception as e:
			print(e,' 5')
		print(url ,'抓取完成')
		sys.exit()

	def main(self,initurl):
		try:
			self.urllist.append(initurl)
			while True:
				#判断线程数量
				if (threading.active_count()) < 100:
					#判断待抓取中是否有
					if len(self.urllist) >= 1:
						url = self.urllist.pop()
						w = threading.Thread(target=self.grab,args=(url,))
						w.start()
						print(threading.active_count(),'个线程正在运行',)
						print('等待抓取的个数 ',len(self.urllist))
					else:
						time.sleep(3)
		except Exception as e:
			print(e,' 6')
		
	
		
			


if __name__ == '__main__':
	
	Spider().main('http://www.500dh.us')
	
