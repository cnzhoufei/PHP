#挂载光盘YUM源
#mkdir /mnt/cdrom
#mount /dev/sr0 /mnt/cdrom

#安装编译工具
yum install -y gcc
yum install -y gcc-c++
yum install -y make

# 1.1 安装libxml2
##如果报错需安装 libxml2-devel
yum  install  -y  libxml2-devel
##必须安装 Python-devel
yum install -y python-devel
cd libxml2-2.9.1

./configure --prefix=/usr/local/libxml2
make && make install && cd ..

# 1.2安装 libmcrypt
 cd libmcrypt-2.5.8
 ./configure --prefix=/usr/local/libmcrypt/
 make && make install
 cd libltdl
 ./configure --enable-ltdl-install
 make
 make install
 cd ..
 cd ..

 # 1.3 安装mhash
cd mhash-0.9.9.9
./configure 
make
make install && cd ..

# 1.4 安装mcrypt
cd mcrypt-2.6.8

LD_LIBRARY_PATH=/usr/local/libmcrypt/lib:/usr/local/lib  \
./configure --with-libmcrypt-prefix=/usr/local/libmcrypt

make
make install
cd ..

# 1.5 安装zlib
cd zlib-1.2.3
./configure
 make
 make install  >>  /root/zlib_makeinstall.log
 cd ..

# 1.6 安装 libpng
cd libpng-1.2.31
 ./configure --prefix=/usr/local/libpng
 make
 make install && cd ..

 #1.7 安装jpeg6
 ## 需手工建立安装目录
mkdir /usr/local/jpeg6	
 mkdir /usr/local/jpeg6/bin
 mkdir /usr/local/jpeg6/lib
 mkdir /usr/local/jpeg6/include
 mkdir -p /usr/local/jpeg6/man/man1


 cd jpeg-6b
 ./configure --prefix=/usr/local/jpeg6/ --enable-shared --enable-static
 make	
 make install
cd ..

# 1.8 安装freetype
cd freetype-2.3.5
./configure --prefix=/usr/local/freetype
make && make install && cd ..

# 1.9 安装pcre
yum install -y openssl-devel
cd pcre-8.34
./configure && make && make install && cd ..


# 1.10 安装apache2.4.7
cd httpd-2.4.7
cp -r ../apr-1.4.6 ./srclib/apr
cp -r ../apr-util-1.4.1 ./srclib/apr-util

./configure --prefix=/usr/local/apache2/ --sysconfdir=/usr/local/apache2/etc/ --with-included-apr --enable-so --enable-deflate=shared --enable-expires=shared --enable-rewrite=shared
make && make install && cd ..


#apache安装好 
echo "iptables -F" >> /etc/rc.d/rc.local
echo "/usr/local/apache2/bin/apachectl start" >> /etc/rc.d/rc.local
#安装mysql
yum -y install ncurses-devel
yum -y install cmake
yum -y install bison
groupadd mysql
useradd -g mysql mysql
mkdir -p /usr/local/mysql/data
cd mysql-5.5.23
cmake  -DCMAKE_INSTALL_PREFIX=/usr/local/mysql    -DMYSQL_UNIX_ADDR=/tmp/mysql.sock  -DEXTRA_CHARSETS=all   -DDEFAULT_CHARSET=utf8    -DDEFAULT_COLLATION=utf8_general_ci    -DWITH_MYISAM_STORAGE_ENGINE=1   -DWITH_INNOBASE_STORAGE_ENGINE=1    -DWITH_MEMORY_STORAGE_ENGINE=1  -DWITH_READLINE=1    -DENABLED_LOCAL_INFILE=1   -DMYSQL_USER=mysql  -DMYSQL_TCP_PORT=3306
make
make install
############开始设置mysql
rm -rf /etc/my.cnf
cd /usr/local/mysql
./scripts/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data

