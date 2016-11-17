/*
*for game - canvas-mouse
*create @ 2012.01.29
*by ajccom
*qq:136157536
*email:136157536@qq.com
*/
var log = function (t) {
	if(window.console){
		console.log(t);
	}
};
var canvasMouse = {
	ele: null,
	context: null,
	wrap: null,
	currentFont: {
		src: 'img/font.png',
		size: ''
	},
	currentImgSize: {
		x: 44,
		y: 32
	},
	offset: {
		left: 0,
		top: 0
	},
	ini: function () {
		this.getWrap();
		this.getCanvas();
		this._bind();
	},
	getWrap: function () {
		this.wrap = $('#main-wrap');
		this.offset = $('#main-wrap').offset();
	},
	getCanvas: function () {
		var draw = document.getElementById('draw');
		this.ele = draw;
		if(draw.getContext){
			this.context = draw.getContext('2d');
		} else {
			this.context = false;
		}
	},
	mousePos: function(e){
		var x,y;
		var e = e||window.event;
		return {
			x:e.clientX,
			y:e.clientY
		};
	},
	draw: function (e, ox, oy, img, imgx, imgy) {
		var ctx = this.context, client = this.mousePos(e), x = client.x - ox, y = client.y - oy;
		//log(x + '///' + y);
		//if(ctx !== false){
			//ctx.beginPath();
			ctx.moveTo(x, y);
			ctx.drawImage(img,x-10,y-10, imgx, imgy);
			//ctx.arc(x, y, 5, 0,Math.PI*2);
			//ctx.stroke();
			//ctx.fillStyle = '#000';
			//ctx.fill();
		//}
	},
	clear: function () {
		var ctx = this.context;
		ctx.clearRect(0,0,1000,500);
	},
	_bind: function () {
		var ctx = this.context, that = this, ele = this.ele, ox = this.offset.left, oy = this.offset.top, img =new Image();
		if(ctx !== false){
			ele = ele instanceof jQuery ? ele : $(ele);
			ele.mousedown(function (event) {
				var imgSize = that.currentImgSize;
				img.src=that.currentFont.src;
				log(imgSize);
				ele.bind('mousemove', function (event) {
					that.draw(event, ox, oy, img, imgSize.x, imgSize.y);
					//log(event.clientX + '//' +event.clientY);
				});
			});
			ele.mouseup(function () {
				ele.unbind('mousemove');
				//log('unbind');
			});
		}
		
		$('.fonts a').click(function () {
			var size = $('.size').val(), reg = /^\d+$/g;
			that.currentFont.src = $(this).find('img').attr('src');
			$('.fonts a').removeClass('current');
			$(this).addClass('current');
			size = (reg.test(size)) ? size : 44;
			that.currentImgSize = {
				'x': size,
				'y': ($(this).find('img').height() / $(this).find('img').width()) * size
			}
		});
		
		$('.clear-canvas').click(function(){
			that.clear();
		});
		
		$('.size').blur(function () {
			var size = $(this).val(), reg = /^\d+$/g, currentImg = $('.fonts a.current').find('img');
			size = (reg.test(size)) ? size : 44;
			that.currentImgSize = {
				'x': size,
				'y': (currentImg.height() / currentImg.width()) * size
			}
		
		});
		
	}
};
$(function(){
	canvasMouse.ini();
});