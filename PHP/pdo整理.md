1.准备一个dsn
$dsn = 'mysql:host=localhost;dbname=zf_shop;charset=utf8';//port=3306 默认是3306如果改了端口就加上这个


2.得到pdo对象
$pdo = new PDO($dsn,'root','123');

3.设置错误模式
$pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING);


4.准备sql语句

5.执行

6.处理



 //将会影响sql语句结构的特殊字符转义
    $name = $pdo->quote($username); // '1\' or 1=1 or 1=\'1'




try {
        //PDO的准备工作
        //1.准备一个DSN
        $dsn = 'mysql:host=192.168.11.254;port=3306;charset=utf8;dbname=shop';

        //2.得到一个PDO对象
        $pdo = new PDO($dsn, 'root', '', array(PDO::ATTR_ERRMODE=>PDO::ERRMODE_WARNING));

    } catch (PDOException $e) {
        echo $e->getMessage();
        exit;
    }

    $sql = "select * from users";

    $pdo->query($sql);

    $pdo->exec($sql);   //返回受影响行数
    $pdo->lastInsertId();



//设置错误模式
    setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING);

 //获取结果集
 fetchAll(PDO::FETCH_ASSOC);


获取错误信息
 errorInfo()

 //获取跟数据库句柄上一次操作相关的 SQLSTATE
    $res = $pdo->errorCode();
    var_dump($res);


PDO::lastInsertId — 返回最后插入行的ID或序列值



/******************** 预处理 ********************/
预处理需要记住的方法：
        bindValue() //绑定参数
        execute()   //确认执行一条sql模板
        fetchAll()  //获取所有结果集
        rowCount()  //返回受影响的行数




 //预先准备好一个sql语句的模板
    $sql = "insert into shop_users(`username`, `pwd`, `addtime`) values(:username, :pwd, :addtime)";

    // 发送sql模板语句
    $stmt = $pdo->prepare($sql);

    //$_POST就长这个样
    $data = array(
        array('username'=>'张1', 'pwd'=>md5(123), 'addtime'=>time()),
        array('username'=>'张2', 'pwd'=>md5(123), 'addtime'=>time()),
        array('username'=>'张3', 'pwd'=>md5(123), 'addtime'=>time()),
        array('username'=>'张4', 'pwd'=>md5(123), 'addtime'=>time()),
        array('username'=>'张5', 'pwd'=>md5(123), 'addtime'=>time()),
    );

    foreach($data as $v){
        //确认执行的同时传一个数组
        $bool = $stmt->execute($v);
        var_dump($bool);
    }











    <?php

    $dns = 'mysql:host=localhost;dbname=zhoufei;charset=utf8';

    $pdo = new PDO($dns,'root','123');

    $pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING);

    $sql = "insert into users(`name`,`pass`,`sex`,`tel`,`email`,`addtime`) values(:name, :pass, :sex, :tel,:email, :addtime)";
    //发送模板
    $stmt = $pdo->prepare($sql);

   $name = htmlspecialchars($_POST['name']);//用户名
   $pass = md5($_POST['pass']);//密码
   $pass_confirm = md5($_POST['pass_confirm']);//确认密码
   $tels = $_POST['tels'];//手机
   $sex = $_POST['sex'];//性别
   $email = htmlspecialchars($_POST['email']);//邮箱
   $name = htmlspecialchars($_POST['name']);
   $addtime = time();

   $arr = array('name'=>$name,'pass'=>$pass,'sex'=>$sex,'tel'=>$tels,'email'=>$email,'addtime'=>$addtime);

    //确认执行
    
      $bool = $stmt->execute($arr);
      if($bool){
            echo "<script>alert('注册成功');window.location.href='./index.html';</script>";
      }else{
        echo "<script>alert('注册失败！');window.location.href='./registered.html';</script>";
      }
    






$sql = 'select shop_users.name,shop_youqing.name from shop_users,shop_youqing';

$res = $pdo->query($sql);

var_dump($res);

$arr = $res->fetchAll(PDO::FETCH_ASSOC);
echo '<pre>';
print_r($arr);