
linux下最强大的搜索命令为”find“。它的格式为”find <指定目录> <指定条件> <指定动作>“；比如使用find命令搜索在根目录下的所有interfaces文件所在位置，命令格式为”find / -name  'interfaces'



lsof -i:80 查看端口是否被使用

df -hl  查看磁盘

vim /etc/inittab   系统启动方式在这里修改

find / -name httpd.conf
sudo

配置静态ip
1.setup -> 选择 Network configuration 回车 再选择 dcvicc configuration 回车 再选择第一个 

2.ifup eth0 开启网卡

3.service network restart 重启网络服务


修改端口：
改Linux SSH的默认端口（22），那么你只要修改：/etc/ssh/sshd_config中Port 22，这里把22改成自己要设的端口就行了，不过千万别设和现已有的端口相同哦，以防造成未知后果。

禁止root登录
vim /etc/ssh/sshd_config
修改：PermitRootLogin yes
改为：PermitRootLogin no
banner

创建用户并创建密码
1.创建用户：useradd 用户名
2.为谁更改密码：passwd 用户名
3.输入新密码
4.再输入新密码
切换用户：su - 用户名

新建目录：mkdir 目录名
删除目录：rm -rf 目录名   （r是递归删除  f是强制）

新建文件：touch 文件名     
删除文件：rm -rf 文件名     （r是删除文件  f是强制）


pwd  是显示当前路径

 权限
r 读 4  ， w 写  2  ， x 执行  1
修改目录或文件权限：chmod 777 文件名


重启命令：

1、reboot

2、shutdown -r now 立刻重启(root用户使用)

3、shutdown -r 10 过10分钟自动重启(root用户使用)

4、shutdown -r 20:35 在时间为20:35时候重启(root用户使用)

5、apachectl graceful  优雅重启  不会断开链接

关机命令：

1、halt   立刻关机

2、poweroff  立刻关机

3、shutdown -h now 立刻关机(root用户使用)

4、shutdown -h 10 10分钟后自动关机   Ubuntu：service apache2 graceful
  




userdel可删除用户帐号与相关的文件。若不加参数，则仅删除用户帐号，而不删除相关文件
命 令: userdel 
功能说明：删除用户帐号。 
语　　法：userdel [-r][用户帐号] 
补充说明：userdel可删除用户帐号与相关的文件。若不加参数，则仅删除用户帐号，而不删除相关文件。 
参　　数： 
-f 　删除用户登入目录以及目录中所有文件。 
userdel很简单，只有一个参数可选 -r ；如果加参数-r ，表示在删除用户的同时，一并把用户的家目录及本地邮件存储的目录或文件也一同删除；比如我们现在有个用户jb51，其家目录位于ar目录中，现在我们来删除这个用户； 
userdel jb51 注：删除用户jb51，但不删除其家目录及文件； 
userdel -r jb51 注：删除用户jb51，其家目录及文件一并删除； 
警告： 请不要轻易用-r参数；他会删除用户的同时删除用户所有的文件和目录，切记；如果用户目录下有重要的文件，在删除前请备份； 
其实也有最简单的办法，但这种办法有点不安全，也就是直接在/etc/passwd中删除您想要删除用户的记录；但最好不要这样做，/etc/passwd 是极为重要的文件，可能您一不小心会操作失误； 
其相似命令groupdel 是用来删除用户组的； 
语法格式：groupdel 用户组 
groupdel admin 
假如删除的时候忘记带r参数 以后想删除这个用户的文件 可以用下面这条命令 
find / --nouser -exec rm - rf {} \ 
删除所有 用户不存在而遗留的文件(因为用户已被删除，其文件的拥有者为其UID,参数nouser用于删除此类文件)




ACL权限
1	getfacl  文件名		查询文件的acl权限

2	setfacl  选项  文件名		设定acl权限
				-m			设定权限
				-b			删除权限

setfacl  -m  u:用户名:权限   文件名
setfacl -m u:zhoufei:rwx -R /www

setfacl  -m  g:组名：权限   文件名

