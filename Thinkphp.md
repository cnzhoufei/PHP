 
http://wenku.baidu.com/link?url=v5bSvJ9fQ26Ak4FcR8isT7gr-zv7IQxiWAldsov6r0ggRJcEIXlgkPbqGBWAUDAXZM4krSNWMGWw8lXujAJMKFQumTo-6RNO2pl_XT3jgP_



/=============================== 注意事项 ==============================/

每个模块都得有EmptyController.class.php这个控制器里面有个空方法_empty() 做404页面

每个控制器都得有一个空方法__empty()用来做404页面

每个模块都要有一个CommonController.class.php公共的控制器 里面有一个_initialize()方法 用来做判断 比如判断有没有登录没有就跳转到登录页面 除了登录一面外都要继承它 


自己写的函数 放到Common 命名为function.php 可以直接调用





//隐藏Home
$arr    =    explode('/',$_SERVER['PHP_SELF']);
 if(count($arr) > 2 && $arr[2]!=='Admin' && $arr[2]!=='admin'){
    
    define('BIND_MODULE','Home');
 }








/******************** index.php ********************/
//定义项目目录
    define('APP_PATH', './Web/');

    //开启调试模式
    define('APP_DEBUG', true);

    //包含主入口文件
    include './ThinkPHP/ThinkPHP.php';


    


 'DATA_CACHE_TIME'       =>  5,      // 数据缓存有效期 0表示永久缓存


    /* 数据库设置 */
    'DB_TYPE'               =>  'mysql',     // 数据库类型
    'DB_HOST'               =>  '192.168.11.254', // 服务器地址
    'DB_NAME'               =>  'shop',          // 数据库名
    'DB_USER'               =>  'root',      // 用户名
    'DB_PWD'                =>  '',          // 密码
    'DB_PREFIX'             =>  'shop_',    // 数据库表前缀

    'URL_MODEL'             =>  2,          //重写模式
    'SHOW_PAGE_TRACE'       =>  true,       //开启页面trace
    'URL_HTML_SUFFIX'       =>  'asp',      //设置伪静态


    //域名部署
    'APP_SUB_DOMAIN_DEPLOY'  =>    1, // 开启子域名配置
    'APP_SUB_DOMAIN_RULES'   =>    array(       
        'admin'  => 'Admin',  
    ),

  
AllowOverride None 将None改为 All 这里指的是下面代码的下方
 DocumentRoot "f:/wamp/Apache24/htdocs"
<Directory "f:/wamp/Apache24/htdocs">



Model类的方法
count()  查总数
select()  查询全部
cache('key',5) 缓存
limit($page->firstRow.','.$page->listRows) 查询条数
find()查询一条结果


  S('name', 'jack', 7000);数据缓存 S(变量名,值,缓存时间) 一个参数是取值

  U('Admin/Index/add?id=5')只能写3层：模块/控制器/方法
    // echo U('del?id=5&name=jack');
    // echo U('del', 'id=5&name=jack');
    // echo U('del', array('id'=>4), 'txt');txt 是伪静态后缀
    
    I
    isset($_POST['id']) ? $_POST['id'] : '大爷没传POST的id';  
    echo I('post.id', '大爷没传POST的id'); I(接收参数，默认值，调用函数)  //等效上一行代码
    $pwd = I('get.pwd', '123', 'md5');把$_GET['pwd']加密 没有传参就取中间的默认值不会加密
    var_dump(I('get.'));    //相当于$_GET
    
    M
     //这是直接实例化Model基类
    // $user = M('Users');

    D
    //会先去你的Model层看看有没有UsersModel.class.php，如果没有，再去实例化Model基类
     $user = D('Users');
        
        $page = new Page($user->count(), 4);
        $arr = $user->limit($page->firstRow.','.$page->listRows)->getData();
        // var_dump($arr);
        //获取分页按钮
        $btn = $page->show();






    成功跳转，默认往$_SERVER['HTTP_REFERER']跳转，时间是1秒
    $this->success('成功鸟！', U('User/index'), 5);success(提示文字，跳转链接，跳转时间);默认为一秒

    失败跳转，默认往javascript:go(-1)跳转，时间是3秒
    $this->error('失败了');


    重定向
    $this->redirect('Admin/User/index', array('id'=>2), 5, '页面跳转中...');$this->redirect(跳转链接，传参，时间秒，提示文字)
    redirect('http://www.sogou.com'); //可以跳转到其他网站去 不能要$this
   



    //初始化方法，会在所有的方法之前执行
    public function _initialize()
    {
        //判断权限
        echo '会在所有方法之前执行<br>';
    }

    //前置操作
    public function _before_index()
    {
        echo '会在index方法之前执行<br>';
    }

    //后置操作
    public function _after_index()
    {
        echo '会在index方法之后执行<br>';
    }




    验证 验证码
    $verify = new \Think\Verify();    
     $verify->check($yzm);




