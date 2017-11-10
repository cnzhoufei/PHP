<?
fopen()	打开文件或者 URL	$handle = fopen("ftp://user:password@example.com/somefile.txt", "w");
fclose()	关闭一个已打开的文件指针	"$handle = fopen('somefile.txt', 'r');
fclose($handle);"
文件属性		
file_exists()	检查文件或目录是否存在	"$filename = '/path/to/foo.txt';
if (file_exists($filename)) {
    echo ""exists"";
} else {
    echo ""does not exist"";
}"
filesize()	取得文件大小	"$filename = 'somefile.txt';
echo $filename . ': ' . filesize($filename) . 'bytes';"
is_readable()	判断给定文件是否可读	"$filename = 'test.txt';
if (is_readable($filename)) {
    echo '可读';
} else {
    echo '不可读';
}"
is_writable()	判断给定文件是否可写	"$filename = 'test.txt';
if (is_writable($filename)) {
    echo '可写';
} else {
    echo '不可写';
}"
is_executable()	判断给定文件是否可执行	"$file = 'setup.exe';
if (is_executable($file)) {
    echo '可执行';
} else {
    echo '不可执行';
}"
filectime()	获取文件的创建时间	"$filename = 'somefile.txt';
echo filectime($filename);"
filemtime()	获取文件的修改时间	"$filename = 'somefile.txt';
echo filemtime($filename);"
fileatime()	获取文件的上次访问时间	"$filename = 'somefile.txt';
echo fileatime($filename);"
stat()	获取文件大部分属性值	"$filename = 'somefile.txt';
var_dump(fileatime($filename));"
文件操作		
fwrite()	写入文件	"$filename = 'test.txt';
$somecontent = ""添加这些文字到文件\n"";
$handle = fopen($filename, 'a');    fwrite($handle, $somecontent);
fclose($handle);"
fputs()	同上	
fread()	读取文件	"$filename = ""/usr/local/something.txt"";
$handle = fopen($filename, ""r"");
$contents = fread($handle, filesize ($filename));
fclose($handle);"
feof()	检测文件指针是否到了文件结束的位置	"$file = @fopen(""no_such_file"", ""r"");
while (!feof($file)) {
}
fclose($file);"
fgets()	从文件指针中读取一行	"$handle = @fopen(""/tmp/inputfile.txt"", ""r"");
if ($handle) {
    while (!feof($handle)) {
        $buffer = fgets($handle, 4096);
        echo $buffer;
    }
    fclose($handle);
}"
fgetc()	从文件指针中读取字符	"$fp = fopen('somefile.txt', 'r');
if (!$fp) {
    echo 'Could not open file somefile.txt';
}
while (false !== ($char = fgetc($fp))) {
    echo ""$char\n"";
}"
file()	把整个文件读入一个数组中	###############################################################################################################################################################################################################################################################
readfile()	输出一个文件	
file_get_contents()	将整个文件读入一个字符串	echo file_get_contents('http://www.baidu.com');
file_put_contents()	将一个字符串写入文件	file_put_contents('1.txt','aa');
ftell()	返回文件指针读/写的位置	"$fp=fopen('tx.txt','r'); 
 fseek($fp,10);
 echo ftell($fp);
 fread($fp,4);
 echo ftell($fp);"
fseek()	在文件指针中定位	"$fp=fopen('tx.txt','r'); 
 fseek($fp,10);
 echo ftell($fp);
 fread($fp,4);
 echo ftell($fp);"
rewind()	倒回文件指针的位置	"$fp=fopen('tx.txt','r'); 
 fseek($fp,3);
 echo ftell($fp);
 fread($fp,4);
 rewind($fp);
 echo ftell($fp);"
flock()	轻便的咨询文件锁定	"$fp=fopen('tx.txt','r');
flock($fp, LOCK_SH);//共享锁
//flock($fp, LOCK_EX);//独立锁，写文件时用它打开
//flock($fp, LOCK_NB);//附加锁
flock($fp, LOCK_UN);//释放锁
fclose($fp);"
目录		
basename()	返回路径中的文件名部分	"path = ""/home/httpd/html/index.php"";
$file = basename($path);
$file = basename($path,"".php""); "
dirname()	返回路径中的目录部分	"$path = ""/etc/passwd"";
$file = dirname($path);"
pathinfo()	返回文件路径的信息	"echo '<pre>';
print_r(pathinfo(""/www/htdocs/index.html""));
echo '</pre>';"
opendir()	打开目录句柄	"$fp=opendir('E:/xampp/htdocs/php/study/19');
echo readdir($fp);
closedir($fp);"
readdir()	从目录句柄中读取条目	"$fp=opendir('E:/xampp/htdocs/php/study/19');
echo readdir($fp);
closedir($fp);"
closedir()	关闭目录句柄	"$fp=opendir('E:/xampp/htdocs/php/study/19');
echo readdir($fp);
closedir($fp);"
rewinddir()	倒回目录句柄	"$fp=opendir('E:/xampp/htdocs/php/study/19');
echo readdir($fp).'<br />';
echo readdir($fp).'<br />';
echo readdir($fp).'<br />';
rewinddir($fp);
echo readdir($fp).'<br />';
closedir($fp);"
mkdir()	新建目录	mkdir('123');
rmdir()	删除目录	rmdir('123');
unlink()	删除文件	"unlink('123/1.txt');
rmdir('123');"
copy()	拷贝文件	copy('index.php','index.php.bak');
rename()	重命名一个文件或目录	rename('tx.txt','txt.txt');
文件的上传与下载		
is_uploaded_file()	判断文件是否是通过 HTTP POST 上传的	"if(is_uploaded_file($_FILES['bus']['tmp_name'])){
  if( move_uploaded_file($_FILES['bus']['tmp_name'], $NewPath) ){
   echo '上传成功<br /><img src=""'.$NewPath.'"">';
  }else{
   exit('失败');
   }
 }else{
  exit('不是上传文件');
 }"
move_uploaded_file()	将上传的文件移动到新位置	"if(is_uploaded_file($_FILES['bus']['tmp_name'])){
  if( move_uploaded_file($_FILES['bus']['tmp_name'], $NewPath) ){
   echo '上传成功<br /><img src=""'.$NewPath.'"">';
  }else{
   exit('失败');
   }
 }else{
  exit('不是上传文件');
 }"


