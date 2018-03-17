# strs = "innssss,"
# print(strs[0:300])
import pymysql

DBconnect = pymysql.connect(host='localhost',user='root',passwd='',db='spider',charset='utf8',port=3306)
DBcursor = DBconnect.cursor();#创建一个游标

print(dir(DBconnect))