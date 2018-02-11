画图  www.processon.com

paramiko #ssh ftp

pyyam


#接收地址栏参数
from sys import argv
 
script,first = argv
print "the script is called:", script
print "the first variable is:", first

#linxu 安装python3
#安装依赖
# yum -y groupinstall development
# yum -y install zlib zlib-devel
# yum -y install bzip2 bzip2-devel
# yum -y install ncurses ncurses-devel
# yum -y install readline readline-devel
# yum -y install openssl openssl-devel
# yum -y install openssl-static
# yum -y install xz lzma xz-devel
# yum -y install sqlite sqlite-devel
# yum -y install gdbm gdbm-devel
# yum -y install tk tk-devel
# wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4rc1.tgz
# gzip -d Python-3.6.4rc1.tgz
# tar xf Python-3.6.4rc1.tar
# ./configure
#make
# make install


#打包成 .exe
# pyinstaller -F ss.py


# 生成单个pyc文件
# 对于py文件，可以执行下面命令来生成pyc文件。

# python -m foo.py
# 另外一种方式是通过代码来生成pyc文件。

# import py_compile
# py_compile.compile('/path/to/foo.py')
# 批量生成pyc文件
# 针对一个目录下所有的py文件进行编译。python提供了一个模块叫compileall，具体请看下面代码：

# import compileall
# compileall.compile_dir(r'/path')
# 这个函数的格式如下：

# compile_dir(dir[, maxlevels[, ddir[, force[, rx[, quiet]]]]])
# 参数含义：

# maxlevels: 递归编译的层数
# ddir: If ddir is given, it is prepended to the path to each file being compiled for use in compilation time tracebacks, and is also compiled in to the byte-code file, where it will be used in tracebacks and other messages in cases where the source file does not exist at the time the byte-code file is executed. (谁能翻译一下( ⊙o⊙?)不懂)
# force: 如果True，不论是是否有pyc，都重新编译
# rx: 一个正则表达式，排除掉不想要的目录
# quiet：如果为True，则编译不会在标准输出中打印信息
# 命令行为：

# python -m compileall <dir>



#linux下 后台运行python脚本： nohup python3 -u monitoringDZ.py > monitoringDZ.log 2>&1 &

# python安装
# https://www.continuum.io/downloads
#国内 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive
#linux ubuntu系统
#sudo apt-get install python3-dev build-essential libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev
#sudo apt-get install python3
#sudo apt-get install python3-pip
whereis python3



F:\Python36\Scripts\
F:\Python36\
F:\Python36\Scripts
F:\phantomjs-2.1.1-windows\bin