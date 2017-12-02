<?php


ini_set('display_errors', 'Off');

$aid = is_numeric($_GET['id'])?$_GET['id']:'';

if($aid){
require_once(dirname(__FILE__).'/../data/common.inc.php');


$connect = mysqli_connect($cfg_dbhost,$cfg_dbuser,$cfg_dbpwd,$cfg_dbname) or exit('连接数据库失败！！！');
mysqli_set_charset($connect,$cfg_db_language);
//获取主表数据
$sql = "select * from {$cfg_dbprefix}archives where id = ".$aid;
$obj = mysqli_query($connect,$sql);
$data = mysqli_fetch_assoc($obj);//文章data
if(!$data){exit('文章不存在');}

//获取模型表
$sql2 = "select addtable from {$cfg_dbprefix}channeltype where id = ".$data['channel'];
$obj2 = mysqli_query($connect,$sql2);
$data2 = mysqli_fetch_assoc($obj2);//文章data
if(!$data2){exit('文章模型不存在');}

//获取模型表数据
$sql3 = "select * from ".$data2['addtable']." where aid = ".$aid;
$obj3 = mysqli_query($connect,$sql3);
$data3 = mysqli_fetch_assoc($obj3);//文章data
if(!$data3){exit('文章模型不存在');}
// var_dump($GLOBALS);


//操作 dede_arctiny
$arctinysql = "select * from {$cfg_dbprefix}arctiny where id = ".$aid;
$arctinyda = mysqli_query($connect,$arctinysql);
$arctinydata = mysqli_fetch_assoc($arctinyda);
if(!$arctinydata){exit('dede_arctiny操作失败');}
//查询最大文章id
$maxsql = "select max(id) as max from {$cfg_dbprefix}arctiny";
$maxobj = mysqli_query($connect,$maxsql);
$maxid = mysqli_fetch_assoc($maxobj)['max'] + 1;//文章data

$arctinydata['id'] = $maxid;
$arctinysqlstr = '';
$arctinysqlstrdata = '';
foreach ($arctinydata as $key => $value) {
			$arctinysqlstr .= "`{$key}`,";
			$arctinysqlstrdata .= '"'.$value.'",';
}

$arctinysqlstr = substr($arctinysqlstr, 0,-1);
$arctinysqlstrdata = substr($arctinysqlstrdata, 0,-1);

$insertarctinysql ="insert into {$cfg_dbprefix}arctiny({$arctinysqlstr}) values({$arctinysqlstrdata})";
if(!mysqli_query($connect,$insertarctinysql)){
	exit('dede_arctiny写入失败');
}


//开始插入数据
//文章主表 dede_archives
$archivesdata = '';
$filedsqlstrs = '';
$data['id'] = $maxid;
foreach($data as $k=>$v){
		
			$filedsqlstrs .= "`{$k}`,";
			$archivesdata .= '"'.$v.'",';
		
}
$filedsqlstrs = substr($filedsqlstrs, 0,-1);
$archivesdata = substr($archivesdata, 0,-1);

$insertsql ="insert into {$cfg_dbprefix}archives({$filedsqlstrs}) values({$archivesdata})";
if(!mysqli_query($connect,$insertsql)){
	mysqli_query($connect,"delete from {$cfg_dbprefix}arctiny where id = ".$maxid);
	exit('文章写入失败！');
}

//模型表

$data3['aid'] = $maxid;
$filedsqlstrs2 = '';
$archivesdata2 = '';
foreach($data3 as $kk=>$vv){
		$filedsqlstrs2 .= "`{$kk}`,";
		$archivesdata2 .= '"'.$vv.'",';
}
$filedsqlstrs2 = substr($filedsqlstrs2, 0,-1);
$archivesdata2 = substr($archivesdata2, 0,-1);

$insertsql2 ="insert into {$data2['addtable']}({$filedsqlstrs2}) values({$archivesdata2})";
if(!mysqli_query($connect,$insertsql2)){
	mysqli_query($connect,"delete from {$cfg_dbprefix}archives where id = ".$maxid);
	mysqli_query($connect,"delete from {$cfg_dbprefix}arctiny where id = ".$maxid);
	exit('文章写入失败！');
}



mysqli_close($connect);
	
	header('location:'.$_SERVER['HTTP_REFERER']);

}else{

	header('location:'.$_SERVER['HTTP_REFERER']);
}


