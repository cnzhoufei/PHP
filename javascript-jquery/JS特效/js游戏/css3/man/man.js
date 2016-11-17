var log = function (t) {
	if(window.console){
		console.log(t);
	}
};

var man = {
	time: null,
	boomBirthTime: null,
	ini: function () {
		this._bindDrag(document.querySelector('.man'));
		this._bindBoxDrop(document.querySelector('.box'));
	},
	addTime: function () {
		var that = this;
		this.time = setTimeout(function () {
			$('.time span').text(parseInt($('.time span').text(), 10)+1);
			that.addTime();
		},1000);
	},
	createBoom: function () {
		var that = this;
		this.boomBirthTime = setTimeout(function () {
			that.letItMove();
			that.createBoom();
		}, (25 + Math.random()*100));
	},
	letItMove: function () {
		var b = $('.box').offset(), rX = Math.random()*1000, rY = Math.random()*500, birthX = 0, birthY = 0, deadX = 0, deadY = 0, boom = null;
		if(Math.round(Math.random()) === 0){//x-random
			birthX = rX;
			deadX = Math.random()*1000;
			if(Math.round(Math.random()) === 0){
				birthY = 0;
				deadY = 500;
			} else {
				birthY = 500;
				deadY = 0;
			}
		} else {
			if(Math.round(Math.random()) === 0){
				birthX = 0;
				deadX = 1000;
			} else {
				birthX = 1000;
				deadX = 0;
			}
			birthY = rY;
			deadY = Math.random()*500;
		}
		boom = document.createElement('div');
		$(boom).addClass('boom').css({
			'top': birthY,
			'left': birthX
		});
		$(boom).animate({left: deadX, top: deadY}, 2000, function () {
			$(this).remove();
		});
		$(boom).appendTo('.box');
		this._bindBoomDrop(boom);
	},
	start: function () {
		log('s');
		$('.time span').text(0);
		$('.msg').text('');
		this.addTime();
		this.createBoom();
	},
	end: function () {
		clearTimeout(this.time);
		clearTimeout(this.boomBirthTime);
		log('game over');
		$('.msg').text('ƒ„º·≥÷¡À'+ $('.time span').text() +'√Î');
	},
	_bindDrag: function (ele) {
		var that = this;
		ele.onselectstart = function() {
			ev.preventDefault();
			return false;
		};
		ele.ondragstart = function(ev) {
			ev.dataTransfer.effectAllowed = "move";
			ev.dataTransfer.setData("text", '');
			ev.dataTransfer.setDragImage(document.querySelector('.man'), 15, 15);
			that.start();
			return true;
		};
		ele.ondragend = function(ev) {
			$('.man').css({
				'display': 'block'
			});
			return false;
		};
	},
	_bindBoxDrop: function (ele) {
		var that = this;
		ele.ondragover = function(ev) {
			ev.preventDefault();
			return true;
		};
		ele.ondragleave = function(ev) {
			//that.end();
			return true;
		};
		ele.ondragenter = function(ev) {
			//log('enter');
			$('.man').css({
				'display': 'none'
			});
			return true;
		};
		ele.ondrop = function(ev) {
			that.end();
			//log('drop');
			return false;
		};
	},
	_bindBoomDrop: function (ele) {
		var that = this;
		ele.ondragover = function(ev) {
			ev.preventDefault();
			log('game over: touch boom!!!');
			return true;
		};
		ele.ondragleave = function(ev) {
			log('game over: touch boom!!!');
			return true;
		};
		ele.ondragenter = function(ev) {
			that.end();
			$('.box').css('background-color', '#000');
			setTimeout(function () {
				$('.box').css('background-color', '#fff');
			}, 100);
			log('game over: touch boom!!!');
			return true;
		};
		ele.ondrop = function(ev) {
			log('game over: touch boom!!!');
			return false;
		};
	}
};

$(function(){
	man.ini();
});