mkdir /usr/local/mysql/etc
cp support-files/my-medium.cnf /usr/local/mysql/etc/my.cnf
ln -s /usr/local/mysql/my.cnf /etc/my.cnf
#要修改这个文件里边的两行，可以用别的文件替换
#例如
#cp /usr/loacl/src/lamp/mysqld /etc/rc.d/init.d/
cp ./support-files/mysql.server /etc/rc.d/init.d/mysqld
chmod 755 /etc/init.d/mysqld
chkconfig mysqld on
##设置mysql密码
##mysql_secure_installation
#修改 /etc/rc.d/init.d/mysqld文件 找到
#basedir=
#datadir=
#改为
#basedir=/usr/local/mysql
#datadir=/usr/local/mysql/data
############################################
#下面安装php
cd /usr/local/src/lamp/
cd php-5.6.15
echo "/usr/local/lib" >> /etc/ld.so.conf.d/local.conf
ldconfig -v
./configure --prefix=/usr/local/php/ --with-config-file-path=/usr/local/php/etc/ --with-apxs2=/usr/local/apache2/bin/apxs --with-mysql=/usr/local/mysql/ --with-libxml-dir=/usr/local/libxml2/ --with-jpeg-dir=/usr/local/jpeg6/ --with-png-dir=/usr/local/libpng/ --with-freetype-dir=/usr/local/freetype/  --with-gd  --with-mcrypt=/usr/local/libmcrypt/ --with-mysqli=/usr/local/mysql/bin/mysql_config --enable-soap --enable-mbstring=all --enable-sockets  --with-pdo-mysql=/usr/local/mysql  --without-pear
#配置报错
#checking for known struct flock definition... configure: error: Don't know how to define struct flock on this system, set --enable-opcache=no
#解决办法
#vim /etc/ld.so.conf.d/local.conf     # 编辑库文件
#/usr/local/lib                       # 添加该行
#:wq                                  # 保存退出
#ldconfig -v                          # 使之生效
make
make install
mkdir /usr/local/php/etc/
#生产环境
#cp /usr/local/src/lamp/php-5.6.15/php.ini-production /usr/local/php/etc/php.ini
#开发环境
cp /usr/local/src/lamp/php-5.6.15/php.ini-development /usr/local/php/etc/php.ini
#编辑apache配置文件,使apche解析php文件
##vim /usr/local/apache2/etc/httpd.conf
## AddType application/x-httpd-php .php .phtml 
## AddType application/x-httpd-php-source .phps
#编辑php配置文件 设置默认时区
##date.timezone = PRC
##这句有问题
#?????/echo "export PATH=/usr/local/php/bin:$PATH" >> /etc/profile
#使生效
#source /etc/profile
###PHP安装完成 继续
#openssl
yum -y install openssl-devel
yum -y install autoconf
cd /usr/local/src/lamp/php-5.6.15/ext/openssl
mv config0.m4 config.m4
/usr/local/php/bin/phpize
./configure --with-openssl --with-php-config=/usr/local/php/bin/php-config 
make
make install
# 编译安装memcache
yum -y install zlib-devel  
cd /usr/local/src/lamp/memcache-3.0.8 
/usr/local/php/bin/phpize
./configure --with-php-config=/usr/local/php/bin/php-config
make && make install

#编译安装mcrypt
cd /usr/local/src/lamp/php-5.6.15/ext/mcrypt/
/usr/local/php/bin/phpize
./configure --with-php-config=/usr/local/php/bin/php-config --with-mcrypt=/usr/local/libmcrypt/
make
make install
##
#修改/usr/local/php/etc/php.ini
#extension_dir = "/usr/local/php/lib/php/extensions/no-debug-zts-20131226/"
#打开注释，并修改
#extension="memcache.so";
#extension="mcrypt.so"; 
#extension="openssl.so";
#添加
#重启apache，在phpinfo中可以找到这三个模块

#安装memcache源代码
#首先安装依赖包libevent
# yum -y install "libevent*"
yum install -y libevent libevent-devel
#wget  http://cloud.github.com/downloads/libevent/libevent/libevent-2.0.16-stable.tar.gz
#tar -zxvf libevent-2.0.16-stable.tar.gz
cd /usr/local/src/lamp/memcached-1.4.17
./configure --prefix=/usr/local/memcache --with-libevent=/usr
make && make install
#ta
useradd memcache
/usr/local/memcache/bin/memcached -umemcache &
#加入开机自启动
#vim /etc/rc.d/rc.local
#/usr/local/memcache/bin/memcached -umemcache &
echo "/usr/local/memcache/bin/memcached -umemcache &" >> /etc/rc.d/rc.local

#phpmyadmin
cp -r /usr/local/src/lamp/phpMyAdmin-4.1.4-all-languages /usr/local/apache2/htdocs/phpmyadmin
cd /usr/local/apache2/htdocs/phpmyadmin
cp config.sample.inc.php config.inc.php
#编辑phpmyadmin初始化文件










