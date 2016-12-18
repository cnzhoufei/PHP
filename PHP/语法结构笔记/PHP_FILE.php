本章任务
	1. 文件系统概述
	2. 目录的基本操作
	3. 文件的基本操作

1. 文件系统概述
	

	1.1 文件类型
		在程序运行时，程序本身和数据一般都存在内存中，当程序运行结束后，存放在内存中的数据被释放。
如果需要长期保存程序运行所需的原始数据，或程序运行产生的结果，就必须以文件形式存储到外部存储介质上。
文件一般指存储在外部介质上具有名字（文件名）的一组相关数据集合。用文件可长期保存数据，并实现数据共享。
PHP是以UNIX的文件系统为模型的。因此在Windows系统中我们只能获得”file”、”dir”或者“unknown”三种文件类型。而在UNIX系统中，我们可以获得block、char、dir、fifo、file、link和unknown七种类型。
可以使用函数filetype（）获取文件的具体类型。
语法：string filetype ( string filename ) 


UNIX系统中7种文件类型说明
	文件类型 	描述
	block 		块设备文件，如某个磁盘分区，软驱，光驱CD-ROM等
	char 		字符设备是指在I/O传输过程中以字符为单位进行传输的设备，如键盘、打印机等
	dir			目录类型，目录也是文件的一种
	fifo 		命名管道，常用于将信息从一个进程传递到另一个进程
	file 		普通文件类型，如文本文件或可执行文件等
	link 		符号链接，是指向文件指针的指针。类似Windows中的快捷方式
	unknown 	未知类型。


文件相关函数：
	is_dir( ) -- 判断给定文件名是否是一个目录
	语法结构：bool is_dir（名称）
	返回类型：文件名存在并且是一个目录则返回 true，否则返回 false
	is_executable( ) -- 判断给定文件名是否可执行
	语法结构：bool is_executable（名称）
	返回类型：如果文件存在且可执行则返回 true ，否则返回 false 。
	is_file( ) -- 判断给定文件名是否为一个正常的文件
	语法结构：bool is_file(名称)	
	返回类型：如果文件存在且为正常的文件则返回 true 。
	is_link( ) -- 判断给定文件名是否为一个符号连接
	语法结构：bool is_link(名称) 	
	返回类型：如果文件存在并且是一个符号连接则返回 true。
	is_readable( ) -- 判断给定文件名是否可读
	语法结构：bool is_readable（文件名称）	
	返回类型：如果文件存在并且可读则返回 true 。
	is_writable( ) -- 判断给定的文件名是否可写
	语法结构：bool is_writable(文件名称)	
	返回类型：如果文件存在并且可写则返回 true 。


1.2 文件的属性
	file_exists() 		检查文件或目录是否存在
	filesize() 	 		取得文件大小
	is_readable() 		判断文件是否可读
	is_writable() 		判断文件是否可写
	is_executable() 	判断文件是否可执行
	filectime() 		获取文件的创建时间
	filemtime() 		获取文件的修改时间
	fileatime()  		获取文件的访问时间
	stat() 				获取文件大部分属性


2. 目录的基本操作
	2.1 解析目录路径
		使用PHP脚本可以方便对目录进行操作，如创建目录、遍历目录、复值目录与删除目录等操作。
		常用的文件目录路径格式：
		$unixPath="/var/www/html/index.php";	
			//在UNIX系统中的绝对路径，必须使用"/"分隔
		$winPath="C:\\Appserv\\www\\index.php"; 
			//在Windows系统的绝对路径，默认使用"\"分隔
		$winPath2="C:/Appserv/www/index.php";   
			//在Windows系统中也可使用“/”分隔。
		注意使用绝对路径与相对路径。

	PHP文件路径相关函数
		basename -- 返回路径中的文件名部分 
		dirname -- 返回路径中的目录部分

			$path = "/home/httpd/html/index.php";
	        $file = basename($path);		// $file值："index.php"
	        $file = basename($path, ".php "); 	// $file值："index "
	        $file = dirname($path);   	 // $file值："/home/httpd/html

		pathinfo -- 返回文件路径的信息 
			$path_parts = pathinfo("/www/htdocs/index.html");
			echo $path_parts["dirname"]."\n";    // /www/htdocs
			echo $path_parts["basename"]."\n";   // index.html
			echo $path_parts["extension"]."\n";  // html
		realpath -- 返回规范化的绝对路径名 


	2.2 遍历目录
		opendir -- 打开目录句柄 
		readdir -- 从目录句柄中读取条目 
		closedir -- 关闭目录句柄 
		rewinddir -- 倒回目录句柄 
			一个句柄是指使用的一个唯一的整数值，即一个4字节(64位程序中为8字节)长的数值，来标识应用程序中的不同对象和同类中的不同的实例，诸如，一个窗口，按钮，图标，滚动条，输出设备，控件或者文件等。应用程序能够通过句柄访问相应的对象的信息，但是句柄不是指针，程序不能利用句柄来直接阅读文件中的信息。如果句柄不在I/O文件中，它是毫无用处的。 句柄是Windows用来标志应用程序中建立的或是使用的唯一整数

			目录遍历

	2.3 统计目录大小
		disk_free_space -- 返回目录中的可用空间 
		disk_total_space -- 返回一个目录的磁盘总大小 

		统计指定目录大小的函数  要自定义 

	2.4 建立与删除目录
		mkdir -- 新建目录 
		rmdir -- 删除目录 
		unlink -- 删除文件




	2.5 复制目录
		copy -- 拷贝文件 
		如何定义一个目录复制函数呢？

