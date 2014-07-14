// Gallery
// Included twice - first for initial page (when initial document loads), 
// and then again for new pages (when each subsequent page is inserted)
// TODO tidy this up!!
$('.gallery').each(function() {
	var gallery = $(this);
	var thumbs = gallery.find('.thumbnail');
	var largeImage = gallery.find('.large-image img');
	var imageTitle = gallery.find('.image-title');

	thumbs.bind('click', largeImage, function() {
		var url = $(this).attr('data-url');
		// Remove last word from thumbnail alt value
		var alt = $(this).attr('alt').split(' ').slice(0,-1).join(' ');
		largeImage.attr('src', url);
		largeImage.attr('alt', alt);
		imageTitle.text(alt);

		// Clear all thumbnail borders...
		thumbs.css('border', '');
		// And apply border only to clicked thumbnail
		$(this).css('border', '1px solid black');
	});
});
// End of gallery-specific js

$.endlessPaginate({
	paginateOnScroll: true,
	paginateOnScrollMargin: 5,

	// When each page has loaded and been inserted into the DOM
	onCompleted: function() {
		// Gallery
		$('.gallery').each(function() {
			var gallery = $(this);
			var thumbs = gallery.find('.thumbnail');
			var largeImage = gallery.find('.large-image img');

			thumbs.bind('click', largeImage, function() {
				var url = $(this).attr('data-url');
				// Remove last word from thumbnail alt value
				var alt = $(this).attr('alt').split(' ').slice(0,-1).join(' ');
				largeImage.attr('src', url);
				largeImage.attr('alt', alt);

				// Clear all thumbnail borders...
				thumbs.css('border', '');
				// And apply border only to clicked thumbnail
				$(this).css('border', '1px solid black');
			});
		});
		// End of gallery-specific js
	}
});
