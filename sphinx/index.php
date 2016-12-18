<?php

// require 'sphinxapi.php';
$s = new SphinxClient();
$s->SetServer('localhost', 9312);
$result = $s->Query('家具');
echo '<pre>';

$key = array_keys($result['matches']);
print_r($key) ;
// print_r($result);
echo '</pre>';
echo '<br /><br />';
$result = $s->Query('中文');
print_r($result);



 // public function search()
 //        {
 //                $keyword = I('post.keywords');
 //        $url = $_SERVER['HTTP_REFERER'];//dump($url);//如果关键词为空就跳回去
 //        if (empty($keyword)) {
 //            redirect($url);die;
 //        }
 //        //1创建sphinx对象
 //        $sphinx = new \SphinxClient();
 //        //2.连接sphinx服务
 //        $sphinx->setServer('localhost','9312');
 //        //3.设置匹配模式
 //        $sphinx->setMatchMode(SPH_MATCH_ANY);
 //        //4.进行sphinx查询
 //        $result = $sphinx->query("$keyword",'main');

 //        //用于返回的数组
 //        $arr = [];
 //        if($result['total'] == 0){ //没有查询到返回空数组
 //            return $arr;
 //        }
 //        $idarr = array_keys($result['matches']);    //得到关键字索引出的id数组
 //         $ids = join(',',$idarr);

 //        //链接数据库执行
 //        $map['id'] = array('IN',$ids);
 //        $arr = $this->where($map)->select();

 //        return $arr;
 //        // dump($arr);die;
 //        }















