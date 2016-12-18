


http://www.cnblogs.com/superangle/archive/2011/09/22/jQuery.html --整理资料
//临时存储数据
	$('#des').data ('key','val');


//相对于同辈元素的位置，下标从0开始
	alert($('#des').index());


get方法不传参数，会返回一个纯数组
	var res = obj.get();

 //释放$符号，意味着，这行以后不能用$来调用了
    var j = $.noConflict();




  // alert($('p').length);
    // 就是获取length属性的值
    // alert($('p').size());




  $('p').each(function(i){
			//这是最常用的对象转换
			$(this).html('test' + i);
		});


内容里面包含hello的指定元素
    // $('p:contains('+ val +')').css('color', 'red');




  没有后代的元素
    // $('p:empty').css('border', '5px solid red');


  //匹配的是当了爹的元素
    // $('p:parent').css('border', '5px solid red');
//匹配后代里面包含指定选择器的p元素
    $('p:has(.des)').css('border', '5px solid red');






   //匹配ul下面的大儿子li（符合大儿子身份的li）
    // $('ul li:first-child').css('color', 'red');

    // 符合小儿子身份的li
    // $('ul li:last-child').css('color', 'red');

    //符合2儿子身份的li（找的是第几个li，下标从1开始）
    // $('ul li:nth-child(2)').css('color', 'red');

    //符合独生子身份的li
    $('ul li:only-child').css('color', 'red');


    

    $('p').css('fontSize','20px').last().css('color','red');//所有p标签字体20px 最后一个变红

    $('p').css('fontSize','20px').first().css('color','red');//所有p标签字体20px 第一个变红

    $('p').css('fontSize','20px').eq(-2).css('color','red');//所有p标签字体20px 第-2个变红



//检测第一个p标签中是否有 class等于red的有则返回ture
    var res = $('p').eq(1).hasClass('red');//这个不用加点('red')
	var res = $('p').eq(1).is('.red');//这个要加点('.red');




判断 存在删除  不存在就添加
	$('p').click(function(){
		if($(this).hasClass('red')){
			//移除class
			$(this).removeClass('red');
		}else{
			//添加一个class
			$(this).addClass('red');
		}
	})


	//从当前集合中保留出符合filter条件的
	$('p').filter('.red').css('color','blue');


	//从当前集合中干掉符合not条件的
	$('p').not('.red').css('color','blue');//除了not()选中的



	/切割：下标从0开始（包含前面的，不包含后面的）从哪里到哪里
$('p').slice(2,5).css('color','red');//




//匹配后代中有i的p标签
    // $('p').has('i').css('color', 'red');
    // $('p:has(i)').css('color', 'red');


//给所有按钮绑定一个单击事件 然后手动循环 在把值用逗号链接起来
    $('button').click(function(){
	var obj = $(':checked').map(function(){
		return $(this).val();
	}).get().join(',');
	alert(obj);
})


//下一个同辈元素
$('#test').next().next().css('color','red');

//从#test开始 后面的所有同辈元素
// $('#test').nextAll().css('color','red');	


从#test开始到.stop为止 不包含.stop
$('#test').nextUntil('.stop').css('color','red');	




//parents()         找祖宗，找到html就没了
    //parentsUntil()    到啥啥啥为止，不包含啥啥啥

    //childrent()       //所有的儿子，找不到孙子

    //find()    在所有的后代中查找某个元素
    // $('body').find('i').html('呵呵呵');


 //向上找祖宗，找到离自己最近的那个符合条件的
    $('#des').closest('div').attr('title', 'hello');


//选中所有p标签 字体改为20px并且给p标签添加一个class=red
    $('p').css('fontSize','20PX').add('.red').css('color','red');



	//andSelf() 将自己也添加到当前集合中
	$('#des').siblings().css('color','red').andSelf().css('fontSize','30px');




    //addClass()    removeClass()   toggleClass()   店长推荐



  //val() 获取表单域（原生JS要用value属性来获取的）的值
    alert($('input').val());



    //获取这些值之后不能再进行连贯操作了，因为返回的不是JQ对象了，而是一个数字
    //width()   height()   本身的宽高，不包含边框和内边距
    //innerHeight()  innerWidth()   包含内边距，不包含边框
    //outerHeight()  outerWidth()   包含内边距和边框（常用）
    //scrollTop([val])  scrollLeft() 获取或者设置滚动条的位置（没有兼容性问题）

    //offset()  获取元素的top值和left值
    //返回值：Object {top: 10, left: 20}
    // $('#box').offset().left
    // $('#box').offset().top


  siblings//选中同辈元素除了自己







/*********************** 文档处理 ***********************/
/*************************** 1.创建节点 ***************************/
	var box = $('<div id="box"></div>').html('hello');
	var box = $('<div id="box">我是JQ创建的DIV</div>');
	
