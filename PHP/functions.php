<?php



#随机字符
#len 生成长度
#type 生成类型 1数字,2大写字母,3小写字母,4混合
#special 是否加入特殊字符
#return string
function randomStr($len,$type=4,$special=false)
{
	$str1 = 'ABCDEFGHIJKRMNOPQLSTUVWXYZ';
	$str2 = 'abcdefghijkrmnopqlstuvwxyz';
	$str3 = '0123456789';
	$str4 = '~!@#$%^&*()_+=-?.,<>|{}[]';
	$randstr = '';
	switch ($type) {
		case 1:
			$str = $str3;
			break;
		case 2;
			$str = $str1;
			break;
		case 3:
			$str = $str2;
			break;
		default:
			$str = $str1.$str2.$str3;
			break;
	}
	if($special){
		$str .= $str4;
	}
	for($i = 0;$i < $len;$i++){
		$rand = mt_rand(0,strlen($str)-1);
		$randstr .= $str[$rand];
	}

	return $randstr;
}



#分页
function page($toal,$psize=20)
{

	if($toal <= 0)return ['limit'=>$psize,'page'=>''];
	$p = (isset($_GET['p']) and (int)$_GET['p'])?$_GET['p']:1;
	$pagenum = ceil($toal / $psize);
	if($p <= 0)$p = 1;
	if($p > $pagenum)$p = $pagenum;
	$limit = ($p - 1) * $psize.','.$psize;
	$page = '<style>
	page a{
		display: inline-block;
	    list-style: none;
	    min-width: 30px;
	    border: 3px solid #438EB9;
	    text-align: center;
	    margin-left: 5px;
	    padding-left:5px;
	    padding-right:5px;
	}
	page a.sel{
		color:#f00;
	}
	</style><page>';
	if($pagenum > 1){
	    $_GET['p'] = 1;$query = http_build_query($_GET);
	    $page .= "<a href='?{$query}'>首页</a>";
	    for($i=$p-5;$i<=$p+5;$i++){
	        $_GET['p'] = $i;$query = http_build_query($_GET);
	      if ($i > 0 and $i <= $pagenum){
	        if($i == $p){
	          $page .= "<a class='sel' href='?{$query}'>$i</a>";
	        }else{
	          $page .= "<a href='?{$query}'>{$i}</a>";
	        }
	      }
	      }
	    $_GET['p'] = $pagenum;$query = http_build_query($_GET);
	   $page .= "<a href='?$query'>末页</a></page>";
	  }
	  return ['limit'=>$limit,'page'=>$page];
}



#删除文件
function deldir($dir) {  
    //先删除目录下的文件：  
    $dh = opendir($dir);  
    while ($file = readdir($dh)) {  
        if($file != "." && $file!="..") {  
        $fullpath = $dir."/".$file;  
        if(!is_dir($fullpath)) {  
            unlink($fullpath);  
        } else {  
            deldir($fullpath);  
        }  
        }  
    }  
    closedir($dh);  
       
    //删除当前文件夹：  
    if(rmdir($dir)) {  
        return true;  
    } else {  
        return false;  
    }  
}


function curlGet($url){
		//初始化
        $curl = curl_init();
        //设置抓取的url
        curl_setopt($curl, CURLOPT_URL, $url);
        //设置头文件的信息作为数据流输出
        curl_setopt($curl, CURLOPT_HEADER, 0);
        //设置获取的信息以文件流的形式返回，而不是直接输出。
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
        //执行命令
        $data = curl_exec($curl);
        //关闭URL请求
        curl_close($curl);
        //显示获得的数据
        return $data;
}

function curlPost($url,$data){

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);//跳过证书
        // curl_setopt($ch, CURLOPT_HTTPHEADER, $header); 
        // post数据
        curl_setopt($ch, CURLOPT_POST, 1);
        // post的变量
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

        $output = curl_exec($ch);
        if($output === false){
            echo curl_errno($ch);
            exit();
        }
        curl_close($ch);
        //打印获得的数据
        return $output;
}

#获取微信access_token
function getWeixinToken()
{
	$AppID = config('myconfig.AppID');

	$AppSecret = config('myconfig.AppSecret');
    $redis = new \Redis();
    //连接服务器
    $redis->connect(config('myconfig.redisHost'),config('myconfig.redisPort'));
    $access_token = $redis->get('access_token');
    if($access_token){
        return $access_token;
    }else{
        $url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={$AppID}&secret={$AppSecret}";
        $res = curlGet($url);
        $json_decode = json_decode($res,true);
        if(isset($json_decode['access_token'])){
            $access_token = $json_decode['access_token'];
            $redis->setex('access_token',7000,$access_token);
            return $access_token;
        }
    }

    
}



