time()	返回当前的 Unix 时间戳	time();
mktime()	取得一个日期的 Unix 时间戳	mktime(0, 0, 0, 4, 25, 2012);
date()	格式化一个本地时间／日期	date('Y年m月d日 H:i:s');
checkdate()	验证一个格里高里日期	"if(checkdate(6,31,2012)){
 echo '成立';
}else{
 echo '不成立';
}"
date_default_timezone_set()	设定用于一个脚本中所有日期时间函数的默认时区	date_default_timezone_set('PRC');
getdate()	取得日期／时间信息	"$t=getdate();
var_dump($t);"
strtotime()	将任何英文文本的日期时间描述解析为 Unix 时间戳	"echo strtotime(""now"");
echo strtotime(""10 September 2000"");
echo strtotime(""+1 day"");
echo strtotime(""+1 week"");
echo strtotime(""+1 week 2 days 4 hours 2 seconds"");
echo strtotime(""next Thursday"");
echo strtotime(""last Monday"");"
microtime()	返回当前 Unix 时间戳和微秒数	"$start=microtime(true);
sleep(3);
$stop=microtime(true);
echo $stop-$start;"