/*************************** 2.内部插入 ***************************/
	//添加到最后
	$('body').append(box);
	box.prependTo('body');

	//添加到最前
	$('body').prepend(box);
	box.prependTo('body');


/*********************** 3.外部插入（兄弟节点） ***********************/
	//添加到某某的后面
	$('#des').after(box);
	box.insertAfter('#des');


	//添加到某某的前面
	$('#des').before(box);
	box.insertBefore('#des');

/*********************** 4.包裹 ***********************/
	//穿外套
	$('li').wrap('<div></div>');
	$('p').wrapAll('<div></div>');
	$('li').wrapAll('<div></div>');


	//穿内衣
	$('li').wrapInner('<div></div>');


	//unwrap()脱衣服，一次只能脱一件，脱到body就脱不动了



/*********************** 5.删除 ***********************/
	$('#des').remove();
	$('#des').detach();//这个也是删除

	$('p').click(function(){
		// alert(1);
	})

	//删除之后再添加回来，会保留原来的事件
	$('#des').remove().appendTo('body');
	$('#des').detach().appendTo('body');
	$('html').empty();//清空所有内容

/*********************** 6.替换 ***********************/
	//整个替换，而不是只替换标签
	$('#des').replaceWith(box);
	box.replaceAll('#des');

/*********************** 7.克隆 ***********************/
	$('#des').appendTo('body');
	$('#des').clone().appendTo('body');


	//传个参数true，会携带着事件一起克隆
	$('#des').clone(true).appendTo('body');




/*========================= 、事件列表。 =========================*/



(一)、事件列表。

　　1.blur()　　　　　　当失去焦点时触发。包括鼠标点击离开和TAB键离开。

　　2.change()　　　　  当元素获取焦点后，值改变失去焦点事触发。

　　3.click()　　　　　 当鼠标单击时触发。

　　4.dblclick()　　　　当鼠标双击时触发。

　　5.error()　　　　　 当javascript出错或img的src属性无效时触发。

　　6.focus()　　　　   当元素获取焦点时触发。注意：某些对象不支持。

　　7.focusin()　　　   当元素或其子元素获取焦点时触发，与focus()
                        区别在于能够检测其内部子元素获取焦点的情况。

　　8.focusout()　　　  当元素或者其子元素失去焦点时触发，与focusout()
                        区别在于能够检测内部子元素失去焦点的情况。　

　　9.keydown()　　		当键盘按下时触发。

　　10.keyup()　　　　	当按键松开时触发。

　　11.mousedown()　　　当鼠标在元素上点击后触发。

　　12.mouseenter()　　 当鼠标在元素上穿过时触发。
						mouseenter与mouseover的区别是，
						鼠标从mouseover的子元素上穿过时也会触发而mouseenter不会。

　　13.mouseleave()　　	当鼠标从元素上移出时触发。

　　14.mousemove()　　　 当鼠标在元素上移动时触发。
						 .clientX 和 .clientY分别代表鼠标的X坐标与Y坐标。

　　15.mouseout()　　　　当鼠标从元素上移开时触发。

　　16.mouseover()　　　 当鼠标移入元素时触发。

　　17.mouseup()　　　　 当鼠标左键按下释放时触发。

　　18.resize()　　　　　当浏览器窗口大小改变时触发。
						 $(window).resize();

　　19.scroll()　　　　　当滚动条发生变化时触发。

　　20.select()　　　　　当input里的内容被选中时触发。

　　21.submit()　　　　　提交选中的表单。

　　22.unload()　　　　　当页面卸载时触发。　　

(二)、事件常用方法

　　　　1、绑定事件

　　　　语法：bind(type,[data],fn)　　type参数可以是顶部的22个方法
		(注意：不能带括号); 参数data是属性值传递给事件对象的额外数据，
		fn是处理函数。可以bind多个事件，也可以为同一事件绑定多个函数。

　　　　$("#div1").bind("change",function(){ alert("你好！"); })

　　　　$("#div1").bind("click mouseout",function(){ alert("你好！"); })



　　　　2、切换事件

　　　　　 语法：hover(fn1,fn2);　鼠标移入执行第一个函数，鼠标移出执行第二个函数。
		   相当于mouseenter与mouseleave。

　　　　　　　　$("#div1").hover(function(){alert("鼠标移入我啦");},
				function(){alert("鼠标移出我啦!");})

　　　　3、顺序执行事件

　　　　　 语法：toggle(fn1,fn2,fn3...)　 当鼠标单击时，依次执行绑定的事件

　　　　　　　　$("#div1").toggle(function(){alert(1);},function(){alert(2);},
				function(){alert(3);})

　　　　4、unbind 移除事件

