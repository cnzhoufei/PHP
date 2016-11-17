
HTML CSS
=====================================
   JavaScript 脚本语言   
 
===================================== 
 什么是JavaScript？
	1. JavaScript 是一种客户端脚本语言（脚本语言是一种轻量级的编程语言）。 
	2. JavaScript 通常被直接嵌入 HTML 页面。
	3. JavaScript 是一种解释性语言（就是说，代码执行不进行预编译）。 
	特点：
		1. 弱类型 
		2. 基于对象。(因为面向对象需要具有封装、继承、多态的特征)

在客户端浏览器上执行的脚本：
 1. JavaScript  2. VBscript  3 applet （需要安装JDK）

  ECMAScript总称
     |
     |-- JavaScript
     |
     |-- ActionScript
     |
     |-- ScriptEase

JavaScript语言中包含三个核心：ECMAScript基本语法、DOM、BOM

JavaScript是基于对象的脚本语言。

在HTML中如何使用JavaScript
===============================================
*1. 使用<script></script>标签：
    属性：
	charset（可选）字符集设置、
	defer（可选执行顺序）值：defer、
	language(已废除)、
	src（可选）使用外部的js脚本文件
	type(必选)类型：值：text/javascript

    <script type="text/javascript">
		<!--
		javaScript语言
		//-->
    </script>

2. 在html标签的事件中，超级链接里。
	<button onclick="javaScript语言"></button>
	<a href="javascript:alert('aa');alert('bb')">点击</a>

3. 外部导入方式（推荐）：
	<script type="text/javascript" src="my.js"></script>
	

JavaScript的语法：
===========================================
1.区分大小写：变量名、函数名、运算符以及其他一切东西都是区分大小写的。

2.他和php一样属于弱类型语言。

3.每行结尾的分号可有可无。(js中的每条语句之间的分割符可以是回车换行也可以是";"分号(推荐))

4.脚本注释：
	// 单行注释
	/* 多行注释  */

5.括号表示代码块:{}

6.变量的定义：使用var关键字来声明。
   变量的命名规范是：字母数字，$符和下划线构成，但是不可以以数字开始。
   变量名不可以使用关键字. 
 
   
   typeof函数获取一个变量的类型：
	* undefined - 如果变量是 Undefined 类型的
    	* boolean - 如果变量是 Boolean 类型的
    	* number - 如果变量是 Number 类型的 (整数、浮点数)
    	* string - 如果变量是 String 类型的 （采用""、 ''）
    	* object - 如果变量是一种引用类型或 Null 类型的 
                    如：new Array()/ new String()...
		* funciton -- 函数类型
		  
 7.JavaScript的数据类型：
	undefined 类型 
    	null 类型（对象）
	boolean 类型
	number 类型
		八进制数和十六进制数 012
		浮点数
		特殊的 Number 值
	string 类型
		var s = "hello";
		document.write(s+"<br/>");
		document.write(s[1]+"<br/>"); //使用下标可以取出对应的字符
		document.write(s.length+"<br/>");//求长度
	
	object引用类型
		引用类型通常叫做类（class），也就是说，遇到引用值，所处理的就是对象。
		Object 对象自身用处不大，不过在了解其他类之前，还是应该了解它。
		因为 ECMAScript 中的 Object 对象与 Java 中的 java.lang.Object 相似，
		ECMAScript 中的所有对象都由这个对象继承而来，Object 对象中的所有属性
		和方法都会出现在其他对象中，所以理解了 Object 对象，就可以更好地理解其他对象。
	
8. 类型转换：
	使用：Number（）、parseInt() 和parseFloat（） 做类型转换
	Number()强转一个数值(包含整数和浮点数)。
	*parseInt()强转整数，
	*parseFloat（）强转浮点数
	
	函数isNaN()检测参数是否不是一个数字。 is not a number
	
	ECMAScript 中可用的 3 种强制类型转换如下：
		Boolean(value) - 把给定的值转换成 Boolean 型；
		Number(value) - 把给定的值转换成数字（可以是整数或浮点数）；
		String(value) - 把给定的值转换成字符串；
, 
JavaScript的运算符
=====================================================================
1. 一元运算符
*	delete：用于删除对象中属性的   如：delete o.name; //删除o对象中的name属性
	void：	void 运算符对任何值返回 undefined。没有返回值的函数真正返回的都是 undefined。
*	++ --
	一元加法和一元减法
2. 位运算符
	位运算 NOT ~
	位运算 AND &
	位运算 OR |
	位运算 XOR ^  (不同为1，相同则为0)
	左移运算 <<
	右移运算 >>
