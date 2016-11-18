<?php
namespace Admin\Controller;
use Think\Controller;
class BakController extends Controller 
{

  public function index() 
  {
        $model = new \Think\Model();
        $sql = "show tables";
        $dbname = $model->query($sql);
        $this->assign('dbname',$dbname);
        // dump($dbname);
        $this->display();
         
  }

      /**
       * 备份
       */
      public function bak()
      {

        $dbuser =  C('DB_USER');
        $dbpwd  =  C('DB_PWD');
        $s = '0123456789abcdefghijklmnopqrstuvwxyz'; //62个字符
        $strs = str_shuffle($s);//随机打乱
        $str = substr($strs,mt_rand(6,30),10);
        $time = date('Y-m-d-H-i-s',time());

        mkdir('./bak/'.$time.$str);
        fopen("./bak/{$time}{$str}/index.html", "w");//创建一个index.html文件  保护作用

        foreach ($_POST['dbname'] as $key => $value) {

            $res = exec("mysqldump -u{$dbuser} -p{$dbpwd} yundi {$value} > ./bak/{$time}{$str}/{$value}{$time}.sql");

        }
        if($res === false){

            $this->ajaxReturn('备份失败！');
        }else{

            $this->ajaxReturn('备份成功');
        }
        
      }

      /**
       * 恢复
       */
      public function restore()
      {
            if(IS_POST){

                $dbuser =  C('DB_USER');
                $dbpwd  =  C('DB_PWD');
                $bak = $_POST['bak'];//接收要恢复的文件包
                if(!$bak)$this->ajaxReturn('你没有选择任何数据包！');
                $model = new \Think\Model();
                //查询所有表名  并且删除
                $sql = "show tables";
                $dbname = $model->query($sql);
                foreach($dbname as $v){

                    $dbnames .= ','.$v['Tables_in_yundi'];
                }
                $dbname_s = substr($dbnames,1);
                $res = $model->query("drop table {$dbname_s}");
                if($res === fales){

                     $this->ajaxReturn('清空数据失败！');
                }


                //遍历要还原的sql文件
                $path = "./bak/{$bak}/";
                $dh = opendir($path);//打开目录
                $files = array();
                while($file = readdir($dh)){
                   if($file == '.' || $file == '..' || $eile == 'index.html'){
                        continue;
                   }
                   if(is_file($path.'/'.$file))$files[] = $file;
               }

                foreach($files as $v){

                   
                    $ress = exec("mysql -u{$dbuser} -p{$dbpwd} yundi < ./bak/{$bak}/{$v}");//source F://vzhoufei.sql
                    
                   }

                if($ress === false){

                    $this->ajaxReturn('数据还原失败！');
                    
                }else{

                    $this->ajaxReturn('数据还原成功！');
                }




            }else{

                    $path = './bak/';
                    $dh = opendir($path);//打开目录
                    $files = array();
                    while($file = readdir($dh)){
                       if($file == '.' || $file == '..'){
                            continue;
                       }
                       if(is_dir($path.'/'.$file))$files[] = $file;
                   }
                    $this->assign('files',$files);
                    $this->display();
            }
      }


}

 