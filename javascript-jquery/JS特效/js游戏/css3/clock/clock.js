var log = function (t) {
	if(window.console) {
		console.log(t);
	}
};
var clock = {
	moz : '-moz-transform',
	wkt : '-webkit-transform',
	trans : '',
	ini : function () {
		if(!$.browser.mozilla && !$.browser.webkit) {log('browser error, need Webkir or Mozilla'); return false;}
		this.setTrans();
		this.getStart();
		this.runTime();
	},
	setTrans : function () {
		this.trans = $.browser.mozilla ? this.moz : this.wkt;
	},
	getStart : function () {
		var cur = new Date(), hour = cur.getHours(), hour = hour >= 12 ? hour-12 : hour, min = cur.getMinutes(), sec = cur.getSeconds(), hourDeg = hour * 30, minDeg = min * 6, secDeg = sec * 6, fix;
		this.hour = $('.hour');
		this.min = $('.min');
		this.sec = $('.sec');
		fix = parseInt(minDeg/360 * 30, 10);
		hourDeg = this.getDeg(this.hour) + fix;
		hourDeg = hourDeg >= 360 ? 0 : hourDeg;
		this.setDeg(this.hour, hourDeg);
		this.setDeg(this.min, minDeg);
		this.setDeg(this.sec, secDeg);
	},
	setDeg : function (ele, deg) {
		ele = typeof ele === 'string' ? $(ele) : ele;
		deg = typeof deg === 'string' ? deg : deg+'deg';
		ele.css(this.trans, 'rotate(' + deg + ')');
		ele.css(this.trans, 'rotate(' + deg + ')');
	},
	getDeg : function (ele) {
		ele = typeof ele === 'string' ? $(ele) : ele;
		var deg = 0, cur = new Date(), hour = cur.getHours();
		switch (ele.attr('class')) {
			case 'sec' : deg = cur.getSeconds() * 6;
			break;
			case 'min' : deg = cur.getMinutes() * 6;
			break;
			case 'hour' : deg = (hour >= 12 ? hour-12 : hour) * 30;
			break;
		};
		return deg;
	},
	runTime : function () {
		var that = this, sec = this.sec, min = this.min, hour = this.hour, secDeg, minDeg, hourDeg, fix;
		setTimeout(function () {
			secDeg = that.getDeg(sec) + 6;
			//secDeg = secDeg >= 360 ? 0 : secDeg;
			if(secDeg >= 360) {
				secDeg = 0;
				minDeg = that.getDeg(min) + 6;
				minDeg = minDeg >= 360 ? 0 : minDeg;
				fix = parseInt(minDeg/360 * 30, 10);
				hourDeg = that.getDeg(hour) + fix;
				hourDeg = hourDeg >= 360 ? 0 : hourDeg;
				that.setDeg(hour, hourDeg);
				that.setDeg(min, minDeg);
			}
			that.setDeg(sec, secDeg);
			that.runTime();
		}, 1000);
	}
};

$(function () {
	clock.ini();
});