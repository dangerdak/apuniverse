$(function() {
	var menuIcon = $('.menu-icon');
	var menu = $('.main-nav ul');
	var menuHeight = menu.height();

	$(menuIcon).bind('click', function(e) {
		e.preventDefault();
		menu.slideToggle();
	});
	$(window).resize(function() {
		var w = $(window).width();
		if(w > 600 && menu.is(':hidden')) {
			menu.removeAttr('style');
		}
	});
});
