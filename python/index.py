


www.python.org
www.pycharm.com #开发工具
ldea.lanyus.com #获取pycharm 的秘钥

sublimeREPL插件
1.sublimeREPL->python
2.sublimeREPL->shell


test = 100;
test = 'sssss';
if 5 > 3:
	print('shi');
	pass


print('dd');#输出
id(8);#查询
print(type(1));#类型检测
1 == 1
1 is 1

# None 空类型
# * 乘
# / 除
# % 取于
# ** 次方
# // 返回 整型 去掉 小数点后面的

#类型转换
str(1)#转换字符串
int('sssss');
float(1111);
bin(10)#转换为二进制
hex(10)#转换十六进制
oct(10)#转换成八进制
bool(3);True

round(3.54)#四舍五入 函数
import math #导入模块
math.floor(3.14);#向下取整
math.trunc(-3.14);#往0
margh.ceil(3.12);#向上取整

decimal #模块
import decimal;
decimal.Decimal('0.1')#解决精准度 传值也字符串方式

bool型 True == 1 但是 不等于大于1的
		False == 0 只有 0 或空 等于False
但是用bool() 转换和php差不多



序列
	可变序列
	#和php 的数组一样
	list('优品课堂');#['优','品','课','堂'];
	list(range(5))#[0,1,2,3,4]
	[3] * 4 #[3,3,3,3] 重复序列
	x = [1,2,,5,3,4,5,43.14,'ddddd'];
	a = [21,3,4,[1,2,3]];
	'ddddd' in x #判断一个值是否在序列中
	'ddddd' not in x #取反
	y = x + a #合并两个序列 y等于合并后的 原值不变
	x[1];#取值
	x[-2];#从后面取
	x[2 - 1];#相减以后的下标
	x[0:3] #取0到3的值  不包含3
	x[:3]#从0取到3
	x[0:]#从0取到最后
	x[0:5:2]#跳几个取一个值
	x[0] = 22;#修改
	x[0:3] = [23,45,56]#修改多个值
	x[0:3] =[99]
	x[0:10:2] = [99,33,444,555,66]
	x.append(33);#追加一个元素
	x.extend([2,1,2,3])#追加多个值
	x.insert(0,33)#指定位置追加 0索引位置 33值
	x.[2:2] = [100]#追加到两个下标的中间
	del x[0]#删除
	del x[:3]
	del x[::2]
		x[0:3] = []
	x.remove(2);#删除指定的值 如果有多个会删掉第一个
	x.clear() #删除所有元素
	x.pop()#弹出一个值 返回弹出来的 删除原有的 弹出最后一个
	x.pop(1)#指定弹出

	#要可比较
	len(x)#获取序列的长度
	min(x)#最小值
	max(x)#最大值
	sum(x)#总和
	all(x)
	any(s)
	x.isdigit()#判断是否是数字
	x.index(2)#检索某个值第一次出现的位置 
	x.count(5)#统计某个值出现的次数

	x.reverse();#反转 没有返回 反转的是原来的序列
	l = x#复制 引用 改变一个都会改变
	l = x[:]#复制 从第一个到最后一个给l 完全是复制 操作一个 不会改变另一个
	l = x.copy()#复制 从第一个到最后一个给l 完全是复制 操作一个 不会改变另一个

	#排序
	x.sort();#没有返回值 影响的是原变量
	x.sort(lambda x:x[-1]);#按最后一个字母排序
	x.sort(reverse=True)#反转排序
	用函数来排序
	sorted(x)#返回排序后的


	# 不可变序列
	#tuple 元组 跟序列区别不大 不支持原位改变
	t = (1,2,3); t1 = （1,2,3,'dddd',3.14,(1,2,3);t2 = ('test');如果一个这样写 只是字符串 t2 = ('test',)#元组 t3 = 'test',#元组 t4 = tuple(range(1,6))
	t[1];#跟php数组一样访问

	for x in range(5):
		print('sssss' + str(i));
		pass

	#相当于php foreach
	for key,val in enumerate(data):
		print(key,val)


