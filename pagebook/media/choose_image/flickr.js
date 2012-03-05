$(function(){
	$("<input>").attr("type","text").attr("required","required").attr("id","flickr_text").appendTo("#search_flickr");
	$("<input>").attr("type","submit").attr("value","Go for it!").attr("id","search_button").appendTo("#search_flickr");
	$("#search_button").live('click', function() {
		search($("#flickr_text").val())
	});
});
function search(topic) {
$.getJSON("http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?",
  {
    tags: topic,
    tagmode: "any",
    format: "json"
  },
  function(data) {
	  $("#images").empty();
    $.each(data.items, function(i,item){
      $("<a>").attr("href", "upload_image_flickr/?url="+item.media.m).attr("id","link"+i).appendTo("#images");
    	$("<img/>").attr("src", item.media.m).appendTo("#link"+i);
      
      if ( i == 3 ) return false;
    });
  });
}