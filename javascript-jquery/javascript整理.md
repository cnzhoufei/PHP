 length  长度
 查看数据类型：typeof
isNaN()：检测数值是否是NaN
JS的最大取值范围:Number.MAX_VALUE 
alert(btn.innerHTML);获取标签对中的值


验证码：onclick='this.src = "./Common/yzm.php?id=" + Math.random()'


 /******************** 写在事件里面的JS代码 ********************/
  <button onclick="test()" >按钮</button>


  /******************** 以协议的方式写JS代码 ********************/
  <a href="javascript:void(0)" onclick="test()">百度2</a>



  /*********** 阻止浏览器默认行为，千万不要忘了return ***************/
  <a href="https://www.baidu.com" onclick="return false;">百度</a>


  /******************** 获取鼠标的坐标点 ********************/
 window.onmousemove = function(e){
        //调试鼠标坐标点
        document.title = e.clientX + '_' + e.clientY;

        //改变图片的位置属性
        pic.style.top = e.clientY + 'px';
        pic.style.left = e.clientX + 'px';

    }


/******************** 弹窗 ********************/
echo "<script>alert('我要弹哦');window.location.href= './index.php';</script>";


/******************** 是点击事件 ********************/
<a href="javascript:void(0)" onclick="test()">百度33</a>//onclick 是点击事件
function test(){
    	// alert(1);
    	window.location.href = 'https://www.baidu.com';
    }


    /******************** 通过ID找对象 ********************/     
 		var box = document.getElementById('box');
         alert(box);
        box.style.background = 'red';
         box.title = 'JS改的title属性';




  /******************** 通过标签名找对象，会返回一个集合 ********************/

  		<span title="标题"></span>
        var span = document.getElementsByTagName('span');
        span[0].title = '用js修改的标题';

        


 /******************** JS的调试方式 ********************/

    1. alert()  弹窗调试
        会中断代码执行

    2.document.write()
        相当于PHP中的echo
        当代码执行完毕后，再执行，会覆盖前面的代码

    3.console.log()
    3.1 console.dir()
        用于调试比较复杂的数据
    
    4.document.title = '值'
        用于调试一些动态数据

    5.debugger
        断点调试，必须要打开调试控制台（F12）


/******************** 确认执行 ********************/
<a href="./action.php?a=del&id=5" onclick="return confirm('数据物价，谨慎删除')">删除</a>


/******************** 会自动将with的对象拼接到语句前面 ********************/

    with(document){
        write('#########<br>');
        write('#########<br>');
        write('#########<br>');
        write('#########<br>');
        var a = getElementById('a');
    }



    /******************** 全选 ********************/
    <input type="checkbox" />###############<br>
    <button onclick="select(true)">全选</button>
    <button onclick="select(false)">全不选</button>
    <button onclick="fan()">反选</button>
    var inputs = document.getElementsByTagName('input');

     function select(flag){
        // alert(1);
        for(var i = 0; i < inputs.length; i++){
            inputs[i].checked = flag;
        }
    }

     //反选
    function fan(){
        for(var i = 0; i < inputs.length; i++){
            inputs[i].checked = !inputs[i].checked;
          
        }
    }



    /******************** 定时器 ********************/

     一次性定时器
        setTimeout(回调函数， 时间);
        clearTimeout(就是定时器的返回值);

    周期性定时器
        setInterval(回调函数， 时间);
        clearInterval(就是定时器的返回值)

    ☆：时间的单位都是毫秒


    function test(){
      alert('3秒了');
    }

    var timer = setTimeout(test,1000);
    clearTimeout(timer);

    var i = 1;

    var timer2 = setInterval(function(){
      // console.log(i);
    document.write(i);document.write('<br>');

      i++;
    },10);
    // clearInterval(timer2);



    /******************** 字符串截取 ********************/
    // var res = str.substr(2,2);
    // alert(res);
    // alert(str.length);




    /******************** 类型转换 ********************/

            自动类型转换
                Number()
                    undefined   -》 NaN
                    boolean     -》 0或者1
                    string      -》 只要不是一个纯洁的数字，结果都是NaN

            手动类型转换
                parseInt()
                parseFloat()
                    undefined   -》 NaN
                    boolean     -》 NaN
                    string      -》 只有 a56 会得到NaN，其他参考PHP类型转换





                    获取浏览器的可视宽高
                    window.innerWidth
                    window.innerHeight


                    获取屏幕宽高
                    window.screen.height
                    window.screen.width