　　　　　 语法：unbind([type],[fn])　　　　 移除元素已经绑定的事件,type：指定要移除的事件，fn指定要移除的方法。当没有参数时，所有的事件都移除。注意，用live()方法绑定的方法移出不了，live()绑定的方法要用它自己的die()来移出。

　　　　　　　　$(":button").unbind();　　 移除按钮的所有事件。

　　　　　　　　$(":button").unbind("click");　　 移除按钮的单击事件。

　　　　　　　　$(":button").unbind("click",fn1);　　 移除按钮的单击事件中的fn1函数，如果该事件绑定了多个函数，对其他函数没影响。

　　　 5、one 仅执行一次的事件

　　　　　　语法：one(type,[data],fn)　　　　绑定一个仅执行一次的事件

　　　　　　　　$("#div1").one("click",function(){ alert("我只执行一次!"); })

　　　　6、trigger DOM加载完毕后自动执行的事件

　　　　　　语法：trigger(type,[data])　　　　DOM元素加载完成后自动执行

　　　　　　$("#div1").bind("bclick",function(){ alert("你好"); });

　　　　　　$("#div1").trigger("bclick");　　　　//注意，trigger一定要放在绑定的事件之后，否则不执行。

　　　　7、live() DOM根节点绑定事件

　　　　　　语法：live(type,[fn])　　　　　String,Function

　　　　　　　　　live(type,[data],false) String,Array,bool

　　　　　　live()在根节点绑定事件，通过事件冒泡到DOM根节点($(ducoment))，再对比触发事件的元素来判断事件是否应该执行。效率不高，因此不能完全替代bind()但是有个好处，就是后期加载出来的元素同样能够绑定。但是有个缺点，就是live()方法仅仅能使用CSS选择器选择被绑定元素。

　　　　　　如$('a').live('click', function(){alert("你好!");})　　JQuery把alert函数绑定到$(document)元素上，并使用’click’和’a’作为参数。任何时候只要有事件冒泡到document节点上，它就查看该事件是否是一个click事件，以及该事件的目标元素与’a’这一CSS选择器是否匹配，如果都是的话，则执行函数。

　　　　　　live(type,data,fn)　

　　　　　　$("#div1").live("click",function(){ alert("你好"); })　　//即使页面一开始不存在id="div1"的元素，是后期AJAX或js加载上去的，但是依然有效。　

　　　　　　$("#div1").live("click mouseout",function(){ alert("你好"); })　 //可以live()多个事件。　

　　　　8、die() 解除live()方法绑定的事件　　//绑定与解除是对应的，die()解除不了bind()和delegate绑定的方法。 可以为一个元素live多个事件，也可以为同一事件live多个函数。

　　　　　　语法die(type,[fn])　　string Function其中Function为可选方法。

　　　　　　$("#div1").die();

　　　　　　$("#div1").die("click");

　　　　　　$("#div1").die("click",fn1);　　//其中fn1为某函数名。如果是绑定的是一个匿名函数，第二个参数用于当为同一事件live了多个函数的时候，解除一个函数对其他函数没影响。

　　　　9、delegate() 为指定的元素添加一个或多个事件，并绑定处理函数，一个事件也可以绑定多个函数。注意：此函数要1.4.2版添加。delegate()允许在父元素中将时间绑定当前页面还未的元素，这点与Live()类似，但是即使是$(document).delegate()也比live()方法的效率要高，另外delegate()还能将尚未出现的元素绑定到离它更近的父元素上。

　　　　　　语法：

　　　　　　delegate(selector,[type],fn)　　　　String String Function　　//selector必须为所选元素的子元素

　　　　　　delegate(selector,[type],[data],fn) String String Object Function

　　　　　　delegate(selector,events)　　　　　 String String

　　　　　　如：

