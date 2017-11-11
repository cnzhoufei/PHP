vim /etc/sysoconfig/network-scripts/ifcfg-eth0 --ip修改
who  查看当前登录的用户数量
who | wc -l

重载配置文件
pkill -1 httpd 
pkill -1 nginx

命令历史  
查看历史命令:history
清除历史命令:history -c
调用历史命令:!行号(!3)、!命令前面的字母 会调用最近一条(!str)


命令别名:alias   unalias
设置命令别名：alias 别名='实际执行的命令'
取消已设置的命令别名： unalias 别名


Bash的重定向操作
重定向标准输入 > 将命令的执行结果输出到指定的文件中，而不是直接显示在屏幕上:ls > new.txt
重定向标准输入 >> 将命令执行的结果追加输出到指定文件:ls > new.txt
重定向标准错误 2> 清空指定文件的内容，并将标准错误信,息保存到该文件中 ssss 2> new.txt  追加 2>>
重定向标准输出和标准错误 &> 将标准输出、标准错误的内容全部保存到指定的文件中，而不是直接显示在屏幕上




管道操作符号“|”
通过前面执行的命令结果 给后面的命令再处理
[root@localhost ~]# free -m | head -2
total used free shared buffers cached
Mem: 503 339 163 0 87 199
[root@localhost ~]# free -m | grep "Mem" | awk '{print $2,$4}'
503 163

grep -V "file" a --在a文件中过虐掉file所在的行
grep -E "2004:22:5[0-9]" a --在a文件中查找事件在2004:22:50->2004:22:59的所在行
grep -E "^[^210]" a --在a文件中查找不包含210的行
grep -E "h*p" a --查找a文件中包含h和p的行
grep -E "[5-8][6-9][0-3]" a --查找大于560小于893的行

删除除了某个文件外的所有文件
ls | grep -E "[^xiaochengxu.zip]"|xargs rm -rf

第2章 Shell文件权限和脚本执行
linux权限:
1.r 读
2.w 写
3.x 执行

linux用户:
1.所有者(u)
2.所属组(g)
3.其他用户(o)
4.所有用户(a)

文件权限:
-rw-r--r-- 1 root root    0 Oct 19 12:21 shell.txt
1.所有者(root用户)对shell.txt具有rw(读写)的权限
2.所属组(root组内用户)对shell.txt具有r(只读)的权限
3.其他用户(root以外用户)对shell.txt具有r(只读)的权限

chmod字母权限分配:
chmod u+x file
#对用户单独设置权限

chmod数字权限:
chmod 755 file

acl权限分配:
1.setfacl设置文件权限
setfacl -m u:user1:rw root.txt 给用户user1设置rw权限
setfacl -m u:user2:rwx root.txt

2.getfacl查看文件权限
getfacl root.txt

3.删除文件权限
setfacl -x user:user3 root.txt

4.清空文件权限
setfacl -b root.txt

5.创建和删除文件权限:
#需要对目录设置acl权限即可
setfacl -m u:user4:rwx /mnt

6.如何对目录以及子目录和文件设置acl权限
setfacl -m u:user4:rwx -R /mnt/

7.目录中后期添加的子目录和文件如何继承父目录的权限
setfacl -m d:u:user4:rwx -R /mnt/

设置用户对命令的执行权限-visudo:
1.设置
visudo
user4 localhost=/usr/sbin/useradd,/usr/sbin/userdel

2.使用有密码sudo授权命令
sudo localhost=/usr/sbin/useradd user4
sudo localhost=/usr/sbin/userdel -r user4

3.使用无密码的sudo授权命令 
sudo localhost=NOPASSWD: /usr/sbin/userdel -r user4
sudo ALL=NOPASSWD: /usr/sbin/userdel -r user4


执行shell脚本的方式:
1.bash test.sh
#不需要写解析器
#不需要给脚本设置执行权限

2../test.sh
#需要写解析器
#需要给脚本设置执行权限



第三章 变量的定义和使用
Shell变量的种类
用户自定义变量：由用户自己定义、修改和使用
预定义变量：Bash预定义的特殊变量，不能直接修改
位置变量：通过命令行给程序传递执行参数

定义新的变量：变量名要以英文字母或下划线开头，区分大小
写
格式：变量名=变量值 a = 111
查看 echo $变量名 echo $a 
unset 变量名  --删除变量

从键盘输入内容为变量赋值
格式： read [-p "信息"] 变量名
• 结合不同的引号为变量赋值
双引号 “ ” ：允许通过$符号引用其他变量值
单引号 ‘ ’ ：禁止引用其他变量值，$视为普通字符
反撇号 ` ` ：将命令执行的结果输出给变量 反引号中的会当成一句命令

