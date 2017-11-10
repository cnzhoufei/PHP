<?php
echo $time1 = microtime();
		      	echo "<style>em{color:#f00}</style>";
$q = $_GET['q']?$_GET['q']:'测试';

ini_set('display_errors', 'On');
include "/usr/local/xunsearch/sdk/php/lib/XS.php";   //  引入 xunsearch sdk

// $connect = mysqli_connect('localhost','root','123456','yundi88_com') or exit(mysqli_connect_error().mysqli_connect_erron());
// mysqli_set_charset($connect,'utf8');

// // $sql = "select goods_id,goods_name,keywords,goods_remark,goods_content from yd_goods limit 10000,20000";
// $sql = "select goods_name,keywords,goods_remark,goods_content from yd_goods where goods_name like '%{$q}%' or keywords like '%{$q}%' or goods_remark like '%{$q}%' or goods_content like '%{$q}%'";

// $da = mysqli_query($connect,$sql);
// while($row = mysqli_fetch_assoc($da)){
// 	$data[] = $row;
// }

// var_dump($data);
// exit;
$xs = new XS('yundi88_com');


$index = $xs->index; // 索引对象来自 XS 的属性
// 添加文档
// $doc = new XSDocument;
// 	       foreach($data as $v){
// 			   $doc->setFields($v);
// 		       $index->add($doc);  //添加到索引数据库中
	       	
// 	       }




//分词
$tokenizer = new XSTokenizerScws;
$text = $q;
$words = $tokenizer->getResult($text);
array_unshift($words,['word'=>$q]);
var_dump($words);


//搜索
 $search = $xs->search;   //  获取搜索对象
 $search->setLimit(0); //获取条数 相当于msyql的limit
 $count = 0;
foreach($words as $k=>$v){
 	$docs = $search->setQuery($v['word'])->search();  //  搜索 ‘ 测试’
	$count += $search->setQuery($v['word'])->count();//搜索结果条数

		foreach ($docs as $kk=>$doc)
				{
				   $searchdatas[$k][$kk]['goods_name'] = $search->highlight($doc->goods_name); // 高亮处理 goods_name 字段
				   $searchdatas[$k][$kk]['keywords'] = $search->highlight($doc->keywords); // 高亮处理 keywords 字段
				   $searchdatas[$k][$kk]['goods_remark'] = $search->highlight($doc->goods_remark); // 高亮处理 keywords 字段
				   $searchdatas[$k][$kk]['goods_content'] = $search->highlight($doc->goods_content); // 高亮处理 keywords 字段



				   // echo $doc->rank() . '. ' . $subject . " [" . $doc->percent() . "%] - ";//$doc->percent()匹配相似度
				   // echo date("Y-m-d", $doc->chrono) . "\n" . $subject . "\n";echo '<br>';
		}
	
}
$datas = $searchdatas;

echo '<br>';
echo '共找到'.$count.'条结果';


		     // 处理结果

//转换成一维数组
// foreach ($searchdatas as $key => $value) {
// 		foreach ($value as $k => $v) {
// 			$datas[] = $v;
// 		}
// 	}	



// echo '<pre>';
// print_r(($datas));





//    try {
//       $xs = new XS('demo');    // demo  为项目名称，配置文件是：$sdk/app/demo.ini

//         $index = $xs->index;   //  获取索引对象



// 	        //添加文档
//         	$data = array(
//         		array('id'=>1,'title','sssss'=>'body'=>'sssss'),
//         		array('id'=>2,'title','sssss'=>'body'=>'sssss'),
//         		);
// 	        $doc = new XSDocument;
// 	       foreach($data as $v){
// 			   $doc->setFields($v);
// 		       $index->add($doc);  //添加到索引数据库中
	       	
// 	       }
// 	       // $index->add($doc);//添加文档
// 	       // $index->update($doc); //  更新文档，若有同主键数据则替换之
// 		   // $index->del('123’); //  删除主键值为 234 的文档
// 		   // $index->del(array(‘123’,‘456’)); //  删除主键值为 123 及 456 的文档


		   

//    } catch (XSException $e) {
//        echo $e.'n'.$e->getTraceAsString().'n'; //  发生异常，输出描述
//    }









?>

<!DOCTYPE html>
<html>
<head>
	<title>讯搜测试</title>
</head>
<body>
	<div style="width:500px;height: 50px;margin:0 auto;">
	<form>
		<input type="text" name="q"/><input type="submit" value="搜索">
	</form>

	</div>

	<div style="width:100%;">
		<ul>
		<?php $i = 0; foreach($datas as $v){?>
		<?php if($v){?>
		<?php  foreach($v as $k=>$vv){?>

			<li><?php echo $i;?>关键词：<?php echo $v['keywords'];?>--->商品名称：<?php echo $vv['goods_name']; ?>--->goods_remark:<?php echo $vv['goods_remark']; ?>--->goods_content:<?php echo $vv['goods_content']; ?></li><br><br>
		<?php $i++; }?>
		<?php }?>
		<?php }?>
		</ul>
	</div>
</body>
</html>
<?php $timecost = sprintf("%s",$time1); 
echo "页面运行时间: $timecost 秒"; ?>