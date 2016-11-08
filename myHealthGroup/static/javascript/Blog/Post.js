$( document ).ready(function() {
	$("#like_button").click(function(){
    	if ($(this).text() == "Like")
   	 		window.location.href='like';
    	else
    		window.location.href='dislike';
	});

	$("#edit_button").click(function(){
		window.location.href='edit';
	});
});
