
/*========================= ajax的基本操作 =========================*/

1.创建ajax对象
	var ajax = new XMLHttpRequest();

2.建立请求
	ajax.open('get','./ajax.php?id=1&name=zhoufei',true);//GET方式
	ajax.open('post',./ajax.php,true);//POST方式

3.发送请求
	ajax.send();//GET方式
	ajax.send('id=1&name=zhooufei');//POST方式

4.处理结果
	ajax.onreadystatechange = function()
	{	
		//如果ajax执行到第四步  并且浏览器状态码为200 才继续处理
		if(ajax.readyState == 4 && ajax.status == 200)
		{	
			//接收ajax带回来的数据
			var res = responseText;

			//把ajax带回来的json格式的数据转换成js格式的对象
			var obj = eave('(' + eval + ')');//方式一
			var obj = JSON.parse(res);//方式二  IE8以下不兼容

			//准备一个空变量 用来存储遍历出来的数据
			var str = '';
			for(var k in obj)
			{
				str += '<p>' + obj[k] + '</p>';
			}
				box.innerHTML = str;
		}
	}


	/******************** ajax PHP端 ********************/

	$_GET  或 $_POST  接收  php输出的类容ajax都能捕获带回

	将数组转换成json格式
		json_encode($arr);

	将json字符串转换为数组
    	json_decode('json格式的字符串', true);


   将json字符串转换成json对象
   var res = JSON.parse(msg);