获取键盘变量
read -p '请输入你的名字：' name
echo $name

预定义变量
表示形式如下
$#：命令行中位置参数的个数
$*：所有位置参数的内容
$?：上一条命令执行后返回的状态，当返回状态值为0时表示执行正常，非0值表示执行异常或出错
$0：当前执行的进程/程序名

位置变量
表示为 $n，n为1~9之间的数字

数字变量的运算
echo $(($1+$2)) 或者 expr $1 + $2
计算整数表达式的运算结果
格式：expr 变量1 运算符 变量2 ...[运算符 变量n]
expr的常用运算符
加法运算：+
减法运算： -
乘法运算： \*
除法运算： /
求模（取余）运算： %

shell 俗输入功能
echo -n “please input your name:”
read name
echo $name
read -p ‘please input your name:’
name
echo $name
echo “hello world!”
echo -e “hello world\nvery good!”

echo -e "\033[32;47m [test] \033[0m" \033[前景颜色;背景颜色m   \033[0m  --恢复到系统默认的颜色
字符界面前景颜色
• 30 设置黑色前景
• 31 设置红色前景
• 32 设置绿色前景
• 33 设置棕色前景
• 34 设置蓝色前景
• 35 设置紫色前景
• 36 设置青色前景
• 37 设置白色前景
字符界面背景颜色
• 40 设置黑色背景
• 41 设置红色背景
• 42 设置绿色背景
• 43 设置棕色背景
• 44 设置蓝色背景
• 45 设置紫色背景
• 46 设置青色背景
• 47 设置白色背景




其他命令
more 一屏看不完 分屏看
head 看前十行 head -2 前两行
tail 尾
cat 查看某个文件里的内容 还可以在shell中
cat<<zhoufei
		sssssssssssssssssssssss
zhoufei

tee  输出同时 在保存一份 ./test.sh |tee menum.txt

nl 加上行号


条件测试和流程控制
• 1.shell条件测试
• 2.熟悉shell中的常用语法
• (1)if (2)while (3)for (4)case (5)read
• (6)case (7)shift (8)continue (9)break
• 3.函数使用 

• 测试文件状态
格式：[ 操作符 文件或目录 ]
• 常用的测试操作符
-d：测试是否为目录（Directory）
-e：测试目录或文件是否存在（Exist）
-f：测试是否为文件（File）
-r：测试当前用户是否有权限读取（Read）
-w：测试当前用户是否有权限写入（Write）
-x：测试当前用户是否可执行（Excute）该文件
-L：测试是否为符号连接（Link）文件

#！/bin/bash
if [ -f ./file ]
then
	echo 'file 文件存在'
else
	echo 'file 文件不存在'
	touch  file  #如果不存在创建
fi

• 整数值比较
格式：[ 整数1 操作符 整数2 ]
• 常用的测试操作符
eq：等于（Equal）
ne：不等于（Not Equal）
gt：大于（Greater Than）
lt：小于（Lesser Than）
le：小于或等于（Lesser or Equal）
ge：大于或等于（Greater or Equal）
BootUsage=`df -hT | grep "/boot" | awk '{print $6}' | cut -d "%" -f 1`

 
字符串比较
格式：[ 字符串1 = 字符串2 ]
[ 字符串1 != 字符串2 ]
[ -z 字符串 ]
• 常用的测试操作符
=：字符串内容相同
!=：字符串内容不同，! 号表示相反的意思
-z：字符串内容为空
read -p 'name:' name
read -p 'pass:' pass
if [ $name = 'amdin'] && [ $pass = '123' ]
then
	echo '登录成功'
else
	echo '登录失败'
fi



逻辑测试
ü格式：[ 表达式1 ] 操作符 [ 表达式2 ] ...
• 常用的测试操作符
-a或&&：逻辑与，“而且”的意思
#前后两个表达式都成立时整个测试结果才为真，否
则为假
-o或||：逻辑或，“或者”的意思
#操作符两边至少一个为真时，结果为真，否则结果
为假
!：逻辑否
#当指定的条件不成立时，返回结果为真



流程控制
if [ $score -lt 60];then
	echo '60以下'
elif [ $score -ge 60 ] && [ $score -lt 70 ];then
	echo '60-70之间'
elif [ $score -ge 70 ] && [ $score -lt 80 ];then
	echo '70-80之间'
else
	echo '其他'
fi

case  php中的switch
case $week in
	1)
		echo '周一'
		;;
	2)
		echo '周二'
		;;
	*)
		echo '其他'
		;;
esac

循环控制
while [ $num -gt 0 ]
do
	echo $num
	num = $(($num-1))
done
	echo $num