3. 逻辑运算符
	逻辑 NOT ! 运算符  非
	逻辑 AND && 运算符 与
	逻辑 OR  || 运算符 或
4. 乘性运算符：*（ 乘） /(除) %（取模）求余
5. 加性运算符： + - 
	*其中+号具有两重意思：字串连接和数值求和。
	就是加号”+“两侧都是数值则求和，否则做字串连接  
6. 关系运算符 >  >=  < <=
7. 等性运算符 ==  === != !==
8. 条件运算符  ? : (三元运算符)
9. 赋值运算符 =  +=  -= *= /= %= >>= <<=
10 逗号运算符 
	用逗号运算符可以在一条语句中执行多个运算。
	var iNum1=1, iNum2=2, iNum3=3;

	
	
javaScript（语句流程控制）
====================================================================
	1. 判断语句 if语句；  if... else ...    if ...  else if ... else...

	2. 多分支语句： switch（）{。 case ：。。。。}
			switch (i) {
			  case 20: alert("20");
				break;
			  case 30: alert("30");
				break;
			  case 40: alert("40");
				break;
			  default: alert("other");
			}
	3. 循环语句（迭代语句）
			for：
			
			while
			
			do...while
			
			*for-in 语句: 语句是严格的迭代语句，用于枚举对象的属性。
				var a = [10,20,30,40,50];
				//迭代的是数组的下标。
				for(i in a){
				   document.write(a[i]);
				}
				//输出： 1020304050
				
	4. break 和 continue 语句对循环中的代码执行提供了更严格的控制。	
			
	5. *with 语句用于设置代码在特定对象中的作用域。
	
  //扩充知识：	
	1. 在网页文档中获取一个节点对象（HTML标签）
		document.getElementById("mid"); //获取标签id属性值为mid的节点对象
   
	2. 定时相关函数：
		setTimeout(vCode, iMilliSeconds [, sLanguage]) -- 单次定时执行指定函数 
		clearTimeout(iTimeoutID) -- 取消上面的单次定时
			
		setInterval(vCode, iMilliSeconds [, sLanguage]) --无限次定时执行指定函数 
		clearInterval(iIntervalID)-- 取消上面的多次定时

==================================================
    JS的第一天作业
=============================================
一、理论作业：
   1. 什么是JavaScript？
   2. 在HTML中嵌入JavaScript的方法有几种？
   3. JavaScript的常用类型都有哪些？
   4. 常用的JavaScript的类型转换函数有那两个？
   5. 我们使用哪个函数判断是否不是一个整数？
   6. JavaScript语言的运算符都有哪些？

二、代码题：
   1. 参考课程代码做一个简单的计算器
   2. （选做）一个倒计时的按钮（10,9,8,7,...这是是个灰色不可点击的，当为0是会换成同意字样，并可点击。）
   3. （选做） 做一个倒计时（时 分 秒）。可选带暂停效果
   
 
三、预习作业：
   1. JavaScript的函数如何定义和调用。
   2. 常用的系统函数都有哪些。
   3. 对象的应用与声明。
===================end==========================

=================================================
	JavaScript 第二天内容：
=================================================

一、JavaScript的函数：
--------------------------------------------------------
标准格式： function 函数名（[参数列表..]）{
				函数体。。。
				[return 返回值;]
		   }
	   
JavaScript三种定义函数方法：
	*第一种是使用function语句定义函数
		如上面格式
		
	第二种是使用Function()构造函数来定义函数（不常用）
		var 函数名 = new Function(“参数1”，”参数2”，”参数3”……”函数体”);
		如：
		var 函数名 = new Function(”x”,”y”,”var z=x+y;return z;”);

	*第三种是在表达式中定义函数
		var 函数名 = function(参数1，参数2，…){函数体};
		//例如：
		//定义
			var add = function(a,b){
				return a+b;
			}
			//调用函数
			document.write(add(50,20));
		
	arguments 对象
			在函数代码中，使用特殊对象 arguments，开发者无需明确指出参数名，就能访问它们。
			例如，在函数 sayHi() 中，第一个参数是 message。用 arguments[0] 
			也可以访问这个值，即第一个参数的值（第一个参数位于位置 0，
			第二个参数位于位置 1，依此类推）。
			
	 关于变量和参数问题：
		函数外面定义的变量是全局变量，函数内可以直接使用。
		在函数内部没有使用var定义的=变量则为全局变量，
		*在函数内使用var关键字定义的变量是局部变量，即出了函数外边无法获取。
		js函数定义的参数没有默认值（目前只有最新的火狐浏览器支持）
	
