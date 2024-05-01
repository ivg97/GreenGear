/*начало блока nav*/
document.getElementById('show_close_menu').addEventListener("click", function() {
	var nav=document.getElementById("nav");
	var img=document.getElementById("show_close_menu");
	if (nav.style.height=="100%"){
		nav.style.height="72px";
		img.setAttribute("src", "/static/img/chevron_down_menu.svg");
		img.style.top="30px";
		img.style.right="30px";
	} else {
		nav.style.height="100%";
		img.setAttribute("src", "/static/img/close_menu.svg");
		img.style.top="11px";
		img.style.right="11px";
	}
})
/*конец блока nav*/