for i in user0 user1 user2 user3 user4 user5
do
	echo $i
done

for i in `cat user.txt`
do
	echo $i

done

cat /etc/passwd |awk -F: '{print $1}' -- 查看文件 然后用冒号隔开再拿出第一列



find 查找
1.find . -name "*.txt"
在当前目录下找以txt结尾的文件
2.find . -name "[a-z]*"
在当前目录下找以所有字母开头的文件
3.find /etc -name "host*"
在/etc目录下找以host开头的文件
4.find . -perm 755
在当前目录下找属性为755的文件
5.find -user root
在当前目录下找属主为root的文件
6.find /var -mtime -5
在/var下找更改时间在5天以内的文件
7.find /var -mtime +3
在/var下找更改时间在3天以前的文件
8.find /etc -type d
在/etc下查找文件类型为d的目录文件
9.find /etc -type l
在/etc/下查找文件类型为l的链接文件
10.find . -size +1000000c
在当前目录下查找文件大小大于1M的文件,1M是
1000000个字节
11.find . -perm 700 |xargs chmod 777
找出当前目录下的所有权限为700的文件，并把其
权限重设为777
12.find . -type f |xargs ls -l
查找出文件并查看其详细信息


正则表达式
1 ^linux
以linux开头的行
2 $php
以php结尾的行
3 .
匹配任意单字符
4 .+
匹配任意多个字符
5 .*
匹配0个或者多个字符
6 [0-9a-z]
匹配[]内任意一个字符
7 (linux)+
出现多次linux单词
8 (web){2}
web出现了2次以上
9 \
只用来屏蔽一个元字符的特殊含义

1.grep "li qq" *
在的有文件中查找li qq文件
2.grep -c "file" a
在a文件中有多少行匹配到file
3.grep -n "file" a
在a文件中有多少行匹配到file,同时显示行和行号
4.grep -i "file" a
在a文件中查找file,并不区分大小写
5.grep -v "file" a
在a文件中过滤掉file所在的行
6.grep -E "2004:22:5[0-9]" a
在a文件中查找时间在2004:22:50->2004:22:59的
所在行
7.grep -E "^[^210]" a
在a文件中查找不包含210的行
8.grep -E "h*p" a
查找a文件中包含h和p的行
9.grep -E "[5-8][6-9][0-3]" a
查找大于560小于893的行
10.grep -E "4{2}" a
查找包含两个4的行
11.grep -E "4{2,}" a
查找大于两个4的行
12.grep -E "4{2,4}" a
查找大于两个4小于4个4的行
13.grep -E "^$" a
查找a文件中的空行
14.grep "?" a
查找a文件中包含?的行
15.grep -E "^d" a
查找a文件中以d开头的行
16.grep -E "^[^d]" a
查找a文件中不是以d开头的行

Awk编程使用
1.awk '{print $0}' access.log
查找出file文件中的每一列
2.awk '{print $1"\t"$7}' access.log
查找出file文件中的第1列和第七列
3. cat file | awk '$0 !~ /192.168.10.2/'|grep
"php" |wc -l
~匹配192.168.10.2的ip地址的统计，!~为不匹配


Sed行定位的使用
1.sed -n '2'p file
只打印第二行，不打印其它的行
2.sed -n '1,4'p file
从第一行到第四行的记录
3.sed -n '/los/'p file
打印匹配los的行
5 sed -n '4,/los/'p file
打印从第四行到匹配los的之间的所有行
6. sed '1,2'd file
把第一行和第二行全部删除

Uniq行定位的使用
1.uniq -c file
打印紧挨的重复行出现的次数
2.uniq -d file
只打印重复的行
3.awk '{print $1}' /var/log/httpd/access_log
|sort|uniq -c
把apache网站的所有访问ip全部统计出来，并打
印出统计次数


Sort行定位的使用
1.sort file
把文件按字母的升序进行排序
2.sort -r file
把文件按字母的降充进行排序
3.cat file|sort -t: -k1 -r
为:进行分割后的第一列来倒序排序

Split行定位的使用
1.split -2 file spt
生成fileab,fileac.....fileai等多个文件
把a文件每两行分割成一个文件,每个文件的前缀都
是以file开头的


访问网页
elinks http://www.baidu.com

源代码安装有教程


更改系统运行级别:
init 0|3|5|6
查看运行级别:
runlevel


Rpm包软件
1.服务脚本
/etc/rc.d/init.d/httpd
2.开启或关闭
service httpd start|stop
3.开机启动
chkconfig --level 3 httpd on
4.查看
chkconfig --list httpd


第七章 24课
#!/bin/bash
#myshd
# chkconfig: 2345 90 20
# description: myshd server daemon

查看内存
free -m




44课












