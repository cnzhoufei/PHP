# 操作mysql的框架 sqlalchemy

import pymysql;
import hashlib;
import time;
connect = pymysql.connect(host='192.168.1.66',user='root',passwd='123',db='test',charset='utf8',port=3306);#链接数据库
cursor = connect.cursor();#创建一个游标
# cursor.execute("set names 'utf8'");#设置字符集


#增------------------------------------------------
password = hashlib.md5('123456'.encode('utf-8')).hexdigest();
# addtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
addtime = int(time.time());
insertsql = "insert into user(username,pwd,sex,tel,address,icon,status,addtime,wx,email) values('user7','%s','1','13539993040','广州','/1.jpg',1,%s,'vzhoufei','vzhoufei@qq.com')"%(password,addtime);
# insertsql = "insert into user(id,name) values(1,'zhoufei')";

try:
	res = cursor.execute(insertsql.encode('utf8'));#执行sql
	connect.commit();#执行提交
	print(res)
except Exception as e:
	#如果报错回滚
	connect.rollbock();




#改---------------------------------------------
updatesql = "update user set address = '广东' where id = 92";
try:
	cursor.execute(updatesql.encode('utf8'));
	connect.commit();
except Exception as e:
	print(e)
	# connect.rollbock();



#删------------------------------------------------
delsql = "delete from user limit 1";
try:
	cursor.execute(delsql);
	# connect.commit();
except Exception as e:
	connect.rollbock();


cursor.execute("set names 'utf8'");#设置字符集

#查-------------------------------------------------------
sql = "select * from user";
try:
	cursor.execute(sql);
	data = cursor.fetchall()
	for l in data:
		s = "id=%s,username=%s,pwd=%s,sex=%s,tel=%s,address=%s,icon=%s,status=%s,addtime=%s,wx=%s,email=%s"%(str(l[0]),str(l[1]),str(l[2]),str(l[3]),str(l[4]),str(l[5]),str(l[6]),str(l[7]),str(l[8]),str(l[9]),str(l[10]));
		print(s)
except Exception as e:
		print(e)







connect.close();#关闭
print(updatesql);

