<?php
$val"


abs()	求绝对值	$abs = abs(-4.2); //4.2
ceil()	进一法取整	echo ceil(9.999); // 10 
floor()	舍去法取整	echo floor(9.999); // 9
fmod()	浮点数取余	"$x = 5.7;$y = 1.3;
$r = fmod($x, $y);                           // $r equals 0.5, because 4 * 1.3 + 0.5 = 5.7    "
pow()	返回数的n次方	echo pow(-1, 20); // 1
round()	浮点数四舍五入	echo round(1.95583, 2);// 1.96
sqrt()	求平方根	echo sqrt(9); //3
max()	求最大值	"echo max(1, 3, 5, 6, 7);  // 7
echo max(array(2, 4, 5)); // 5"
min()	求最小值	
mt_rand()	更好的随机数	echo mt_rand(0,9);//n
rand()	随机数	
pi()	获取圆周率值	echo pi(); // 3.1415926535898


echo  bcmul ( '1.34747474747' ,  '35' ,  4 );  // 47.161bcmul — 2个任意精度数字乘法计算

echo  bcdiv ( '105' ,  '6.55957' ,  3 );   // 16.007 bcdiv() - 2个任意精度的数字除法计算 

echo  bcpow ( '4.2' ,  '3' ,  2 );  // 74.08 bcpow — 任意精度数字的成方 

echo  bcsqrt ( '2' ,  3 );  // 1.414 bcsqrt — 任意精度数字的二次方根 

// bcscale — 设置所有bc数学函数的默认小数点保留位数 
bcscale ( 3 );
echo  bcdiv ( '105' ,  '6.55957' );  // 16.007

echo  bcsub (1.234 ,  5 ,  4 );   // -3.7660 bcsub — 2个任意精度数字的减法