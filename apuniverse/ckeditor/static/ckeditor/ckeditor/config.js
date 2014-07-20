/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here.
	// For complete reference see:
	// http://docs.ckeditor.com/#!/api/CKEDITOR.config

		config.plugins = 'dialogui,dialog,a11yhelp,dialogadvtab,basicstyles,blockquote,clipboard,button,panelbutton,panel,floatpanel,colorbutton,colordialog,templates,menu,contextmenu,div,resize,toolbar,elementspath,enterkey,entities,popup,filebrowser,fakeobjects,floatingspace,listblock,richcombo,font,format,horizontalrule,htmlwriter,iframe,wysiwygarea,image,indent,indentblock,indentlist,justify,menubutton,language,link,list,liststyle,magicline,maximize,newpage,pagebreak,pastetext,removeformat,selectall,showborders,sourcearea,specialchar,scayt,tab,table,tabletools,undo,wsc,lineutils,widget,image2,oembed';

    config.skin = 'bootstrapck',

	config.toolbar_Mine =
	[
		{ name: 'basicstyles',
			items : [ 'Bold','Italic','Strike','-','RemoveFormat' ] },
		{ name: 'paragraph',
			items : [ 'NumberedList','BulletedList','-','Blockquote','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock' ] },
		{ name: 'links',
			items : [ 'Link','Unlink','Anchor' ] },
		{ name: 'clipboard',
			items : [ 'Cut','Copy','PasteText','-','Undo','Redo' ] },
		{ name: 'editing',
			items : [ 'SpellChecker', 'Scayt' ] },
    '/',
		{ name: 'insert',
			items : [ 'Image','oembed','Table','HorizontalRule', 'SpecialChar' ] },
		{ name: 'styles',
			items : [ 'Format' ] },
		{ name: 'colors',
			items : [ 'TextColor' ] },
		{ name: 'view',
			items : [ 'Source' ] },
		{ name: 'tools',
			items : [ 'Maximize' ] },
];

	// Set the most common block elements.
	config.format_tags = 'p;h2;h3;h4;pre';
	
//	config.stylesSet = 'myStyles';
};
