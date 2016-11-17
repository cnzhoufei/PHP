var log = function (t) {
	if(window.console) {
		console.log(t);
	}
};

var locDb = {
	score : 100,
	name : 'player',
	wait : 1,
	visitDb : function () {
		var shortnames = 'scoreDB',version = '1.0', displaynames = 'score', maxSize = 65536;
		try {
			boom.db = openDatabase(shortnames,version,displaynames,maxSize);
		} catch(e){  //尝试捕获错误
			if (e == 2){
				log('Invalid database version.');
			} else {
				log("Unknown error "+e+".");
			}
		}
	},
	createTable : function () {
		var db = boom.db;
		if(db){
			db.transaction(
				function (transaction){
					transaction.executeSql(
					'CREATE TABLE IF NOT EXISTS scoreTable (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT, score INTEGER);', function (transaction, error){//errorHandle
						log('Error was: '+ error.message +'(Code:'+ error.code +')');
					});
				}
			);
		}
	},
	loadScore : function (fn) {
		var db = boom.db, highScore = 0, names = 'names', that = this;
		if(db){
			db.transaction(
				function (transaction){
					transaction.executeSql(
					'SELECT * FROM scoreTable order by score DESC;', [], function (transaction, results) {
							if(results.rows.item(0)){
								highScore = results.rows.item(0).score;
								names = results.rows.item(0).name;
								that.score = highScore;
								that.name = names;
							//	log(that.score + '//' +that.name);
								if(typeof fn === 'function'){
									fn([that.name, that.score]);
								}
							} else {
								that.score = 100;
								that.name = 'player';
								db.transaction(
									function (transaction){
										transaction.executeSql('INSERT INTO scoreTable (name, score) VALUES (?, ?);', ['player', 100]);
									}
								);
							}
							that.wait = 0;
						},
						function (transaction, error){
							log('Error was: '+ error.message +'(Code:'+ error.code +')');
						}
					);
				}
			);
		}
	},
	isGetData : function (fn, args) {
		var that = this;
		setTimeout(function () {
			if(that.wait === 0){
				args = args || null;
				if(typeof fn === 'function'){
					fn(args);
					that.wait = 1;
				}
			} else {
				that.isGetData();
			}
		},25);
	},
	saveScore : function (playernames, score) {
		var db = boom.db, currentScore = score, highScore = 0, names = playernames, that = this;
		this.loadScore();
		this.isGetData(function(){
			highScore = that.score;
			if(db && parseInt(highScore, 10) < parseInt(currentScore, 10)){
				that.score = currentScore,
				that.name = names,
				//log(that.score + '//' +that.name);
				db.transaction(
					function (transaction){
						transaction.executeSql(
						'INSERT INTO scoreTable (name, score) VALUES (?, ?);', [names, currentScore], 
						function (transaction, results) {
							boom.showHighScore([that.name, that.score]);
							alert('good,你创造了记录！');
						},
						null);
					}
				);
				db.transaction(
					function (transaction){
						transaction.executeSql('DELETE FROM scoreTable WHERE scroll=100');
					}
				);
			} else {
				log('分数不够高啊，亲。最高分：' + highScore);
			}
		});
	},
	ini : function () {
		var that = this;
		this.visitDb();
		this.createTable();
		this.loadScore(boom.showHighScore);
	}
};

