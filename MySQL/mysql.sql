
http://www.yiibai.com/mysql/mysql-numeric-functions.html  mysql教程

systeminfo  查看windows的系统信息 


rename命令用于修改表名。

rename命令格式：rename table 原表名 to 新表名;


--一次添加多条数据
insert into user(name) values('zhoufei'),('zhoufei2');


SELECT SUM(income - expenses) as "Net Income" FROM gl_transactions;



select count(uid),sum(total),avg(total) from wolf_orders;总共多少条，总数，平均数
select *  from wolf_orders where (select count(uid) from wolf_orders) order by total limit 2; 查销量最好的产品

-- 创建数据库   
create database `g14_shop`;
选库 use 库名
修改字符集   set names utf8;
删除表       drop table 表名

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



not 是取反
avg()求平均数
max() 求最大
min() 求最小
sum() 求总和  
count() 求总行数

group by 分组
order by 排序
group by `字段` 分组   select * from `shop_category` group by `pid`;
select * from `表名` order by `字段名` 升序排序 也可以后面加 asc
order by `字段名` desc 降序排列   order by 可以按多字段排序 字段后再加字段

select * from shop_category order by concat(`path`,`id`) 栏目排序 

五种字句的顺序：where, group by,  having, order by, limit 

create table `现创建的表名` like `要继承表字段的表名`  新建一张表 继承另一张表的字段

insert into `本表名` select * from `有数据的表名` 把一张表的数据导入到另一张表里 查询哪些就是导入哪些 条件是字段要一样

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
GRANT ALL PRIVILEGES ON *.* TO root@"%" IDENTIFIED BY "123456";
flush privileges;