//代码整理：懒人之家 www.lanrenzhijia.com
$(function() {
	var containerH = '345';
	var expandH = '240';
	var liNum = $('#picker li').length;
	var collapseH = (containerH - expandH) / (liNum - 1);
	var ini = '-3';
	$("#picker li").each(function() {
		$(this).attr('pik', 'bottom');
		var bH = ($(this).index() * (100 / (liNum - 1))) - 3;
		$(this).val(bH);
		$(this).css('bottom', bH + 'px')
	});
	$('.right-sidebar').height(containerH + 'px');
	$('.right-sidebar ul li').height(collapseH + 'px');
	var expandH8 = parseInt(expandH) + parseInt(8);
	$('#picker li:last-child').animate({
		height: expandH8 + 'px'
	});
	$('#picker li:last-child').attr('pik', 'on');
	$('#picker li:last-child img').height(expandH8 + 'px');
	$("#picker li").click(function() {
		if ($(this).attr('pik') != 'on') {
			var v = $(this).val();
			var pik = $(this).attr('pik');
			if (pik == 'bottom') {
				var i = $(this).index();
				$("#picker li").each(function() {
					if ($(this).index() > i) {
						$(this).attr('pik', 'top');
						$(this).find('img').height(expandH8 + 'px');
						$(this).animate({
							height: expandH8 + 'px',
							bottom: $(this).val() + "px",
						});
						$(this).css('z-index', 200 - $(this).val())
					}
				})
			} else if (pik == 'top') {
				var i = $(this).index();
				$("#picker li").each(function() {
					if ($(this).index() < i) {
						$(this).attr('pik', 'bottom');
						$(this).find('img').height(expandH8 + 'px');
						$(this).animate({
							height: collapseH + 'px',
							bottom: $(this).val() + "px",
						}, function() {});
						$(this).css('z-index', 200 - $(this).val())
					}
				})
			}
			$(this).attr('pik', 'on');
			$(this).css('z-index', 200 - v);
			$(this).find('img').height(expandH8 + 'px');
			$(this).animate({
				height: expandH8 + 'px',
				bottom: v + "px",
			})
		} else {
			window.open($(this).attr('lanren'))
		}
	})
});