var boom = {
	bed : null,//document.querySelector('.boom-bed')
	blueRoom : null,//document.querySelector('.blue')
	redRoom : null,//document.querySelector('.red')
	boomAppearTime : 3000,
	boomScore : 10,
	boomCreate : null,
	boomNum : 1,
	currentBoom : null,
	life : 3,
	scoreData : false,
	db : null,
	stateMaxBooms : 15,
	winW : $(window).width(),
	ini : function () {
		this.bed = document.querySelector('.boom-bed');
		this.blueRoom = document.querySelector('.blue');
		this.redRoom = document.querySelector('.red');
		this.checkBrowser();
		this.start();
	//	locDb.saveScore('yyy', 503)
	},
	checkBrowser : function () {
		var text = "";
		if(!window.openDatabase){
			this.scoreData = false;
			text += 'T_________T,你的浏览器无法使用本地存储，不能记录最高得分，换个chrome或者Safari吧';
			$('.info').hide();
		} else {
			this.scoreData = true;
		}
		$('.wrap').append(text);
	},
	showHighScore : function (agrs) {
		var names = agrs[0], highScore = agrs[1];
		$('.name').text(names);
		$('.high-score').text(highScore);
	},
	whichLV : function () {
		var score = this.getScore();
		if(score < 50){//LV1
			this.boomScore = 10;
			this.boomNum = 1;
			//log(1);
		}
		if(score >= 50 && score < 200) {//LV2
			this.boomScore = 20;
			this.boomNum = 2;
			//log(2);
		}
		if(score >= 200 && score < 400){//LV4
			this.boomScore = 30;
			this.boomNum = 3;
			//log(3);
		}
		if(score >= 400 && score < 800){//LV4
			this.boomScore = 40;
			this.boomNum = 4;
			//log(4);
		}
	},
	randomBoom : function () {
		var l = Math.round(Math.random()*400), t = Math.round(Math.random()*400);
		l = (l >= 360) ? l - 40 : l;
		t = (t >= 360) ? t - 40 : t;
		if(Math.round(Math.random()) === 0){
			return {
				'classes' : 'boom b',
				'title' : 'im blue',
				'left' : l,
				'top' : t
			};
		} else {
			return {
				'classes' : 'boom r',
				'title' : 'im red',
				'left' : l,
				'top' : t
			};
		}
	},
	createBoom : function () {
		var that = this;
		this.whichLV();
		this.boomCreate = setTimeout(function () {
			var i, r, ele, booms;
			for(i = that.boomNum; i > 0; i--) {
				r = that.randomBoom();
				ele = document.createElement('div');
				$(ele).attr({
					'class': r.classes,
					'draggable': true,
					'title': r.title
				}).css({
					'left': r.left,
					'top': r.top
				});
				that._bind(ele);
				that.bed.appendChild(ele);
			}
			booms = that.getStateBooms();
			that.setStateBooms(booms);
			if(booms <= that.stateMaxBooms){
				that.createBoom();
			} else {
				alert('场上炸弹太多了，GAME OVER');
				that.end();
			}
		}, this.boomAppearTime);
	},
	getStateBooms : function () {
		return $('.boom').length;
	},
	setStateBooms : function (num) {
		num = typeof num === 'number' ? num : parseInt(num, 10);
		$('.state-booms span').html(num);
	},
	_bind : function (ele) {
		var that = this, redBin = document.querySelector('.red'), blueBin = document.querySelector('.blue'), score = that.boomScore, winW = this.winW, winBleft = winW/2 - 400, winRleft = winW/2 + 200, winTop = 70;
		ele.onselectstart = function() {
			return false;
		};
		ele.ondragstart = function(ev) {
			that.currentBoom = this;
			ev.dataTransfer.effectAllowed = 'move';
			ev.dataTransfer.setData('text', '');
			ev.dataTransfer.setDragImage(this, 20, 20);
			return true;
		};
		ele.ondragend = function(ev) {
			ele = null;
			return false
		};
		redBin.ondragover = function(ev) {
			ev.preventDefault();
			return true;
		};

		redBin.ondragenter = function(ev) {
			$(this).css('opacity', 0.8);
			return true;
		};
		redBin.ondrop = function(ev) {
			var dragEle = that.currentBoom;
			$(redBin).css('opacity', 1);
			if($(dragEle).hasClass('r')){
				that.scoreText($(redBin), '<b style="color:#0f0">good, +' + score + '</b>', ev.clientX - winRleft, ev.clientY - winTop, 3000, '#ff0');
				that.setScore(score);
			} else {
				that.scoreText($(redBin), '<b style="color:#000">bad, -' + score + '</b>', ev.clientX - winRleft, ev.clientY - winTop, 3000, '#ff0');
				that.setScore('-' + score);
			}
			$(dragEle).remove();
			that.setStateBooms(that.getStateBooms());
			return false;
		};
		blueBin.ondragover = function(ev) {
			ev.preventDefault();
			return true;
		};
		blueBin.ondragenter = function(ev) {
			$(this).css('opacity', 0.8);
			return true;
		};
		blueBin.ondrop = function(ev) {
			var dragEle = that.currentBoom;
			$(blueBin).css('opacity', 1);
			if($(dragEle).hasClass('b')){
				that.scoreText($(blueBin), '<b style="color:#0f0">good, +' + score + '</b>', ev.clientX - winBleft, ev.clientY - winTop, 3000, '#ff0');
				that.setScore(score);
			} else {
				that.scoreText($(blueBin), '<b style="color:#000">bad, -' + score + '</b>', ev.clientX - winBleft, ev.clientY - winTop, 3000, '#ff0');
				that.setScore('-' + score);
			}
			$(dragEle).remove();
			that.setStateBooms(that.getStateBooms());
			return false;
		};
	},
	scoreText: function (fatEle, text, left, top, time, color) {
		//log('s');
		var div = document.createElement('div'), fatEle = typeof fatEle === 'string' ? $(fatEle) : fatEle;
		div = $(div);
		div.css({
			'position': 'absolute',
			'left': left,
			'top': top,
			'color': color,
			'z-index': 20
		});
		div.html(text);
		fatEle.append($(div));
		//log('p');
		div.animate({
			top: '-=40',
			opacity: 0
		}, time/2, function () {
			div.remove();
			//log('e');
		});
	},
	start : function () {
		var that = this;
		$('.start-btn, .player-name').removeAttr('disabled');
		$('.start-btn').click(function () {
			if($('.player-name').val() !== ''){
				that.setLife(3);
				that.setScore(0, true);
				that.setStateBooms(0);
				that.createBoom();
				$('.start-btn, .player-name').attr('disabled', 'disabled');
			} else {
				alert('请在左框中输入一个游戏名');
			}
		});
		$('.end-btn').click(function () {
			that.end();
		});
	},
	setScore : function (score, isClear) {
		var s = $('.point'), t = 0, life = 0;
		score = typeof score === 'number' ? score : parseInt(score, 10);
		isClear = isClear === true ? true : false;
		t = isClear === true ? (score) : (score + parseInt(s.text(), 10));
		if(t <= 0){
			s.text('0');
		} else {
			s.text(t);
		}
		if(score < 0){
			this.life -= 1;
			life = this.life;
			this.setLife(life);
			if(life <= 0){
				alert('GAME OVER');
				this.end();
			}
		}
	},
	getScore : function () {
		return $('.point').text();
	},
	setLife : function (life) {
		this.life = life;
		$('.life span').text(life);
	},
	end : function () {
		var name = $('.player-name').val(), score = $('.point').text(), booms = $(this.bed).find('.boom');
		$('.start-btn, .player-name').removeAttr('disabled');
		if(booms[0]){
			booms.unbind().remove();
		}
		if(this.scoreData){
			locDb.saveScore(name, score);
		}
		clearTimeout(this.boomCreate);
	}
};

$(function () {
	if(window.openDatabase){
		locDb.ini();
	}
	boom.ini();
});