二、系统中常用的内置函数：	
------------------------------------------------------
	escape()	//字串编码
	unescape()	//字串反编码
	*eval()		//将参数字符串作为脚本代码来执行。
	*isNaN()  	// is not a number (不是一个数值)
	*parseInt()
	*parseFloat()

	
三、JavaScript的对象的定义和使用
-------------------------------------------------------
	1.使用构造函数创建内置对象
		var myObject = new Object();
		myObject.name = “lijie”;
		myObject.age = 20;
		myObject.say = function(){...}
	
	2.直接创建自定义对象
		var 对象名 = {属性名1：属性值，属性名2：属性值2，…….}
	
	*3.使用自定义构造函数创建对象
		function pen(name,color,price){
			//对象的name属性
			this.name = name;
			//对象的color属性
			this.color = color;
			//对象的piece属性
			this.price = price;
			//对象的say方法
			this.say = function(){};
		}
		
		var pen = new pen(“铅笔”,”红色”,20);
		pen.say();
--------------------------------------------------------------
	测试类型:
	1.typeof()  //global对象的其中一个方法，typeof()
	2.对象.constructor; //查看当前对象的构造函数是谁

	if(arr.constructor==Array){
		alert("数组"); //数组推荐用这种方法，因为typeof得到是object
	}

四、常用技巧函数：
---------------------------------------------------------------
		1. HTML的标签（节点）操作
			document.write(""); //输出的
			document.getElementById("id名")； //获取html页面标签中，标签id属性等于此值的对象。
				如：var id = document.getElementById("hid"); //获取id值为hid的标签对象
			
			document.getElementsByTagName("标签名"); //获取当前文档执行的标签对象
			
			html标签对象的操作：
				标签对象.innerHTML="内容"；//在标签对象内放置指定内容
				标签对象.style.css属性名="值" //改变标签对象的样式。
					示例：id.style.color="red";
					注意：属性名相当于变量名,所以css属性名中的减号要去掉，将后面的首字母大写。
						如：font-size（css）---> fontSize(JS属性)
				标签对象.value；	 //获取标签对象的value值
				标签对象.value=”值“；//设置标签对象的value值		
				
--------------------------------------------------
    JS的第二天作业
--------------------------------------------------
	一、理论作业：
	   1. JavaScript三种定义函数方法?
	   2. arguments对象的理解？
	   3. 简述JS中全局变量和局部变量的作用域？
	   4. 系统中常用的内置函数有哪些？

	二、代码题：
	   1. 作业全选/全不选/反选的实例
	   2. 做一个文件进度条的特效。
	   3. 使用自定义构造函数创建对象
	   4. （选做） 做一个树形菜单的点击效果
	 
	三、预习作业：
	   1. JavaScript中常用内置对象都有哪些？
	   2. 如何使用Date获取当前时间。
	   3. 如何创建一个数组对象。
	   4. 如何使用对象的基本操作for..in。
===================end==========================

=================================================
	JavaScript 第三天内容：(内置对象)
=================================================
一、for…in语句
----------------------------------------
	for(var i in window){
		document.write(i+”----”+window[i]);
	}
	这种语句可以遍历对象中的所有属性或数组中的所有元素。

二、with语句
--------------------------------------------
	如果使用with语句，就可以简化对象属性调用的层次。
		document.write(‘test1’);
		document.write(‘test2’);
		document.write(‘test3’);
	可以使用with来简化：
		with(document){
			write(‘test1’);
			write(‘test2’);
			write(‘test3’);
		}

