
$(function() {

        var url = $("#oneFirst img").attr("src");
		console.log(url);
        if (url != "/media/create_page/emptySpace.gif") {
			$("#oneFirst").css({ border: 0});
		}
		url = $("#twoFirst img").attr("src");
		console.log(url);
        if (url != "/media/create_page/emptySpace.gif") {
			$("#twoFirst").css({ border: 0});
		}
		url = $("#twoSecond img").attr("src");
		console.log(url);
        if (url != "/media/create_page/emptySpace.gif") {
			$("#twoSecond").css({ border: 0});
		}
		url = $("#threeFirst img").attr("src");
		console.log(url);
        if (url != "/media/create_page/emptySpace.gif") {
			$("#threeFirst").css({ border: 0});
		}
		url = $("#threeSecond img").attr("src");
		console.log(url);
        if (url != "/media/create_page/emptySpace.gif") {
			$("#threeSecond").css({ border: 0});
		}
		url = $("#threeThird img").attr("src");
		console.log(url);
        if (url != "/media/create_page/emptySpace.gif") {
			$("#threeThird").css({ border: 0});
		}
		var src = $("#handler").find('img').attr('src');
		console.log(src);
		if (src == "/media/create_page/emptySpace.gif") {
				
		}
        return false;
} );
