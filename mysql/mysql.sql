
http://www.yiibai.com/mysql/mysql-numeric-functions.html  mysql教程

systeminfo  查看windows的系统信息 
msinfo32


/etc/init.d/mysqld restart


show variables like '%dir%';查看mysql目录


rename命令用于修改表名。

rename命令格式：rename table 原表名 to 新表名;

truncate table 表名  索引从新归零

FLUSH TABLES WITH READ LOCK;锁住所有表 只可以读
lock table 表名 read; 锁住表
unlock tables; 解除锁

DESC 表名;查看表字段
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

--一次添加多条数据
insert into user(name) values('zhoufei'),('zhoufei2');


SELECT SUM(income - expenses) as "Net Income" FROM gl_transactions;


两个字段相加
select c1 + c2 from table where Id = 1  
如果其中有一个字段有可能为空 那用也下方法
select IFNULL(c1,0) + IFNULL(c2,0) from table where Id = 1


select count(uid),sum(total),avg(total) from wolf_orders;总共多少条，总数，平均数
select *  from wolf_orders where (select count(uid) from wolf_orders) order by total limit 2; 查销量最好的产品

-- 创建数据库 
CREATE DATABASE IF NOT EXISTS 库名 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;  
create database `g14_shop`;
选库 use 库名
修改字符集   set names utf8;
删除表       drop table 表名
删除库       drop database 库名

 修改库名   rename database db_name to new_db_name;--5.17可以改

重命名所有的表
CREATE DATABASE new_db_name;
RENAME TABLE db_name.table1 TO new_db_name.table1,
db_name.table2 TO new_db_name.table2;
DROP DATABASE db_name;

--取之间值
select * from `表名` where `字段` between 20 and 30;
select * from `表名` where `字段` in (20,30); 
还可以用 and (并且)


between and
SELECT * FROM Persons WHERE LastName BETWEEN 'Adams' AND 'Carter'
having