三、JavaScript内置对象
-----------------------------------------------
      * Array（数组）
		var a= new Array(); //创建一个空数组
		a = new Array(10);  //创建一个数组单元为10个的数组。
		a = new Array(10,20,30);//创建一个指定数组单元的数组。
		   
		a=['a','b','c','d']; //快捷定义数组
		常用属性：
			length--获取长度。
		
		常用方法：
			toString() 	把数组转换为字符串，并返回结果。
			sort() 	对数组的元素进行排序
			join() 	把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。
			pop() 删除并返回数组的最后一个元素 
			push() 向数组的末尾添加一个或更多元素，并返回新的长度。 

			。。。。。
			
    * Boolean  布尔值包装类对象
		方法：toSource() 	返回该对象的源代码。 
			toString() 	把逻辑值转换为字符串，并返回结果。
			valueOf() 	返回 Boolean 对象的原始值。
    * Date
		var dd = new Date();
		
		getDate() 	从 Date 对象返回一个月中的某一天 (1 ~ 31)。
		getDay() 	从 Date 对象返回一周中的某一天 (0 ~ 6)。
		getMonth() 	从 Date 对象返回月份 (0 ~ 11)。
		getFullYear() 	从 Date 对象以四位数字返回年份。 
		getYear() 	请使用 getFullYear() 方法代替。 
		getHours() 	返回 Date 对象的小时 (0 ~ 23)。 
		getMinutes() 	返回 Date 对象的分钟 (0 ~ 59)。
		getSeconds() 	返回 Date 对象的秒数 (0 ~ 59)。 
		getMilliseconds() 	返回 Date 对象的毫秒(0 ~ 999)。 
		getTime() 	返回 1970 年 1 月 1 日至今的毫秒数。
		同上还有很多set方法用来设置。
		
    * Math  对象用于执行数学任务。方法是静态的。
		abs(x) 	返回数的绝对值。
		ceil(x) 	对数进行上舍入。
		floor(x) 	对数进行下舍入。
		random() 	返回 0 ~ 1 之间的随机数。
		round(x) 	把数四舍五入为最接近的整数。
		
		max(x,y) 	返回 x 和 y 中的最高值。 
		min(x,y) 	返回 x 和 y 中的最低值。
		
    * Number
		toString();
		toFixed 把数字转换为字符串，结果的小数点后有指定位数的数字。 
		
    * String 子串处理对象
		anchor() 	创建 HTML 锚。
		*charAt() 	返回在指定位置的字符。 	
		charCodeAt()返回在指定的位置的字符的 Unicode 编码。
		*indexOf() 	检索字符串。 
		*lastIndexOf() 	从后向前搜索字符串。
		match() 	找到一个或多个正在表达式的匹配。
		*replace() 	替换与正则表达式匹配的子串。
		search() 	检索与正则表达式相匹配的值。
		slice() 	提取字符串的片断，并在新的字符串中返回被提取的部分。
		split() 	把字符串分割为字符串数组。
		substr() 	从起始索引号提取字符串中指定数目的字符。
		*substring() 	提取字符串中两个指定的索引号之间的字符。
		toLocaleLowerCase() 	把字符串转换为小写。
		toLocaleUpperCase() 	把字符串转换为大写。
		*toLowerCase() 	把字符串转换为小写。
		*toUpperCase() 	把字符串转换为大写。
    * RegExp
		exec()正则匹配
		test()
		match()
    * Global
		escape(string) -- 可对字符串进行编码
		unescape(string) -- 函数可对通过 escape() 编码的字符串进行解码。
		encodeURI(URIstring) -- 函数可把字符串作为 URI 进行编码。
		decodeURI(URIstring) -- 函数可对 encodeURI() 函数编码过的 URI 进行解码。
		*eval(string) -- 函数可计算某个字符串，并执行其中的的 JavaScript 代码。
		getClass(javaobj) -- 函数可返回一个 JavaObject 的 JavaClass。
		*isNaN(x) -- 函数用于检查其参数是否是非数字值。
		Number(object) --函数把对象的值转换为数字。
		*parseFloat(string) -- 函数可解析一个字符串，并返回一个浮点数。
		*parseInt(string, radix)
		
		
---------------------------------------------
  四、 JS的第三天作业
---------------------------------------------
	一、理论作业：
	   1. JavaScript中常用内置对象都有哪些？
	   3. 如何创建一个数组对象方式有几种。

	二、代码题：
	   1. 做一个注册的表单验证，
	   2. 实时问候：如：早上好！
	   3. 给你一个日期"2013-06-01 12:24:36"的时间戳值。
	   4. 显示中文的星期几。
	   5. 做一个随机点名系统（点名多次，也不会重复！）;
	   
	三、预习作业：
	   1. JavaScript中常用事件都有哪些？
	   
===================end==========================

=================================================
	JavaScript 第四天内容：(事件)
