-- 库
create database if not exists `pay` default charset set utf8mb4;
utf8mb4 编码支持存储文字表情
create database if not exists 库名 default charset utf8 collate utf8_general_ci comment '注释';--创建数据库
create database if not exists 库名;--创建数据库
drop database 库名--删除库
show databases;--查看所有库
use 库名;--进入库

--表
--创建表
create table if not exists `表名`(
	`id` int unsigned not null auto_increment primary key comment '注释',
	`name` varchar(255) unique not null default '' comment '注释',
	...
)engine=innodb default charset=utf8 comment '注释'; 
drop table 表名;--删除表
rename table 原表名 to 新表名;--修改表名
use 库名;--进入库
show table;--查看所有表
#表复制
create table 要创建的新表名 like 要复制的表名;
insert into t2 select * from t1;
#视图
create view 要创建的视图名称 as select * from t1 where id > 1000 and id < 10000;#创建视图
drop view 要删除的视图名称;#删除视图

truncate table  表名  索引从新归零
FLUSH TABLES WITH READ LOCK;锁住所有表 只可以读
lock table 表名 read; 锁住表
unlock tables; 解除锁


alter table `表名` add `字段名称` 字段声明;--增加字段 alter table goods add cid int unsigned not null default 0 comment '注释'
alter table 表名 add 要添加的字段名称 字段声明 after 增加在谁的后面;--增加字段  指定在谁的后面
alter table 表名 change 要修改的字段名 新字段名+字段声明;--修改字段
alter table `表名` modify `字段名` 新的字段声明; --修改字段类型
alter table 表名 drop 字段名;--删除字段 
alter table 表名 charset=utf8;


--视图 view（把查询出来的结果保存成一个虚拟表） 视图与表一一对应 一个发生改变另一个也会改变  当一个sql频繁出现的时候 可以做一个是视图
create view 视图名 as 查询语句（用来做条件的记得取别名） --创建视图
drop view 视图名 --删除视图
可以进行权限控制  做一个视图 把不想让别人看到的字段不写入视图表中 把视图表操作权限给他

------------------------------------------- 数据类型------------------------------------------------------------
-- 整型
tinyint(1) --1字节，范围（-128~127） 
smallint --2字节，范围（-32768~32767） 
mediumint(8) --3字节，范围（-8388608~8388607） 
int --4字节，范围（-2147483648~2147483647） 
bigint --8字节，范围（+-9.22*10的18次方） 

--字符串
char(n) --固定长度，最多255个字符 
varchar(n) --可变长度，最多65535个字符 
tinytext --可变长度，最多255个字符 
text --可变长度，最多65535个字符 
mediumtext --可变长度，最多2的24次方-1个字符 
longtext --可变长度，最多2的32次方-1个字符 

-- 浮点型 float(10,2)总长度10位两位是小数
float(m, d) --4字节，单精度浮点型，m总个数，d小数位
double(m, d) --8字节，双精度浮点型，m总个数，d小数位 
decimal(m, d) --decimal是存储为字符串的浮点数 

-- 时间
date --3字节，日期，格式：2014-09-18 
time --3字节，时间，格式：08:42:30 
datetime --8字节，日期时间，格式：2014-09-18 08:42:30 
timestamp --4字节，自动存储记录修改的时间 TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

-- 其它类型
--enum数据类型就是定义了一种枚举，最多包含65535个不同的成员。当定义了一个enum的列时，该列的值限制为列定义中声明的值。如果列声明包含NULL属性，则NULL将被认为是一个有效值，并且是默认值。如果声明了NOT NULL，则列表的第一个成员是默认值。
enum('member1', 'member2', … 'member65535');

-- set数据类型为指定一组预定义值中的零个或多个值提供了一种方法，这组值最多包括64个成员。值的选择限制为列定义中声明的值。数据类型属性
set('member', 'member2', … 'member64');


------------------------------------------------索引-----------------------------------------------

