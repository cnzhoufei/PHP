#!/bin/bash
#mysql.sh

mysql="/usr/local/mysql/bin/mysql -uroot -p123"

case $1 in
	select)	
		sql="select * from test.user order by id"
		;;
	delete)	
		sql="delete from test.user where id=$2"
		;;
	insert)	
		sql="insert into test.user(username,password) values('$2','$3')"
		;;
	update)	
		sql="update test.user set username='$3',password='$4' where id=$2"
		;;
	*)
		sql="select * from test.user order by id"
		;;
esac	

$mysql -e "$sql"
