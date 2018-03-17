
import re

# re.match(正则表达式,字符串,flags=0匹配模式)
content = "Hello 123 4567 World_This is a Regx Demo"
result = re.match("^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$",content)
print('返回一个对象',result)
print('匹配匹配到的字符串',result.group())
print('匹配结果范围',result.span())

content2 = "Hello 1234567 World_This is a Regx Demo"
result2 = re.match("^Hello\s(\d+)",content2)
print('获取()中的内容',result2.group(1))


# result.match('',content,re.S)#加上匹配模式 .*可以匹配任意字符包括换行

# re.search(正则表达式,字符串,flags=0匹配模式) 扫描整个字符串并返回第一个成功的匹配

#re.findall(正则表达式,字符串,flags=0匹配模式) 匹配多个结果 返回一个列表

#re.sub(正则表达式,'替换成什么(可以用反向引用 \1 \2)',原字符串) 替换字符串中每一个匹的子串后 返回替换后的字符串

#re.commpile(正则表达式,匹配模式) #将正则表达式串编译成正则表达式对象
import requests
content=requests.get('https://book.doubdn.com',timeout=100000).text
exit()
pattern = re.compile(r'<li.*?covor.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
results = re.findall(pattern,content)
print(result)
for result in results:
	url,name,author,date = result
	author = re.sub('\s','',author)
	date = re.sub('\s','',date)
print(ur1,name,author,date)

