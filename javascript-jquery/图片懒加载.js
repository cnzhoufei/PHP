window.Echo = (function(window, document, undefined) {
    'use strict';
    var store = [],
    offset,
    throttle,
    poll;
    var _inView = function(el) {
        var coords = el.getBoundingClientRect();
        return ((coords.top >= 0 && coords.left >= 0 && coords.top) <= (window.innerHeight || document.documentElement.clientHeight) + parseInt(offset));
    };
    var _pollImages = function() {
        for (var i = store.length; i--;) {
            var self = store[i];
            if (_inView(self)) {
                self.src = self.getAttribute('data-echo');
                store.splice(i, 1);
            }
        }
    };
    var _throttle = function() {
        clearTimeout(poll);
        poll = setTimeout(_pollImages, throttle);
    };
    var init = function(obj) {
        var nodes = document.querySelectorAll('[data-echo]');
        var opts = obj || {};
        offset = opts.offset || 0;
        throttle = opts.throttle || 250;
        for (var i = 0; i < nodes.length; i++) {
            store.push(nodes[i]);
        }
        _throttle();
        if (document.addEventListener) {
            window.addEventListener('scroll', _throttle, false);
        } else {
            window.attachEvent('onscroll', _throttle);
        }
    };
    return {
        init: init,
        render: _throttle
    };
})(window, document);


// <img src="/style/images/loading-1.gif"  data-echo="/ueditor/php/upload/image/20171216/1513436596530001.jpg"/>

// Echo.init({
//     offset: 0,
//     throttle: 0
// });

##########自定义
function loadimg(){
    height = window.innerHeight;
    imgdata = $('[data-src]')
    for(i = 0;i < imgdata.length;i++){
        sTop = $(window).scrollTop();//滚动条顶部高度
        mtop = $(imgdata[i]).offset().top;//当前元素位置
        activity = mtop - sTop;
        if (activity < (height - 120) && activity > 50){
            $(imgdata[i]).attr('src',$(imgdata[i]).attr('data-src'))
        }
    }
}
window.onscroll=function(){ 

loadimg()
}