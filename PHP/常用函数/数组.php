	
<?php

// 生成一个数组	"
array()	
$a=array("Dog","Cat","Horse");
print_r($a);


// 生成一个数组,用一个数组的值作为键名,另一个数组值作为值
$a1=array("a","b","c","d");
$a2=array("Cat","Dog","Horse","Cow");
print_r(array_combine($a1,$a2));


range()	创建并返回一个包含指定范围的元素的数组。
$number = range(0,50,10);
print_r ($number);

compact()	创建一个由参数所带变量组成的数组
$firstname = "Peter";
$lastname = "Griffin";
$age = "38";
$result = compact("firstname", "lastname", "age");
print_r($result);


// 用给定的填充(值生成)数组
array_fill()	
$a=array_fill(2,3,"Dog");
print_r($a);


数组合并和拆分：		
array_chunk()	把一个数组分割为新的数组块	
$a=array("a"=>"Cat","b"=>"Dog","c"=>"Horse","d"=>"Cow");
print_r(array_chunk($a,2));

array_merge()	把两个或多个数组合并为一个数组。	
$a1=array("a"=>"Horse","b"=>"Dog");
$a2=array("c"=>"Cow","b"=>"Cat");
print_r(array_merge($a1,$a2));



array_slice()	在数组中根据条件取出一段值，并返回。	
$a=array(0=>"Dog",1=>"Cat",2=>"Horse",3=>"Bird");
print_r(array_slice($a,1,2));


数组比较：		
array_diff()	返回两个数组的差集数组	

$a1=array(0=>"Cat",1=>"Dog",2=>"Horse");
$a2=array(3=>"Horse",4=>"Dog",5=>"Fish");
print_r(array_diff($a1,$a2));


array_intersect()	返回两个或多个数组的交集数组	
$a1=array(0=>"Cat",1=>"Dog",2=>"Horse");
$a2=array(3=>"Horse",4=>"Dog",5=>"Fish");
print_r(array_intersect($a1,$a2));


数组查找替换：		
array_search()	在数组中查找一个值，返回一个键，没有返回返回假	
$a=array("a"=>"Dog","b"=>"Cat","c"=>"Horse");
echo array_search("Dog",$a);


array_splice()	把数组中一部分删除用其他值替代	
$a1=array(0=>"Dog",1=>"Cat",2=>"Horse",3=>"Bird");
$a2=array(0=>"Tiger",1=>"Lion");
array_splice($a1,0,2,$a2);
print_r($a1);


array_sum()	返回数组中所有值的总和	
$a=array(0=>"5",1=>"15",2=>"25");
echo array_sum($a);


in_array()	在数组中搜索给定的值,区分大小写	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
if (in_array("Glenn",$people){
  echo "Match found";}else{
  echo "Match not found";}

array_key_exists()	判断某个数组中是否存在指定的 key	
$a=array("a"=>"Dog","b"=>"Cat");
if (array_key_exists("a",$a))
 {
 echo "Key exists!";
 }
else
 {
 echo "Key does not exist!";
 }



数组指针操作:		
key()	返回数组内部指针当前指向元素的键名	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
echo "The key from the current position is: " . key($people);



next()	把指向当前元素的指针移动到下一个元素的位置，并返回当前元素的值	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
echo current($people) . "<br />";
echo next($people); 


prev()	把指向当前元素的指针移动到上一个元素的位置，并返回当前元素的值	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
echo current($people) . "<br />";
echo next($people) . "<br />"; 
echo prev($people);


end()	将数组内部指针指向最后一个元素，并返回该元素的值（如果成功）	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
echo current($people) . "<br />";
echo end($people); 


reset()	把数组的内部指针指向第一个元素，并返回这个元素的值	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
echo current($people) . "<br />";
echo next($people) . "<br />";
echo reset($people);


current()	返回数组中的当前元素（单元）。	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
echo current($people) . "<br />";


list()	用数组中的元素为一组变量赋值	
$my_array=array("Dog","Cat","Horse");
list($a, $b, $c) = $my_array;


array_shift()	删除数组中的第一个元素，并返回被删除元素的值	
$a=array("a"=>"Dog","b"=>"Cat","c"=>"Horse");
echo array_shift($a);
print_r ($a);

array_unshift()	在数组开头插入一个或多个元素	
$a=array("a"=>"Cat","b"=>"Dog");
array_unshift($a,"Horse");
print_r($a);


array_push()	向数组最后压入一个或多个元素	
$a=array("Dog","Cat");
array_push($a,"Horse","Bird");
print_r($a);


array_pop()	删除数组中的最后一个元素	
$a=array("Dog","Cat","Horse");
array_pop($a);
print_r($a);


数组键值操作:		
shuffle()	本函数为 array 中的单元赋予新的键名。这将删除原有的键名而不仅是重新排序	
$my_array = array("a" => "Dog", "b" => "Cat");
shuffle($my_array);
print_r($my_array);


count()	计算数组中的单元数目或对象中的属性个数	
$people = array("Peter", "Joe", "Glenn", "Cleveland");
$result = count($people);
echo $result;


array_flip()	返回一个键值反转后的数组	
$a=array(0=>"Dog",1=>"Cat",2=>"Horse");
print_r(array_flip($a));



array_keys()	返回数组所有的键,组成一个数组	
$a=array("a"=>"Horse","b"=>"Cat","c"=>"Dog");
print_r(array_keys($a));


array_values()	返回数组中所有值，组成一个数组	同上

array_reverse()	返回一个元素顺序相反的数组	同上


array_count_values()	 统计数组中所有的值出现的次数	
$a=array("Cat","Dog","Horse","Dog");
print_r(array_count_values($a));


array_rand()	从数组中随机抽取一个或多个元素,注意是键名!!!	
$a=array("a"=>"Dog","b"=>"Cat","c"=>"Horse");
print_r(array_rand($a,1));


each()		
array_unique()	删除重复值，返回剩余数组	
$a=array("a"=>"Cat","b"=>"Dog","c"=>"Cat");
print_r(array_unique($a));


数组排序:		
sort()	按升序对给定数组的值排序,不保留键名	
$my_array = array("a" => "Dog", "b" => "Cat", "c" => "Horse");
sort($my_array);
print_r($my_array);


rsort()	对数组逆向排序,不保留键名	
$my_array = array("a" => "Dog", "b" => "Cat", "c" => "Horse");
rsort($my_array);
print_r($my_array);


asort()	对数组排序,保持索引关系	
$my_array = array("a" => "Dog", "b" => "Cat", "c" => "Horse");
asort($my_array);
print_r($my_array);


arsort()	对数组逆向排序,保持索引关系	
$my_array = array("a" => "Dog", "b" => "Cat", "c" => "Horse");
arsort($my_array);
print_r($my_array);


ksort()	按键名对数组排序	
$my_array = array("a" => "Dog", "b" => "Cat", "c" => "Horse");
ksort($my_array);
print_r($my_array);


krsort()	将数组按照键逆向排序	
$my_array = array("a" => "Dog", "b" => "Cat", "c" => "Horse");
krsort($my_array);
print_r($my_array);

natsort()	用自然顺序算法对数组中的元素排序	
$temp_files = array("temp15.txt","temp10.txt",
"temp1.txt","temp22.txt","temp2.txt");
sort($temp_files);
echo "Standard sorting: ";
print_r($temp_files);
echo "<br />";

natsort($temp_files);
echo "Natural order: ";
print_r($temp_files);

natcasesort()	自然排序,不区分大小写	
		
		
		