setfacl  -m u:aa:rwx  /test		给test目录赋予aa是读写执行的acl权限

setfacl -m u:cc:rx -R soft/		赋予递归acl权限，只能赋予目录
				-R  递归	

setfacl  -b  /test		删除acl权限
setfacl -x  u:用户名  文件名		删除指定用户的ACL权限
3	setfacl  -m d:u:aa:rwx -R /test		acl默认权限。		注意：默认权限只能赋予目录




进程查看		

		1	ps  aux		查看当前系统所有运行的进程
			-a 	显示前台所有进程
			-u	显示用户名
			-x	显示后台进程

终止进程
			kill  信号  PID		结束单个进程
			-9  强制

			killall  -9  进程名		结束一类进程
			pkill  -9  进程名


			w			判断登录用户
			pkill  -9  -t  终端号	把某个终端登录的用户踢出
			pkill  -9  -t tty1		把本地登录终端1登录用户踢出



服务自启动
	因为/etc/rc.local是开机自动启动。
	所以把命令写到/etc/rc.local里面去

		/usr/local/apache2/bin/apachectl  start




### 压缩/解压

1.  linux常见压缩类型  

    bz2  gz

压缩    tar -zcvf 压缩文件名    需要压缩的文件1  需要压缩的文件2....
        tar -jcvf       gz2后缀类型

    	zip    压缩：zip -r 压缩文件名.zip 要压缩的文件


解压    tar -zxvf  解压文件名
        tar -jxvf   gz2后缀类型






挂载光盘和u盘

1. 先确保光盘插上了

2. mkdir /mnt/cdrom  如果没有才创建

3. 挂载
    mount /dev/sr0   /mnt/cdrom

        或x
    mount /dev/cdrom   /mnt/cdrom


如果挂载不了去插入光盘那里 勾选已连接


挂载数据盘
1、查看数据盘

在没有分区和格式化数据盘之前,使用 “df –h”命令,是无法看到数据盘的,可以使用“fdisk -l”命令查看。如下图:

友情提示:若您执行fdisk -l命令,发现没有 /dev/xvdb 标明您的云服务无数据盘,那么您无需进行挂载,此时该教程对您不适用

2、 对数据盘进行分区

执行“fdisk -S 56 /dev/xvdb”命令,对数据盘进行分区;

根据提示,依次输入“n”,“p”“1”,两次回车,“wq”,分区就开始了,很快就会完成。

3、 查看新的分区
使用“fdisk -l”命令可以看到,新的分区xvdb1已经建立完成了。

 4、格式化新分区

使用“mkfs.ext3 /dev/xvdb1”命令对新分区进行格式化,格式化的时间根据硬盘大小有所不同。

(也可自主决定选用 ext4 格式)

5、挂载
mount /dev/vdb1 /www

卸载
umount /dev/vdb1





光盘作为yum源：
			1	cd  /etc/yum.repos.d/
				mv  CentOS-Base.repo  CentOS-BS.repo.bak  //改变yum，不让它上网找包

			2	mount /dev/hdc  /mnt/cdrom

			3	vi  /etc/yum.repos.d/CentOS-Media.repo
				baseurl=file:///mnt/cdrom/			指定yum源位置
				enabled=1					yum源文件生效
				gpgcheck=0					rpm验证不生效

		pkill -9 yum-updatesd		如果yum报错正在升级，执行此命令，强制杀死升级进程

		






## 如何挂载U盘
1. 先确保光盘插上了
   点击虚拟机>> 可移动设备  >> 倒数第二个

2. mkdir /mnt/usb；如果没有才创建

3. 挂载
    /dev/sdb1   /mnt/usb
    
查看u盘：fdisk -l 




计划任务
crontab  -e

	在某个时间/每多少时间(分、时、日、月、周)，帮你做某种事情。 

	作用：利用计划任务，可以做备份！！   一般是没有人（ 凌晨3,4点 ），就是将MySQL的数据给打包压缩，通过命令传送给另外一台服务器。


	需求：每1分钟，往/tmp/aa.php/   www
			*/1 * * * *  echo 'wwww' >> /tmp/aa.php

	2需求：每天下午5：30  echo '下课'  >> /tmp/out.php

		*分  * 时  *日  *月  *周
		
		30   17   *  * *  echo 'wwww' >> /tmp/out.php


 安装vsftpd
