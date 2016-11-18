<?php

function html($url,$data){
	
	$url = $url;
	$params = $data;
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);    // 要求结果为字符串且输出到屏幕上
	curl_setopt($ch, CURLOPT_HEADER, 0); // 不要http header 加快效率
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)');
	curl_setopt($ch, CURLOPT_TIMEOUT, 15);
	 
	curl_setopt($ch, CURLOPT_POST, 1);    // post 提交方式
	curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
	 
	$output = curl_exec($ch);
	curl_close($ch);
}


		// get请求方法
		//初始化
        $curl = curl_init();
        //设置抓取的url
        curl_setopt($curl, CURLOPT_URL, 'http://ip.taobao.com/service/getIpInfo.php?ip=59.41.183.53');
        //设置头文件的信息作为数据流输出
        curl_setopt($curl, CURLOPT_HEADER, 1);
        //设置获取的信息以文件流的形式返回，而不是直接输出。
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
        //执行命令
        $data = curl_exec($curl);
        //关闭URL请求
        curl_close($curl);
        //显示获得的数据
        print_r($data);

//3.2 Post方式实现

　　 $url = "http://localhost/web_services.php";
　　$post_data = array ("username" => "bob","key" => "12345");

　　$ch = curl_init();

　　curl_setopt($ch, CURLOPT_URL, $url);
　　curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
　　// post数据
　　curl_setopt($ch, CURLOPT_POST, 1);
　　// post的变量
　　curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);

　　$output = curl_exec($ch);
　　curl_close($ch);

　　//打印获得的数据
　　print_r($output);