<?php

// require_once '/usr/local/xunsearch/sdk/php/lib/XS.php';
// $xs = new XS('zl');
// $index = $xs->index;
// $doc = new XSDocument;
echo 'nihao';
$conn=mysqli_connect("localhost", "root", "") or die("Could not connect: " . mysqli_error());
mysqli_select_db('wolf, $conn) or die ('Can\'t use wolf : ' . mysqli_error());
$result=mysqli_query("select * from wolf_goods limit 4429 offset 3000");

var_dump($result);

// while($r=mysql_fetch_array($result)){
// $a["id"]=$r['id'];
// $a["title"]=$r['title'];
// $a["time"]=$r['time'];
// $a["sid"]=$r['sid'];
// $a["content"]=$r['content'];
// $a["key"]=$r['key'];
// $doc->setFields($a);
// $index->update($doc);
// }

//     $xs = new XS('demo');// 必须先创建一个 xs 实例，否则会抛出异常  
//     $tokenizer = new XSTokenizerScws;
//     $text = '迅搜(xunsearch)是优秀的开源全文检索解决方案';
//     $words = $tokenizer->getResult($text);
//     print_r($words);