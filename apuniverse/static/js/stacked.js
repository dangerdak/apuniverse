$(function() {
	var addItem = $('.grp-group .grp-add-handler');
	console.log(addItem.length);
	var doc = $(this);
	addItem.bind('click', doc, function() {
		console.log('Ran')
		doc.find('.grp-items div:nth-last-child(2)').removeClass('grp-closed');
		doc.find('.grp-items div:nth-last-child(2)').addClass('grp-open');
	});
});

