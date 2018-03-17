import os
import sys
import pymysql

path = os.path.dirname(sys.argv[0])+'\\'
path2 = repr(os.path.dirname(sys.argv[0]))[1:-2]

print('开始为软件创建注册表，请注意注册表提示，依次点击 是->是->确定')
#getcookie
print('创建批量获取cookie软件注册表,请点击：是->是->确定')
with open(path+'setregistry/getcookie.reg','r',encoding='utf8') as getcookie:
	getcookiestr = getcookie.read().replace("---PATH---",path2)
with open(path+'getcookie.reg','w',encoding='utf8') as getcookiew:
	getcookiew.write(getcookiestr)
os.system(path+'getcookie.reg')
os.remove(path+'getcookie.reg')


#getcookieone
print('创建获取单个cookie软件注册表,请点击：是->是->确定')
with open(path+'setregistry/getcookieone.reg','r',encoding='utf8') as getcookieone:
	getcookieonestr = getcookieone.read().replace("---PATH---",path2)
with open(path+'getcookieone.reg','w',encoding='utf8') as getcookieonew:
	getcookieonew.write(getcookieonestr)
os.system(path+'getcookieone.reg')
os.remove(path+'getcookieone.reg')


#registered
print('创建注册软件注册表,请点击：是->是->确定')
with open(path+'setregistry/registered.reg','r',encoding='utf8') as registered:
	registeredstr = registered.read().replace("---PATH---",path2)
with open(path+'registered.reg','w',encoding='utf8') as registeredw:
	registeredw.write(registeredstr)
os.system(path+'registered.reg')
os.remove(path+'registered.reg')


#monitoring
print('创建推广软件注册表,请点击：是->是->确定')
with open(path+'setregistry/monitoring.reg','r',encoding='utf8') as monitoring:
	monitoringstr = monitoring.read().replace("---PATH---",path2)
with open(path+'monitoring.reg','w',encoding='utf8') as monitoringw:
	monitoringw.write(monitoringstr)
os.system(path+'monitoring.reg')
os.remove(path+'monitoring.reg')

print('创建数据库和info表')
try:
	database = {}
	with open(path+'config.ini','r',encoding='utf8') as f:
		for line in f.readlines():
			line = line.strip()#去除两段空字符
			#如果为空或者为注释跳过
			if len(line) < 1 or line[0] == '#':
				continue
			#配置文件类型
			if line[0] == '[' and line[-1] == ']':
				class_ = line[1:-1]
			#数据库
			if '=' in line and class_ == 'database':
				conf = line.split('=')
				database[conf[0].strip()] = conf[1].strip()
	connect = pymysql.connect(host=database['host'],user=database['user'],passwd=database['passwd'],charset=database['charset'],port=int(database['port']))
	cursor = connect.cursor();#创建一个游标
	cursor.execute("create database if not exists "+database['db'])
	cursor.execute("use "+database['db'])
	connect = pymysql.connect(host=database['host'],user=database['user'],passwd=database['passwd'],db=database['db'],charset=database['charset'],port=int(database['port']))
	cursor = connect.cursor();#创建一个游标
	cursor.execute("""
	CREATE TABLE `info` (
	  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `perform` tinyint(1) unsigned NOT NULL DEFAULT '1' COMMENT '是否执行(1是，0否)',
	  `seal` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否被封号(1是，0否)',
	  `type` char(100) NOT NULL DEFAULT '' COMMENT '类型',
	  `name` char(200) NOT NULL DEFAULT '' COMMENT '网站名称',
	  `url` char(200) NOT NULL DEFAULT '' COMMENT '网址',
	  `registered` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '注册(1可以注册，0不可以注册)',
	  `listen` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '收听(1是，0否)',
	  `message` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '消息(1是，0否)',
	  `friends` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '好友(1是，0否)',
	  `hello` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '招呼(1是，0否)',
	  `vip` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT 'vip(1是，0否)',
	  `username` char(200) NOT NULL DEFAULT '' COMMENT '用户名',
	  `password` char(200) NOT NULL DEFAULT '' COMMENT '密码',
	  `email` char(100) NOT NULL DEFAULT '' COMMENT '邮箱',
	  `note` varchar(200) NOT NULL DEFAULT '' COMMENT '备注',
	  `addtime` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '添加时间',
	  `cookie` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT 'cookie是否存在(1是，0否)',
	  PRIMARY KEY (`id`),
	  KEY `name` (`name`),
	  KEY `url` (`url`),
	  KEY `username` (`username`)
	) ENGINE=InnoDB AUTO_INCREMENT=751 DEFAULT CHARSET=utf8;
	""")
	print('创建库表完成')
except Exception as e:
	print('mysql配置错误或'+database['db']+'库已经存在')


print('软件初始化完成')

