function ShowPicture(id,Source) {
	if (Source=="1"){
		if (document.layers) document.layers[''+id+''].visibility = "show"
		else if (document.all) document.all[''+id+''].style.visibility = "visible"
		else if (document.getElementById) document.getElementById(''+id+'').style.visibility = "visible"
		}
	else if (Source=="0"){
			if (document.layers) document.layers[''+id+''].visibility = "hide"
			else if (document.all) document.all[''+id+''].style.visibility = "hidden"
			else if (document.getElementById) document.getElementById(''+id+'').style.visibility = "hidden"
		}
} 