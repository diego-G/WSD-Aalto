
$(function() {
	$("#back").live('click', function() {
        // Take the target url from the link that was clicked
        var url = $("#back a").attr("href");
        
        // Replace the contents of #tableContainer with data 
        // that is dynamically from the link's target url
        $("#dynamicContent").load(url);
        
        // Return false to prevent the default behavior of "click" (changing the page)
        return false;
    });
	$("#next").live('click', function() {
        // Take the target url from the link that was clicked
        var url = $("#next a").attr("href");
        
        // Replace the contents of #tableContainer with data 
        // that is dynamically from the link's target url
        $("#dynamicContent").load(url);
        
        // Return false to prevent the default behavior of "click" (changing the page)
        return false;
    });
} );
