正则表达式：http://www.jb51.net/article/43190.htm
var str = '12345abcdefghijkrmnopqlstuvwxyz';
function insertSpace(s) 
        { 
            //匹配任意一个字符 每匹配到一个用$1引用并加上一个逗号
        var result =s.replace(/(.{1})/g,"$1,"); 
        //匹配任意3个字符为一组 每匹配到一组用$1引用并加上一个空格
        var result =s.replace(/(.{3})/g,"$1 "); 

        return result; 
        } 
        var string = insertSpace(str);
        alert(string);

=================================================================

document.title :选中标题标签
length  长度
查看数据类型：typeof
isNaN()：检测数值是否是NaN
JS的最大取值范围:Number.MAX_VALUE 
alert(btn.innerHTML);获取标签对中的值
onclick="test()": 点击事件

浏览器信息：window.navigator.userAgent

arguments：包含所有实参的集合
自动类型转换:Number()
手动类型转换 parseInt() parseFloat()    
str.substr(2,2);  字符串截取   
document.getElementById
document.getElementsByTagName('span');
document.write()
console.log()
document.title = '值'
断点调试:debugger
onclick="return confirm('数据物价，谨慎删除')"
一次性定时器
        setTimeout(回调函数， 时间);
        clearTimeout(就是定时器的返回值);

    周期性定时器
        setInterval(回调函数， 时间);
        clearInterval(就是定时器的返回值)



============================================================



/********** 获取浏览器的详细信息 ******/
window.navigator.userAgent

if(str.indexOf('MSIE') != -1)
{
    alert('IE');
}else{
    alert('标准');
}



 /******************** 写在事件里面的JS代码 ********************/
  <button onclick="test()" >按钮</button>



  /******************** 以协议的方式写JS代码 ********************/
  <a href="javascript:void(0)" onclick="test()">百度2</a>



  /*********** 阻止浏览器默认行为，千万不要忘了return ***************/
  <a href="https://www.baidu.com" onclick="return false;">百度</a>


  /******************** 获取鼠标的坐标点 ********************/

<div id="box" onclick="test(event,this)"></div>

var box = document.getElementById('box');

box.onclick = function(e){
    var e = event || e;
    document.title = e.clientX + '_' + e.clientY;
}



  
 window.onmousemove = function(e){
        //调试鼠标坐标点
        document.title = e.clientX + '_' + e.clientY;

        //改变图片的位置属性
        pic.style.top = e.clientY + 'px';
        pic.style.left = e.clientX + 'px';

    }


/******************** 弹窗 ********************/
echo "<script>alert('我要弹哦');window.location.href= './index.php';</script>";


/******************** 点击事件 ********************/
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




/******************** arguments：包含所有实参的集合 ********************/
 function sum(){


        alert(typeof arguments);
        console.dir(arguments);

        var num = 0;//undefined
        
        for(k in arguments){
            var tmp = parseInt(arguments[k]);

            if(!isNaN(tmp)){
                num += tmp;
            }
        }

        return num;
    }

var res = sum(1,2,3,4);
alert(res);


    


/******************** 可以自宫的函数 ********************/

<button onclick="zan()">赞一个</button>

function zan(){
    alert('赞一个！！');

    zan = function(){
        alert('你已经赞过了');
    }
}



/******************** 子调函数 ********************/
//自调函数：可以用来模拟命名空间
(function(){
    var num = 10;
    alert(2);

})()


/******************** 递归 ********************/

var res = prompt('请输入用户名','sb');
alert(res);



//递归
function login(){
    var res = prompt('你叫啥名字？');
    if(res == 'sb'){
        alert('欢迎你，sb');
    }else{
        login();
    }
}

login();




/******************** 自写时间函数 ********************/

