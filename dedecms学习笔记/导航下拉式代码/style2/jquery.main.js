//jQuery Cookie Plugin v1.4.0
(function(factory){if(typeof define==="function"&&define.amd){define(["jquery"],factory)}else{factory(jQuery)}}(function($){var pluses=/\+/g;function encode(s){return config.raw?s:encodeURIComponent(s)}function decode(s){return config.raw?s:decodeURIComponent(s)}function stringifyCookieValue(value){return encode(config.json?JSON.stringify(value):String(value))}function parseCookieValue(s){if(s.indexOf('"')===0){s=s.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\")}try{s=decodeURIComponent(s.replace(pluses," "))}catch(e){return}try{return config.json?JSON.parse(s):s}catch(e){}}function read(s,converter){var value=config.raw?s:parseCookieValue(s);return $.isFunction(converter)?converter(value):value}var config=$.cookie=function(key,value,options){if(value!==undefined&&!$.isFunction(value)){options=$.extend({},config.defaults,options);if(typeof options.expires==="number"){var days=options.expires,t=options.expires=new Date();t.setDate(t.getDate()+days)}return(document.cookie=[encode(key),"=",stringifyCookieValue(value),options.expires?"; expires="+options.expires.toUTCString():"",options.path?"; path="+options.path:"",options.domain?"; domain="+options.domain:"",options.secure?"; secure":""].join(""))}var result=key?undefined:{};var cookies=document.cookie?document.cookie.split("; "):[];for(var i=0,l=cookies.length;i<l;i++){var parts=cookies[i].split("=");var name=decode(parts.shift());var cookie=parts.join("=");if(key&&key===name){result=read(cookie,value);break}if(!key&&(cookie=read(cookie))!==undefined){result[name]=cookie}}return result};config.defaults={};$.removeCookie=function(key,options){if($.cookie(key)!==undefined){$.cookie(key,"",$.extend({},options,{expires:-1}));return true}return false}}));
(function($){
  $.fn.ruifoxSlide = function(options) {
    var defaults = {
      event:"click",
      speed:800,
      time:4000,
      auto:true
    };
    var settings = $.extend({}, defaults, options || {});
    var event=settings.event,speed=settings.speed,time=settings.time,auto=settings.auto;
    var slide=$(this).append('<div class="slide-btn"></div>'),slideImg=$("ul:first li",slide),slideTxt=$("div>img",slideImg),slideTxt2=$("div>.txt",slideImg),slideBtn=$(".slide-btn",slide),tabBtn=$("#why .ul-tab li");
    if(slideImg.length<2){
      return false;
    }
    slideImg.not(":first").hide();
    slideTxt.css({"margin-left":"100px","opacity":"0"});
    slideTxt2.css({"margin-left":"-100px","opacity":"0"});
    slideTxt.eq(0).animate({marginLeft:"0",opacity:1},speed);
    slideTxt2.eq(0).animate({marginLeft:"0",opacity:1},speed);
    slideImg.each(function(i){
      slideBtn.append('<a href="javascript:;">'+i+'</a>');
    });
    var slideBtnA=$("a",slideBtn);
    var curIndex=0,t;
    slideBtnA.first().addClass("cur");
    slideBtnA.bind(event,function(){
      var n=$(this).index();
      if(n==curIndex) return false;
      $.showSlide(n);
      curIndex=n;
      window.clearInterval(t);
      t=window.setInterval("$.autoSlide();",time);
    });
    if(auto)t=window.setInterval("$.autoSlide();",time);
    $.showSlide=function(i){
      slideTxt.filter(":visible").animate({marginLeft:"100px",opacity:0},speed);
      slideTxt2.filter(":visible").animate({marginLeft:"-100px",opacity:0},speed);
      slideImg.filter(":visible").stop(false,true).fadeOut(speed);
      slideImg.eq(i).stop(false,true).fadeIn(speed,function(){
        slideTxt.eq(i).stop(false,true).animate({marginLeft:"0",opacity:1},speed);
        slideTxt2.eq(i).stop(false,true).animate({marginLeft:"0",opacity:1},speed);
      });
      slideBtnA.filter(".cur").removeClass("cur");
      slideBtnA.eq(i).addClass("cur");
      i<2?tabBtn.eq(0).trigger("click",["ck"]):tabBtn.eq(1).trigger("click",[true]);
    }
    $.autoSlide=function(){
      var n=(curIndex+1)%slideImg.length;
      curIndex=n;
      $.showSlide(curIndex);
    }
  };
})(jQuery);
//jQuery ruifoxTabs Plugin v1.0.0
(function(e){e.fn.myTabs=function(t){var n={tab_tit:".tabs-tit",tab_con:".tabs-con",event:"mouseover"},r=e.extend({},n,t||{}),i=r.tab_tit,s=r.tab_con,o=r.event,u=e(this),a=e(i,u),f=e(s,u);a.eq(0).addClass("cur");a.bind(o,function(){var t=e(this).index();return a.removeClass("cur").eq(t).addClass("cur"),f.hide().eq(t).show(),!1})}})(jQuery);
var select=$(".select");
select.click(function(event){
  $("ul",select).stop(true,false).fadeOut("fast");
  $("ul",this).stop(true,false).fadeIn("fast");
  event.stopPropagation();
});
$(window).click(function(){
  $("ul",select).stop(true,false).fadeOut("fast");
});

$(".nv>ul>li").hover(function(){
  $(this).addClass("hover");
	$(this).children('.subnav:not(:animated)').stop(false,true).slideDown("fast")
},function(){
  $(this).removeClass("hover");
	$(this).children('.subnav').stop(false,true).slideUp("fast");
});

if(!$.cookie("welcome")){
  $(".dialog-bg,.dialog").fadeIn();
}
$(".dialog .btn").click(function(){
  $(".dialog-bg,.dialog").fadeOut();
  $.cookie("welcome","1",{path:"/"})
});