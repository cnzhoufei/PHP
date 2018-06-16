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

    public function findUserInfoById($mobile=18318889786)
    {

    	// 1.如果你的内容不敏感，一个快捷的方法是使用curl_exec()之前跳过ssl检查项。

		// 　　curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		//     	2.下载一个ca-bundle.crt ，放到对应的目录，在php.ini文件中配置下路径

		// 　　https://github.com/bagder/ca-bundle/blob/e9175fec5d0c4d42de24ed6d84a06d504d5e5a09/ca-bundle.crt

		// 　　在php.ini加入 ，重启web服务器

		// curl.cainfo="真实路径/ca-bundle.crt"

        $url = "https://open.workec.com/user/findUserInfoById";
        $post_data = ["account"=>$mobile];
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);//跳过证书
        $header = [];
        $header[] = "authorization:Mejk079No1gvbVMAQe1";
        $header[] = "corp_id:5698610";
        $header[] = "content-type:application/json";
        $header[] = "cache-control:no-cache";
        curl_setopt($ch, CURLOPT_HTTPHEADER, $header); 
        // post数据
        curl_setopt($ch, CURLOPT_POST, 1);
        // post的变量
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);

        $output = curl_exec($ch);
        if($output === false){
            echo curl_errno($ch);
            exit();
        }
        curl_close($ch);
        //打印获得的数据
        print_r($output);
    }


// http://www.site-digger.com/html/articles/20151227/114.html