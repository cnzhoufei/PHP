
#表复制
create table 要创建的新表名 like 要复制的表名;
insert into t2 select * from t1;

#索引
create index on t1(name);
drop index name form t1;

#视图
create view 要创建的视图名称 as select * from t1 where id > 1000 and id < 10000;#创建视图
drop view 要删除的视图名称;#删除视图

#预处理
prepare stmt1 from "select * from t1 where id >?";
set @i = 1;
execute stmt1 using @i;
drop prepare stmt1;

#事务处理 只有innodb 才支持事务处理
alter table t1 engine=innodb;#修改表引擎
set autocommit = 0;#关闭自动提交功能
delete from t1 where id = 11;
savepoint p1;#创建还原点
delete from t1 where id = 10;
savepoint p2;#创建还原点
delete from t1 where id = 9;
savepoint p3;#创建还原点
rolloback to p2;#回滚到p2
commit;#提交


#存储 相当于函数
 crate procedure p3()
 begin
 set @i = 1;
 while @i < 10000 do
 insert inot t3(name) values(concat('user'),@i);
 set @i + 1;
 end while;
 end;
 show procedure status;#查看存储
 show create procedure p3;#查看存储
 call p3();#调用存储

 重排auto_increment
 truncate table 表名;#清空表 子增重新归1 或者alter table 表名 auto_increment =1;

#外键 只有innodb支持
create table temp(
	id int,
	name char(20),
	foreign key(id) references outable(id) on delete cascade on update cascade);
)

#查看帮助
? contents;#这个帮助文档可以一层一层往下找
? %
? create
?reg%



#优化
	通过show status 命令了解各种sql的执行频率
	格式：show [session|global] status;
	session 当前链接(默认)
	global 表示自数据库启动至今
	#查询
	show status like "com_insert%"
	show status like "com_select%"
	show status like "com_upate%"
	show status like "com_delete%"
	#只针对inoodb存储的 返回的是影响行数
	InnoDB_ROWS_READ 执行select的次数
	InnoDB_ROWS_upated 执行update的次数
	InnoDB_ROWS_delete 执行delete的次数
	InnoDB_ROWS_insert 执行insert的次数
	#其他
	connections 链接mysql的数量
	Uptime 服务器已经工作的秒数
	Slow_queries慢查询的次数

查看配置文件
show variables like "%slow%";查看慢查询是否开启


#定位执行效率较低的sql语句
explain select * from table where id > 1000;
desc select * from table where id > 1000;

select * from dede_archaives where like "测试%"#可以用到索引
select * from dede_archaives where like "%测试%"#用不到索引
select * from dede_archaives where like "%测试"#用不到索引
select * from dede_archaives where title is null;#可以用到索引
如果使用 and 或 or 必须两个都有索引 才会用到索引

表优化
check table 表名;#检测一个表是否有错误
optimize table 表名;#优化表


导出数据
select name,title from t1 outfile into '/test.txt'; 
导入
load data infile "/test.txt" inot table t1(title)
alter table t1 disable keys;#关闭索引 提高导入速度
set unique_checks=0;#关闭唯一索引
alter table t1 enable keys;#打开索引 导入数据完成后
set unique_checks=1;#打开唯一索引
InnoDB还可以先关闭事务自动提交导入完成后在打开




用order by 来关闭group by 分组的默认排序

select * from t1 where id in(select uid from t2);
select t1.* from t1,t2 where t1.id = t2.uid;#这条更优化


lock table t1 read;读锁 读锁不能增删改 可以查
lock table t1 write;写锁 写锁阻塞增删改查
unlock tables;#解锁



\s;查看数据库信息


开启慢查询 mysql.cnf msqld下
log_show_queries=slow.log
long_query_time=5#大于五秒的记录


socket问题
socket.sock 文件丢失重启后会从新创建 如果有用户访问不能重启临时登陆方法：mysql -uroot -pwei --protocol tcp -hlocalhost


root 密码丢失
1.关闭mysql
2.mysqld_safe --skip-grant-tables --user=mysql & #跳过授权标mysql.user和mysql.db这些表
3.mysql -uroot
4.set password=password('123456');#这条会报错因为用了--skip-grant-tables
4.update user set password=password('123456') where user='root' and host="localhost";
5.set password for root@localhost=password('123456');
6.set password=password('123456');#和第五步一样都可以修改密码
