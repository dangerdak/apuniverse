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
	var menuIcons = $('.side-menu-icon');
	var menus = $('.links-box nav');
	var menuHeight = menus.height();

	$(menuIcons).bind('click touchstart', function(e) {
		e.preventDefault();
		menus.slideToggle();
	});
	$(window).resize(function() {
		var w = $(window).width();
		if(w > 480 && menus.is(':hidden')) {
			menus.removeAttr('style');
		}
	});
});
