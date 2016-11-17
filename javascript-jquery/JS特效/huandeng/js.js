
		var array =  ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg'];
		var path  =  './images/';
		var box = document.getElementById('box');
		var a = document.getElementById('a');
		var b = document.getElementById('b');
		var bnt = document.getElementById('bnt');
		var button = document.getElementsByTagName('button');
		var i = 1;
		var num = 1;
		function huandeng(){
			var time = setInterval(function(){
				button[i - 1].style.background = '';
				if(i >= 5)i = 0;
				box.style.background = 'url(' + path + array[i] + ') 100% 100%';
				i++;
				num = i;
				button[i - 1].style.background = '#f00';
			},2000)

			box.onmouseenter = function(){
				clearInterval(time);
				a.style.display = '';
				b.style.display = '';
			}
			box.onmouseleave = function(){
				a.style.display = 'none';
				b.style.display = 'none';
				huandeng();
			}


		/**********************数字****************************/

			button[0].onmouseenter = function(){
					clearInterval(time);
					box.style.background = 'url(' + path + array[0] + ') 100% 100%';
					button[0].style.background = '#f00';

			}
			button[0].onmouseleave = function(){
					button[0].style.background = '';
					huandeng();

			}
			button[1].onmouseenter = function(){
					clearInterval(time);
					box.style.background = 'url(' + path + array[1] + ') 100% 100%';
					button[1].style.background = '#f00';
			}
			button[1].onmouseleave = function(){
					button[1].style.background = '';
					huandeng();

			}
			button[2].onmouseenter = function(){
					clearInterval(time);
					box.style.background = 'url(' + path + array[2] + ') 100% 100%';
					button[2].style.background = '#f00';
			}
			button[2].onmouseleave = function(){
					button[2].style.background = '';
					huandeng();

			}

			button[3].onmouseenter = function(){
					clearInterval(time);
					box.style.background = 'url(' + path + array[3] + ') 100% 100%';
					button[3].style.background = '#f00';
			}
			button[3].onmouseleave = function(){
					button[3].style.background = '';
					huandeng();

			}
			button[4].onmouseenter = function(){
					clearInterval(time);
					box.style.background = 'url(' + path+ array[4] + ') 100% 100%';
					button[4].style.background = '#f00';
			}
			button[4].onmouseleave = function(){
					button[4].style.background = '';
					huandeng();

			}
			
		/**********************左箭头****************************/
			a.onmouseenter = function(){
					clearInterval(time);

				}

			window.onmousedown = function(){
				a.style.display = '';
				b.style.display = '';
				clearInterval(time);
			
			}
			window.onmouseup = function(){
				if(a.style.display) a.style.display = 'none';
				if(b.style.display) b.style.display = 'none';
				clearInterval(time);

			}

			a.onclick = function(){
				button[num - 1].style.background = '';
				a.style.display = '';
				if(num >= 5)num = 0;
				num += 1;
				box.style.background = 'url(' + path +  array[num - 1] + ') 100% 100%';
				button[num - 1].style.background = '#f00';
				console.dir(num);
				a.onmouseleave = function(){
					button[num - 1].style.background = '';
					
				}

			}

	/**********************右箭头****************************/

			b.onmouseenter = function(){
					clearInterval(time);

				}
		
			b.onclick = function(){
				button[num - 1].style.background = '';
				b.style.display = '';
				if(num <= 1)num = 6;
				num -= 1;
				box.style.background = 'url(' + path +  array[num- 1] + ') 100% 100%';
				button[num - 1].style.background = '#f00';
				console.dir(num);
				b.onmouseleave = function(){
					button[num - 1].style.background = '';
					
				}

			}

		}

		huandeng();

