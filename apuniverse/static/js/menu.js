$(function() {
	var menuIcon = $('#menu-icon');
	var menu = $('.nav-main ul');
	var menuHeight = menu.height();

	$(menuIcon).bind('click touchstart', function(e) {
		e.preventDefault();
		menu.slideToggle();
	});
	$(window).resize(function() {
		var w = $(window).width();
		if(w > 640 && menu.is(':hidden')) {
			menu.removeAttr('style');
		}
	});
});

$(function() {
	$('.links-box').each(function() {
		var menuIcon = $(this).find('.side-menu-icon');
		var menu = $(this).find('nav');

		$(menuIcon).bind('click touchstart', function(e) {
			e.preventDefault();
			menu.slideToggle();
		});
		$(window).resize(function() {
			var w = $(window).width();
			if(w > 480 && menu.is(':hidden')) {
				menu.removeAttr('style');
			}
		});
	});
});
