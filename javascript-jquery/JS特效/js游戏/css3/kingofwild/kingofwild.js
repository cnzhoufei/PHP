var log = function (t) {
	if(window.console){
		console.log(t);
	}
};

var KOW = {
	round: 0,//回合
	currentPlayer: 0,
	currentChess: null,
	ini: function () {
		this.createMap();
		this.iniChess();
		this._bind();
	},
	data: {
		chess: {
			length: 8,
			clas: ['mou', 'cat', 'fox', 'dog', 'leo', 'tig', 'lio', 'ele'],
			'8': {//象
				text: '象',
				lv: 8,
				cla: 'ele',
				river: 2,//2 - 走过， 1 - 跳过， 0 - 不能过
				loc: [[7, 3], [1, 7]]
			},
			'7': {//狮
				text: '狮',
				lv: 7,
				cla: 'lio',
				river: 1,
				loc: [[1, 1], [7, 9]]
			},
			'6': {//虎
				text: '虎',
				lv: 6,
				cla: 'tig',
				river: 1,
				loc: [[7, 1], [1, 9]]
			},
			'5': {//豹
				text: '豹',
				lv: 5,
				cla: 'leo',
				river: 0,
				loc: [[3, 3], [5, 7]]
			},
			'4': {//狗
				text: '狗',
				lv: 4,
				cla: 'dog',
				river: 0,
				loc: [[2, 2], [6, 8]]
			},
			'3': {//狐
				text: '狐',
				lv: 3,
				cla: 'fox',
				river: 0,
				loc: [[5, 3], [3, 7]]
			},
			'2': {//猫
				text: '猫',
				lv: 2,
				cla: 'cat',
				river: 0,
				loc: [[6, 2], [2, 8]]
			},
			'1': {//鼠
				text: '鼠',
				lv: 1,
				cla: 'mou',
				river: 2,
				loc: [[1, 3], [7, 7]]
			}
		},
		map: {
			size: [7, 9],
			trap: {
				loc: [[3, 1], [5, 1], [4, 2], [4, 8], [3, 9], [5, 9]],
				cla: 'trap',
				text: '穴'
			},
			river: {
				loc: [[2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [5, 4], [5, 5], [5, 6], [6, 4], [6, 5], [6, 6]],
				cla: 'river',
				text: ''
			},
			home: {
				loc: [[4, 1], [4, 9]],
				cla: 'home',
				text: '巢'
			}
		},
		player: {
			'0': {
				cla: 'blue'
			},
			'1': {
				cla: 'red'
			}
		}
	},
	getMap: function (args) {
		var map = this.data.map;
		if(args === 'trap'){
			return map.trap;
		}
		if(args === 'river'){
			return map.river;
		}
		if(args === 'home'){
			return map.home;
		}
		return {
			'x': map.size[0],
			'y': map.size[1],
			'trap': map.trap,
			'river': map.river,
			'home': map.home
		};
	},
	getChess: function (args) {//可以使用 lv\中文文字\class类名 查询
		var chess = this.data.chess, len = chess.length, i = 0;
		if(typeof args === 'number') {
			return chess[args];
		}
		if(args === 'clas') {
			return chess.clas;
		}
		if(typeof args === 'string') {
			for(i = len; i--;){
				if(chess[i].text === args || chess[i].cla === args){
					return chess[i];
				}
			}
		}
		return chess;
	},
	getPlayer: function (args) {
		if (args === 1 || args === 0) {
			return this.data.player[args];
		}
		return this.data.player;
	},
	createMap: function () {
		var map = this.getMap(), mapX = map.x, mapY = map.y, trapLoc = map.trap.loc, riverLoc = map.river.loc, homeLoc = map.home.loc, html = '', i = 1, j = 1, z = 0, locs = $.merge($.merge(trapLoc.slice(0), riverLoc), homeLoc), locsLen = locs.length, cla = '', trapCla = map.trap.cla, riverCla = map.home.cla, homeCla = map.river.cla, text = '', trapTxt = map.trap.text, riverTxt = map.home.text, homeTxt = map.river.text;
		this.map = $('.map');
		for (i = 1; i <= mapY; i++) {
			for (j = 1; j <= mapX; j++) {
				cla = '';
				text = '';
				for(z = 0; z < locsLen; z++) {
					if(locs[z][0] === j && locs[z][1] === i){
						if(this.isInArray(locs[z], trapLoc)){
							cla = trapCla;
							text = trapTxt;
						} else {
							cla = '';
							if(this.isInArray(locs[z], homeLoc)){
								cla = riverCla;
								text = riverTxt;
							} else {
								cla = '';
								if(this.isInArray(locs[z], riverLoc)){
									cla = homeCla;
									text = homeTxt;
								}
							}
						}
					}
				}
				html += '<div class="x'+ j +' y'+ i +' '+ cla +'">'+ text +'</div>';
			}
		}
		this.map.html(html);
	},
	isInArray: function (val, arr) {
		var len = arr.length, i = 0, j = 0, vlen = 0, hit = 0;
		if($.isArray(val)){
			for(i = len; i--;){
				if(!$.isArray(arr[i])){
					return false;
				}
				if (val.length === arr[i].length) {
					vlen = val.length;
					for (j = vlen; j--;){
						if(val[j] === arr[i][j]){
							hit++;
						}
					}
					if (hit === vlen) {
						return true;
					} else {
						hit = 0;
					}
				}
			}
		} else {
			for(i = len;i--;){
				if (val === arr[i]) {
					return true;
				}
			}
		}
		return false;
	},
	iniChess: function () {
		var chess = this.getChess(), chessLen = chess.length, currentChess, currentChessLocLen, currentChessLocX, currentChessLocY, player = this.getPlayer(), playerCla = [player[0].cla, player[1].cla], html = '', size = this.getMap(), i, j, own = '';
		this.control = $('.control');
		this.control.find('div').remove();
		for (i = 1; i <= size.y; i++) {
			for (j = 1; j <= size.x; j++) {
				html += '<div class="x'+ j +' y'+ i +'"></div>';
			}
		}
		this.control.append(html);
		//摆放棋子
		for (i = chessLen; i > 0; i--) {
			currentChess = chess[i];
			currentChessLocLen = currentChess.loc.length;
			for (j = currentChessLocLen; j--;) {
				currentChessLocX = currentChess.loc[j][0];
				currentChessLocY = currentChess.loc[j][1];
				currentChessLocY >= 4 ? own = playerCla[1] : own = playerCla[0];		
				this.control.find('.x' + currentChessLocX + '.y' + currentChessLocY).append('<span class="chess '+ own +' '+ currentChess.cla +'">'+ currentChess.text +'</span>');
			}
		}
		
		this.control.find('.x4.y9').addClass(playerCla[1]);
		this.control.find('.x4.y1').addClass(playerCla[0]);
	},
	runRound: function () {
		this.round += 1;
		this.currentPlayer = (this.currentPlayer + 1) % 2;
	},
	showMask: function (ele, x, y) {
		var contain = $('.control'), mapContain = $('.map'), river = 0, riverType = 0, riverLoc = [], i, riverLocLen = 0, tempCla = '';
		ele = typeof ele === 'string' ? $(ele) : ele;
		mapContain.find('.unmove').remove();
		contain.find('div').removeClass('hit');
		mapContain.find('div').append('<div class="unmove"></div>');
		riverType = this.getChessByElement(ele, 'river');
		
		tempCla += '.x'+x+'.y'+y+', .x'+(x - 1)+'.y'+y +', .x' + (x + 1) + '.y' + y + ', .x' + x +'.y' + (y + 1) + ', .x' + x + '.y' + (y - 1) + ' , ';
		mapContain.find(tempCla).find('.unmove').remove();
		contain.find(tempCla).addClass('hit');
		
		if (riverType === 0) {
			this.fixMask(tempCla);
		}
		if (riverType === 1) {//2 - 走过， 1 - 跳过， 0 - 不能过
			if(this.jump(ele, x, y, 'check')) {
				river = this.jump(ele, x, y, 'getLoc');
				riverLocLen = river.length;
				if(riverLocLen > 0) {//river = [[1,2],[3,4]]
					for(i = (riverLocLen - 1); i >= 0; i--) {
						tempCla += '.x' + river[i][0] + '.y' + river[i][1] + ', ';
					}
					this.fixMask(tempCla);
				}
			} else {
				this.fixMask(tempCla);
			}
		}
		
	},
	hideMask: function () {
		var contain = $('.control'), mapContain = $('.map');
		contain.find('div').removeClass('hit');
		mapContain.find('.unmove').remove();
	},
	fixMask: function (claString) {
		var contain = $('.control'), mapContain = $('.map');
		mapContain.find(claString).find('.unmove').remove();
		contain.find(claString).addClass('hit');
		if(mapContain.find(claString).hasClass('river')){
			var tempHit = mapContain.find(claString);
			tempHit.each(function () {
				if($(this).hasClass('river')){
					//log($(this));
					claString = '.' + $.trim($(this).attr('class').split('river')[0]).replace(' ', '.');
					//log(claString + '/////');
					$(this).find('.unmove').remove();
					$(this).append('<div class="unmove"></div>');
					contain.find(claString).removeClass('hit');
				}
			});
		}
	},
	_bind: function () {
		var that = this;
		$('.chess').bind('click', function () {
			var currentLoc = that.getChessCurrentLoc($(this));
			if(that.getChessOwnByElement($(this)) === that.getPlayer(that.currentPlayer).cla){
				that.showMask($(this), currentLoc.x, currentLoc.y);
				that.currentChess = $(this);
			}
			//log(that.currentChess);
		});
		$('.hit').live('click', function () {
			that.move($(this));
		});
		$('.control .x4.y9, .control .x4.y1').bind('click', function () {
			var own = that.getPlayer(that.currentPlayer).cla;
			that.move($(this));
			if(!$(this).hasClass(own)) {
				that.gameEnd();
				setTimeout(function () {
					that.reset();
				}, 3000);
			}
		});
	},
	_unbind: function () {
		$('.hit').die();
		$('.chess, .control .x4.y9, .control .x4.y1').unbind();
	},
	move: function (ele) {
		var tempLocChess = null, result = false;
		ele = typeof ele === 'string' ? $(ele) : ele;
		if(ele.find('.chess')[0]){
			tempLocChess = ele.find('.chess');
			if(this.getChessOwnByElement(tempLocChess) === this.getPlayer(this.currentPlayer).cla){
				return false;
			} else {
				result = this.fight(this.currentChess, tempLocChess);
				if(result){
					tempLocChess.remove();
					ele.append(this.currentChess);
					this.moveEnd();
				}
			}
		} else {
			//log(that.currentChess);
			ele.append(this.currentChess);
			this.moveEnd();
		}
	},
	moveEnd: function () {
		this.hideMask();
		this.runRound();
	},
	gameEnd: function () {
		alert('game over');
		this._unbind();
	},
	reset: function () {
		this.currentPlayer = 0;
		this.round = 0;
		this.iniChess();
		this._bind();
	},
	jump: function (ele, x, y, args) {
		var contain = $('.control'), river = this.getMap('river'), riverCla = river.cla, riverLoc = river.loc, chessLoc = [x, y], d = '', riverStart = [x, y], riverEnd = 0, riverHeight = 3, riverWidth = 2, endLocEle = null, tempLocChess = null;
		ele = typeof ele === 'string' ? $(ele) : ele;
		if(this.isInArray([x+1, y], riverLoc)) {
			d += 'x + ';
			riverEnd = [x+riverWidth, y];
		}
		if (this.isInArray([x-1, y], riverLoc)){
			d += 'x - ';
			riverEnd = [x-riverWidth, y];
		}
		if (this.isInArray([x, y+1], riverLoc)) {
			d = 'y +';
			riverEnd = [x, y+riverHeight];
		}
		if(this.isInArray([x, y-1], riverLoc)) {
			d = 'y -';
			riverEnd = [x, y-riverHeight];
		}
		if(args === 'getLoc') {
			return this.checkJump(d, riverStart, 'getLoc');
		}
		if(args === 'check') {
			if(this.checkJump(d, riverStart)){
				return true;
			} else {
				return false;
			}
		}
		if (this.checkJump(d, riverStart)) {
			endLocEle = contain.find('.x'+ riverEnd[0] +'.y'+ riverEnd[1]);
			if(endLocEle.find('.chess')[0]){
				tempLocChess = endLocEle.find('.chess');
				if (this.getChessOwnByElement(ele) !== this.getChessOwnByElement(tempLocChess)) {
					if(this.fight(ele, tempLocChess)) {
						endLocEle.append(ele);
					}
				}
			}
		}
	},
	checkJump: function (d, start, args) {
		var contain = $('.control'), dir = d.split(' ')[0], sum = d.split(' ')[1], x = 2, y = 3, i = 0, loc = [];
		if(d.length > 5){
			dir = 'x';
			sum = '+-';
		}
		if (dir === 'x' && sum === '-'){
			for (i = x; i >= 0; i--) {
				start = [start[0] - 1, start[1]];
				loc.push(start);
				if (contain.find('.x' + start[0] + '.y' + start[1]).find('.chess')[0] && i !== 0) {
					return false;
				}
			}
			if(args === 'getLoc') {
				return loc;
			}
			return true;
		}
		if (dir === 'x' && sum === '+'){
			for (i = x; i >= 0; i--) {
				start = [start[0] + 1, start[1]];
				loc.push(start);
				if (contain.find('.x' + start[0] + '.y' + start[1]).find('.chess')[0] && i !== 0) {
					return false;
				}
			}
			if(args === 'getLoc') {
				return loc;
			}
			return true;
		}
		if (dir === 'y' && sum === '-'){
			for (i = y; i >= 0; i--) {
				start = [start[0], start[1] - 1];
				loc.push(start);
				if (contain.find('.x' + start[0] + '.y' + start[1]).find('.chess')[0] && i !== 0) {
					return false;
				}
			}
			if(args === 'getLoc') {
				return loc;
			}
			return true;
		}
		if (dir === 'y' && sum === '+'){
			for (i = y; i >= 0; i--) {
				start = [start[0], start[1] + 1];
				loc.push(start);
				if (contain.find('.x' + start[0] + '.y' + start[1]).find('.chess')[0] && i !== 0) {
					return false;
				}
			}
			if(args === 'getLoc') {
				return loc;
			}
			return true;
		}
		if (dir === 'x' && sum === '+-'){
			for (i = x; i >= 0; i--) {
				start = [start[0] - 1, start[1]];
				loc.push(start);
				if (contain.find('.x' + start[0] + '.y' + start[1]).find('.chess')[0] && i !== 0) {
					return false;
				}
			}
			
			start = [(start[0] + x + 1), start[1]];
			for (i = x; i >= 0; i--) {
				start = [start[0] + 1, start[1]];
				loc.push(start);
				if (contain.find('.x' + start[0] + '.y' + start[1]).find('.chess')[0] && i !== 0) {
					return false;
				}
			}
			if(args === 'getLoc') {
				return loc;
			}
			
			return true;
		}
		if(args === 'getLoc') {
			return [];
		}
	},
	fight: function (ele, tempLocChess) {
		var eleLv = this.getChessByElement(ele, 'lv'), tempLocChessLv = this.getChessByElement(tempLocChess, 'lv'), tempLocChessLoc = this.getChessCurrentLoc(tempLocChess);
		ele = typeof ele === 'string' ? $(ele) : ele;
		tempLocChess = typeof tempLocChess === 'string' ? $(tempLocChess) : tempLocChess;
		if($('.map').find('.x'+ tempLocChessLoc.x + '.y' + tempLocChessLoc.y).hasClass('trap')){
			tempLocChess.remove();
			return true;
		} else {
			if(eleLv >= tempLocChessLv) {
				if(eleLv === 8 && tempLocChessLv === 1) {
					return false;
				}
				tempLocChess.remove();
				return true;
			} else {
				if (eleLv === 1 && tempLocChessLv === 8) {
					tempLocChess.remove();
					return true;
				}
				return false;
			}
		}
	},
	getChessByElement: function (ele, args) {
		var clas = this.getChess('clas'), len = clas.length, i, detail = '';
		ele = typeof ele === 'string' ? $(ele) : ele;
		if(args === 'lv') {
			for (i = len; i > 0; i--) {
				if (ele.hasClass(clas[i-1])) {
					return i;
				}
			}
		}
		if(args === 'river') {
			for (i = len; i > 0; i--) {
				if (ele.hasClass(clas[i-1])) {
					return this.getChess(i).river;
				}
			}
		}
		
	},
	getChessCurrentLoc: function (ele) {
		var x = 0, y = 0, clas = '';
		ele = typeof ele === 'string' ? $(ele) : ele;
		clas = ele.parent().attr('class');
		x = parseInt(clas.split('x')[1].split('y')[0], 10);
		y = parseInt(clas.split('y')[1].split(' ')[0], 10);
		return {
			'x': x,
			'y': y
		};
	},
	getChessOwnByElement: function (ele) {
		var playerCla = this.getPlayer();
		ele = typeof ele === 'string' ? $(ele) : ele;
		if (ele.hasClass(playerCla[0].cla)) {
			return playerCla[0].cla;
		} else {
			return playerCla[1].cla;
		}
	}
};

$(function(){
	KOW.ini();
});