#字符串 和php 差不多
str = 'ssssss';
str[1]
str = """
wwww.baidu.com
sssllldljldljld
dlkjhlkgkldddds
""";#相当于php 的定界符 会保留换行符
#\n 换行 
#\t tab
#\a 响铃
#\b 退格
#\r 回车
#\' 转义
#\? ?
#\0 空字符
#\ooo 以八进制数声明
#\xhh 以十六进制数声明

str = r"d:\test\test.txt";# r 忽略转义符
#序列的通用操作都可以

#连接字符串 用 + 像js
s.replace('a','b')#字符替换 返回替换后的结果
s.replace('a','b',2)#指定替换几个
s.capitalize();#手写大写
s.upper()#全部替换成大写
s.lower()#全部替换成小写
s.startswith('www');#判断是否已某字符开头
s.endswith('.com');#判断是否已某字符结尾
s.isalpha();#判读是否是字母
s.isnumeric();#判读是否是数字
s.split('.');#以某个字符拆分字符串 返回列表
':'.join(lst);#以某个字符连接列表的值
#格式化字符串
'姓名：{0}，年龄：{1}，工作：{2},部门：{department}'.format(name,age,job,department='开发');#
 '{0} = {1}'.format('优品课堂',133.1224);
 '{0:10} = {1:9}'.format('优品课堂',133.1224);#占位符 指定长度
 '{0:>10} = {1:<9}'.format('优品课堂',133.1224);#< 左对齐 > 右对齐
 '{:f} , {2:.2f} ,{}'.format(3.149,3.149,3.149);#指定类型 f普通浮点型 .2f保留两位小数
 '{:f} , {2:.2f} ,{:06.2f}'.format(3.149,3.149,3.149);#指定类型 保留长度
 '{:X},{:o},{:b}'.format(230,230,230);#指定进制 X十六 o八 b二


#映射
#dict 字典表 相当于 php 的索引数组
#通过(key)而非位置偏移
#序列的通用操作都可以
d = {}
d = {'sex':'男','age':8,'name':'zhoufei'}
dict(key=value,key=>value);
d['sex']#不存在会报错
d.get('age')#不存在不报错
d.get('age','默认值');
d.keys();#返回所以健 返回视图 
d.values();#返回所以的值
for v in d.values():
	print(v);
	pass
d.items()#返回键值对
for (k,v) in d.items():
	print('{}=>{}'.format(k,v))
	pass

# 函数
def test():
	print('test');
	pass

	person = {'name':'jerry','hello':test}


	# 文件处理
	open(路径,[模式],[encoding=编码])
	# r 读 
	# w 写
	# rw
	# a 追加
	f = open(r'F:\Demo\data.txt','r');
	f.tell()#查看指针位置
	f.read()#获取文本信息 读取后指针移到最后 再次直接读取不到数据
	f.read(4)#指定数量读取 读取四个字符
	f.seek(0)#移动指针 重新把指针移到 开头位置
	f.encoding()#文件编码
	f.fileno()#系统对文件编号
	f.flush()# 刷新到文件
	f.truncate()#截取
	f.close()#关闭

	remove() 同 unlink() 的功能是一样的 删除文件

	open('ssss','a')#追加
	open('ssss','r+')#读写
	open('sssss','w+')#写读
	open('sss','rb')#二进制读取
	open('sssss','wb').write('hello'.encode())#写二进制

	f.readlines()#读取所有的行  返回一个列表
	f.readline()#每次读取一行
	for line in f.readlines():
		print(line)
		pass

	#推荐使用
	for line in f:
		print(line,end='');#去除print 默认的换行
		pass


	import os
	os.getcwd();#当前脚本路径
	os.chdir(r'F:\demo');#切换目录


	#写操作
	f = open('test.txt','w',encoding='utf8');
	f.write('测试测试');#写入数据
	f.writelines(file);#一次写入多行 可以传入一个列表
	f.close()#要关闭后才会正式写入到文件中
	f.flush();#不关闭直接输出缓存到文件中
	#结束后会自动关门打开的文件资源
	with open('test.txt','r',encoding='utf8') as f:
		for line in f:
			print(line)


import time
time.sleep(1)#睡一秒

#语句与流程控制
PEP8 python标准
txt = input('接受用户的输入 请输入：');

