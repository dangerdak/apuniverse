// Gallery
// Show larger image when thumbnail is clicked
$(function() {
	'use strict';
	$('.gallery').each(function() {
		var gallery = $(this);
		var thumbs = gallery.find('.thumbnail');
		var largeImage = gallery.find('.large-image img');
		thumbs.bind('click', largeImage, function() {
			var url = $(this).attr('data-url');
			largeImage.attr('src', url);
		})
	})

});
