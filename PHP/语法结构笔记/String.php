<?php 

PHP 中的字符串
===============================================================================
1. 字符串的处理介绍
	在C语言中字符串是作为字节数组处理的。在Java语言中字符串是作为对象处理的。而php则把字符串作为基本数据类型来处理。
	通常对字符串的处理涉及字符串的格式化。字符串的分割和连接、字符串的比较、以及字符串的查找、匹配和替换。
	
2. 常用的字符串输出函数
	2.1 常用的输出字符串函数：
		echo( )   -- 输出字符串
		print( )  -- 输出一个字符串
		die( )    -- 输出一条消息，并退出当前脚本
		printf( ) -- 输出格式化字符串
		sprintf( )-- 把格式化的字符串写入一个变量中
	2.2 printf与sprintf都是格式化字串：
		字符串转换格式：
			%%	返回百分比符号
			%b	二进制数
			%c	依照ASCII值的字符
			%d	带符号十进制数
			%e    	可续计数法（如1.5e3）
			%u	无符号十进制数
			%f或%F 	浮点数
			%o	八进制数
			%s	字符串
			%x或%X  十六进制数
3. 常用的字符串格式化函数
	3.1 去除空格和字符串填充补函数
		ltrim()
		rtrim()
		trim()
		str_pad()
	3.2 字符串大小写的转换
		strtolower()
		strtoupper()
		ucfirst()
		ucwords()
	3.3 和HTML标签相关联的字符串格式化
		nl2br
		htmlspecialchars()
		htmlentities()
		strip_tags()
	3.4 其他字符串格式化函数
		strrev()
		strlen()
		number_format()
		md5()
4 字符串操作函数
	4.1 字符串比较函数
		 strcmp()
		 strncmp()
		 strcasecmp()
		 strnatcmp()
		 similar_text()
	4.2 字符串分割与拼装
		explode()
		implode()
		join()
	4.3 字符串截取
		substr()
	4.4 字符串查找
		strstr() strchr()
		strrchr()
		strpos()
		strrpos()
	4.5 字符串替换
		str_replace()
		