while True:
	txt = input('请输入数字：')
	if txt == 'stop':
		break
	elif not txt.isdigit():
		print('不是一个数字')
	else:
		num = int(txt)
		if num < 20:
			print('太小了')
		elif num > 20:
			print('太大了')
		else:
			print('刚刚好')



			# \ 反斜杠 续行


			dir();#获取对象支持的属性和方法
			help(list.pop) #某个方法的具体帮助
			print(object.__doc__)#获取可调用的对象文档字串

			#工厂函数
			set() frozenset()



			if 表达式:
				print(1)
			elif 表达式：
				print(2)
			else:
				print(3)

	url = 'www.zhoufei.com';
	while url:
		print(url);
		url = url[0:-1];
	else:
		print('结束');

	break#跳出整个循环
	continue#跳出本次循环
	pass #占位语句
	else #循环正常终止才会执行 可选



# 集和
set()#可以去除列表的重复值  返回一个集合
list_ = [1,2,3,4,5,1,2,3]
list_2 = [1,2,3,4,5,1,2,3,7,8,90,0]
list_3 = set(list_)

list_.intersection(list_2) #求交集 &
list_.union(list_2)#求并集 |
list_.difference(list_2)#求差集 -
list_1.issubset(list_2)#子集 
list_1.issuperset(list_2)#父集
list_1.symmetric_difference(list_2)#对称差集 ^
list_.add('1');#添加一个值
list_.update([1,2,3,4])#添加多个
list_.remove('h')#删除一个值
list_.discard('dd')#不存在不报错
x in s #测试 x 是否是 s 的成员
x not in s #测试 x 是否不是 s 的成员


文件处理
1.mkdir( path [,mode] )  只创建一个目录，上层目录没有就抛出错误
      作用：创建一个目录，可以是相对或者绝对路径，mode的默认模式是0777。 

      如果目录有多级，则创建最后一级。如果最后一级目录的上级目录有不存在的，则会抛出一个OSError。

 2.makedirs( path [,mode] )-------可以创建级联目录
      作用： 创建递归的目录树，可以是相对或者绝对路径，mode的默认模式也是0777。
      如果子目录创建失败或者已经存在，会抛出一个OSError的异常，Windows上Error 183即为目录已经存在的异常错误。如果path只有一级，与mkdir一样。例如：



判断文件是否存在
import os
os.path.exists(test_file.txt)
#True

os.path.exists(no_exist_file.txt)
#False
判断文件夹是否存在
import os
os.path.exists(test_dir)
#True

os.path.exists(no_exist_dir)
#False

 
#可以打开多个文件  with执行完成后会自动关闭释放内存
with open('ssssssss','r') as f:
	f.readline()


with open('1.txt') as f1,open('2.txt','r') as f2:


s = '你好'
a = s.encode();#编码成unicode 默认utf-8
b = a.decode()#解码
#如果编码是GBK
a = s.encode('gbk')
b = a.edcode('gbk') 

# 函数
def test(x,y,z):
	print(x)
	print(y)
	print(z)
	return x,y,z#可以返回多个值  返回格式是一个元祖

test(1,2,3)#传位置参数
test(z=1,y=2,x=3)#指定形参

#接收所有参数 parameter接收到的是一个元祖
def test(*args):
	print(args)
test(1,2,3,4,5,65,6)
test(*[1,2,3,4,5,65,6])

#前面对应该 多余的参数wkargs接收
def test(name,*args):
	print(name)
	print(args)
test('alex',age=18,sex='0')


#接收字典方式传值 接收到的是一个字典
def test(**kwargs):
	print(kwargs)

test(name='zhoufei',age=18,sex=1)
test(**{'name'='zhoufei','age'=18,'sex'=1})

#前面对应该 多余的参数wkargs接收
def test(name,**wkargs):
	print(name)
	print(wkargs)
test('alex',age=18,sex='0')




#变量作用域和php 一样 在函数体里修改全局变量用 global声明(只要字符串和整型有局部变量)
def test(name):
	global name
	name = '2222'
	print(name)

name = '1111'
test(name)
print(name)	

#生成器
#只有在调用时才会生成
# 用for循环调取或者用c.__next__()(下一个)
c = (i * 2 for i in range(10))