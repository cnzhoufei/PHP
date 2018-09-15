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
	  return ['limit'=>$limit,'page'=>$page,'pagenum'=>$pagenum];
}



#删除文件
function delDir($dir) {  
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


#获取微信jsdk所需ticket
function getJsApiTicket(){

    $redis = new \Redis();
    //连接服务器
    $redis->connect('localhost',6379);
    $weixin_ticket = $redis->get('weixin_ticket');
    // if($weixin_ticket){
    //     return $weixin_ticket;
    // }

    $accessToken = getWeixinToken();
    $url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token={$accessToken}";
    $res = json_decode(curlGet($url));
    $ticket = $res->ticket;
    if($ticket){
        $redis->setex('weixin_ticket',7000,$ticket);
        return $ticket;
    }else{
        return '获取ticket失败';
    }
}


/**
 * 获取php.exe的路径
 */
function phpPath() {   
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
function getIp(){
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


#过滤数据
function filter($data) {
    foreach($data as &$v){
      $v = trim($v);
      $v = stripslashes($v);
      $v = htmlspecialchars($v);
    }
    return $data;
}



#微信签名
#key 商户后台配置的密钥
function getSign($data,$key){
    $data = array_filter($data);//去除数组中的空值
    ksort($data);//按照键名字典排序
    $str = http_build_query($data). "&key=".$key;//连接
    $str = urldecode($str);//URL解码为中文
    echo $str;
    return  strtoupper(md5($str));
}


/**
 * 数组转xml字符
 * @param  string   $xml xml字符串
**/
function arrayToXml($data){
    if(!is_array($data) || count($data) <= 0){
        return false;
    }
    $xml = "<xml>";
    foreach ($data as $key=>$val){
        if (is_numeric($val)){
            $xml.="<".$key.">".$val."</".$key.">";
        }else{
            $xml.="<".$key."><![CDATA[".$val."]]></".$key.">";
        }
    }
    $xml.="</xml>";
    return $xml; 
}


/**
 * 将xml转为array
 * @param  string   $xml xml字符串或者xml文件名
 * @param  bool     $isfile 传入的是否是xml文件名
 * @return array    转换得到的数组
 */
function xmlToArray($xml,$isfile=false){   
    //禁止引用外部xml实体
    libxml_disable_entity_loader(true);
    if($isfile){
        if(!file_exists($xml)) return false;
        $xmlstr = file_get_contents($xml);
    }else{
        $xmlstr = $xml;
    }
    $result= json_decode(json_encode(simplexml_load_string($xmlstr, 'SimpleXMLElement', LIBXML_NOCDATA)), true);        
    return $result;

}


#判断设备
function isMobile() {
    static $is_mobile = null;
  
     if (isset($is_mobile)) {
        return $is_mobile;
     }
  
    if (empty($_SERVER['HTTP_USER_AGENT'])) {
        $is_mobile = false;
    } elseif ( strpos($_SERVER['HTTP_USER_AGENT'], 'Mobile') !== false 
      || strpos($_SERVER['HTTP_USER_AGENT'], 'Android') !== false
      || strpos($_SERVER['HTTP_USER_AGENT'], 'Silk/') !== false
      || strpos($_SERVER['HTTP_USER_AGENT'], 'Kindle') !== false
      || strpos($_SERVER['HTTP_USER_AGENT'], 'BlackBerry') !== false
      || strpos($_SERVER['HTTP_USER_AGENT'], 'Opera Mini') !== false
      || strpos($_SERVER['HTTP_USER_AGENT'], 'Opera Mobi') !== false ) {
        $is_mobile = true;
     } else {
        $is_mobile = false;
     }
  
    return $is_mobile;
}


#获取图片类型
function getImgType($url)
{
    $type = get_headers($url)[3];
    switch ($type) {
        case 'Content-Type: image/jpeg':
            return 'jpeg';
            break;
        case 'Content-Type: image/png':
            return 'png';
            break;
        case 'Content-Type: image/gif':
            return 'gif';
            break;
        case 'Content-Type: image/jpg':
            return 'jpg';
            break;
        default:
            return $type;
            break;
    }
}



#获取远程图片到本地
function getImg($url,$path='./',$filename=''){
    if(!is_dir($path)){
        mkdir($path,0777,true);
    }
    $type = getImgType($url);
    if(!$filename){
        $filename = mt_rand(111111,999999);
    }
    if (file_exists($path . $filename.'.'.$type)){
        return $path . $filename.'.'.$type;
    }
      $ch = curl_init();
      curl_setopt($ch, CURLOPT_URL, $url);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
      curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);
      $file = curl_exec($ch);
      curl_close($ch);
      $resource = fopen($path . $filename.'.'.$type, 'a');
      fwrite($resource, $file);
      fclose($resource);
      return $path . $filename.'.'.$type;
}

#处理成圆图片,如果图片不是正方形就取最小边的圆半径,从左边开始剪切成圆形
function yjImg($imgpath) {

    #获取图片类型
    $ext     = pathinfo($imgpath);
    $src_img = null;
    switch ($ext['extension']) {
    case 'png':
        $src_img = imagecreatefrompng($imgpath);
        break;
    default:
        $src_img = imagecreatefromjpeg($imgpath);
        break;
    }
    $wh  = getimagesize($imgpath);
    $w   = $wh[0];
    $h   = $wh[1];
    $w   = min($w, $h);
    $h   = $w;
    $img = imagecreatetruecolor($w, $h);
    imagesavealpha($img, true);
    //拾取一个完全透明的颜色,最后一个参数127为全透明
    $bg = imagecolorallocatealpha($img, 255, 255, 255, 127);
    imagefill($img, 0, 0, $bg);
    $r   = $w / 2; //圆半径
    $y_x = $r; //圆心X坐标
    $y_y = $r; //圆心Y坐标
    for ($x = 0; $x < $w; $x++) {
        for ($y = 0; $y < $h; $y++) {
            $rgbColor = imagecolorat($src_img, $x, $y);
            if (((($x - $r) * ($x - $r) + ($y - $r) * ($y - $r)) < ($r * $r))) {
                imagesetpixel($img, $x, $y, $rgbColor);
            }
        }
    }

    header('content-type:image/png');
    imagepng($img);
}


#判断访问模式
function requestType()
{
    if(isset($_SERVER['REQUEST_METHOD'])){
        $REQUEST_METHOD = strtoupper($_SERVER['REQUEST_METHOD']);
        if($REQUEST_METHOD == 'POST'){
            return 'POST';
        }
        if($REQUEST_METHOD == 'GET'){
            return 'GET';
        }

    }elseif(isset($_SERVER['HTTP_X_REQUESTED_WITH'])){
        if(strtoupper($_SERVER['HTTP_X_REQUESTED_WITH'])=='XMLHTTPREQUEST'){
            return 'AJAX';
        }

    }elseif(PHP_SAPI === 'cli' OR defined('STDIN')){
        return 'cli';//命令行模式
    }
}