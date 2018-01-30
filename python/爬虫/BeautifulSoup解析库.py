# pip install beautifulsoup4
from bs4 import BeautifulSoup
html = ''
soup BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title.string())

#选择器
soup.title #选择title标签
soup.head #选择head标签

soup.title.name #标签名称

soup.attrs['name']#获取name属性

soup.p.string #获取内容


soup.head.title.string #嵌套选择

soup.p.contents #包括html 返回一个列表 所有子节点

soup.p.chidren#包括html 返回一个列表 所有子节点

soup.a.parent  #获取父节点

soup.a.parents #获取多级父节点

soup.a.next_siblings #获取下一个兄弟节点
soup.a.previous_siblings #获取上一个兄弟节点

soup.find_all('ul') #查找所有ul标签 返回列表
# find() 返回单个元素 find_all()返回多个
soup.find_all(attrs={'id':'list'})#id选择器
soup.find_all(attrs={'name':'uname'})#name选择器
soup.find_all(class_='class名')#class选择器
soup.find_all(text='fol')#文本内容选择器

find_parents()  find_parent()

find_next_siblings() find_next_sibling()
find_previous_siblings() find_previous_sibling()

find_all_enxt() find_next()  #返回符合后的

find_all_previous() find_previous()#返回符合前的

css选择器 通过select() 直接传入css选择器既可完成选择
soup.select('.panel .panel-head')
soup.select('ul li')
soup.select('#list li')
#获取属性
for ul in soup.select('ul'):
	ul['id']
	ul.attrs['id']
	ul.get_text()#获取内容