============================ 接口的使用 ==============================



//查询IP地址的接口
function getIp($ip){
    $ch = curl_init();
    $url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip='.$ip;
    $header = array(
        'apikey: e9c8d1b2fc9b6eae535d76bd935db6bb',
    );
    // 添加apikey到header
    curl_setopt($ch, CURLOPT_HTTPHEADER  , $header);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    // 执行HTTP请求
    curl_setopt($ch , CURLOPT_URL , $url);
    $res = curl_exec($ch);

    return json_decode($res, true);
}


//机器人接口
function turing($info){
    $ch = curl_init();
    $url = 'http://apis.baidu.com/turing/turing/turing?key=879a6cb3afb84dbf4fc84a1df2ab7319&info='.$info.'&userid=eb2edb736';
    $header = array(
        'apikey: e9c8d1b2fc9b6eae535d76bd935db6bb',
    );
    // 添加apikey到header
    curl_setopt($ch, CURLOPT_HTTPHEADER  , $header);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    // 执行HTTP请求
    curl_setopt($ch , CURLOPT_URL , $url);
    $res = curl_exec($ch);

    return json_decode($res, true);
}





============================ 图片处理 ==============================
public function upload()
        {   
            if(IS_POST){

                $upload = new \Think\Upload();// 实例化上传类    
                $upload->maxSize   =     3145728 ;// 设置附件上传大小    
                $upload->exts      =     array('jpg', 'gif', 'png', 'jpeg');// 设置附件上传类型   
                $upload->savePath  =      './Uploads'; // 设置附件上传目录    // 上传文件     
                $info   =   $upload->upload();    
                if(!$info) {// 上传错误提示错误信息        
                $this->error($upload->getError());    
                }else{// 上传成功        
                    $info[0]['savename'];//图片名
                    $info[0]['ext'];//后缀
                    $path =  "./Uploads".substr($info[0]['savepath'],1);
                   
                    $image = new \Think\Image(); 
                    foreach($info as $k=>$v){
                   
                    //图片剪切
                    $image->open("{$path}{$v['savename']}");//将图片裁剪为400x400并保存为corp.jpg
                    $image->thumb(1200, 1200)->save("{$path}{$v['savename']}");

                        //添加水印
                        $image->open("{$path}{$v['savename']}")->text('周飞','./FZSTK.TTF',100,'#000000',\Think\Image::IMAGE_WATER_SOUTHEAST)->save("{$path}{$v['savename']}"); 
                      
                        
                    }

                    



                    $this->success('上传成功！'); 
                }
            }else{

                $this->display();
            } 
        }


        /*========================= 生成静态 =========================*/
         public function index()
        {
            //创建对象
            $users = D('Users');
            $count = $users->count();
            $Page  = new \Think\Page($count,5);
            $show  = $Page->show();// 分页显示输出
            //计算多少页
            $num = ceil($count / 5);
            //查询数据
            $arr = $users->limit($Page->firstRow.','.$Page->listRows)->getData();
            //分配数据
            $this->assign('arr',$arr);
            //分配分页按钮
            $this->assign('show',$show);
            //分配总条数
            $this->assign('count',$count);
            //分配显示多少页
            $this->assign('num',$num);
            //显示模板
            // $this->display();
            
            //获取当前url
            $pre = '/\/\w*.html$/';
            $strs = '.'.$_SERVER['REQUEST_URI'];
            //用正则去除 后面的 *.html
            $newstr = preg_replace($pre,'', $strs);

            //判断如果不存在就递归创建目录
            if(!file_exists($newstr)){
             mkdir($newstr,777,true);
            } 

            //读取当前页的所有html
            $str = $this->fetch('index'); 
           //写入到文件中 做静态页面
           file_put_contents($strs,$str);

           echo $str;
                



        }



