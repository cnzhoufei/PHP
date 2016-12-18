function getAjax(url,func){
	var ajax = new XMLHttpRequest();

		ajax.open('get',url,true);

		ajax.send();

		ajax.onreadystatechange = function(){

			if(ajax.readyState == 4 && ajax.status == 200){

				var res = ajax.responseText;

				func(res);
			}
		}
}



getAjax('ajax.php',function(res){

});


//将数组转换成json格式
	//json_encode($arr);

//将json字符串转换为数组
    //json_decode('json格式的字符串', true);