function date(_a,_b,_c,_d,_e,_f){
        if(_a == 'zh'){
                    var _a = '年';
            if(!_b) var _b = '月';
            if(!_c) var _c = '日 ';
            if(!_d) var _d = ':';
            if(!_e) var _e = ':';
            if(!_f) var _f = ' ';
            
        }else{
            if(!_a) var _a = '-';
            if(!_b) var _b = '-';
            if(!_c) var _c = '  ';
            if(!_d) var _d = ':';
            if(!_e) var _e = ':';
            if(!_f) var _f = ' ';
            
        }


        var date = new Date;

        document.write(d.toLocaleString());//返回一个完整的时间
        var Y = date.getFullYear( );// 返回Date对象的年份字段
        var m = date.getMonth( ) + 1;// 返回Date对象的月份字段
        var d = date.getDate( );//; //返回一个月中的某一天 
        var H = date.getHours( );// 返回Date对象的小时字段 
        var i = date.getMinutes( );// 返回Date对象的分钟字段 
        var z = date.getSeconds( );// 返回Date对象的秒字段 
        return Y + _a + m + _b + d + _c + H + _d + i + _e + z + _f;

/******************** 分割 ********************/
    function getLocalTime(nS) {       
      return new Date(parseInt(nS) * 1000).toLocaleString().replace(/年|月/g, "-").replace(/日/g, " ");        
   }       
   alert(getLocalTime(1177824835));  



/******************** 自动刷新+几秒后跳转 ********************/
   <meta http-equiv="refresh" content="5;
url=http://localhost<?php echo $_SERVER['REQUEST_URI'] ?>">

 window.location.reload();//刷新当前页

/***** 变相的实现自动添加数组值 ***********/
    // arr[arr.length] = 1;
    // arr[arr.length] = 2;




/******** 构造器函数 可以用来模拟继承************/
function Person(name,age){
    this.name = name;
    this.age = age;

    this.say = function(){
        alert('瞎嚷嚷');
    }
  }

  Person.prototype.eat = function(){
    alert('今天晚上吃啥？');
  }

  var p = new Person('jack',19);
  var p2 = new Person('rose',19);
  p.eat();
  p2.eat();
  p.say();
  p2.say();


  /******************** 通过js找css的样式 ********************/
  var box = document.getElementById('box');


  //IE浏览器的获取方式
    var css = box.currentStyle;

//标准浏览器获取方式
    // var css = document.defaultView.getComputedStyle(box)


/******************** 获取浏览器在屏幕中的位置 ********************/
IE/chrome
// alert(window.screenLeft);
// alert(window.screenTop);

火狐
alert(window.screenX);
alert(window.screenY);




/******************** 获取屏幕的宽高 ********************/
//获取屏幕的宽高
    // alert(window.screen.width);
    // alert(window.screen.height);

    //获取屏幕的可用宽高
    // alert(window.screen.availHeight);   
    // alert(window.screen.availWidth);  

/******************** 分割 ********************/
alert(window.history.length);
    // window.history.back();  //后退一个页面
    // window.history.forward();//前进一个页面
    //记住这个就好
     window.history.go(-3); 去到指定的页面


     /******************** 事件列表 ********************/

     鼠标:
        *   onclick     单击
        *   ondblclick  双击
            contextmenu (在body) 文本菜单（鼠标右键使用） 
                要想屏蔽鼠标右键使用return false
                window.document.oncontextmenu=function(ent){...}
            reset()重致
            submit() 提交 
            focus()  默认选中input表单
            onmousedown 按下
            onmouseup   抬起
        *   onmousemove 移动
        *   onmouseenter 鼠标放上去的时候
        *   onmouseleave  鼠标离开的时候
            onmouseover 鼠标放上去的时候
            onmouseout 鼠标离开的时候
        *   button 鼠标的按键码 



        键盘：
            keypress  键盘事件
        *  onkeydown   按下
        *   keyCode   键盘编码 返回按键码数字
        $(document).keydown(function(event){ 
        console.log(event.keyCode); 
        }); 


        图片事件
            * onload 图片加载完成后
            * onerror 图片加载发生错误的时候
             onabort //当图片加载中断的时候


        文档：(主要使用在body标签中)
        *   onload   文档加载完成后
            onunload 关闭(为了兼容可使用下面函数)
            onbeforeunload 关闭之前
        
        表单： 
        *   oninput 当input框的值改变的时候 时时改变
            onpropertychange input框的值改变的时候 IE
        *   onfocus 获取焦点的时候触发
        *   onblur  失去焦点的时候触发
        *   onsubmit 提交事件
        *   onreset  当重置表单的时候   
        *   onchange （如下拉框选择事件）当改变表单域的时候触发 通常不会绑定在input框上
        onselect  选中文本时   小贼，想复制？
        其它：
        *   scroll 滚动事件(常用延迟加载、瀑布流技术)
            window.onscroll=function(){
                document.documentElement.scrollTop;//获取滚动条的上距离
                document.documentElement.scrollLeft;//滚动条的左距离
            }
            
            selectd 事件
        *   onresize 调整了窗口大小
        *   oncontextmenu   当右键菜单要弹出来的时候触发

        //阻止事件冒泡的属性
        *e.cancelBubble = true;

        //阻止事件冒泡的属性
        e.stopPropagation();


        offset
    元素本身的宽高（包含边框和内边距，没有包含外边距）
    offsetHeight
    offsetWidth

    元素距离浏览器原点的距离
    offsetTop
    offsetLeft

scroll
    整个文档的宽高
    scrollHeight
    scrollWidth

    滚动条的位置，可读可写（有点兼容性问题）
    scrollTop
    scrollLeft

client
    元素的宽高（不包含border）
    clientHeight
    clientWidth

    获取元素的边框大小
    clientTop
    clientLeft

    //通常是这样用的 —— 获取浏览器的可用宽高
    document.write(document.documentElement.clientHeight);
    document.write(document.documentElement.clientWidth);


    //获取滚动条的位置
    window.onscroll = function(){
        
    //chrome
    //document.title = document.body.scrollTop;//body
    //
    //IE  FF
    //document.title = document.docuemntElement.scrollTop;//html
    //
    //用短路解决兼容性问题
    var top = document.body.scrollTop || document.documentElement.scrollTop;

    document.title = top;

    }



/******************** 节点 ********************/   

节点信息
        nodeName（节点名称） 
            元素节点的 nodeName 是标签名称 
            属性节点的 nodeName 是属性名称 
            文本节点的 nodeName 永远是 #text 
            文档节点的 nodeName 永远是 #document 
            注释节点的 nodeName 永远是 #comment  

        nodeValue（节点值） 
            对于文本节点，nodeValue 属性包含文本。
            对于属性节点，nodeValue 属性包含属性值。
            nodeValue 属性对于文档节点和元素节点是不可用的。

        nodeType（节点类型）
            元素 1 
            属性 2 
            文本 3 
            注释 8 
            文档 9 

    根节点（就是不用找就能用的节点）
        document.documentElement      HTML
        document.body                 BODY

    定位节点
        document.getElementById('ID');
        document.getElementsByTagName('标签名');
        document.getElementsByClassName('class名');


属性
        //向下找儿子
        firstChild          //找大儿子
        lastChild           //找小儿子
        childNodes          //找所有的子节点（包括文本节点，不常用）
        children            //找所有的元素节点儿子（不包含文本节点，常用）

        //向上找爹
        parentNode

        //找兄弟
        nextSibling         //找下一个兄弟
        previousSibling     //找上一个兄弟

        //所有属性节点
        attributes     



        方法
        创建一个节点(只创建，不添加)
            document.createElement('标签名')

        添加节点(只能添加子节点)
            appendChild()       die.appendChild(son);
            只能添加到die的最后

            insertBefore()      die.insertBefore(son, position);




克隆节点
        cloneNode()   newObj = old.cloneNode(true);
        只有传了参数true，才会带着子节点一起克隆

    删除节点
        removeChild()    die.removeChild(son);

        //变相的删除自己
        son.parentNode.removeChild(son);



        设置属性
        setAttribute()
        用setAttribute设置的属性可以在页面源代码里面看到

    获取属性
        getAtrribute()
        可以获取HTML的标准属性或者非标准属性



document.forms  获取页面上所有form表单的集合
    fom.elements    获取fom表单中所有的表单元素集合
    
    可以直接通过表单里面的name值选中对象
        fom.username
        fom.pwd

    页面中所有的ID可以直接使用，但是不推荐

    select.options  返回下拉框中所有的option集合

    select.options.length   可读可写，下拉框中option的数量

    table.rows              返回表格中所有行的集合
    table.rows[0].cells     返回表格中第一行中所有的单元格集合


    跳转到上一个页面
    window.history.go(-1);



选中单选按钮触发
     $("#editors:radio").click(function(){
      alert(1)
  });



//打开一个新窗口
function SelectTemplets(tpl)
{
    // 
   var posLeft = 200;
   var posTop = 300;
   window.open("{{:U('SelectTemplets')}}?path=./Templates/Pc&tplname="+tpl, "poptempWin", "scrollbars=yes,resizable=yes,statebar=no,width=600,height=400,left="+posLeft+", top="+posTop);
}
//将此窗口的值写入到另一个窗口 
  function gb(filename)
{
    window.opener.document.form.<?php echo $tplname;?>.value=filename;//将此窗口的值写入到另一个窗口 name等于form下的name等于tpl的表单
    if(document.all) window.opener=true;
    window.close();//关闭窗口
}



怎样添加、移除、移动、复制、创建和查找节点？

1）创建新节点
createDocumentFragment() //创建一个DOM片段
createElement() //创建一个具体的元素
createTextNode() //创建一个文本节点
2）添加、移除、替换、插入
appendChild() //添加
removeChild() //移除
replaceChild() //替换
insertBefore() //插入
3）查找
getElementsByTagName() //通过标签名称
getElementsByName() //通过元素的Name属性的值
getElementById() //通过元素Id，唯一性



在父窗口中获取iframe中的元素
格式：$("#iframe的ID").contents().find("#iframe中的控件ID").click();//jquery 方法1  
实例：$("#ifm").contents().find("#btnOk").click();//jquery 方法1  

在iframe中获取父窗口的元素
格式：$('#父窗口中的元素ID', parent.document).click();  
实例：$('#btnOk', parent.document).click();  

iframe 中给父窗口传值
$('#urlss', window.parent.document).val('sssssssssssssssss');

1, window.location.href
整个URl字符串(在浏览器中就是完整的地址栏)
本例返回值: http://www.maidq.com/index.html?ver=1.0&id=6#imhere

2,window.location.protocol
URL 的协议部分
本例返回值:http:

3,window.location.host
URL 的主机部分
本例返回值:www.maidq.com

4,window.location.port
URL 的端口部分
如果采用默认的80端口(update:即使添加了:80)，那么返回值并不是默认的80而是空字符
本例返回值:""

5,window.location.pathname
URL 的路径部分(就是文件地址)
本例返回值:/fisker/post/0703/window.location.html

6,window.location.search
查询(参数)部分
除了给动态语言赋值以外，我们同样可以给静态页面,并使用javascript来获得相信应的参数值
本例返回值:?ver=1.0&id=6

7,window.location.hash
锚点
本例返回值:#imhere



        <script language="javascript" type="text/javascript">
                function IsPC() {
            var userAgentInfo = navigator.userAgent;
            var Agents = ["Android", "iPhone",
                        "SymbianOS", "Windows Phone",
                        "iPad", "iPod"];
            var flag = true;
            for (var v = 0; v < Agents.length; v++) {
                if (userAgentInfo.indexOf(Agents[v]) > 0) {
                    flag = false;
                    break;
                }
            }
            return flag;
                }
                var flag = IsPC(); //true为PC端，false为手机端
                if(flag == true){

                        window.setTimeout("window.location='pc/index.html'");

                }if(flag == false){
                        window.setTimeout("window.location='mobile/index.html'");
                }
        </script>