<?php



//$a = new ascii;

//echo $a->encode('周菲');

//echo bin2hex('');


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





