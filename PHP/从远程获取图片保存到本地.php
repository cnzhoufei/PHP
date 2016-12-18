<?php


// $url = "http://www.zjlsjj.cn/data/config.cache.inc.php";
// $params = "dopost=save";
// $ch = curl_init();
// curl_setopt($ch, CURLOPT_URL, $url);
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);    // 要求结果为字符串且输出到屏幕上
// curl_setopt($ch, CURLOPT_HEADER, 0); // 不要http header 加快效率
// curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)');
// curl_setopt($ch, CURLOPT_TIMEOUT, 15);
 
// curl_setopt($ch, CURLOPT_POST, 1);    // post 提交方式
// curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
 
// $output = curl_exec($ch);
// curl_close($ch);



function get_photo($url,$filename='',$savefile='test/')   
{     
    $imgArr = array('gif','bmp','png','ico','jpg','jepg');  
  
    if(!$url) return false;  
    
    if(!$filename) {     
      $ext=strtolower(end(explode('.',$url)));     
      if(!in_array($ext,$imgArr)) return false;  
      $filename=date("dMYHis").'.'.$ext;     
    }     
  
    if(!is_dir($savefile)) mkdir($savefile, 0777);  
    if(!is_readable($savefile)) chmod($savefile, 0777);  
      
    $filename = $savefile.$filename;  
  
    ob_start();     
    readfile($url);     
    $img = ob_get_contents();     
    ob_end_clean();     
    $size = strlen($img);     
    
    $fp2=@fopen($filename, "a");     
    fwrite($fp2,$img);     
    fclose($fp2);     
    
    return $filename;     
 }     
   
  
 $img=get_photo("http://www.b2b.com/Public/upload/goods/2016/12-16/585382ca363cd.jpg",'');     
 echo $img ? '<pre><img src="'.$img.'"></pre>' : "false";  