=================================================
  事件处理
	一、事件源: 任何一个HTML元素（节点） body, div , button p, a, h1 ....... 
	二、事件: 你的操作
		鼠标:
		*	onclick     单击
		*	ondblclick  双击
			contextmenu (在body) 文本菜单（鼠标右键使用） 
				要想屏蔽鼠标右键使用return false
				window.document.oncontextmenu=function(ent){...}
				
		
			onmousedown 按下
			onmouseup   抬起
		*	onmousemove 移动
		*	onmouseenter 鼠标放上去的时候
		*	onmouseleave  鼠标离开的时候
			onmouseover 鼠标放上去的时候
			onmouseout 鼠标离开的时候
		*	button 鼠标的按键码 



		键盘：
			keypress  键盘事件
			onkeydown   按下
		*	keyCode   键盘编码 返回按键码数字



		图片事件
			* onload 图片加载完成后
			* onerror 图片加载发生错误的时候
			 onabort //当图片加载中断的时候


		文档：(主要使用在body标签中)
		*	onload   文档加载完成后
			onunload 关闭(为了兼容可使用下面函数)
			onbeforeunload 关闭之前
		
		表单： 
		*	onfocus 焦点
		*	onblur  失去焦点
		*	onsubmit 提交事件	
		*	onchange 改变（如下拉框选择事件）
		其它：
		*	scroll 滚动事件(常用延迟加载、瀑布流技术)
			window.onscroll=function(){
				document.documentElement.scrollTop;//获取滚动条的上距离
				document.documentElement.scrollLeft;//滚动条的左距离
			}
			
			selectd 事件
		*	onresize 调整了窗口大小
		*	oncontextmenu	当右键菜单要弹出来的时候触发
		
			。。。。

	三、事件处理程序
		 使用一个匿名或回调函数

有三种方法加事件

	第一种： 
		格式： <tag  on事件="事件处理程序" />
	*第二种：
		<script>
			对象.on事件=事件处理程序
		</script>
	第三种：(火狐不兼容)
		<script for="事件源ID" event="on事件">事件处理程序</script>

事件对象：

	属性：
		1. srcElement
		2. keyCode  键盘值
		
	事件 event    window.event

	  1. srcElement  代表事件源对象
	  2. keyCode     事件发生时的键盘码  keypress ,  keydown keyup
	  3. clientX, clientY  坐标位置
	  4. screenX, screenY
	  5. returnValue
	  6. cancelBubble;	 
	
	//为页面添加鼠标右点击事件
	window.document.oncontextmenu=function(ent){
		//兼容IE和火狐浏览器兼容
		var event=ent || window.event;
		//获取事件坐标位置
		var x=event.clientX;
		var y=event.clientY;
		...
	}
	/*********************对象添加事件*******************/
	function addEvent(obj,type,fun){
		obj=$(obj);
		if(obj.addEventListener){
			obj.addEventListener(type,fun);  //FF
			return true;
		}else if(obj.attachEvent){
			return obj.attachEvent("on"+type,fun); //IE
		}else{
			return false;
		};
	};
	/*********************对象删除事件*******************/
	function delEvent(obj,type,fun){
		obj=$(obj);
		if(obj.addEventListener){
			obj.removeEventListener(type,fun);
			return true;
		}else if(obj.attachEvent){
			obj.detachEvent("on"+type,fun);
			return true;
		}else{
			return false;
		};
	}; 
		
	
	 document.getElementById("one").offsetHeight; //获取one对应对象的高度
		obj.offsetTop 指 obj 距离上方或上层控件的位置，整型，单位像素。
		obj.offsetLeft 指 obj 距离左方或上层控件的位置，整型，单位像素。
		obj.offsetWidth 指 obj 控件自身的宽度，整型，单位像素。
		obj.offsetHeight 指 obj 控件自身的高度，整型，单位像素。
			 
	 document.all ? 'IE' : 'others'：在IE下document.all值为1，而其他浏览器下的值为0；
=============================================
第四天：
作业，1. 完善注册的表单验证提示，
	  2. 横向的菜单特效
	  3. 为图片轮换播放添加按钮
	  5.（选做）滚动图片替换
	  6.（选做）键盘事件的处理（通过键盘事件移动图层）
	  
预习：1.JavaScript中的其他事件：（滚动事件，键盘事件。。）
			2.常用的BOM都有哪些？
		    3.HTML中的DOM都有哪些？
		
		
	第五天 讲解BOM