index --普通索引  仅仅加快查询速度
unique index --唯一索引  加快查询速度 and 行上的值不能重复
primary key --主键索引 
fulltext index --全文索引
create index orderid_productid on orders(order_id, product_id)
show index from 表名 --查看表的所有索引
--建立索引
alter table 表名 add index/unique/fulltext/primary key [索引名](列名(长度));
alter table dede_article add index (aid);#创建普通索引
alter table dede_article add primary key (id);#创建主键索引
alter table article add index typeid1_pypeid2_pyteid3(typeid1,typeid2,typeid3);#创建组合索引--组合索引查询时遵循最左匹配(只有查询时用到了最左边的字段才会用到索引)
#创建表时创建索引
create table if not exists g(
	`gid` int(11) unsigned not null auto_increment comment '商品id',
	`gname` char(200) not null default '' comment '商品名称',
	`title` char(200) not null default '' comment '商品title',
	`much` int(11) unsigned not null default 0 comment '商品库存',
	PRIMARY KEY (`gid`) comment '主键索引',
  	KEY `gname` (`gname`) comment '普通索引',
  	UNIQUE KEY `title` (`title`) comment '唯一索引'
)engine=innodb default charset=utf8 comment '商品表';


alter table 表名 drop index 索引名;--删除索引
alter table 表名 drop primary key; --删除主键索引 如果有自增 要先删除自增
select * from 表名 where match(全文索引的字段名称) against ('要搜索的关键词');--全文索引的查询方法



