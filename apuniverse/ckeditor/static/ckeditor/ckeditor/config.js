/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here.
	// For complete reference see:
	// http://docs.ckeditor.com/#!/api/CKEDITOR.config

		config.plugins = 'dialogui,dialog,about,a11yhelp,dialogadvtab,basicstyles,bidi,blockquote,clipboard,button,panelbutton,panel,floatpanel,colorbutton,colordialog,templates,menu,contextmenu,div,resize,toolbar,elementspath,enterkey,entities,popup,filebrowser,find,fakeobjects,flash,floatingspace,listblock,richcombo,font,forms,format,horizontalrule,htmlwriter,iframe,wysiwygarea,image,indent,indentblock,indentlist,smiley,justify,menubutton,language,link,list,liststyle,magicline,maximize,newpage,pagebreak,pastetext,pastefromword,preview,print,removeformat,save,selectall,showblocks,showborders,sourcearea,specialchar,scayt,stylescombo,tab,table,tabletools,undo,wsc,lineutils,widget,image2';

    config.skin = 'bootstrapck',

	config.toolbar_Mine =
	[
		{ name: 'basicstyles',
			items : [ 'Bold','Italic','Underline','Strike','-','RemoveFormat' ] },
		{ name: 'clipboard',
			items : [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ] },
		{ name: 'editing',
			items : [ 'SpellChecker', 'Scayt' ] },
    '/',
		{ name: 'paragraph',
			items : [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock' ] },
		{ name: 'links',
			items : [ 'Link','Unlink','Anchor' ] },
		{ name: 'insert',
			items : [ 'Image','Flash','Table','HorizontalRule', 'SpecialChar' ] },
		'/',
		{ name: 'styles',
			items : [ 'Styles','Format','Font' ] },
		{ name: 'colors',
			items : [ 'TextColor','BGColor' ] },
		{ name: 'tools',
			items : [ 'Source','Maximize','-','About' ] },
];

	// Remove some buttons provided by the standard plugins, which are
	// not needed in the Standard(s) toolbar.
//	config.removeButtons = 'Underline,Subscript,Superscript';

	// Set the most common block elements.
	config.format_tags = 'p;h1;h2;h3;pre';

	// Simplify the dialog windows.
//	config.removeDialogTabs = 'image:advanced;link:advanced';
};
