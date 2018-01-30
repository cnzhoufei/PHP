
# urllib.request 请求模块
# urllib.error  异常处理
# urllib.parse  url解析模块
# urllib.robotparser  robots.txt解析模块



# url 网站
# data post提交时提交的数据
# timeout 设置网站访问超时时间
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)


# urlopen返回对象提供方法：
# read() , readline() ,readlines() , fileno() , close() ：对HTTPResponse类型数据进行操作
# info()：返回HTTPMessage对象，表示远程服务器返回的头信息
# getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
# geturl()：返回请求的url

#get
import urllib.request

# url='http://www.baidu.com/'  
# def getHtml(url):  
#     page=urllib.request.urlopen(url)  
#     html=page.read().decode(encoding='utf-8',errors='strict')  
#     return html  
# html = getHtml(url)
# f = open('baidu.html',mode="wb")
# f.write(html.encode())
# f.close()


#post
# import urllib.parse

# data = bytes(urllib.parse.urlencode({'word':'hello'}).encode('utf-8'))
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# print(bytes('sss'.encode('utf-8')))

# ---------------------------------------------------------------------------------------------
# 使用Request
# url 连接  data 提交的数据 headers 头信息  method模式(get/post)
# urllib.request.Request(url, data=None, headers={}, method=None)
# 使用request（）来包装请求，再通过urlopen（）获取页面。

# 用来包装头部的数据：
# User-Agent ：这个头部可以携带如下几条信息：浏览器名和版本号、操作系统名和版本号、默认语言
# Referer：可以用来防止盗链，有一些网站图片显示来源http://***.com，就是检查Referer来鉴定的
# Connection：表示连接状态，记录Session的状态。
# url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
# headers = {
#     'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
#     'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
#     'Connection': 'keep-alive'
# }
# req = urllib.request.Request(url, headers=headers)
# page =urllib.request.urlopen(req)
# html = page.read()
# print(dir(html))
# print(html.title())
# html = html.decode('utf-8')

# .Post数据
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
# from urllib import request, parse
# url = r'http://www.lagou.com/jobs/positionAjax.json?'
# headers = {
#     'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
#     'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
#     'Connection': 'keep-alive'
# }
# data = {
#     'first': 'true',
#     'pn': 1,
#     'kd': 'Python'
# }
# data = parse.urlencode(data).encode('utf-8')
# req = request.Request(url, headers=headers, data=data)
# page = request.urlopen(req).read()
# page = page.decode('utf-8')

# --------------------------------------------------------------------
# urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None)
# urlencode（）主要作用就是将url附上要提交的数据。 
# data = {
#     'first': 'true',
#     'pn': 1,
#     'kd': 'Python'
# }
# data = parse.urlencode(data).encode('utf-8')


# -----------------------------------------------------------------------------
# 使用代理 
# urllib.request.ProxyHandler(proxies=None)
# 当需要抓取的网站设置了访问限制，这时就需要用到代理来抓取数据。
from urllib import request, parse
data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
url = r'http://www.lagou.com/jobs/positionAjax.json?'

proxy = request.ProxyHandler({'http': '5.22.195.215:80'})  # 设置proxy
opener = request.build_opener(proxy)  # 挂载opener
request.install_opener(opener)  # 安装opener
data = parse.urlencode(data).encode('utf-8')
page = opener.open(url, data).read()
page = page.decode('utf-8')
print(page)

f = open('baidu.html',mode="wb")
f.write(page.encode())
f.close()
# print(page)


comda list 