/**
 * 获取php.exe的路径
 */
function php_path() {   
    $php_path='';    
    if ($php_path != '') {           
        return $php_path;      
    }
    if (substr(strtolower(PHP_OS), 0, 3) == 'win') {           
        $ini = ini_get_all();                    
        $path = $ini['extension_dir']['local_value'];           
        $php_path = str_replace('\\', '/', $path);           
        $php_path = str_replace(array('/ext/', '/ext'), array('/', '/'), $php_path);           
        $real_path = $php_path . 'php.exe';       
    } else {           
        $real_path = PHP_BINDIR . '/php';       
    }
    if (strpos($real_path, 'ephp.exe') !== FALSE) {           
        $real_path = str_replace('ephp.exe', 'php.exe', $real_path);  
    }       
    $php_path = $real_path;       
    return $php_path;   
}



#微信域名验证
function checkSignature()
{
    $signature = @$_GET["signature"];
    $timestamp = @$_GET["timestamp"];
    $nonce = @$_GET["nonce"];

	$tmpArr = array($timestamp, $nonce);
	sort($tmpArr, SORT_STRING);
	$tmpStr = implode( $tmpArr );
	$tmpStr = sha1( $tmpStr );

	if( $signature ){
		return true;
	}else{
		return false;
	}
}



//不同环境下获取真实的IP
function get_ip(){
    //判断服务器是否允许$_SERVER
    if(isset($_SERVER)){    
        if(isset($_SERVER['HTTP_X_FORWARDED_FOR'])){
            $realip = $_SERVER['HTTP_X_FORWARDED_FOR'];
        }elseif(isset($_SERVER['HTTP_CLIENT_IP'])) {
            $realip = $_SERVER['HTTP_CLIENT_IP'];
        }else{
            $realip = $_SERVER['REMOTE_ADDR'];
        }
    }else{
        //不允许就使用getenv获取  
        if(getenv("HTTP_X_FORWARDED_FOR")){
              $realip = getenv( "HTTP_X_FORWARDED_FOR");
        }elseif(getenv("HTTP_CLIENT_IP")) {
              $realip = getenv("HTTP_CLIENT_IP");
        }else{
              $realip = getenv("REMOTE_ADDR");
        }
    }

    return $realip;
}      




#1.生成公钥、私钥对
	#生成原始RSA私钥文件rsa_private_key.pem
    #openssl genrsa -out rsa_private_key.pem 1024
#2. 将原始的RSA私钥转换为pkcs8模式 得到私钥
	#openssl pkcs8 -topk8 -inform PEM -in rsa_private_key.pem -outform PEM -nocrypt -out private_key.pem
#3.生成RSA公钥 rsa_public_key.pem
	#openssl rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem
#数据加密
function encryption($clear){
    #公钥加密
    //这个函数可用来判断公钥是否是可用的
    $pu_key = openssl_pkey_get_public(config('public_key'));//这个函数可用来判断公钥是否是可用的
    $encrypted = '';
    openssl_public_encrypt($clear, $encrypted, $pu_key);
    $encrypted = base64_encode($encrypted);
    return $encrypted;
}
#数据解密
function decryption($cipher){
    #私钥解密
    //这个函数可用来判断私钥是否是可用的，可用返回资源id Resource id
    $pi_key = openssl_pkey_get_private(config('private_key'));
    $decrypted = '';
    $encrypted = base64_decode($cipher);
    openssl_private_decrypt($encrypted,$decrypted,$pi_key);//私钥解密
    return $decrypted;
}




#生成缩略图
function imgCompression($file,$width,$height){
	$path = '/thumb/';
	$filename = $width.'_'.$height.'_'.md5($file);	
	if(file_exists('.'.$path.$filename.'.jpg'))  return $path.$filename.'.jpg'; 
    if(file_exists('.'.$path.$filename.'.jpeg')) return $path.$filename.'.jpeg'; 
    if(file_exists('.'.$path.$filename.'.gif'))  return $path.$filename.'.gif'; 
    if(file_exists('.'.$path.$filename.'.png'))  return $path.$filename.'.png';
	$image = \think\Image::open('.'.$file);
	$type = $image->type();
	#图片保存到 /thumb
	if(!is_dir('.'.$path)){
		mkdir('.'.$path,0777,true);
	}
	$filename .= '.'.$type;
	$image->thumb($width, $height)->save('.'.$path.$filename);
	return $path.$filename;
}