=============================================================================
一、BOM
---------------------------------------
	<button onclick="window.location=''">跳转</button>
	1. window对象
		常用的属性：
			*document ：对 Document 对象的只读引用
			*history	：对 History 对象的只读引用。
			*location：用于窗口或框架的 Location 对象 
			Navigator： 对 Navigator 对象的只读引用 
			*parent： 返回父窗口。 
			length: 设置或返回窗口中的框架数量。 
			Screen: 对 Screen 对象的只读引用 
			status: 设置窗口状态栏的文本。 
			top: 返回最顶层的先辈窗口。 
		
		常用方法：
			alert() 显示带有一段消息和一个确认按钮的警告框。 
			confirm() 显示带有一段消息以及确认按钮和取消按钮的对话框。
			prompt() 显示可提示用户输入的对话框。
			
			close() 关闭浏览器窗口。			
			open() 打开一个新的浏览器窗口或查找一个已命名的窗口。 
			scrollTo() 把内容滚动到指定的坐标。 
			
			setTimeout() 在指定的毫秒数后调用函数或计算表达式。 
			clearTimeout() 取消由 setTimeout() 方法设置的 timeout。 
			setInterval() 按照指定的周期（以毫秒计）来调用函数或计算表达式。 
			clearInterval() 取消由 setInterval() 设置的 timeout。 

	2. Navigator 对象
			Navigator 对象包含的属性描述了正在使用的浏览器。可以使用这些属性进行平台专用的配置。
		常用属性：
            with(document) {
                 write ("你的浏览器信息：<ul>");
                 write ("<li>代码："+navigator.appCodeName+"</li>");
                 write ("<li>名称："+navigator.appName+"</li>");
                 write ("<li>版本："+navigator.appVersion+"</li>");
                 write ("<li>语言："+navigator.language+"</li>");
                 write ("<li>编译平台："+navigator.platform+"</li>");
                 write ("<li>用户表头："+navigator.userAgent+"</li>");
                 write ("</ul>");
            }
			

	3. Screen 对象包含有关客户端显示屏幕的信息。

		常用属性：
            document.write( "屏幕宽度："+screen.width+"px<br />" );
            document.write( "屏幕高度："+screen.height+"px<br />" );
            document.write( "屏幕可用宽度："+screen.availWidth+"px<br />" );
            document.write( "屏幕可用高度："+screen.availHeight+"px" );
		
			
	4. History 对象包含用户（在浏览器窗口中）访问过的 URL。
		
		
	5. Location 对象包含有关当前 URL 的信息。
	
		
	//获取页面中第二form表单中，一个username输入框的值（7种方式）
		//alert(document.forms[1].username.value);
		alert(document.myform.username.value);
		//alert(document.forms.myform.username.value);
		//alert(document.forms.item(1).username.value);
		//alert(document.forms['myform'].username.value);
		//alert(document['myform'].username.value);
		//alert(document.forms.item('myform').username.value); //火狐不兼容
	
	

	第六天 讲解DOM
=============================================================================	
一、基本概念
--------------------------------------------------------------------------	
	HTML DOM 定义了访问和操作HTML文档的标准方法。
	HTML DOM 把 HTML 文档呈现为带有元素、属性和文本的树结构（节点树）。
	DOM 被分为不同的部分：
	  1.Core DOM 
		定义了一套标准的针对任何结构化文档的对象 
	  2.XML DOM 
		定义了一套标准的针对 XML 文档的对象 
	  3.HTML DOM 
		定义了一套标准的针对 HTML 文档的对象。 
	
	节点：根据 DOM，HTML 文档中的每个成分都是一个节点。
	  DOM 是这样规定的：
		>整个文档是一个文档节点 <html></html>
		>每个 HTML 标签是一个元素节点 
		>包含在 HTML 元素中的文本是文本节点 
		>每一个 HTML 属性是一个属性节点 
		>注释属于注释节点 
	
	节点彼此间都存在关系。
		>除文档节点之外的每个节点都有父节点。
		>大部分元素节点都有子节点。
		>当节点分享同一个父节点时，它们就是同辈（同级节点）。
		>节点也可以拥有后代，后代指某个节点的所有子节点，或者这些子节点的子节点
		>节点也可以拥有先辈。先辈是某个节点的父节点，或者父节点的父节点
	
	查找并访问节点
	  你可通过若干种方法来查找您希望操作的元素：
		>通过使用 getElementById() 和 getElementsByTagName() 方法 
		>通过使用一个元素节点的 parentNode、firstChild 以及 lastChild childNodes属性 
	
	节点信息
	  每个节点都拥有包含着关于节点某些信息的属性。这些属性是：
		nodeName（节点名称） 
		nodeValue（节点值） 
		nodeType（节点类型）

	nodeName 属性含有某个节点的名称。
		元素节点的 nodeName 是标签名称 
		属性节点的 nodeName 是属性名称 
		文本节点的 nodeName 永远是 #text 
		文档节点的 nodeName 永远是 #document 
	


