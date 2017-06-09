#环境 CentOS7.3 + git version 1.8.3.1
yum -y install git
useradd git
passwd git
123

cd /
mkdir git
cd git
mkdir gitdemo
cd gitdemo
git init --bare
cd hooks
cp post-update.sample post-update
vim post-update
	注释掉一行 加两行
	
	#exec git update-server-info
	cd /opt/www/gitdemo
	env -i git pull

cd /git
chown -R git:git gitdemo


cd /opt/www
#clone 一次 以后就用脚本pull了
git clone /git/gitdemo

setfacl -m u:git:rwx -R /www
setfacl -m d:u:git:rwx -R /www



setfacl -m u:nobody:rwx -R /opt/www
setfacl -m d:u:nobody:rwx -R /opt/www

setfacl -m u:git:rwx -R /opt/www
setfacl -m d:u:git:rwx -R /opt/www
##本地这么做
d盘 www
git clone git@120.xx.xx.1:/git/gitdemo
cd gitdemo
编写文件 1.php 1111
git add 1.php
git commit -m '1.php'


##去web目录里看看是不是已经自动发布了
over