3. 文件的基本操作
3.1 文件的打开与关闭

	fopen -- 打开文件或者 URL 
	语法：resource fopen ( string filename, string mode [, bool use_include_path [, resource zcontext]] )
	filename参数需要提供要被打开文件的URL。这个URL可以是脚本所在的服务器中的绝对路径，也可以是相对路径，还可以是网络资源用的文件。 
	mode 参数指定了所要求到该流的访问类型,(强烈建议附加b模式)。 
	如果也需要在 include_path中搜寻文件的话，可以将可选的第三个参数 use_include_path 设为 '1' 或 TRUE。 
	如果打开失败，本函数返回 FALSE。

	fclose -- 关闭一个已打开的文件指针 
	语法：bool fclose ( resource $handle )
	将 handle 指向的文件关闭。 成功时返回 TRUE， 或者在失败时返回 FALSE. 

    //使用绝对路径打开file.txt文件，选择只读模式，并返回资源$handle
    $handle = fopen("/home/rasmus/file.txt", "r");

    //访问文档根目录下的文件，也以只读模式打开
    $handle = fopen(“{$_SERVER['DOCUMENT_ROOT']}/data/info.txt", "r");

    //在 Windows 平台上，转义文件路径中的每个反斜线，或者用斜线，
      以二进制和只写模式组合
    $handle = fopen("c:\\data\\file.gif", "wb");

    //使用相对路径打开file.txt文件，选择只读模式，并返回资源$handle
    $handle = fopen("../data/info.txt", "r");

    //打开远程文件， 使用HTTP协议只能以只读的模式打开
    $handle = fopen("http://www.example.com/", "r");

    //使用FTP协议打开远程文件，如果FTP服务器可写，则可以以写的模式打开
    $handle = fopen("ftp://user:password@example.com/somefile.txt", "w");

    打开方式：
    	r 		只读方式打开
		r+		读写方式打开， 指针指向开头位置
		w		只写方式打开， 指针指向开头位置，大小截为0， 如果不存在尝试创建
		w+	读写方式打开， 指针指向开头位置，大小截为0， 如果不存在尝试创建
		a		以只写方式打开，文件指针指向末尾， 如果不存在，尝试创建
		a+	以读写方式打开，文件指针指向末尾， 如果不存在，尝试创建
		x		以只写方式打开， 如果文件存在报错，不存在创建， 指针指向开头
		x+	以读写方式打开， 如果文件存在报错，不存在创建， 指针指向开头

3.2 写入文件
	fwrite -- 写入文件（可安全用于二进制文件）
	file_put_contents()   向文件中写入内容

3.3 读取文件内容
	fread() 	读取文件（可安全用于二进制文件）
	fgets() 	从打开的文件中读取一行
	fgetc() 	从打开的文件中读取一个字符
	file() 		把文件读入一个数组中（无需使用fopen打开）
	readfile() 	读取一个文件，并输出到输出缓冲（无需使用fopen打开）
	file_get_contents() 将文件读入字符串


3.4 访问远程文件
	如果需要访问远程文件，必须在PHP的配置文件中激活“allow_url_fopen”选项，才能使用fopen( )函数打开运程文件。而且还要确定其他服务器中的文件是否访问权限，如果使用PHP协议对远程文件进行链接，只能以“只读”模式打开。如果需要访问的远程FTP服务器中，对所提供的用户开启了“可写”权限，则使用FTP协议链接远程的文件时，就可以使用“只写”或“只读”模式打开文件。但不可以使用“可读可写”的模式。
	使用PHP访问远程文件就像访问本地文件一样，都是使用相同的读写函数处理。
	$file=fopen(“http://www.lampbrother.com/”,”r”) or die(“打开远程文件失败！！”)；
	$file=fopen(“ftp://user:password@ftp.lampbrother.net/path/to/file”,”w”);

3.5 移动文件指针
	ftell -- 返回文件指针读/写的位置 
	fseek -- 在文件指针中定位 
	rewind -- 倒回文件指针的位置 

3.6 文件的锁定机制
	flock()		文件锁
	文件锁的类型（第二个参数）
		LOCK_EX   	独占锁（用于写）
		LOCK_SH		共享锁	（用于读）
		LOCK_UN		释放锁
		LOCK_NB		避免阻塞
3.7 文件的一些基本操作函数
	copy -- 拷贝文件 
	unlink -- 删除文件 
	ftruncate -- 将文件截断到给定的长度 
	rename -- 重命名一个文件或目录 


	