-------------------------------------------------外键约束-------------------------------------------------------
#创建一个文章表
create table if not exists `article`(
	`article_id` int unsigned not null auto_increment,
	`article_name` char(255) not null default '',
	`type_id` int unsigned not null default 0,
	`article_addtime` datetime not null default CURRENT_TIMESTAMP
	PRIMARY KEY (`article_id`) comment '主键索引',
	KEY `typeid`(`type_id`)
)engine=innodb default charset=utf8;
#创建文章分类表
create table if not exists `type`(
	`type_id` int unsigned not null auto_increment,
	`type_name` char(255) not null default '',
	PRIMARY KEY (`type_id`) comment '主键索引'
)engine=innodb default charset=utf8;
#创建外键约束
-- ALTER TABLE `article` ADD CONSTRAINT `fk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);
alter table `article(文章表名)` add constraint `typeid(文章表中的索引名)` foreign key (`type_id(文章表中的字段)`) references `type(文章分类表名)`(`type_id(文章分类表中的索引)`);
--如果文章表中的数据和文章分类表还有关联时，删除分类表中对应的一条数据会保存
--如果子表试图创建一个在父表中不存在的外键值，InnoDB会拒绝任何INSERT或UPDATE操作。如果父表试图UPDATE或者DELETE任何子表中存在或匹配的外键值，最终动作取决于外键约束定义中的ON UPDATE和ON DELETE选项。InnoDB支持5种不同的动作，如果没有指定ON DELETE或者ON UPDATE，默认的动作为RESTRICT:
--删除外键
ALTER TABLE article DROP FOREIGN KEY typeid;
--添加外键
ALTER TABLE `article` ADD CONSTRAINT `typeid` FOREIGN KEY ( `type_id` )
REFERENCES `type` ( `type_id` )
ON DELETE CASCADE ON UPDATE CASCADE

--此时article中的记录也会被删除
delete from category where id=1;
--此时article中的category_id也会被更新成3
UPDATE `test`.`category` SET `id` = '3' WHERE `category`.`id` =2;


-------------------------------------------------增删改查-------------------------------------------------------
-- 增
insert into 表名(字段信息) values(数据信息);--数据和字段一一对应
insert into 表名(字段信息) values('数据信息'),('数据信息2'),('数据信息3');--增加多条数据
insert into 表名 values(完整的数据信息);--省略字段信息
insert into `本表名` select * from `有数据的表名`;--把一张表的数据导入到另一张表里 查询哪些就是导入哪些 条件是字段要一样

--删
truncate `表名`; --清空一张表的所有数据 
delete from 表名 where id = 1;--删除id等于1的行

-- 改
update 表名 set 字段名 = '数据' where id = 1;--update goods set goods_name = '修改商品名称' where id = 1;
update  `shop_users` set `name` = '{$name}' ,`pass` = '{$pass}' ,`sex` = '{$sex}'  where id = {$id};
update yd_goods set name=REPLACE(name, '测试', '') where status = 1;--将状态等于1的name字段中的测试替换成空字符


-- 查
五种字句的顺序：where, group by,  having, order by, limit 
select * from 表名;
--where 条件
select * from goods where id = 1;#goods表中id字段等于1的
--两个字段相加
select c1 + c2 from table where Id = 1  
--如果其中有一个字段有可能为空 那用也下方法
select IFNULL(c1,0) + IFNULL(c2,0) from table where Id = 1

select count(uid),sum(total),avg(total) from wolf_orders;--总共多少条，总数，平均数
select *  from wolf_orders where (select count(uid) from wolf_orders) order by total limit 2; --查销量最好的产品

--取之间值
select * from `表名` where `字段` between 20 and 30;
SELECT * FROM Persons WHERE LastName BETWEEN 'Adams' AND 'Carter';
select * from `表名` where `字段` in (20,30,40,45); 

select distinct name,id from table group by name;--查询去重 distinct

--order by 排序
select * from 表名 where status = 1 order by id asc;--降序
select * from 表名 where status = 1 order by id desc;--升序
select * from 表名 where status = 1 order by id,name;--已多个字段排序
select * From `goods` where id in (178,171,176,188,189) order by field(id,178,171,176,188,189);--不排序

--group by 分组
select *,count(typeid)每个分组的个数 from 表名 where status = 1 order by id asc group by `字段`;--   select * from `shop_category` group by `pid`;
select *,count(pname) from 表名  where status = 1  group by cnanme,pname with rollup;#再次聚合 后面会得到一个总数with rollup不能喝order 不要一起使用

select *,count(userid) as user from behavior group by userid order by user desc limit 10;#查询userid 最多的

SELECT *, count( * ) AS count
FROM lginlog 
GROUP BY userid
ORDER BY count DESC
LIMIT 20
--like 搜索
select * from 表名 where 字段 like '%要搜索的关键词%';--select * from goods where goods_name like '%测试商品%';

--正则匹配搜索 regexp
select * from 表名 where 字段 regexp '表达式';--select * from goods where goods_name regexp '测试商品';

--limit 分页
select * from 表名 limit 10;--查询10条
select * from 表名 limit 5,10;--跳过5条 取10条

select * from goods where (status = 1 and goods_name like '%测试商品%') group by cid order by goods_id desc limit 10;


left join --左连接  以左边表为准
select goods_id,gooos.cat_id,cat_name,goods_name,shop_price from goods left join category on goods.cat_id = category.cat_id;

right join --右连接 以右边为准
select goods_id,gooos.cat_id,cat_name,goods_name,shop_price from goods right join category on goods.cat_id = category.cat_id;
 
inner join --内连接
select Persons.LastName, Persons.FirstName, Orders.OrderNo from Persons inner join Orders on Persons.Id_P = Orders.Id_P order by Persons.LastName
--多表联查 把前面查询的结果当成一个表 后面继续 inner join 
select .... from t1 inner join t2 on t1.id = t2.id inner join t3 
select store.store_id from yd_store as store inner join yd_shouji on store.store_id = yd_shouji.userid where store.tpl like '%shuma%' and store.store_id > 9 ;

--其它查询
mysql -uroot -p123456 -e "select * from database.table";--不用登陆mysql 直接查询数据
mysql -uroot -p123456 -e "select * from database.table" > mysql.sql;--在linux时下直接将查询结果写入到文件中

group_concat(id) 用逗号链接某一个字段(结果是所有记录) 默认长度为1024 GROUP_CONCAT(`key` SEPARATOR '_') ;两个字段相连
group_concat_max_len = 1024 #你要的最大长度 在配置文件中修改长度
SET GLOBAL group_concat_max_len=10240000; #sql语句修改 作用域全局
SET SESSION group_concat_max_len=102400;#作用域session
ESCAPE --用于转移特殊字符如下划线
SELECT * FROM `yd_goods_category` WHERE ( parent_id_path like '0#_1#_2#_%' ESCAPE '#' )
SELECT * FROM `yd_navigation` WHERE ( url like '%Goods%');



show variables like '%dir%';--查看mysql目录
--查看建表语句
use information_schema;
select * from columns where table_name='表名';
select group_concat(column_name) from INFORMATION_SCHEMA.columns where table_name = '表名' and table_schema='库名';--将所有字段用逗号链接起来
select COLUMN_NAME,column_comment from INFORMATION_SCHEMA.Columns where table_name='zp_company' and table_schema='zhaopin';
1、informaiton_schema.columns 常用列：
1、table_catalog　　　　　　　　：不管是table | view 这个列的值总是def
2、table_schema　　　　　　　　 ：表 | 视图所在的数据库名
3、table_name　　　　　　　　　 ：表名 | 视图名
4、column_name　　　　　　　　　：列名
5、column_default　　　　　　　 ：列的默认值
6、is_nullable　　　　　　　　　：是否可以取空值
7、data_type　　　　　　　　　　：列的数据类型
8、character_maximum_length　　 ：列的最大长度（这列只有在数据类型为char | varchar 时才有意义）
9、column_type　　　　　　　　　：列类型这个类型比data_type列所指定的更加详细，如data_type 是int 而column_type 就有可以能是int(11)
10、column_key　　　　　　　　　：列上的索引类型 主键-->PRI  | 唯一索引 -->UNI  一般索引 -->MUL





DESC 表名;--查看表字段
SHOW FULL COLUMNS FROM 表名 --查询表结构
SHOW CREATE TABLE 表名 --查询表结构--建表语句
SHOW TABLE STATUS ---查询所有表及表信息
OPTIMIZE TABLE 表名 --优化表
REPAIR TABLE  表名   --修复表

select database(); 查看当前使用的数据库
show variables  like 'port'; 查看数据库使用端口
select concat(round(sum(data_length)/(1024*1024),2) + round(sum(index_length)/(1024*1024),2),'MB') as 'DB Size' from tables where table_schema='库名'; 查看数据库大小
select concat(round(sum(data_length)/(1024*1024),2),'MB') as 'DB Size' from tables where table_schema='库名'; 查看数据所占的空间大小
select concat(round(sum(index_length)/(1024*1024),2),'MB') as 'DB Size' from tables where table_schema='库名';查看索引所占的空间大小

SELECT VERSION() as version; 查看数据库版本
show variables like 'character%';查看数据库编码
character_set_client      为客户端编码方式；
character_set_connection  为建立连接使用的编码；
character_set_database    为数据库的编码；
character_set_results     为结果集的编码；
character_set_server      为数据库服务器的编码；
show variables like 'collation%';
status; 也可以查看数据库的编码

select distinct concat('user: ''',user,'''@''',host,''';') as query from mysql.user;查看数据库的所有用户信息
show grants for 'root'@'localhost';查看某个具体用户的权限
show variables like '%max_connections%';查看数据库的最大连接数

show status like 'Threads%';查看数据库当前连接数，并发数。
Threads_cached : 代表当前此时此刻线程缓存中有多少空闲线程。
Threads_connected :代表当前已建立连接的数量，因为一个连接就需要一个线程，所以也可以看成当前被使用的线程数。
Threads_created :代表从最近一次服务启动，已创建线程的数量。
Threads_running :代表当前激活的（非睡眠状态）线程数。并不是代表正在使用的线程数，有时候连接已建立，但是连接处于sleep状态，这里相对应的线程也是sleep状态。
show variables like '%datadir%';查看数据文件存放路径

select unix_timestamp(now()) ;获取当前时间戳
select UNIX_TIMESTAMP(datetime);--格式化的日期格式转换成时间戳
select FROM_UNIXTIME(unixtime);--将时间戳转换成格式化的时间格式
比如运行SELECT UNIX_TIMESTAMP('2010-03-01 00:00:00')
返回1267372800
运行SELECT FROM_UNIXTIME(1267372800)
返回'2010-03-01 00:00:00'


-----------------------------------------常用函数----------------------------------------------------
IFNULL(字段,0) 如果为空就给0
not 是取反
avg()求平均数
max() 求最大
min() 求最小
sum() 求总和  
count() 求总行数
rand()   随机函数

concat() 连接字段
lcase()转换成小写
ucase()转换成大写
length()字符串的长度
ltrim()去除前端的空
rtrim()去除后端的空
repeat()重复多次 select repeat('test',10) 
replace(要替换的字符串，要搜索的值，替换成什么)字符串替换
substring(原字符，从第几，取到第几)字符串截取
space(count)生成count个空格
bin()十进制转二进制
ceiling() 向上取整
floor()向下取整
sqrt()开平方
rand()返回0-1的内置随机值

curdate()返回当前的日期
curtime()返回当前的时间
now();#当前时间 select now();--2017-12-13 20:20:20
UNIX_TIMESTAMP(datetime)#当前时间转换成时间戳 比如运行SELECT UNIX_TIMESTAMP('2010-03-01 00:00:00')返回1267372800
FROM_UNIXTIME(unixtime)#格式化时间戳 运行SELECT FROM_UNIXTIME(1267372800)返回'2010-03-01 00:00:00'
week() 返回日期data为一年中的第几周
datediff()返回起始时间和结束时间 间的天数

mysql_real_escape_string()--防止sql注入 php函数
group_concat()链接字段的值
RAND();随机函数
explain | desc#explain或者desc 查看执行计划 explain select * from t where name = 'bbs' and keyword = 'bbs';
-- type=const表示通过索引一次就找到了；
-- key=primary的话，表示使用了主键；
-- type=all,表示为全表扫描；
-- key=null表示没用到索引。type=ref,因为这时认为是多个匹配行，在联合查询中，一般为REF。

\s;查看数据库信息
#查看帮助
? contents;#这个帮助文档可以一层一层往下找
? %
? create
?reg%



允许远程登录命令
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'KsfD$NsL*8S@KD8sK&SgFJ3GS3G' WITH GRANT OPTION;--允许所有主机登录
GRANT ALL PRIVILEGES ON *.* TO 'jack'@'10.10.50.127' IDENTIFIED BY '654321' WITH GRANT OPTION;--允许指定ip登录
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION
flush privileges;--更新权限

--权限 *.*(库名.表名)
create user yundi88@'localhost'  IDENTIFIED by '$mysql_osdf'; --创建用户 先设置该用户只有show database权限
grant select,insert,update,delete on *.* to yundi888@localhost identified by '$mysql_osdf';--给定指定权限
grant all privileges on *.* to yundi88@localhost identified by '$mysql_osdf';--给予所有权限 *.*(库名.表名)星号代表所有
revoke select on mysql.* from yundi88@localhost; --回收权限 如果权限不存在会报错
update  mysql.user  set  password=password('xxxx')  where user='otheruser';更改密码

-- 案例
grant insert on linfei.* to yundi888@localhost identified by '$mysql_osdf';
grant all privileges on linfei.* to yundi888@localhost identified by '$mysql_osdf';
revoke insert on linfei.* from yundi888@localhost; --回收权限 如果权限不存在会报错


修改密码
UPDATE user SET password=PASSWORD('gNiQffsg$WFfff3@&7ssj*GfYX') WHERE user='hk_dna_cc';
FLUSH PRIVILEGES;



--sql语句不严谨时 无法使用insert 
将：sql-mode="STRICT_ALL_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ZERO_DATE,NO_ZERO_IN_DATE,NO_AUTO_CREATE_USER"
改成：sql-mode="NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
或者用sql语句：set @@sql_mode="NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION";

REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ANSI



处理重复数据
查询重复数据
select count(*) as repetitions, last_name, first_name from person_tbl group by last_name, first_name having repetitions > 1;
查询时过虐重复数据 distinct
select distinct last_name, first_name from person_tbl;
select last_name, first_name from person_tbl group by (last_name, first_name);

删除重复数据
如果你想删除数据表中的重复数据，你可以使用以下的sql语句：
create table tmp select last_name, first_name, sex from person_tbl group by (last_name, first_name, sex);--创建临时表把查出去重后的数据写入
drop table person_tbl;--删除原表
alter table tmp rename to person_tbl;--将临时表改名为原表名


备份数据前应该锁定所以表 备份完成后解锁
备份表：mysqldump -u用户名 -p密码 库名 表名1 表名2 -l -F > 地址/文件名;#-l锁住insert和delete -F生成新的binlog日志
mysqldump -uroot -p123 liuyan liuyan -l -F > F://vzhoufei.sql


备份库下面的所有表：mysqldump -u用户名 -p密码 库名 -l -F > 地址/文件名

备份库：mysqldump -u用户名 -p密码 -B 库名1 库名2 库名3  -l -F > 地址/文件名
备份所有库：mysqldump -u用户名 -p密码 -A -l -F> 地址/文件名


登录状态下恢复：
以库为单位：source 备份文件地址
以表为单位：进入库以后再：source 备份文件地址
source F://vzhoufei.sql


不登录状态下恢复：可选参数 -v 查看导入的详细信息 -f 当遇到错误时继续执行
以库为单位：mysql -u用户名 -p密码 < 备份文件地址
以表为单位：mysql -u用户名 -p密码 库名 表名 <备份文件地址

root 密码丢失
1.关闭mysql
2.mysqld_safe --skip-grant-tables --user=mysql & #跳过授权标mysql.user和mysql.db这些表
3.mysql -uroot
4.set password=password('123456');#这条会报错因为用了--skip-grant-tables
4.update user set password=password('123456') where user='root' and host="localhost";
5.set password for root@localhost=password('123456');
6.set password=password('123456');#和第五步一样都可以修改密码



开启慢查询 mysql.cnf msqld下
log_show_queries=slow.log
long_query_time=5#大于五秒的记录

-----------------------------------------------触发器----------------------------------------------------------

create database if not exists test;



create table if not exists o(
	`oid` int(11) unsigned not null auto_increment primary key comment '订单id',
	`gid` int(11) unsigned not null default 0 comment '商品id',
	`num` int(11) unsigned not null default 0 comment '商品数量'
)engine=innodb default charset=utf8 comment '点单表';


#创建触发器
create trigger monitoring_o
after insert on o
for each row
begin
update g set much = much - new.num where gid = new.gid;
end$


------------------------------------------------php操作MySQL-----------------------------------------------


mysqli_insert_id($conn);#获取最后插入的自增id

mysql 存储文字表情 需要修改配置如下然后重启(库和表字符集也必须是utf8mb4)
#mysqld部分
[mysqld]
character-set-server=utf8mb4
collation_server=utf8mb4_unicode_ci
init-connect="SET NAMES utf8mb4"
#mysql部分
[mysql]
default-character-set=utf8mb4



#事务处理
MYSQL 事务处理主要有两种方法：
1、用 BEGIN, ROLLBACK, COMMIT来实现

BEGIN 开始一个事务
ROLLBACK 事务回滚
COMMIT 事务确认
2、直接用 SET 来改变 MySQL 的自动提交模式:

SET AUTOCOMMIT=0 禁止自动提交
SET AUTOCOMMIT=1 开启自动提交

mysqli_query($conn, "set names utf8");
mysqli_select_db( $conn, 'RUNOOB' );
mysqli_query($conn, "SET AUTOCOMMIT=0"); // 设置为不自动提交，因为MYSQL默认立即执行
mysqli_begin_transaction($conn);            // 开始事务定义
 
if(!mysqli_query($conn, "insert into runoob_transaction_test (id) values(8)"))
{
    mysqli_query($conn, "ROLLBACK");     // 判断当执行失败时回滚
}
mysqli_commit($conn);   