<?php

namespace Min\Controller;

use Think\Controller;

header('Expires: Mon, 26 Jul 1997 05:00:00 GMT'); 
header('Last-Modified: ' . gmdate('D, d M Y H:i:s') . 'GMT'); 
header('Cache-Control: no-cache, must-revalidate'); 
header('Pragma: no-cache'); 

class MsgController extends Controller 
{

		protected $appid = '';
		protected $appsecret = '';

	public function index()
	{

		$msg = $GLOBALS['HTTP_RAW_POST_DATA'];//接收微信服务器推送的消息 --用户发的
		$json = json_decode($msg,true);
		if(!$json){return;}
		$str = '{"ToUserName":"'.$json['FromUserName'].'","FromUserName":"gh_b443ea71004c","CreateTime":"'.$json['CreateTime'].'","MsgType":"transfer_customer_service"}';
		echo $str;
	}

		// 获取ACCESS_TOKEN
		public function getaccess_token()
		{
			$access_token = M('access_token')->order('id desc')->find();
			if($access_token && (time() - $access_token['addtime']) < 7000){
				return $access_token['access_token'];
			}else{
				$data = $this->getdata("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=".$this->appid."&secret=".$this->appsecret);
	        	$access_token = json_decode($data,true);
	        	if($access_token['expires_in']){
		        	$datas['access_token'] = $access_token['access_token'];
		        	$datas['addtime'] = time();
		        	M('access_token')->add($datas);
		        	return $access_token['access_token'];
	        		
	        	}else{
	        		echo '获取ACCESS_TOKEN失败';
	        	}
				
			}


		}


		//给用户发送文本消息消息
		public function postmsg($user,$msg)
		{
			$access_token = $this->getaccess_token();
			$url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={$access_token}";
			// $data = ['touser'=>$user,'msgtype'=>'text','text'=>['content'=>$msg]];
			// $json = json_encode($data,true);
			// dump($json);
			// $json = "{'touser':'oxpcg0YO57STTt6_EfsXLfVAR8lk','msgtype':'text','text':{'content':'很高兴为您服务'}}";
			$json = '{"touser":"'.$user.'","msgtype":"text","text":{"content":"'.$msg.'"}}';
			return $this->postdata($url,$json);
		}

		//post发送数据
		public function postdata($url,$data)
		{
			$ch = curl_init();
			curl_setopt($ch, CURLOPT_URL, $url);
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);    // 要求结果为字符串且输出到屏幕上
			curl_setopt($ch, CURLOPT_HEADER, 0); // 不要http header 加快效率
			curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)');
			curl_setopt($ch, CURLOPT_TIMEOUT, 15);
			 
			curl_setopt($ch, CURLOPT_POST, 1);    // post 提交方式
			curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
			 
			$output = curl_exec($ch);
			curl_close($ch);
			return $output;
			

		}


	//检验signature
    private function checkSignature()
    {
    	 	$signature = $_GET["signature"];
		    $timestamp = $_GET["timestamp"];
		    $nonce = $_GET["nonce"];

		    $token = '13539993040123456';
		    $tmpArr = array($token, $timestamp, $nonce);
		    sort($tmpArr, SORT_STRING);
		    $tmpStr = implode( $tmpArr );
		    $tmpStr = sha1( $tmpStr );

		    if( $tmpStr == $signature ){
		    // file_put_contents('./test.txt',$signature.'_'.$timestamp.'_'.$nonce.'_'.$tmpStr);
		        return true;
		    }else{
		        return false;
		    }


		    //在填写的消息页面验证
		  //   $echoStr = $_GET["echostr"];
			 // if ($this->checkSignature()) {
			 // echo $echoStr;
			 // exit;


			 // }


	}


	//get方式请求数据
	public function getdata($url)
	{
		$curl = curl_init();
        //设置抓取的url
        curl_setopt($curl, CURLOPT_URL, $url);
        //设置头文件的信息作为数据流输出
        curl_setopt($curl, CURLOPT_HEADER, 0);
        //设置获取的信息以文件流的形式返回，而不是直接输出。
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
        //执行命令
        $datas = curl_exec($curl);
        //关闭URL请求
        curl_close($curl);
	  //显示获得的数据
        return $datas;

	}





}