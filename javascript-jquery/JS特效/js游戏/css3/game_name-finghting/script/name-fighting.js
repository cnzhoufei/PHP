/*
*for game - name-fighting
*create @ 2011.12.23
*by ajccom
*qq:136157536
*email:136157536@qq.com
*/
var debug = debug || {};
debug = {
	log : function (t) {
		if(window.console){
			console.log(t);
		}
	}
};
var NF = NF || {};
NF = {
	data : {
		actor : {
			'0' : {
				able : {
					name : '',
					att : 0,
					def : 0,
					spd : 0,
					hp : 0,
					intro : '',
					face : 'def.gif'//0-10 10套
				},
				status : 'n',//分别是[n]ormal,[i]njured,[l]ost,[w]in
				currentHp : 0
			},
			'1' : {
				able : {//[0-100]
					name : '',
					att : 0,
					def : 0,
					spd : 0,
					hp : 0,
					intro : '',
					face : 'def.gif'//0-10 10套
				},
				status : 'n',//分别是[n]ormal,[i]njured,[l]ost,[w]in
				currentHp : 0
			}
		},
		otherDate : {
			intro : {
				num :10,
				'0' : 'intro0',
				'1' : 'intro1',
				'2' : 'intro2',
				'3' : 'intro3',
				'4' : 'intro4',
				'5' : 'intro5',
				'6' : 'intro6',
				'7' : 'intro7',
				'8' : 'intro8',
				'9' : 'intro9'
			},
			face : {
				imgPath : 'img/face/'
			//	faceSetStyle : 0,//0-使用背景利用position定位表情，1-使用单独的gif图像显示表情
			},
			fightingDesc : {
				num : 10,
				'0' : '一顿拳打脚踢, 共造成',
				'1' : '狠狠蹂躏了顿, 共造成',
				'2' : '扔了一袋三鹿奶粉,他乐呵呵的吃了起来, 造成',
				'3' : '施放了炎龙斩, 共造成',
				'4' : '放了个屁，共造成',
				'5' : '施放了奥义-连牙断空, 共造成',
				'6' : '送了一张动车票, 共造成',
				'7' : '送了个飞吻, 共造成',
				'8' : '邮寄了一个炸弹, 共造成',
				'9' : '使用了爆菊战法, 共造成'
			}
		}
	},
	common : {
		ua : navigator.userAgent,
		isWebKit : function () {
			return this.ua.indexOf('webkit') > (-1) ? true : false;
		},
		getAble : function (id) {
			return NF.data.actor[id].able;
		},
		getName : function (id) {
			return NF.data.actor[id].able.name;
		},
		getFightDescOption : function () {
			return NF.data.otherDate.fightingDesc;
		},
		setName : function (id, str) {
			NF.data.actor[id].able.name = str;
		},
		getIntroOption : function () {
			return NF.data.otherDate.intro;
		},
		getFaceOption : function () {
			return NF.data.otherDate.face;
		},
		getHp : function (id) {
			return NF.data.actor[id].able.hp;
		},
		setAble : function (id, str) {
			var s = str || 'a', able = this.getAble(id), intro = this.getIntroOption(), face = this.getFaceOption(), ables = ['att', 'def', 'spd', 'hp', 'intro','face'], current;
			for(var i = ables.length; i--;){
				able[ables[i]] = (str.charCodeAt(i%str.length)+i*5+2)%100;
				current = able[ables[i]];
				if(current <= 10 ){
					able[ables[i]] = current + 15;
				}
			}
			if(able.hp <= 20){
				able.hp = able.hp * 2;
			}
			able.name = str;
			able.intro = intro[able.intro%intro.num];
			able.face = face.imgPath + able.face%10 + '/face.gif';
			NF.ui.dataReady = true;
		},
		restart : function () {
				//var time = +new Date();
				var name0 = $('#actor0-name').val(), name1 = $('#actor1-name').val();
				if(NF.ui.nameReady !== true){/*console.log('请正确输入姓名');*/return}
				NF.state.contextBox.text('');
				this.setAble(0 , name0);
				this.setAble(1 , name1);
				NF.ui.setFace(0, 'n');
				NF.ui.setFace(1, 'n');
				NF.ui.setAble(0);
				NF.ui.setAble(1);
				NF.state.ready();
				//console.log('create:' + (+new Date()-time) + 'ms');
		},
		_bind : function (ele){
			var that = this;
			ele = typeof ele === 'string' ? $(ele) : ele;//ele instanceof jQuery
			ele.bind('click', function () {that.restart()});
		},
		ini : function () {
			this._bind('#start');
		}
	},
	state : {
		firstActor : 0,
		currentActor : 0,//0或者1，代表当前活动的角色
		round : 0,
		contextBox : null,
		actBtn : null,
		ready : function () {
			var that = this;
			var actor0 = NF.common.getAble(0), actor1 = NF.common.getAble(1), current = (actor0.spd >= actor1.spd ? 0 : 1), next = (current === 0 ? 1 : 0);
			that.round = 0;
			that.firstActor = current;
			that.currentActor = current;
			that.fight(current, next);
			that.actBtn.unbind('click').addClass('disable');
		},
		end : function (current , next) {
			this.showReport('', '', '', '<div>战斗结束</div>');
			NF.ui.setFace(current, 'w');
			NF.ui.setFace(next, 'l');
			this.firstActor = 0;
			this.currentActor = 0;
			this.round = 0;
			this.actBtn.bind('click', function () {NF.common.restart()}).removeClass('disable');
		},
		showReport : function (actCurrentName, actNextName, harmNum ,txt) {
			var conBox = $('#act-content .content'), otherDesc = parseInt(Math.random()*2, 10) ===1 ? true : false, parent = $('#act-content');
			txt = txt || '';
			this.round++;
			if(actCurrentName ==='' && actNextName === '' && harmNum === ''){
				conBox.append(txt);
			} else {
				if(otherDesc){
					var fd = NF.common.getFightDescOption();
					useFd = fd[parseInt(Math.random()*10, 10)%fd.num];
					conBox.append('<div>第'+this.round+'回合,<span class="green">'+actCurrentName+'</span>对<span class="red">'+actNextName+'</span>'+ useFd +'<span class="red">'+harmNum+'</span>伤害'+(txt === '' ? '' : ','+txt)+'</div>');
				} else {
					conBox.append('<div>第'+this.round+'回合,哇塞<span class="green">'+actCurrentName+'</span>对<span class="red">'+actNextName+'</span>造成了<span class="red">'+harmNum+'</span>伤害'+(txt === '' ? '' : ','+txt)+'</div>');
				}
			}
			debug.log('conBox.height()' + conBox.height() + '//parent.height():' + parent.height());
			//if(conBox.height() > parent.height()){
				//如果超出输出框...
			//}
		},
		fight : function (current, next) {
			var that = this;
			var act = setTimeout(function () {
				//var time = +new Date();
				/*console.log('current:'+current);*/
				NF.ui.setFace(current, 'n');
				NF.ui.setFace(next, 'i');
				var ableC = NF.common.getAble(current), ableN = NF.common.getAble(next), bonus2 = false, bonus3 = false;
				var harm = parseInt((ableC.att/ableN.def)*10, 10) + Math.round(Math.pow(-1,parseInt(Math.random()))*Math.random()*5);
				if(Math.round(Math.random()*10) <= 2){
					var random = Math.round(Math.random()*10);
					if(random >= 6){
						harm = harm * 2;
						bonus2 = 2;
					} else {
						harm = harm * 3;
						bonus3 = 3;
					}
				}
				if(harm <= 0){
					harm = 0;
					that.showReport('', '', '', '<div><span class="green">' + ableC.name + '</span><span class="red">攻击失误！！！</span></div>');
				}
				ableN.hp = ableN.hp - harm;
				if(ableN.hp <= 0){
					NF.ui.setHp(next, 0);
					that.showReport(ableC.name, ableN.name, harm, (bonus2 ? '2倍伤害！！！' : (bonus3 ? '3倍伤害！！！' :''))+'<span class="green">胜利的是' + ableC.name + '</span>');
					clearTimeout(act);
					that.end(current, next);
					//console.log('out~');
					return false;
				} else{
					NF.ui.setHp(next, ableN.hp);
					that.showReport(ableC.name, ableN.name, harm, (bonus2 ? '2倍伤害！！！' : (bonus3 ? '3倍伤害！！！' :'')));
				}
				current = next === 0 ? 0 : 1;
				next = current === 0 ? 1 : 0;
				/*console.log('next:'+current);*/
				that.fight(current, next);
				//console.log('fight:' + (+new Date()-time));
			},2000);
		},
		ini : function () {
			this.contextBox = $('#act-content .content');
			this.actBtn = $('#start');
		}
	},
	ui : {
		dataReady : false,
		uiReady : function () {
			$('body').addClass('ready');
			return true;
		},
		nameReady : false,
		reload : function () {
			$('body').removeClass('ready');
		},
		setFace : function (current , status) {
			/*status = n , i , l , w*/
			var common = NF.common;currentAble = common.getAble(current), face = currentAble.face, ele = $('#actor' + current + '-able'), faceEle = ele.find('.face');;
			//faceEle.css('background-image',face);//图片齐全后开放
			faceEle.removeClass('n i l w');
			faceEle.addClass(status);
		},
		placeHold : function (ele, t) {
			var that = this;
			ele = typeof ele === 'string' ? $(ele) : ele;
			ele.val(t);
			ele.addClass('def');
			ele.focus(function () {
				var ele = $(this);
				ele.addClass('focus');
				if(ele.val() !== t){
					ele.removeClass('def');
				} else {
					if(ele.hasClass('def')){
						ele.val('');
						ele.removeClass('def');
					}
				}
			});
			ele.blur(function () {
				var ele = $(this),val = ele.val();
				if(val !== t && val !== ''){
					ele.removeClass('def');
					that.nameReady = true;
				} else {
					ele.val(t);
					ele.addClass('def');
				}
				ele.removeClass('focus');
			});
		},
		setClass : function (eles, num, lv1, lv2) {
			var parent = eles.parent();
			if(typeof num !== 'number'){/*console.log('setClass传入参数num类型错误，您传入了一个'+(typeof num)+'类型的参数,值：'+num);*/return}
			if(parent.hasClass('hp') || parent.hasClass('att') || parent.hasClass('def') || parent.hasClass('spd')){
				if(num >= lv1){
					eles.removeClass('yellow').removeClass('red').addClass('green');
				} else {
					if(num < lv1 && num >= lv2){
						eles.removeClass('green').removeClass('red').addClass('yellow');
					} else {
						if(num < lv2){
							eles.removeClass('yellow').removeClass('green').addClass('red');
						}
					}
				}
			}
		},
		setHp : function (id, hp) {
			var hpStatus, ele = $('#actor' + id + '-able .hp span'), eles = $('#actor' + id + '-able .hp em, #actor' + id + '-able .hp span');
			eles.text(hp);
			this.setClass(eles, hp, 70, 40);
			ele.animate({'width' : (hp/100)*ele.parent().width()+'px'},500);
		},
		setAble : function (id) {
			if(this.dataReady === true){
				var able = NF.common.getAble(id), ele = $('#actor' + id + '-able'), eles = $('#actor' + id + '-able span, #actor' + id + '-able em'), ables = ['att', 'def', 'spd', 'hp', 'intro','face'];
				ele.find('.name').text(able.name);
				for(var i = ables.length; i--;){
					var parent = ele.find('.' + ables[i]);
					var current = parent.children();
					current.text(able[ables[i]]);
					if(parent.find('span')[0]){
						var span = parent.find('span');
						span.css('width', (able[ables[i]]/100)*parent.width()+'px');
					}
					this.setClass(current, able[ables[i]], 70, 40);
				}
			}
			this.uiReady();
		},
		ini : function () {
			this.placeHold('#actor0-name,#actor1-name', '请输入名字');
		}
	},
	ini : function () {
		this.common.ini();
		this.state.ini();
		this.ui.ini();
	}
};
$(function(){
	NF.ini();
});