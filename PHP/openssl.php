<?php

#1.生成公钥、私钥对
	#生成原始RSA私钥文件rsa_private_key.pem
    #openssl genrsa -out rsa_private_key.pem 1024
#2. 将原始的RSA私钥转换为pkcs8模式 得到私钥
	#openssl pkcs8 -topk8 -inform PEM -in rsa_private_key.pem -outform PEM -nocrypt -out private_key.pem
#3.生成RSA公钥 rsa_public_key.pem
	#openssl rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem



// openssl_get_cipher_methods();查询openssl支持的对称加密算法

// 加密：openssl_encrypt($data, $method, $passwd, $options, $iv);
	// 参数说明：
	// $data: 加密明文
	// $method: 加密方法
	// $passwd: 加密密钥
	// $options: 数据格式选项（可选）
	// $iv: 加密初始化向量（可选）
// 解密：openssl_decrypt($data, $method, $passwd, $options, $iv);
	// 参数说明：
	// $data: 解密密文
	// $method: 解密加密方法
	// $passwd: 解密密钥
	// $options: 数据格式选项（可选）
	// $iv: 解密初始化向量（可选）



// 私钥
$private_key = '-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDS6VbgEpOwVc8jXYx/uL6ItMS6aBPVo8fvw0pd90jLJYvfJcFJ
dYVFh6JPRdpGhlIrED45VdsktcJvJj0cLNI5ZIZ680aS6JTFe3ScBY4Mi7bLKzBN
YtMBtnkAFbMmWlCXV4qzZYg8+xNktY5ClZZCvZzzlaU5djtUSoxTLkxcmwIDAQAB
AoGAZT944gZo+bynvH17JhEk/nFxA19VLjj6kSH6AFPmkQcMN2pjeIU/Hhq3k0Cg
QTzYEy4wAMwzcFME7OC5c14c6GsnOQVEbzT3jA5lNuMnrvb+ehyE0w/O7ah8sSLQ
3B42GFKkaKiuY2ufsVC4pv6LMn5Sh26ApW332yO0dXZXagECQQDvAWV+n41R9pUp
iB0+ycBvkuE6yjlohc2MqAxdD+EYNgO4jb1F21pZcqasd/SbpiQwVUKk/uxlOvl9
3dBlcOWbAkEA4eiMv8UiGwBxjBGrz+I/tBq56gcnjvlOkJFyAyxbKaA1C9C51eVv
39OftI9DqCzcuAYZsCmspb6XEPBIB01VAQJAZVyAQM1Fz+b1p6F0VbaWiDsQjjBJ
XIyyed6jL6yWWABAX7qs9L1sedbn3OkashAp9N2T4AnFE8GJIdo6kWrp1QJAGOiF
LFfWDNgdrO393av6jicsPIuRZwhCC1qeEY+AdbR+ZNEczGLB1RIGV+g7830O0ROL
HYtax+Od0HZN2tBCAQJBANIg+HO5+Qy5hgRO3+uRHERgUQxqHzheLdo5GnoQ/sfT
sex4mxgze6oq+HldvNWzVjBu9g9417T5WMgyWQ8Unhw=
-----END RSA PRIVATE KEY-----';

// 公钥
$public_key = '-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDS6VbgEpOwVc8jXYx/uL6ItMS6
aBPVo8fvw0pd90jLJYvfJcFJdYVFh6JPRdpGhlIrED45VdsktcJvJj0cLNI5ZIZ6
80aS6JTFe3ScBY4Mi7bLKzBNYtMBtnkAFbMmWlCXV4qzZYg8+xNktY5ClZZCvZzz
laU5djtUSoxTLkxcmwIDAQAB
-----END PUBLIC KEY-----';



#数据加密
function encryption($clear){
	echo $aaa;
	#公钥加密
	global $public_key;
	//这个函数可用来判断公钥是否是可用的
	$pu_key = openssl_pkey_get_public($public_key);//这个函数可用来判断公钥是否是可用的
	$encrypted = '';
	openssl_public_encrypt($clear, $encrypted, $pu_key);
	$encrypted = base64_encode($encrypted);
	return $encrypted;
}

function decryption($cipher){
	#私钥解密
	global $private_key;
	//这个函数可用来判断私钥是否是可用的，可用返回资源id Resource id
	$pi_key = openssl_pkey_get_private($private_key);
	$decrypted = '';
	$encrypted = base64_decode($cipher);
	openssl_private_decrypt($encrypted,$decrypted,$pi_key);//私钥解密
	return $decrypted;
}

$a = encryption('周菲');
var_dump($a);
var_dump(decryption($a));exit;


print_r($pi_key);  echo "<br/>";
print_r($pu_key);  echo "<br/>";

// 原始数据
$data = 'codeman';
$encrypted = '';
$decrypted = '';

echo "source data:",$data,"<br/>";
echo "private key encrypt:<br/>";
echo "私钥加密，公钥解密：<br/>";

// 私钥加密
openssl_private_encrypt($data, $encrypted, $pi_key);
$encrypted = base64_encode($encrypted);//加密后的内容通常含有特殊字符，需要编码转换下，在网络间通过url传输时要注意base64编码是否是url安全的
echo $encrypted,"<br/>";

// 公钥解密
echo "public key decrypt:<br/>";
openssl_public_decrypt(base64_decode($encrypted),$decrypted,$pu_key);//私钥加密的内容通过公钥可用解密出来
echo $decrypted,"<br/><br/>";

echo "公钥加密，私钥解密：<br/>";
//公钥加密
openssl_public_encrypt($data, $encrypted, $pu_key);
$encrypted = base64_encode($encrypted);
echo $encrypted,"<br/>";

// 私钥解密
echo "private key decrypt:<br/>";
openssl_private_decrypt(base64_decode($encrypted),$decrypted,$pi_key);//私钥解密
echo $decrypted,"<br/>";