　　　　　　$('#container').delegate('a', 'click', function() { alert("你好!") }); 
　　　　　　JQuery扫描文档查找$(‘#container’)，并使用click事件和’a’这一CSS选择器作为参数把alert函数绑定到$(‘#container’)上。任何时候只要有事件冒泡到$(‘#container’)上，它就查看该事件是否是click事件，以及该事件的目标元素是否与CCS选择器相匹配。如果两种检查的结果都为真的话，它就执行函数。

　　　　　　$("#div1").delegate("#button1","click",function(){ alert("你好啊！"); });　　//注意：#button1必须为#div1的子元素

　　　　10、undelegate()　 删除有delegate()函数绑定的一个或多个事件处理函数

　　　　　　语法：

　　　　　　undelegate(selector,[type])　　　　String String

　　　　　　undelegate(selector,[type],fn)　　 String String Function

　　　　　　undelegate(selector,events)　　　　String String

　　　　　　undelegate(namespace)　　　　　　String

　　　　 11、ready()　　当DOM元素加载完成后绑定处理事件

　　　　　　$(document).ready()


ready　　当DOM元素加载完成后绑定处理事件

$('button').off('click');清楚事件

一次性事件
		$('button').one('click',function(){
			alert(2);
		})

//事件委派：动态产生的元素，只要匹配该选择器，都能拥有该事件
$('button').live('click',function(){
				$('<button>后妈生的</button>').appendTo('body');

				$('button').die('click');
			})

//给子元素委派事件
			$('body').delegate('button','click',function(){
				$('<button>后妈生的</button>').appendTo('body');

				//取消delegate的事件委派
				$('body').undelegate('button','click');
			})



//阻止事件冒泡
$('#die').on('click',function(){
		alert('大的');
	})

	$('#son').on('click',function(e){
		alert('小的');

		//阻止事件冒泡 同样可以阻止浏览器默认行为
		return false;
		
	})




//专门用于触发事件的
	$('#son').trigger('click');
	$('#fom').trigger('submit');

//也是用来触发事件的，但是默认会阻止事件冒泡和浏览器默认行为
	$('#son').triggerHandler('click');
	$('#fom').triggerHandler('submit');



//循环执行你传进去的函数
		$('button').toggle(function(){
			alert('满足你');
		},function(){
			alert('再来');
		},function(){
			alert('还要');
		},function(){
			alert('够了没有');
		})



//动画效果

$('button:first').on('click',function(){
		$('#die').show(3000,function(){
			alert('显示完毕');//动画执行完毕之后会执行这个回调函数
		})//往左角收缩

		$('#die').slideDown(1000,'easeOutBounce');//从上往下掉  要用到easing.js插件

		$('#die').fadeIn(3000);//淡入淡出
	}).next().on('click',function(){
		隐藏
		$('#die').hide(1000);
		$('#die').slideUp(1000,'easeOutBounce');

		$('#die').fadeOut(1000);

	}).next().on('click',function(){
		 $('#die').slideToggle(1000);

		$('#die').fadeToggle(1000);
	}).next().on('click',function(){
		$('#die').fadeTo(1000,0.5);
	})



//自定义动画
$('button:first').on('click', function(){
        //animate({CSS集合}, 时间)
        //.delay(2000) 延时执行下一步动画
        $('#die').animate({'top':'400px'}, 1000).animate({'left':'500px'},1000).animate({'top':'40px'}, 1000).animate({'left':'20px'}, 1000);
    }).next().on('click', function(){
        //第一个参数，是否清楚队列
        //第二个参数，是否立即完成当前动画
        $('#die').stop(true, true);
    })
    //.delay(2000) 延时执行下一步动画



    //ajax

    // $.get('./ajax.php?id=2',{'name':'jack','age':18},function(res){
	// 	alert(res);
	// 	alert(res.name);
	// },'json')

	// $.post('./ajax.php?id=1',{'name':'jack','age':18},function(res){
	// 	alert(typeof res);
	// },'json')


	$.getJSON('./ajax.php',function(res){
		alert(res.name);
	})




	function check(){
		//自动将表单里面的表单域序列化为id=5&name=jack格式
		var res = $('#fom').serialize()

		return false;
	}
	


	$.ajax({
		url:'ajax.php',//请求的URL地址
		type:'post',//请求的方式
		data:'id=5&name=jack',//要传的参数，data有两种传参格式
		//data:{name:'jack',age:18},
		//dataType:'json',//返回的数据的格式（不要骗它）
		//async:true,//true：异步     false：同步
		jsonp:'hehe',//指定get里面回调函数的下标
        // jsonpCallback: 'haha',  //指定函数名
		success:function(res){
			alert(typeof res);
		},error:function(){
			alert('请求失败');
		}

	})



滚动式获取滚动条离顶部的高度
$(window).scroll( function() { 
    
  var st = $(this).scrollTop();
console.log(st);



   } );


   获取某个元素当前离顶部的距离
   mTop = $('#mdiv')[0].offsetTop;
    sTop = $(window).scrollTop();
    result = mTop - sTop;
    console.log(result);




    
alert($(window).height()); //浏览器时下窗口可视区域高度
alert($(document).height()); //浏览器时下窗口文档的高度
alert($(document.body).height());//浏览器时下窗口文档body的高度
alert($(document.body).outerHeight(true));//浏览器时下窗口文档body的总高度 包括border padding margin
alert($(window).width()); //浏览器时下窗口可视区域宽度
alert($(document).width());//浏览器时下窗口文档对于象宽度
alert($(document.body).width());//浏览器时下窗口文档body的高度
alert($(document.body).outerWidth(true));//浏览器时下窗口文档body的总宽度 包括border padding margin

alert($(document).scrollTop()); //获取滚动条到顶部的垂直高度
alert($(document).scrollLeft()); //获取滚动条到左边的垂直宽度 