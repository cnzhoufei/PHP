import requests
# httpbin.org
# response = requests.get('https://www.baidu.com');
# print('返回的类型',type(response))
# print('返回的状态',response.status_code)
# print('返回的文本类型',type(response.text))
# print('返回的文本',response.text)
# print('返回的cookie',response.cookies)
# print('返回的headers',response.headers)
# print('返回的url',response.url)
# print('返回的history',response.history)


# requests.get("https://github.com/timeline.json") #GET请求
# requests.post("http://httpbin.org/post") #POST请求
# requests.put("http://httpbin.org/put") #PUT请求
# requests.delete("http://httpbin.org/delete") #DELETE请求
# requests.head("http://httpbin.org/get") #HEAD请求
# requests.options("http://httpbin.org/get") #OPTIONS请求

#传参
# data = {'name':'germey','age':22}
# # response = requests.get('http://www.httpbin.org/get',params=data)
# response = requests.post('http://www.httpbin.org/post',params=data)
# #解析json
# json = response.json();
# print(json)

#获取二进制
# response = requests.get('http://5b0988e595225.cdn.sohucs.com/images/20180121/d15dc33bbfa44d348eb7d558a699e534.jpeg')
# print(type(response.content))
# with open('11111111.jpeg','wb') as f:
	# f.write(response.content)
	# f.close()


#添加headers
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36',
#     'Referer': 'http://www.lagou.com/zhaopin/Python/?labelWords=label',
#     'Connection': 'keep-alive'
# }
# response = requests.get('http://www.lagou.com/zhaopin/Python/?labelWords=label',headers=headers)
# print(response.text)



#post
# data = {'name':'germey','age':22}
# response = requests.post('http://www.httpbin.org/post',params=data,headers=headers)
# print('返回的history',response.history)


#状态码
# exit() if response.status_code == requests.codes.ok else print('cuow')


# 高级操作
#文件上传
# files = {'file':open('111.jpeg','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)

#获取cookie
# response = requests.get('https://www.baidu.com')
# print(response.cookies)
# for key,val in response.cookies.items():
# 	print(key + '=' + val)

#会话维持
# requests.get('http://httpbin.org/set/number/123456789')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)


# s = requests.Session() #开启会话维持
# s.get('http://httpbin.org/cookies/set?number=123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)


#证书验证
# from requests.packages import urllib3
# urllib3.disable_wamings#屏蔽警告
# response = requests.get('https://www.12306.cn',verlfy=False)#不验证证书
# print(response.status_code)

# response = requests.get('https://www.12306.cn',cert='证书路径')#验证证书
# print(response.status_code)


# #代理设置
# proxies = {
# 	"http":"http://127.0.0.1:9743",
# 	"https":"https://127.0.0.1:9743"
# }
# response = requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)

#代理有用户名和密码的情况
# proxies = {
# 	"http":"http://user:password@127.0.0.1:9743"
# }
# response = requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)

#如果代理类型是 socks 需要安装requests{socks}
#pip install requests{socks}
# proxies = {
# 	"http":"socks5://127.0.0.1:9743"
# 	"https":"socks5://127.0.0.1:9743"
# }
# response = requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)


#超市设置 单位秒
# from requests.exceptions import ReadTimeout
# try:
# 	response = requests.get('https://www.taobao.com',timeout=1)
# 	print(response.status_code)
# except ReadTimeout:
# 	print('请求超时')

#认证设置
# from requests.auth import HTTPBasicAauth
# r = requests.get('http://120.27.34.24:9001',auth=HTTPBasicAauth('user','123'))#第一种写法
# r = requests.get('http://120.27.34.24:9001',auth=('user','123'))#第二种写法
# print(r.status_code)


from requests.exceptions import ReadTimeout,HTTPError,RequestExceptlon

try:
	response = requests.get('http://httpbin.org',timeout=0.5)
	print(response.status_code)
except ReadTimeout:
	print('timeout')
except HTTPError:
	print('HTTPError')

except RequestExceptlon:
	print('RequestExceptlon')
