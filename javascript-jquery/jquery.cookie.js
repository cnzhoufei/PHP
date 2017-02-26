/*!
 * jQuery Cookie Plugin v1.4.1
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
(function (factory) {
	if (typeof define === 'function' && define.amd) {
		// AMD
		define(['jquery'], factory);
	} else if (typeof exports === 'object') {
		// CommonJS
		factory(require('jquery'));
	} else {
		// Browser globals
		factory(jQuery);
	}
}(function ($) {

	var pluses = /\+/g;

	function encode(s) {
		return config.raw ? s : encodeURIComponent(s);
	}

	function decode(s) {
		return config.raw ? s : decodeURIComponent(s);
	}

	function stringifyCookieValue(value) {
		return encode(config.json ? JSON.stringify(value) : String(value));
	}

	function parseCookieValue(s) {
		if (s.indexOf('"') === 0) {
			// This is a quoted cookie as according to RFC2068, unescape...
			s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
		}

		try {
			// Replace server-side written pluses with spaces.
			// If we can't decode the cookie, ignore it, it's unusable.
			// If we can't parse the cookie, ignore it, it's unusable.
			s = decodeURIComponent(s.replace(pluses, ' '));
			return config.json ? JSON.parse(s) : s;
		} catch(e) {}
	}

	function read(s, converter) {
		var value = config.raw ? s : parseCookieValue(s);
		return $.isFunction(converter) ? converter(value) : value;
	}

	var config = $.cookie = function (key, value, options) {

		// Write

		if (value !== undefined && !$.isFunction(value)) {
			options = $.extend({}, config.defaults, options);

			if (typeof options.expires === 'number') {
				var days = options.expires, t = options.expires = new Date();
				t.setTime(+t + days * 864e+5);
			}

			return (document.cookie = [
				encode(key), '=', stringifyCookieValue(value),
				options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
				options.path    ? '; path=' + options.path : '',
				options.domain  ? '; domain=' + options.domain : '',
				options.secure  ? '; secure' : ''
			].join(''));
		}

		// Read

		var result = key ? undefined : {};

		// To prevent the for loop in the first place assign an empty array
		// in case there are no cookies at all. Also prevents odd result when
		// calling $.cookie().
		var cookies = document.cookie ? document.cookie.split('; ') : [];

		for (var i = 0, l = cookies.length; i < l; i++) {
			var parts = cookies[i].split('=');
			var name = decode(parts.shift());
			var cookie = parts.join('=');

			if (key && key === name) {
				// If second argument (value) is a function it's a converter...
				result = read(cookie, value);
				break;
			}

			// Prevent storing a cookie that we couldn't decode.
			if (!key && (cookie = read(cookie)) !== undefined) {
				result[name] = cookie;
			}
		}

		return result;
	};

	config.defaults = {};

	$.removeCookie = function (key, options) {
		if ($.cookie(key) === undefined) {
			return false;
		}

		// Must not alter options, thus extending a fresh object...
		$.cookie(key, '', $.extend({}, options, { expires: -1 }));
		return !$.cookie(key);
	};

}));




// 使用方法：

// 1.引入jquery.cookie.js

// <script src="scripts/jquery-1.6.4.js" type="text/javascript"></script>  
// <script src="scripts/jquery.cookie.js" type="text/javascript"></script>  
// 2.使用方法

// 1).新添加一个会话 cookie：

// $.cookie('the_cookie', 'the_value');

// 注：当没有指明 cookie有效时间时，所创建的cookie有效期默认到用户关闭浏览器为止，所以被称为

// “会话cookie（session cookie）”。

// 2).创建一个cookie并设置有效时间为 7天:

// $.cookie('the_cookie', 'the_value', { expires: 7 });

// 注：当指明了cookie有效时间时，所创建的cookie被称为“持久 cookie （persistent  cookie）”。 

// 3).创建一个cookie并设置 cookie的有效路径：

// $.cookie('the_cookie', 'the_value', { expires: 7, path: '/' });

// 注：在默认情况下，只有设置 cookie的网页才能读取该 cookie。如果想让一个页面读取另一个页面设

// 置的cookie，必须设置cookie的路径。cookie的路径用于设置能够读取 cookie的顶级目录。将这

// 个路径设置为网站的根目录，可以让所有网页都能互相读取 cookie （一般不要这样设置，防止出现冲突） 。 

// 4).读取cookie：

// $.cookie('the_cookie'); // cookie存在 => 'the_value'

// $.cookie('not_existing'); // cookie不存在 => null

// 5).删除cookie，通过传递null作为cookie的值即可：

// $.cookie('the_cookie', null);