二、HTML DOM 对象参考
----------------------------------------------------------------------
	Document: 代表整个 HTML 文档，可被用来访问页面中的所有元素 
		常用集合属性：forms
	Anchor 	: 代表 <a> 元素 
	Area 	: 代表图像映射中的 <area> 元素 
	Base 	: 代表 <base> 元素 
	Body 	: 代表 <body> 元素 
	Button 	: 代表 <button> 元素 
	Event 	: 代表某个事件的状态 
	Form 	: 代表 <form> 元素 
	Frame 	: 代表 <frame> 元素 
	Frameset: 代表 <frameset> 元素 
	Iframe 	: 代表 <iframe> 元素 
	Image 	: 代表 <img> 元素 
	Input button 	: 代表 HTML 表单中的一个按钮 
	Input checkbox 	: 代表 HTML 表单中的复选框 
	Input file 		: 代表 HTML 表单中的文件上传 
	Input hidden 	: 代表 HTML 表单中的隐藏域 
	Input password  : 代表 HTML 表单中的密码域 
	Input radio 	: 代表 HTML 表单中的单选按钮 
	Input reset 	: 代表 HTML 表单中的重置按钮 
	Input submit 	: 代表 HTML 表单中的确认按钮 
	Input text 		: 代表 HTML 表单中的文本输入域（文本框） 
	Link 	: 代表 <link> 元素 
	Meta 	: 代表 <meta> 元素 
	Object  : 代表 <Object> 元素 
	Option  : 代表 <option> 元素 
	Select 	: 代表 HTML 表单中的选择列表 
	Style 	: 代表单独的样式声明 
	Table 	: 代表 <table> 元素 
	TableData : 代表 <td> 元素 
	TableRow  : 代表 <tr> 元素 
	Textarea  : 代表 <textarea> 元素 
	
	第七天 继续讲解DOM(重点讲XML DOM)
====================================================================
一、HTML的DOM
---------------------------------------------------------
	Object  : 代表 <Object> 元素 
	Option  : 代表 <option> 元素 
	Select 	: 代表 HTML 表单中的选择列表 
	Style 	: 代表单独的样式声明 
	Table 	: 代表 <table> 元素 
	TableData : 代表 <td> 元素 
	TableRow  : 代表 <tr> 元素 
	Textarea  : 代表 <textarea> 元素 
	
