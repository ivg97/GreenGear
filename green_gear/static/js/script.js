/*начало блока nav*/
document.getElementById('show_menu').addEventListener("click", function() {
	var nav=document.getElementById("nav");
	var img_show=document.getElementById("show_menu");
	var img_close=document.getElementById("close_menu");
	nav.style.height="100%";
	img_show.style.display="none";
	img_close.style.display="block";
})

document.getElementById('close_menu').addEventListener("click", function() {
	var nav=document.getElementById("nav");
	var img_show=document.getElementById("show_menu");
	var img_close=document.getElementById("close_menu");
	nav.style.height="72px";
	img_show.style.display="block";
	img_close.style.display="none";
})
/*конец блока nav*/