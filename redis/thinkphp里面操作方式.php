<?php



// namespace Home\Controller;
//  use Think\Controller;
echo '<meta charset="utf-8" />';
$dsn = 'mysql:host=localhost;dbname=wolf;charset=utf8';

$pdo = new PDO($dsn,'root','123');

$pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING);

 	$sql = "select wolf_goods.id,wolf_goods.cid,wolf_goods.goods_name from wolf_goods inner join wolf_category on wolf_goods.cid = wolf_category.id";

    $res = $pdo->query($sql);

$arr = $res->fetchAll(PDO::FETCH_ASSOC);

 



	//加载predis
	require('ThinkPHP/Library/Vendor/predis-1.0/autoload.php');

	//实例化
	$redis = new Predis\Client();

	//利用set设置值
	$redis->set('user:name','zhangsan');

	//set 

	// $arr = array(
	// 			array('name'=>'zhoufei',
	// 			'age'=>18,
	// 			'xb'=>'男'),
	// 			array('name'=>'zhoufei2',
	// 			'age'=>19,
	// 			'xb'=>'男'),
	// 			array('name'=>'zhoufei3',
	// 			'age'=>20,
	// 			'xb'=>'男')

		
	// 	);


		$res = $redis->get('arr');
	
	if(!$res){
		
		$arrs = serialize($arr);
		$redis->setex('arr',3,$arrs);
		echo '直接输出';
		$aa = unserialize($arrs);
		
		
	}else{

		$aa = unserialize($res);
	}
	echo '<pre>';
	var_dump($aa);

