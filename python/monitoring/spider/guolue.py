# strs = "innssss,"
# print(strs[0:300])
import pymysql,re

DBconnect = pymysql.connect(host='localhost',user='root',passwd='',db='spider',charset='utf8',port=3306)
DBcursor = DBconnect.cursor();#创建一个游标


DBconnect2 = pymysql.connect(host='localhost',user='root',passwd='',db='vip',charset='utf8',port=3306)
DBcursor2 = DBconnect2.cursor();#创建一个游标
id_ = 1
sql = "select id,title,url from info"
DBcursor.execute(sql);
data = DBcursor.fetchall()

for i in data:
	insertsql = 'insert into info(name,url) values("%s","%s")'%(i[1][0:10],i[2])
	DBcursor2.execute(insertsql.encode('utf8'))
	DBconnect2.commit()
	print(insertsql)


# for i in data:
# 	msglist = re.findall("[\u4E00-\u9FA5]",i[1])
# 	msg = ''.join(msglist)
# 	if '残疾' in msg:

# 		delsql = "delete from info where id = "+str(i[0])
# 		res = DBcursor.execute(delsql.encode('utf8'));#执行sql
# 		DBconnect.commit();#执行提交
# 		print(i[2],i[1])
