import xlrd
import pymysql



workbook = xlrd.open_workbook('6545456sssss.xlsx')
#总行数
table = workbook.sheets()[1]
count = table.nrows
booksheet = workbook.sheet_by_index(1)
f = open('insert1.sql','a',encoding='utf8')
for index in range(count):
	if index == 0:
		continue
	row = booksheet.row_values(index)  #读取第一行
	# print(row)
	url = 'http://'+row[0]
	name = row[1]
	type_ = row[2]
	if row[8]:
		username = row[8]
	else:
		username = 'QQ群:577457992'
	if row[9]:
		password = row[9]
	else:
		password = 'Wang~8899'

	if row[0]:
		f.write("insert into info(url,name,type,username,password,registered,listen,message,friends,hello) values('%s','%s','%s','%s','%s','1','1','1','1','1');\r"%(url,name,type_,username,password))
	# config.append({'url':url,'name':name,'username':username,'passwrod':passwrod})
f.close()



workbook = xlrd.open_workbook('6545456sssss.xlsx')
#总行数
table = workbook.sheets()[2]
count = table.nrows
booksheet = workbook.sheet_by_index(2)
f = open('insert2.sql','a',encoding='utf8')
for index in range(count):
	if index == 0:
		continue
	row = booksheet.row_values(index)  #读取第一行
	# print(row)
	url = 'http://'+row[0]
	name = row[1]
	type_ = row[2]
	if row[6]:
		username = row[6]
	else:
		username = 'QQ群:577457992'
	if row[7]:
		password = row[7]
	else:
		password = 'Wang~8899'

	if row[0]:
		f.write("insert into info(url,name,type,username,password,registered,listen,message,friends,hello) values('%s','%s','%s','%s','%s','1','1','1','1','1');\r"%(url,name,type_,username,password))
	# print("insert into info(url,name,type,username,password) values('%s','%s','%s','%s','%s');\r"%(url,name,type_,username,password))
	# config.append({'url':url,'name':name,'username':username,'passwrod':passwrod})
f.close()



workbook = xlrd.open_workbook('6545456sssss.xlsx')
#总行数
table = workbook.sheets()[5]
count = table.nrows
booksheet = workbook.sheet_by_index(5)
f = open('insert5.sql','a',encoding='utf8')
for index in range(count):
	if index == 0:
		continue
	row = booksheet.row_values(index)  #读取第一行
	# print(row)
	url = 'http://'+row[0].replace('http://','').replace('https://','')
	name = row[1]
	type_ = row[2]
	if row[7]:
		username = row[7]
	else:
		username = 'QQ群:577457992'
	if row[8]:
		password = row[8]
	else:
		password = 'Wang~8899'
	if row[0]:
		# print("insert into info(url,name,type,username,password) values('%s','%s','%s','%s','%s');\r"%(url,name,type_,username,password))
		f.write("insert into info(url,name,type,username,password,registered,listen,message,friends,hello) values('%s','%s','%s','%s','%s','1','1','1','1','1');\r"%(url,name,type_,username,password))
	# config.append({'url':url,'name':name,'username':username,'passwrod':passwrod})
f.close()



workbook = xlrd.open_workbook('6545456sssss.xlsx')
#总行数
table = workbook.sheets()[6]
count = table.nrows
booksheet = workbook.sheet_by_index(6)
f = open('insert6.sql','a',encoding='utf8')
for index in range(count):
	if index == 0:
		continue
	row = booksheet.row_values(index)  #读取第一行
	# print(row)
	url = 'http://'+row[0].replace('http://','').replace('https://','')
	name = row[1]
	type_ = row[2]
	if row[8]:
		username = row[8]
	else:
		username = 'QQ群:577457992'
	if row[9]:
		password = row[9]
	else:
		password = 'Wang~8899'
	if row[0]:
		# print("insert into info(url,name,type,username,password) values('%s','%s','%s','%s','%s');\r"%(url,name,type_,username,password))
		f.write("insert into info(url,name,type,username,password,registered,listen,message,friends,hello) values('%s','%s','%s','%s','%s','1','1','1','1','1');\r"%(url,name,type_,username,password))
	# config.append({'url':url,'name':name,'username':username,'passwrod':passwrod})
f.close()



workbook = xlrd.open_workbook('6545456sssss.xlsx')
#总行数
table = workbook.sheets()[9]
count = table.nrows
booksheet = workbook.sheet_by_index(9)
f = open('insert9.sql','a',encoding='utf8')
for index in range(count):
	if index == 0:
		continue
	row = booksheet.row_values(index)  #读取第一行
	# print(row)
	url = 'http://'+row[0].replace('http://','').replace('https://','')
	name = row[1]
	type_ = row[2]
	if row[8]:
		username = row[8]
	else:
		username = 'QQ群:577457992'
	if row[9]:
		password = row[9]
	else:
		password = 'Wang~8899'
	if row[0]:
		# print("insert into info(url,name,type,username,password) values('%s','%s','%s','%s','%s');\r"%(url,name,type_,username,password))
		f.write("insert into info(url,name,type,username,password,registered,listen,message,friends,hello) values('%s','%s','%s','%s','%s','1','1','1','1','1');\r"%(url,name,type_,username,password))
	# config.append({'url':url,'name':name,'username':username,'passwrod':passwrod})
f.close()