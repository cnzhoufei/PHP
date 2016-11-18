<?php 


1.数组的概述
	PHP 中的数组实际上是一个有序图。图是一种把 values 映射到 keys 的类型。此类型在很多方面做了优化，因此可以把它当成真正的数组来使用，或列表（矢量），散列表（是图的一种实现），字典，集合，栈，队列以及更多可能性。因为可以用另一个 PHP 数组作为值，也可以很容易地模拟树。 

	1.1 所谓的数组下标可以视为资料内容在此数组中的识别名称，通常被称为数组下标。
	1.2 当索引值为数值时，也代表此资料内容在数组中的储存位置。
	1.3 数组中有几个索引值就被称为几维数组。
	1.4 数组分类：
		在PHP中有两种数组：索引数组和关联数组。
			1.索引（indexed）数组的索引值是整数，以0开始。当通过位置来标识东西时用索引数组。
			2.关联（associative）数组以字符串做为索引值，关联数组更像操作表。索引值为列名，用于访问列的数据。
		按照维度： 
			1.一维数组、二维数组、三维数组...
			数组中有几个索引值就被称为几维数组。

2.数组的定义
	数组常用的赋值方式：
	由于 PHP 是属于弱类型数据，因此源代码中的数组并不需要经过特别的声明操作，直接将一组数值指定给某一数组元素即可。

2.1 直接赋值的方式声明数组
	1.直接赋值格式：
		$数组变量名[索引值]=资料内容
	2.其中索引值（下标）可以是一个字符串或一个整数。等价于整数（不以0开头）的字符串值被当作整数对待。
	因此，数组$array[3]与$array['3']是引用相同的元素。但是$array['03']引用的另外不同的元素。
	3.一维数组
		数组中索引值(下标)只有一个的数组称为一维数组。在数组中这是最简单的，也是最常用的了。
2.2  使用array( )语言结构新建数组

	1.格式：
	    array( [key =>] value , ... ) 
		$a=array(“spam@126.com “,”abuse@sohu.com”);
	2.key 可以是 integer 或者 string。如果键名是一个 integer 的标准表达方法，则被解释为整数（例如 “8” 将被解释为 8，而 “08” 将被解释为 “08”）。key 中的浮点数被取整为 integer。PHP 中没有不同的数字下标和关联下标数组，数组的类型只有一种，它可以同时包含整型和字符串型的下标。 
	3.如果对给出的值没有指定键名，则取当前最大的整数索引值，而新的键名将是该值加一。如果指定的键名已经有了值，则该值会被覆盖。 


	2.3  使用[ ] 定义数组 5.3后才支持
		$a=[“spam@126.com “,”abuse@sohu.com”];
	2.4  多维数组的声明

3.数组的遍历
	3.1 使用for语句循环遍历数组
		 for ($i = 0; $i < 数组长度; $i ++){
		      数组[$i];
		  }
	3.2 使用foreach语句遍历数组
		foreach (数组  as $value){}
		foreach (数组  as $key => $value){}
		Ps:foreach是最好用的数组的遍历方式
		  多维数组的遍历可以通过foreach嵌套来完成
	3.3 联合使用list( )、each( )和while循环遍历数组
		$fruit= array('a' => 'apple', 'b' => 'banana', 'c' => 'cranberry');
		reset($fruit);
		while (list($key,$val) = each($fruit)) {
		    echo "$key => $val\n";
		}

	3.4 使用数组的内部指针控制函数遍历数组
		next()
		prev()
		end()
		reset()
		key()
		current()



预定义数组(超全局数据)
1  服务器变量： $_SERVER
	$_SERVER 是一个包含诸如头信息（header）、路径（path）和脚本位置（script locations）的数组。数组的实体由 web 服务器创建。不能保证所有的服务器都能产生所有的信息；服务器可能忽略了一些信息，或者产生了一些未在下面列出的新的信息。这是一个自动全局变量。这只不过意味这它在所有的脚本中都有效。

2  环境变量：$_ENV
	在解析器运行时，这些变量从环境变量转变为 PHP 全局变量名称空间（namespace）。它们中的许多都是由 PHP 所运行的系统决定。完整的列表是不可能的。请查看系统的文档以确定其特定的环境变量。
	这是一个自动全局变量。它在所有的脚本中都有效。在函数或方法中不需要使用 global $_ENV; 

	variables_order = "GPCS" 改成
	variables_order = "EGPCS"

3  HTTP GET变量：$_GET
	通过 HTTP GET 方法传递的变量组成的数组。

4  HHTP POST变量：$_POST
	通过 HTTP POST 方法传递的变量组成的数组。
	与$_GET相似，只是方法不一样。

5  request变量：$_REQUEST
	包含 $_GET，$_POST 和 $_COOKIE 中的全部内容。

6  HTTP文件上传变量：$_FILES
	通过 HTTP POST 方法传递的已上传文件项目组成的数组。

7  HTTP Cookies:$_COOKIE
	通过 HTTP cookies 传递的变量组成的数组。

8  Session变量：$_SESSION
	包含当前脚本中 session 变量的数组。

9  Global变量：$_GLOBALS
	由所有已定义全局变量组成的数组。变量名就是该数组的索引。 



数组的相关处理函数
5. 数组的相关处理函数
		5.1  数组的键/值操作函数
			array_values()
			array_keys()
			in_array()
			array_flip()
			array_reverse()
		5.2  统计数组元素的个数与唯一性
		    count()
			array_count_values()
			array_unique()
		5.3  使用回调函数处理数组的函数
			array_filter()
			array_walk()
			array_map()
		5.4  数组的排序函数
			sort()
			rsort()
			usort()
			asort()
			arsort()
			uasort()
			ksort()
			krsort()
			uksort()
			natsort()
			natcasesort()
			array_multisort()
		5.5  拆分、合并、分解与结合数组
			array_slice()
			array_splice()
			array_combine()
			array_merge()
			array_intersect()
			array_diff()
		5.6  数组与数据结构
			array_pop()
			array_push()
			array_shift()
			array_unshift()
		5.7  其他有用的数组处理函数
			array_rand()
			shuffle()











