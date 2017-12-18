<?php
sprintf('%011d','100');#不够11位用0补
trim()	删除字符串两端的空格或其他预定义字符	"$str = ""\r\nHello World!\r\n"";
echo trim($str);
"
rtrim()	删除字符串右边的空格或其他预定义字符	"$str = ""Hello World!\n\n"";
echo rtrim($str);"
chop()	rtrim()的别名	
ltrim()	删除字符串左边的空格或其他预定义字符	"$str = ""\r\nHello World!"";
echo ltrim($str);"
dirname()	返回路径中的目录部分	echo dirname("c:/testweb/home.php");
字符串生成与转化:		
str_pad()	把字符串填充为指定的长度	"$str = ""Hello World"";
echo str_pad($str,20,""."");"
str_repeat()	重复使用指定字符串	echo str_repeat(".",13);
str_split()	把字符串分割到数组中	print_r(str_split("Hello"));
strrev()	反转字符串	echo strrev("Hello World!");
wordwrap()	按照指定长度对字符串进行折行处理	"$str = ""An example on a long word is: Supercalifragulistic"";
echo wordwrap($str,15);"
str_shuffle()	随机地打乱字符串中所有字符	echo str_shuffle("Hello World");
parse_str()	将字符串解析成变量	"parse_str(""id=23&name=John%20Adams"",$myArray);
print_r($myArray);"
number_format()	通过千位分组来格式化数字	"
"
大小写转换:		
strtolower()	字符串转为小写	echo strtolower("Hello WORLD!");
strtoupper()	字符串转为大写	echo strtoupper("Hello WORLD!");
ucfirst()	字符串首字母大写	echo ucfirst("hello world");
ucwords()	字符串每个单词首字符转为大写	echo ucwords("hello world");
html标签关联:		
htmlentities()	把字符转为HTML实体	"$str = ""John & 'Adams'"";
echo htmlentities($str, ENT_COMPAT);"
htmlspecialchars()	预定义字符转html编码	
nl2br()	\n转义为<br>标签	echo nl2br("One line.\nAnother line.");
strip_tags()	剥去 HTML、XML 以及 PHP 的标签	echo strip_tags("Hello <b>world!</b>");
addcslashes()	在指定的字符前添加反斜线转义字符串中字符	"$str = ""Hello, my name is John Adams."";
echo $str;
echo addcslashes($str,'m');"
stripcslashes()	 删除由addcslashes()添加的反斜线	echo stripcslashes("Hello, \my na\me is Kai Ji\m.");
addslashes()	指定预定义字符前添加反斜线	$str = "Who's John Adams?";echo addslashes($str);
stripslashes()	删除由addslashes()添加的转义字符	echo stripslashes("Who\'s John Adams?");
quotemeta()	在字符串中某些预定义的字符前添加反斜线	"$str = ""Hello world. (can you hear me?)"";
echo quotemeta($str);"
chr()	从指定的 ASCII 值返回字符	echo chr(052);
ord()	返回字符串第一个字符的 ASCII 值	echo ord("hello");
字符串比较:		
strcasecmp()	不区分大小写比较两字符串	echo strcasecmp("Hello world!","HELLO WORLD!");
strcmp()	区分大小写比较两字符串	
strncmp()	比较字符串前n个字符,区分大小写	int strncmp ( string $str1 , string $str2 , int $len )
strncasecmp()	比较字符串前n个字符,不区分大小写	int strncasecmp ( string $str1 , string $str2 , int $len )
strnatcmp()	自然顺序法比较字符串长度,区分大小写	int strnatcmp ( string $str1 , string $str2 )
strnatcasecmp()	自然顺序法比较字符串长度,不区分大小写	int strnatcasecmp ( string $str1 , string $str2 )
字符串切割与拼接:		
chunk_split()	将字符串分成小块	str chunk_split(str $body[,int $len[,str $end]])
strtok()	切开字符串	str strtok(str $str,str $token)
explode()	使用一个字符串为标志分割另一个字符串	array explode(str $sep,str $str[,int $limit])
implode()	同join,将数组值用预订字符连接成字符串	string implode ( string $glue , array $pieces )
substr()	截取字符串	string substr ( string $string , int $start [, int $length ] )
字符串查找替换:		
str_replace()	字符串替换操作,区分大小写	mix str_replace(mix $search,,mix $replace,mix $subject[,int &$num])
str_ireplace()	字符串替换操作,不区分大小写	mix str_ireplace ( mix $search , mix $replace , mix $subject [, int &$count ] )
substr_count()	统计一个字符串,在另一个字符串中出现次数	"int substr_count ( string $haystack , string $needle [, int $offset = 0 [, int $length ]] )
"
substr_replace()	替换字符串中某串为另一个字符串	mixed substr_replace ( mixed $string , string $replacement , int $start [, int $length ] )
similar_text()	返回两字符串相同字符的数量	int similar_text(str $str1,str $str2)
strrchr()	返回一个字符串在另一个字符串中最后一次出现位置开始到末尾的字符串	string strrchr ( string $haystack , mixed $needle )
strstr()	返回一个字符串在另一个字符串中开始位置到结束的字符串	string strstr ( string $str, string $needle , bool $before_needle )
strchr()	strstr()的别名,返回一个字符串在另一个字符串中首次出现的位置开始到末尾的字符串	string strstr ( string $haystack , mixed $needle [, bool $before_needle = false ] )
stristr()	返回一个字符串在另一个字符串中开始位置到结束的字符串，不区分大小写	string stristr ( string $haystack , mixed $needle [, bool $before_needle = false ] )
strtr()	转换字符串中的某些字符	 string strtr  ($str , string $from , string $to )
strpos()	寻找字符串中某字符最先出现的位置	int strpos ( string $haystack , mixed $needle [, int $offset = 0 ] )
stripos()	寻找字符串中某字符最先出现的位置,不区分大小写	int stripos ( string $haystack , string $needle [, int $offset ] )
strrpos()	寻找某字符串中某字符最后出现的位置	int strrpos ( string $haystack , string $needle [, int $offset = 0 ] )
strripos()	寻找某字符串中某字符最后出现的位置,不区分大小写	int strripos ( string $haystack , string $needle [, int $offset ] )
strspn()	返回字符串中首次符合mask的子字符串长度	int strspn ( string $str1 , string $str2 [, int $start [, int $length ]] )
strcspn()	返回字符串中不符合mask的字符串的长度	int strcspn ( string $str1 , string $str2 [, int $start [, int $length ]] )
字符串统计:		
str_word_count()	统计字符串含有的单词数	mix str_word_count(str $str,[])
strlen()	统计字符串长度	int strlen(str $str)
count_chars()	统计字符串中所有字母出现次数(0..255)	mixed count_chars ( string $string [, int $mode ] )
字符串编码:		
md5()	字符串md5编码	"$str = ""Hello"";
echo md5($str);
"
