<?php
// /usr/local/xunsearch/sdk/php/util/RequiredCheck.php

include "/usr/local/xunsearch/sdk/php/lib/XS.php";   //  引入 xunsearch sdk
   try {
      $xs = new XS('test');    // demo  为项目名称，配置文件是：$sdk/app/demo.ini

        $index = $xs->index;   //  获取索引对象



	        //添加文档
        	$data = array(
        		array('id'=>1,'title','sssss'=>'body'=>'sssss'),
        		array('id'=>2,'title','sssss'=>'body'=>'sssss'),
        		);
	        $doc = new XSDocument;
	       foreach($data as $v){
			   $doc->setFields($v);
		       $index->add($doc);  //添加到索引数据库中
	       	
	       }
	       // $index->add($doc);//添加文档
	       // $index->update($doc); //  更新文档，若有同主键数据则替换之
		   // $index->del('123’); //  删除主键值为 234 的文档
		   // $index->del(array(‘123’,‘456’)); //  删除主键值为 123 及 456 的文档


		   //搜索
		   	 $q = $_GET['q']?$_GET['q']:'测试';
			 $search = $xs->search;   //  获取搜索对象
		     $search->setLimit(20); //获取条数 相当于msyql的limit
		     $docs = $search->setQuery($q)->search();  //  搜索 ‘ 测试’
 			 $count = $search->setQuery($q)->count();//搜索结果条数
		     // 处理结果
		      echo "<style>em{color:#f00}</style>";
				foreach ($docs as $doc)
				{
				   $subject = $search->highlight($doc->goods_name); // 高亮处理 goods_name 字段
				   $message = $search->highlight($doc->keywords); // 高亮处理 keywords 字段
				   echo $doc->rank() . '. ' . $subject . " [" . $doc->percent() . "%] - ";//$doc->percent()匹配相似度
				   echo date("Y-m-d", $doc->chrono) . "\n" . $goods_name . "\n";
				}

   } catch (XSException $e) {
       echo $e.'n'.$e->getTraceAsString().'n'; //  发生异常，输出描述
   }
















      } catch (XSException $e) {
       echo $e.'n'.$e->getTraceAsString().'n'; //  发生异常，输出描述
   	  }