首先确保光盘已挂载
yum  -y  install  gcc  还有确保这个包已安装

1.yum -y install vsftpd 安装 不要写全名
2.vim /etc/vsftpd/vsftpd.conf 打开配置文件
	nonymous_enable=YES 是否允许匿名用户登录
	write_enable=YES    是否能网里面写入东西
	local_umask=022 权限
	anon_mkdir_write_enable=YES  如果把注释打开匿名用户就能网里面写入东西  不打开
	connect_from_port_20=YES  端口
	idle_session_timeut=600   过期时间 注释打开生效

这个一定要把注释打开 限制用户访问目录 chroot_local_user=YES只有此句，所有用户限制在家目录下  在97行 

3.重启vftpds服务 service vsftpd restart


 4、关闭防火墙 
setup
 5、vim /etc/selinux/config
修改这个为 SELINUX=disabled  
//SELINUX这个选项开启后，你这个linux非常安全。这个开启后linux会非常安全 但就不能访问了  所以要改成disabled

6、reboot
            
7、service vsftpd start




3) yum卸载
   
   yum remove -y 软件名
   或
   yum erase -y 软件名



samba服务器安装
 1.yum -y install samba 安装samba

2.vim /etc/samba/smb.conf
[global]
	workgroup  =  工作组

	server  string  =  描述

	log  file  =	日志位置

	max  log  size  =  日志最大大小 			KB

	security  =  user		安全等级
	user	使用samba用户登录。注意：samba用户由系统用户转变过来。
            要把用户生成为samba用户，此用户必须已经是系统用户
						share	不用密码
						server	使用验证服务器验证
				

	share   definitions		共享设置

		[共享目录名]
			Comment  =  目录描述
			browseable  =  yes		目录是否对用户可见
			writeable  =  yes		可写（要与系统目录权限相与）
			valid  users  =  用户名	用户限制（目录是哪个用户所有）
			path  =  /www			指定共享目录位置

共享两个目录，一个是pub    位置在 /pub 	所有用户都能访问，所有用户都能上传

		另一个目录是soft	位置在  /soft	只有aa用户能访问，上传(写)。其他用户不能访问


答案(配置samba的完整步骤)：

3. vim /etc/samba/smb.conf   在文件末尾添加以下内容：
			       
[pub]
        browseable = yes
        path = /pub
        writable = yes
[soft]
        browseable = yes
        path = /soft
        writable = yes
	
4. 按照这个命令来设置

			mkdir  /pub
			mkdir  /soft
			chmod 777 /pub
			chmod 700 /soft
             useradd zhoufei 创建一个用户把soft这个目录给他
             passwd zhoufei
			chown zhoufei  /soft

5. smbpasswd  -a  zhoufei   //将aa这个系统用户声明为samba用户

6. 重启服务
service  smb  restart
service  nmb  restart 重启
service  nmb  stop 关闭
service  nmb  start 启动

7.把系统用户声明为samba用户

			smbpasswd  -a  系统用户名
			smbpasswd  -a  aa   //将aa这个系统用户声明为samba用户

			smbpasswd  -x  用户名		删除samba用户

			pdbedit  -L	查看samba用户

		8.	重启服务
			service  smb  restart
			service  nmb  restart
			
				注意：samba权限和系统权限取最严格权限
					  samba用户必须是系统用户
					  启动的服务名是smb

		

9.	客户端使用

				windows：	共享目录方式
						net  use  *  /del			删除缓存

				linux客户端：
					smbclient  //192.168.140.251/soft -U aa



目录别名

修改 主配置文件vim /usr/local/apache2/etc/httpd.conf      
            开启 Include etc//extra/httpd-autoindex.conf

子配置文件名	vim /usr/local/apache2/etc/extra/httpd-autoindex.conf