union --合并查询结果 把2次或多次查询结果合并起来
要求：两次查询的列数要一致（两张表字段不一致时取前面的） 可以查询多张表 （想当于查询两次结果合并成一个数组）
如果两张表的字段和值完全相同会覆盖（去重），如果不要去重 用 union all (比如：在计算两张表相同字段相加的时候)
select id,num from ta where num < 5000 union select id,num from tb where num < 5000; 
select id,sum(num) form (select * from ta union all select * from tb) as tmp group by id; 查询两张表把相同id的值相加 
如果字句中有order by,limit 须加() ,推荐放到所以字句之后 即对最终合并的结果来排序(根据需求而定)
(select goodsid,cat_id,goods_name,shop_price from goods where cat_id = 4) union (select goodsid,cat_id,goods_nmae,shop_price from goods where cat_id = 5) order by shop_price desc;
取两个栏目的商品价格前三高和前两高
(select * from 表名 where 栏目id = 3 order by desc limit 3 union (select * from 表名 where 栏目id = 4 order by desc limit 2);

left join 左连接  
select goods_id,gooos.cat_id,cat_name,goods_name,shop_price from goods left join category on goods.cat_id = category.cat_id;

right join 右连接
select goods_id,gooos.cat_id,cat_name,goods_name,shop_price from goods right join category on goods.cat_id = category.cat_id;

inner join 内连接
select Persons.LastName, Persons.FirstName, Orders.OrderNo from Persons inner join Orders on Persons.Id_P = Orders.Id_P order by Persons.LastName
多表联查 把前面查询的结果当成一个表 后面继续 inner join 
select .... from t1 inner join t2 on t1.id = t2.id inner join t3 
select store.store_id from yd_store as store inner join yd_shouji on store.store_id = yd_shouji.userid where store.tpl like '%shuma%' and store.store_id > 9 ;

select * from yundi88 where store_id not in(1,2);
IFNULL(字段,0) 如果为空就给0
not 是取反
avg()求平均数
max() 求最大
min() 求最小
sum() 求总和  
count() 求总行数
concat() 连接字段
group_concat(id) 用逗号链接某一个字段(结果是所有记录) 默认长度为1024
group_concat_max_len = 1024 #你要的最大长度 在配置文件中修改长度
SET GLOBAL group_concat_max_len=10240000; #sql语句修改 作用域全局
SET SESSION group_concat_max_len=102400;#作用域session
ESCAPE --用于转移特殊字符如下划线
SELECT * FROM `yd_goods_category` WHERE ( parent_id_path like '0#_1#_2#_%' ESCAPE '#' )
SELECT * FROM `yd_navigation` WHERE ( url like '%Goods%');

--sql语句不严谨时 无法使用insert 
将：sql-mode="STRICT_ALL_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ZERO_DATE,NO_ZERO_IN_DATE,NO_AUTO_CREATE_USER"
改成：sql-mode="NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
或者用sql语句：set @@sql_mode="NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION";

REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ANSI

--不排序
select * From `goods` where id in (178,171,176,188,189) order by field(id,178,171,176,188,189)


distinct --查询去重 
select distinct name,id from table group by name





select sn_id,concat(sn_id,'_',sn_sort) as aa  from yd_store_navigation;

group by 分组
order by 排序
group by `字段` 分组   select * from `shop_category` group by `pid`;
select * from `表名` order by `字段名` 升序排序 也可以后面加 asc
order by `字段名` desc 降序排列   order by 可以按多字段排序 字段后再加字段

select * from shop_category order by concat(`path`,`id`) 栏目排序 

五种字句的顺序：where, group by,  having, order by, limit 

create table `现创建的表名` like `要继承表字段的表名`  新建一张表 继承另一张表的字段

insert into `本表名` select * from `有数据的表名` 把一张表的数据导入到另一张表里 查询哪些就是导入哪些 条件是字段要一样
insert into yd_shouji select null,store_id from yd_store; 将一张表中的某个字段添加到另一张表
truncate `表名` 清空一张表的所有数据 


--修改字段类型
alter table `表名` modify `字段名` int unsigned not null 
alter table `shop_orders` modify `total` float(20,2) not null 
--增加字段
alter table `shop_users` add `Rname` varchar(255)

--增加字段  指定在谁的后面
alter table shop_users add rnmae varchar(255) after id(增加在id的后面)
如果要把增加的放在第一例 后面用 first

--修改字段
alter table 表名 change 要修改的字段名 新字段名+字段声明

--删除字段
alter table 表名 drop 字段名 


--视图 view（把查询出来的结果保存成一个虚拟表） 视图与表一一对应 一个发生改变另一个也会改变  当一个sql频繁出现的时候 可以做一个是视图
create view 视图名 as 查询语句（用来做条件的记得取别名） --创建视图
drop view 视图名 --删除视图
可以进行权限控制  做一个视图 把不想让别人看到的字段不写入视图表中 把视图表操作权限给他





--查找约束名字
exec sp_helpconstraint [约束所在表]
 
--删除该约束
alter table [约束所在表] drop constraint XXXX
 
--最后删除你的索引 
drop index stu_limit_table.sub_number_unique on tbname(column)






-- 创建会员表
create table if not exists `shop_users`(
	`id` int unsigned not null auto_increment primary key,
	`name` varchar(255) unique not null,--用户名
	`pass` char(32) not null,--密码
	`sex` enum('0','1','2') not null default '2',--性别
	`tel` char(11) ,--手机
	`email` varchar(255),--邮箱
	`icon` varchar(255) default 'default.jpg',--头像
	`grade` tinyint unsigned default 3,--会员级别
	`status` tinyint unsigned default 1,--状态
	`addtime` int unsigned not null --注册时间

)engine=innodb default charset=utf8;
create table if not exists `tests`(
                    `id` int unsigned not null auto_increment primary key,
                    `type` varchar(255) COMMENT '表单类型',
                    `instructions` varchar(255) COMMENT '中文说明',
                    `field` varchar(255) COMMENT '字段名称',
                    `value` varchar(255) COMMENT '值'
                    )engine=innodb default charset=utf8;
--添加会员表字段
--name 用户名
--sex性别
--tel手机
--email邮箱
--icon头像
--grade会员级别
--status 状态
--addtime 注册时间
--Rname 真实姓名
--age年龄
--birthday生日
--Blood 血型
--constellation 星座
--hobby 爱好
alter table `shop_users` add `Rname` varchar(255)
alter table `shop_users` add `age` int unsigned
alter table `shop_users` add `birthday` char(100)
alter table `shop_users` add `Blood` char(2)
alter table `shop_users` add `constellation` char(100)
alter table `shop_users` add `hobby` varchar(255)





-- 添加超级管理(只有一个，不能删除)
insert into `users`(name,pass,sex,tel,email,icon,grade,status,addtime) 
	values('zhoufei2',md5(123),'1','13539993040','869688800@qq.com','default.jpg',0,1,unix_timestamp());


--添加用户  表名shop_users
insert into `show_users`(`name`,`pass`,`sex`,`tel`,`emali`,`icon`,`grade`,`status`)
values({$namu},{$pass},{$sex},{$tel},{$icon},{$grade},{$status},{$time});


delete from `student` where id = 3;--删除


用商品表的 cateid 取分类表的 分类名

-- 创建商品表 commodity
create table if not exists `shop_commodity`(
	`id` int unsigned not null auto_increment primary key,
	`cateid` int unsigned not null comment '商品分类ID', 
	`name` varchar(255) not null,--商品名
	`picture` varchar(255) not null,--图片
	`price` float(8,2) not null,--价格
	`store` int unsigned default 0,--库存
	`views` int unsigned default 0,--访问量
	`buy` int unsigned default 0,--销售量
	`describe` text not null comment '描述',
	`display` tinyint(1) default 1 comment '0:下架，1：上架',
	`status` tinyint(1) default 1 comment '0：热销，1：新品，2：猜你喜欢',
	`addtime` int unsigned not null 
)engine=innodb default charset=utf8;

--添加商品表字段  是否在首页是显示According
`according` tinyint(1) default 1
alter table `shop_commodity` add `according` tinyint(1) default 1 comment '0:不在首页显示，1：在首页显示',








-- 创建分类表 category
create table if not exists `shop_category`(
	`id` int unsigned not null auto_increment primary key,
	`pid` int unsigned not null comment '父级ID',
	`name` varchar(255) not null comment '分类名',
	`path` varchar(255) not null comment '分类路径',
	`addtime` int unsigned not null 
)engine=innodb default charset=utf8;


--添加分类数据
insert into `shop_category`(`pid`,`name`,`path`,`addtime`)
insert into `shop_users`(`name`,`pass`,`sex`,`email`)

-- 修改execu($sql)
update `shop_category` set `name` = '{$name}' where id = {$id}
update  `shop_users` set `name` = '{$name}' ,`pass` = '{$pass}' ,`sex` = '{$sex}' ,`tel` = '{$tel}' ,`email` = '{$email}' ,`icon` = '{$icon}' ,`grade` = '{$grade}' , `status` = '{$status}' , `addtime` = '{$time}' where id = {$id}

--查询query($sql)
select * from  `shop_users` where name = '{$name}


	--分页搜索
$sql = 'select * from ' . PIX . "commodity order by id desc limit {$offset},{$num}";
	
--1. 查总数 query($sql)
select count(*) total from shop_commodity';

--按标题搜索
select count(*) total from shop_commodity where `name` like '%床%' --返回总数
select * from shop_commodity where `name` like '%床%' order by id desc limit 0,2 --返回结果并分页
select * from shop_commodity where `name` like '%标题%' order by id desc limit 0,2

--按id搜索
select count(*) total from shop_commodity where `id` = '13' --返回总数
select * from shop_commodity where `id` = '13' order by id desc limit 0,2--返回结果并分页
select * from shop_commodity where `id` = '1' order by id desc limit 0,2 


--添加字段
alter table `shop_guanggao` add `addtime` int unsigned;


--创建广告表  表名shop_guanggao
create table if not exists `shop_guanggao`(
`id` int unsigned not null auto_increment primary key,
`name` varchar(255) not null, --广告标识
`title` varchar(255) not null, --广告标题
`url` varchar(255), --跳转链接
`image` varchar(255) not null, --图片
`width` int unsigned, --图片宽
`height` int unsigned, --图片高
`according` tinyint(1) default 1,--是否显示
`addtime` int unsigned--添加时间
)engine innoDB default charset=utf8;

update `shop_guanggao` set `url` = './list.php'




--创建友情链接表
create table if not exists `shop_youqing`(
`id` int unsigned not null auto_increment primary key,
`name` varchar(255) not null,
`dizhi` varchar(255) not null,
`xianshi` tinyint(1) default 1,
`addtime` int unsigned 
)engine=innoDB default charset=utf8;


--创建订单表
create table if not exists `shop_orders`(
`id` int unsigned not null auto_increment primary key,--订单id（订单号）
`uid` int unsigned not null, --用户id
`linkman` varchar(50) not null, --收货人
`phone` char(11) not null, --手机号
`code` char(6) not null, --邮编
`total` float(8,2) not null,--总价
`addtime` int unsigned not null, --下单时间
`status` tinyint not null default 0,--订单状态
`address` varchar(255) not null--收货地址
)engine=innoDB default charset=utf8;

insert into `shop_orders` values(1000000,1,'周飞','13539993040','000000',1000000,1460981035,3)


--订单详情表
create table if not exists `shop_detail`(
`id` int unsigned not null auto_increment primary key,
`oid` int unsigned not null,--订单号 (就是订单表的id)
`cid` int unsigned not null,----商品id
`num` int unsigned not null,-- 商品数量
`price` float(8,2) not null,--商品价格
`name` varchar(255) not null--商品名
)engine=innoDB default charset=utf8;








mysqli_insert_id($link);//获取上一个影响行数的id

--创建评论表
create table if not exists `shop_liuyan`(
`id` int unsigned not null auto_increment primary key,
`uid` int unsigned not null,--用户id
`goodsid` int unsigned not null,--商品id
`liuyan` varchar(255),--留言类容
`time` int unsigned--留言时间
)engine=innoDB default charset=utf8;





允许远程登录命令
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;--允许所有主机登录
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
UPDATE user SET password=PASSWORD('j$ass&aDg9DaSk5') WHERE user='root';
FLUSH PRIVILEGES;


MySQL数据类型 含义 
date 3字节，日期，格式：2014-09-18 
time 3字节，时间，格式：08:42:30 
datetime 8字节，日期时间，格式：2014-09-18 08:42:30 
timestamp 4字节，自动存储记录修改的时间 
year 1字节，年份 


数值数据类型


整型

MySQL数据类型 含义（有符号） 
tinyint 1字节，范围（-128~127） 
smallint 2字节，范围（-32768~32767） 
mediumint 3字节，范围（-8388608~8388607） 
int 4字节，范围（-2147483648~2147483647） 
bigint 8字节，范围（+-9.22*10的18次方） 


上面定义的都是有符号的，当然了，也可以加上unsigned关键字，定义成无符号的类型，那么对应的取值范围就要翻翻了，比如：

tinyint unsigned的取值范围为0~255。

浮点型

MySQL数据类型 含义 
float(m, d) 4字节，单精度浮点型，m总个数，d小数位 
double(m, d) 8字节，双精度浮点型，m总个数，d小数位 
decimal(m, d) decimal是存储为字符串的浮点数 


我在MySQL中建立了一个表，有一列为float(5, 3)；做了以下试验：

1.插入123.45678，最后查询得到的结果为99.999；
2.插入123.456，最后查询结果为99.999；
3.插入12.34567，最后查询结果为12.346；

所以，在使用浮点型的时候，还是要注意陷阱的，要以插入数据库中的实际结果为准。

字符串数据类型

MySQL数据类型 含义 
char(n) 固定长度，最多255个字符 
varchar(n) 可变长度，最多65535个字符 
tinytext 可变长度，最多255个字符 
text 可变长度，最多65535个字符 
mediumtext 可变长度，最多2的24次方-1个字符 
longtext 可变长度，最多2的32次方-1个字符 

1.char（n）和varchar（n）中括号中n代表字符的个数，并不代表字节个数，所以当使用了中文的时候(UTF8)意味着可以插入m个中文，但是实际会占用m*3个字节。
2.同时char和varchar最大的区别就在于char不管实际value都会占用n个字符的空间，而varchar只会占用实际字符应该占用的空间+1，并且实际空间+1<=n。
3.超过char和varchar的n设置后，字符串会被截断。
4.char的上限为255字节，varchar的上限65535字节，text的上限为65535。
5.char在存储的时候会截断尾部的空格，varchar和text不会。
6.varchar会使用1-3个字节来存储长度，text不会。

其它类型

1.enum(“member1″, “member2″, … “member65535″)
 enum数据类型就是定义了一种枚举，最多包含65535个不同的成员。当定义了一个enum的列时，该列的值限制为列定义中声明的值。如果列声明包含NULL属性，则NULL将被认为是一个有效值，并且是默认值。如果声明了NOT NULL，则列表的第一个成员是默认值。

2.set(“member”, “member2″, … “member64″)
 set数据类型为指定一组预定义值中的零个或多个值提供了一种方法，这组值最多包括64个成员。值的选择限制为列定义中声明的值。

数据类型属性

上面大概总结了MySQL中的数据类型，当然了，上面的总结肯定是不全面的，如果要非常全面的总结这些内容，好几篇文章都不够的。下面就再来总结一些常用的属性。

1.auto_increment

auto_increment能为新插入的行赋一个唯一的整数标识符。为列赋此属性将为每个新插入的行赋值为上一次插入的ID+1。

MySQL要求将auto_increment属性用于作为主键的列。此外，每个表只允许有一个auto_increment列
