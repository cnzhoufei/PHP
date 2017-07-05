<?php



//$a = new ascii;

//echo $a->encode('周菲');

//echo bin2hex('');

//中文转十六进制  ASCll转换Unicode
function unicode_encode($str, $encoding = 'GBK', $prefix = '&#', $postfix = ';') {
    $str = iconv($encoding, 'UCS-2//IGNORE', $str);
   
    $arrstr = str_split($str, 2);

    
    $unistr = '';
    for($i = 0, $len = count($arrstr); $i < $len; $i++) {
        $dec = hexdec(bin2hex($arrstr[$i]));
      
        $unistr .= '&#' . $dec .';';
    } 
    return $unistr;
}



function unicode_encode2($text){
	
	$str = file_get_contents($text);
	
	$encode = unicode_encode($str);

		$arr = explode('&#10;',$encode);

		$strs = implode('
',$arr);

	file_put_contents('./2.txt',$strs);
	echo $strs;
	
	
}
var_dump(unicode_encode2('./1.txt'));






//将十六进制转换为中文  Unicode转换ASCll
function unicode_decode($unistr, $encoding = 'utf-8', $prefix = '&#', $postfix = ';') {
 $arruni = explode($prefix, $unistr);
 $unistr = '';
 for ($i = 1, $len = count($arruni); $i < $len; $i++) {
  if (strlen($postfix) > 0) {
   $arruni[$i] = substr($arruni[$i], 0, strlen($arruni[$i]) - strlen($postfix));
  }
  $temp = intval($arruni[$i]);
  $unistr .= ($temp < 256) ? chr(0) . chr($temp) : chr($temp / 256) . chr($temp % 256);
 }
 return  iconv('UCS-2', $encoding, $unistr);
}