========================= 递归读取删除文件函数 =========================

$path = './Home/';


    function showdir($path){
             $dh = opendir($path);//打开目录

             while(($d = readdir($dh)) != false)
             {
                 //逐个文件读取，添加!=false条件，是为避免有文件或目录的名称为0
                 if($d=='.' || $d == '..'){//判断是否为.或..，默认都会有

                 continue;
                 }
                 // echo $d."<br />";
                 if(is_dir($path.'/'.$d)){//如果为目录

                 showdir($path.'/'.$d);//继续读取该目录下的目录或文件

                 }
                 //如果为文件就删除
                 if(is_file($path.'/'.$d))unlink($path.'/'.$d);
             }
    }
 
// $path = './';//当前目录
showdir($path);




/*========================= where条件 =========================*/

        //根据用户名模糊查询
        if(!empty(I('get.username'))) $map['username'] = array('like', "%".I('get.username')."%");

        //根据状态查询
        if(strlen(I('get.status')) > 0) $map['status'] = I('get.status');

        $user = D('Users');
        $total = $user->where($map)->count();
        $page = new \Think\Page($total, 4);
        $arr = $user->where($map)->limit($page->firstRow.','.$page->listRows)->select();



        /*========================= 自动验证 和 自动完成 =========================*/
        public function add()
    {
        if (IS_POST) {
            $user = D('Users');
            //create方法会过滤非法字段；还会触发自动验证和自动完成
            $data = $user->create($_POST);
            
            //判断数据是否创建成功
            if($data){
                dump($data);exit;
                //创建成功后代表数据已经经过了验证和自动完成
                if($user->add($data)){
                    $this->success('添加成功', U('User/index'));
                }else{
                    $this->error('添加失败');
                }
            }else{
                $this->error($user->getError());
            }
        } else {
            $this->display();
        }
    }



    class UsersModel extends Model
{
    //自动验证
    protected $_validate = array(
        array('name', 'require', '用户名不能为空'),
        array('email', 'email', '邮箱格式不正确'),
        array('repwd','pwd','确认密码不正确',0,'confirm'),
        array('name','','帐号名称已经存在！',0,'unique',3),
    );

    //自动完成
    protected $_auto = array(
        array('pwd','md5',3,'function'),
        array('addtime', 'time', 1, 'function'),
    );

    //字段映射
    protected $_map = array(
        'name' => 'username', // 把表单中name映射到数据表的username字段
    );



/*========================= windows定时任务 =========================*/

http://blog.csdn.net/alongken2005/article/details/7873057

1.新创建一个index.php 类容如下 所有路径都要写绝对的
<?php
<meta charset='utf-8'>
file_put_contents('D:\www\root\1.txt','ok');
?>

2.新建.bat文件，代码如下：
"D:\Program Files\wamp\bin\php\php5.3.10\php.exe" -f "D:\www\test\index.php"
保存，并命名为run.bat。

3.到windows下设置定时任务



/**
 *获取html文本里的img
 * @param string $content
 * @return array
 */
function sp_getcontent_imgs($content){
    import("phpQuery");
    \phpQuery::newDocumentHTML($content);
    $pq=pq();
    $imgs=$pq->find("img");
    $imgs_data=array();
    if($imgs->length()){
        foreach ($imgs as $img){
            $img=pq($img);
            $im['src']=$img->attr("src");
            $im['title']=$img->attr("title");
            $im['alt']=$img->attr("alt");
            $imgs_data[]=$im;
        }
    }
    \phpQuery::$documents=null;
    return $imgs_data;
}