Alias /icons "/usr/local/apache2//icons/"     /icons --目录名    绝对路径
<Directory "/usr/local/apache2//icons">        这里也要指明绝对路径
    Options Indexes MultiViews			MultiViews多编码支持
    AllowOverride None
    Require all granted 
</Directory>	




让目录结构不显示
vim /usr/local/apache2/etc/httpd.conf   
Options Indexes FollowSymLinks
Indexes：	浏览权限（当此目录下没有默认网页文件时，显示目录内容）,网站上线后不要这个选项







启动命令：./apachectl start
重启命令：./apachectl restart
关闭服务：./apachectl stop




2e 21 1d




克隆后网卡的解决方法 首先 service network restart

 1.vim /etc/udev/rules.d/70-persistent-net.rules 
00:50:56:2E:A5:80
 -------------------------------------------------------------------------
  把下面这段注释掉
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:38:d6:90", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
----------------------------------------------------------------------------------
把最后的NAME="eth1" 改成NAME="eth0"
# PCI device 0x1022:0x2000 (pcnet32)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:76:7e:6c", ATTR{type}=="1", KERNEL=="eth*", NAME="eth1"



2.vim /etc/sysconfig/network-scripts/ifcfg-eth0 修改HWADDR=00:0c:29:76:7e:6c跟第一步ATTR{address}=="00:0c:29:76:7e:6c" 的00:0c:29:76:7e:6c改为一样
DEVICE=eth0
BOOTPROTO=none
HWADDR=00:0c:29:76:7e:6c
NM_CONTROLLED=yes
ONBOOT=yes
TYPE=Ethernet
UUID="50e7f123-0b09-43b5-9f37-e76fc6949cc8"
IPADDR=192.168.11.138
GATEWAY=192.168.11.1
DNS1=114.114.114.114
IPV6INIT=no
USERCTL=no

3.reboot
如果是直接复制的文件，新执行上面代码一次，在恢复快照，然会在执行上面代码




linux下如何添加一个用户并且让用户获得root权限

1、添加用户，首先用adduser命令添加一个普通用户，命令如下： #adduser tommy //添加一个名为tommy的用户
#passwd tommy //修改密码
Changing password for user tommy.
New UNIX password: //在这里输入新密码
Retype new UNIX password: //再次输入新密码
passwd: all authentication tokens updated successfully.
2、赋予root权限方法一：修改/etc/sudoers 文件，找到下面一行，把前面的注释（#）去掉
## Allows people in group wheel to run all commands
%wheel ALL=(ALL) ALL
然后修改用户，使其属于root组（wheel），命令如下：
#usermod -g root tommy
修改完毕，现在可以用tommy帐号登录，然后用命令 su - ，即可获得root权限进行操作。
方法二：修改/etc/sudoers 文件，找到下面一行，在root下面添加一行，如下所示：
## Allow root to run any commands anywhere
root ALL=(ALL) ALL
tommy ALL=(ALL) ALL
修改完毕，现在可以用tommy帐号登录，然后用命令 su - ，即可获得root权限进行操作。
方法三：修改/etc/passwd 文件，找到如下行，把用户ID修改为 0 ，如下所示：
tommy:x:500:500:tommy:/home/tommy:/bin/bash修改后如下tommy:x:0:500:tommy:/home/tommy:/bin/bash
保存，用tommy账户登录后，直接获取的就是root帐号的权限。
友情提醒：虽然方法三看上去简单方便，但一般不推荐使用，推荐使用方法二。





----------------------用php动态配置域名----------------------------------
在root用户环境中做如下操作
cd ……/apache/bin  --进入apache  bin目录 修改httpd文件权限
chown root httpd
chmod u+s httpd
再 su - USERNAME   --切换到普通用户 测试
到普通用户下，通过
……/apache/bin/apachectl start即可










<VirtualHost *:80> 
   ServerAdmin yd@admin.com 
  DocumentRoot '/www/web/yundi88_com/public_html' 
    ServerName www.yundi88.com 
   ErrorLog 'logs/dummy-host2.example.com-error_log' 
  CustomLog 'logs/dummy-host2.example.com-access_log' common 
</VirtualHost> 
