

触发器
create trigger 触发器名称
after/before insert/update/delete on 表名
for each row
begin
sql语句
end;

create trigger tg1
after insert on o
for each row
begin
 update g set num = num - 3 where id = 2;
end;
删除触发器
drop grigger 触发器名称

修改mysql的默认结束符号 ;
delimiter $ #修改成$符号

create trigger tg2
after inster on o
for each row
begin
#update 要修改的表名 num(字段) = num - new.much(新曾的行表名用new.要取值的字段) where id = new.gid;
update g set num = num - new.much where id = new.gid;
end$



#删除订单表中的值时
#1.删除一个订单，库存相应增加
#监听地点 O表
#监听事件 delete
#触发事件 update
#触发时间 after
create trigger tg3
after delete on o
for each row
begin update g set num = num + old.much where id = old.gid;
end$

#2修改订单的数量
对于update 来说
被修改的行，修改前的数据用 old 来表示，lod.列名引用被修改之前行中的值
修改后的数据用new来表示，new列名引用被修改之后行中的值
create trigger tg4
after update on o
for each row
begin 
upate g set num = num + old.much - new.much where id = old.gid;
end$



before 和 after 的区别
after 是先完成数据的增删改 再触发，触发中的语句晚于增删该改 无法影响前面的增删改动作

before 是先完成触发，再增删改，触发的语句先于监视的增删改发生 我们会有机会判断，修改即将发生的操作
#监视地点 o表
#监视事件 insert
#触发事件 update
#触发时间 before
#目的 触发事件先于监视事件发生，并判断监视事件的数据
create trigger tg5
before insert on o
for each row
begin
	if new.nuch > 5 then
		set new.much = 5;
	end if;
	update g set num = num - new.nuch where id = new.gid
end$

查看触发器
show trigger