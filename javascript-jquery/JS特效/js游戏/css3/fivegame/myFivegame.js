var log = function (t) {
	if(window.console){
		console.log(t);
	}
};

var fivegame = {
	layout: null,
	context: null,
	control: null,
	currentPlayer: 0,
	ini: function () {
		this.getEle();
		this.createLayout(this.option.xNum,this.option.yNum);
		this.setFirstPlayer();
		this._bind();
	},
	getEle: function () {
		this.layout = $('#layout');
		this.context = $('#context');
		this.control = $('#option');
	},
	floMiddle: function (xNum, yNum) {
		var winWidth = $(window).width();
		this.layout.css({
			'width': (xNum + 1)*20 +'px',
			'height': (yNum + 1)*20 +'px',
			'left': (winWidth/2 - (xNum + 1)*10) + 'px'
		});
		this.context.css({
			'width': xNum * 20 +'px',
			'height': yNum * 20 +'px',
			'left': (winWidth/2 - xNum*10 - 10) + 'px'
		});
		this.control.css({
			'width': (xNum + 1)*20 +'px',
			'margin-left': (winWidth/2 - (xNum + 1)*10) + 'px'
		});
	},
	createLayout: function (xNum, yNum) {
		var _div = [], _span = [], i = 0, j = 0, spanleng = xNum * yNum, divleng = (xNum+1)*(yNum+1), html = '';
		this.floMiddle(xNum, yNum);
		for(i = divleng; i > 0; i--){
			html += '<div class="div"></div>';
		}
		this.layout.html(html);
		html = '';
		
		for(j=0; j< spanleng; j++){
			html += '<span class="x' + j%xNum + ' y' + parseInt(j/xNum, 10) + '"></span>';
		}
		this.context.html(html);
	},
	option: {
		xNum: 35,
		yNum: 30,
		firstPlayer: 0,
		timeout: 30,//30秒未动则超时
		player: {
			'0': {
				chess: '白',
				cla: 'white',
				name: '小明',
				first: false
			},
			'1': {
				chess: '黑',
				cla: 'black',
				name: '小红',
				first: true
			}
		}
	},
	setOption: function (args) {
		jQuery.extend(this.option, args);
	},
	setPlayer: function (args) {
		jQuery.extend(this.option.player, args);
	},
	setFirstPlayer: function () {
		this.currentPlayer = this.option.player[0].first === true ? 0 : 1;
	},
	_bind: function () {
		var that = this;
		$('#context').find('span').click(function () {
			that.chess($(this));
		});
	},
	_unbind: function () {
		$('#context').find('span').unbind();
	},
	chess: function (ele) {
		var cla = this.option.player[this.currentPlayer].cla, x = 0, y = 0, eleCla = ele.attr('class');
		if(!ele.hasClass('white') && !ele.hasClass('black')){
			ele.addClass(cla);
			x = eleCla.split('x')[1].split(' ')[0];
			y = eleCla.split('y')[1].split(' ')[0];
			this.check(cla, parseInt(x, 10), parseInt(y, 10));
			this.currentPlayer = this.currentPlayer === 1 ? 0 : 1;
		}
	},
	check: function (cla, x, y) {//根据坐标判断是否有5子相连
		var i = 0, h=v=c1=c2=hu=vu=c1u=c2u= 1, temph=tempv=tempc1=tempc2= 0; //h - 水平方向，v - 垂直方向，c1 - -45度角斜线，c2 - 45度角斜线，u表示反向
		//log('sssh:'+h + ' cla:'+cla);
		for(i = 1; i <= 5; i++){
			if($('.x' + (x + i) + '.y' + y).hasClass(cla)) {
				h += 1;
			} else {
				temph += h;
				break;
			}
		//	log('h:'+h);
		}
		for(i = 1; i <= 5; i++){
			if($('.x' + (x - i) + '.y' + y).hasClass(cla)) {
				hu += 1;
			} else {
				temph += (hu - 1);
				break;
			}
		}
		
		for(i = 1; i <= 5; i++){
			if($('.x' + x + '.y' + (y + i)).hasClass(cla)) {
				v += 1;
			} else {
				tempv += v;
				break;
			}
		}
		for(i = 1; i <= 5; i++){
			if($('.x' + x + '.y' + (y - i)).hasClass(cla)) {
				vu += 1;
			} else {
				tempv += (vu - 1);
				break;
			}
		}
		
		for(i = 1; i <= 5; i++){
			if($('.x' + (x + i) + '.y' + (y + i)).hasClass(cla)) {
				c1 += 1;
			} else {
				tempc1 += c1;
				break;
			}
		}
		for(i = 1; i <= 5; i++){
			if($('.x' + (x - i) + '.y' + (y - i)).hasClass(cla)) {
				c1u += 1;
			} else {
				tempc1 += (c1u - 1);
				break;
			}
		}
		
		for(i = 1; i <= 5; i++){
			if($('.x' + (x - i) + '.y' + (y + i)).hasClass(cla)) {
				c2 += 1;
			} else {
				tempc2 += c2;
				break;
			}
		}
		for(i = 1; i <= 5; i++){
			if($('.x' + (x + i) + '.y' + (y - i)).hasClass(cla)) {
				c2u += 1;
			} else {
				tempc2 += (c2u - 1);
				break;
			}
		}
		log(tempc2);
		if (h >= 5 || v >= 5 || c1 >= 5 || c2 >= 5 || hu >= 5 || vu >= 5 || c1u >= 5 || c2u >= 5 || temph >= 5 || tempv >= 5 || tempc1 >= 5 || tempc2 >= 5) {
			if(h > 5 || v > 5 || c1 > 5 || c2 > 5 || hu > 5 || vu > 5 || c1u > 5 || c2u > 5 || temph > 5 || tempv > 5 || tempc1 > 5 || tempc2 > 5){
				this.outNum();
			} else {
				log(h +'||'+ v +'||'+c1 +'||'+ c2 +'||'+ hu +'||'+ vu+'||'+ c1u +'||'+ c2u +'||'+ temph +'||'+ tempv +'||'+ tempc1 +'||'+ tempc2);
				this.win();
			}
		}
	},
	outNum: function () {
		alert('too much! 超过5个可是算输得哦');
		this.lost();
	},
	win: function () {
		this._unbind();
		alert('you win');
	},
	lost: function () {
		this._unbind();
	},
	start: function () {
		this.clear();
		this._bind();
	},
	clear: function () {
		this.context.find('span').removeClass('white black');
	}
};
var webSocketIO = {
	socket: null,
	ini: function () {
		this.socket = new WebSocket('ws://localhost:8080/websocket/fivegame');
	},
	_bind: function (socket, event) {
		socket.onopen = function(event) {
			log('create handle socket');

			// 监听消息
			socket.onmessage = function(event) {
				log('Client received a message',event);
			};

			// 监听Socket的关闭
			socket.onclose = function(event) {
				log('Client notified socket has closed',event);
			};

			// 关闭Socket....
			//socket.close()
		};
	},
	
};

$(function(){
	//webSocketIO.ini();
	fivegame.ini();
});