二、XML的DOM
---------------------------------------------------------
	DOM （Document Object Model） 文档对象模型
	1. document 文档  HTML XML 文件 （标记语言)
	 <body>
		<div>
			<!--  -->
			<a href="#">wwww</a>
		</div>
	 </body>
	 节点：
		将文档想成一个倒树， 每一个部分（根、元素、文本（内容）， 属性， 注释）都是一节点。
		根据 DOM，HTML 文档中的每个成分都是一个节点。

		DOM 是这样规定的：
			1. 整个文档是一个文档节点(根节点) 
			2. 每个 HTML 标签是一个元素节点 
			3. 包含在 HTML 元素中的文本是文本节点 
			4. 每一个 HTML 属性是一个属性节点 
			5. 注释属于注释节点 
			
	2. 父、子和同级节点
		节点树中的节点彼此之间都有等级关系。

		父、子和同级节点用于描述这种关系。父节点拥有子节点，位于相同层级上的子节点称为同级节点（兄弟或姐妹）。
			1. 在节点树中，顶端的节点成为根节点 
			2. 根节点之外的每个节点都有一个父节点 
			3. 节点可以有任何数量的子节点 
			4. 叶子是没有子节点的节点 
			5. 同级节点是拥有相同父节点的节点 
		
		只要知道一个节点， 按关系找到其它节点
			父节点：   parentNode
			子节点（第一个， 最后一个） childNodes    firstChild   lastChild
			同胞（同辈）节点 （上一个， 下一个）nextSibling   previousSibling

	3。 获取节点的方式：
		array  getElementsByTagName("节点名"); //获取所对应节点名（所有），返回的是数组
		object getElementById("id名"); //获取id名的唯一节点对象
		
		示例：(找节点)
			document.getElementsByTagName("li"); //所有所有li节点
			document.getElementById("lid"); //获取id值为lid的唯一节点
			document.getElementById("uid").getElementsByTagName("li"); 
			//获取id值为uid中所有li子节点
			document.getElementsByTagName("ul")[0].getElementsByTagName("li"); 
			//获取第一个ul节点中所有li子节点
			
		获取到的标记名(多个)、 id（唯一）、 name（多个）
		
	4. 每个节点中的内容
			节点类型nodeType、节点名nodeName，节点值nodeValue 
		
		节点名nodeName：
			nodeName 是只读的 
			元素节点的 nodeName 与标签名相同 
			属性节点的 nodeName 是属性的名称 
			文本节点的 nodeName 永远是 #text 
			文档节点的 nodeName 永远是 #document 
			
		节点值nodeValue 
			元素节点的 nodeValue 是 undefined 
			文本节点的 nodeValue 是文本自身 
			属性节点的 nodeValue 是属性的值 
		
		nodeType（节点类型）
		     元素类型		节点类型
				元素			1
				属性			2
				文本			3
				注释			8
				文档			9

			
	 4. Object 对象 （HTML元素 转成的对象(js对象)）
	注意： 如果使用js操作HTML文档， 就需要选将HTML文档结构转成Js对象
		a. 操作属性: 
			nodeName（节点名称） 
			nodeValue（节点值） 
			nodeType（节点类型）
			其他属性：（针对于节点）
				childNodes 返回节点到子节点的节点列表。
				firstChild 返回节点的首个子节点。
				lastChild 返回节点的最后一个子节点。
				nextSibling 返回节点之后紧跟的同级节点。
				previousSibling 属性可返回某节点之前紧跟的节点（处于同一树层级）				
				parentNode 返回节点的父节点。 
				textContent设置或返回节点及其后代的文本内容。
					
		b. 操作内容
			innerText(IE) textContent(FF) //获取的是显示的内容，不包含HTML标签
			innerHTML //获取的是显示的内容，会包含HTML
			outerText
			outerHTML
			表单
			   value
		c. 操作样式
			aobj.style.backgroundColor="red";
			aobj.style.fontSize="3cm";
			className
			aobj.className="test";
			aobj.className+=" demo";
			aobj.className="";
		e. 操作节点：
			appendChild() 	向节点的子节点列表的结尾添加新的子节点。
			cloneNode()		复制节点。
			removeChild()	删除（并返回）当前节点的指定子节点。
			replaceChild() 	用新节点替换一个子节点。
			hasAttributes() 判断当前节点是否拥有属性。  
			hasChildNodes() 判断当前节点是否拥有子节点。 
			insertBefore()  在指定的子节点前插入新的子节点。

		f. 创建节点：
			* createElement() 创建元素节点 
			  createAttribute() 来创建属性节点  可以：元素节点.属性名=值；
			  createTextNode() 来创建新的文本节点 可以：元素节点.innerHTML=文本内容；

		有了以上三点的操作之前先转成对象
		转成对象的两种形式：
		 1.  标记名(多个)、 id（唯一）、 name（多个）
		 	document中的三个方法
			var objs=document.getElementsByTagName("div"); //获取多个
			var objs=document.getElementById("one");	//获取一个
			var objs=document.getElementsByName("two");

			
			

==================================================================
	1.Document
	
	2.Element
	
	3.Event
	
	4.HTMLElement
	
	5.Node
	
	6.XMLHttpRequest 
	
	
	第八天  Ajax
===========================================================
AJAX
---------------------------------------
  var xmlhttp;
 
 1. 创建请求对象
	if(window.XMLHttpRequest){
		// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}else{
		// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
 
 2. 设置回调函数（监听）
	xmlhttp.onreadystatechange=函数名；
	或
	xmlhttp.onreadystatechange=function(){
		函数体。。。
	}

 3. 初始化：
	xmlhttp.open("GET","gethint.php?q="+str,true); //异步以get方式发送到gethint.php
	
 4. 发送：
	xmlhttp.send();
	
	
其中：xmlhttp请求对象：
  **属性：
    *readyState  //请求状态：0,1,2,3,4
	*responseText//响应内容
	responseXML //xml响应对象
	*status	//浏览器响应状态：200正常， 404 请求地址不存在 ,,
	statusText //状态内容
	*onreadystatechange //回调函数属性
	
  方法：
	abort() //取消当前响应，关闭连接并且结束任何未决的网络活动。
	getAllResponseHeaders() //把 HTTP 响应头部作为未解析的字符串返回。
	getResponseHeader() //返回指定的 HTTP 响应头部的值
	*open()	//初始化 HTTP 请求参数
	*send() //发送 HTTP 请求，使用传递给 open() 方法的参数
	*setRequestHeader() //向一个打开但未发送的请求设置或添加一个 HTTP 请求。

模拟POST提交代码：
	xmlhttp.open("POST","ajax_test.php",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send("fname=Bill&lname=Gates");
		
			