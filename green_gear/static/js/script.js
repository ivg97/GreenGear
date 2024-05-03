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

/*начало блока footer*/
/*конец блока footer*/

/*начало блока home*/
/*конец блока home*/

/*начало блока about ux*/
/*конец блока about ux*/

/*начало блока services*/
/*конец блока services*/

/*начало блока list_page*/
try {
	var list_page_view_all=document.getElementById("list_page_view_all");
	var list_page_ai_insights=document.getElementById("list_page_ai_insights");
	var list_page_automation=document.getElementById("list_page_automation");
	var list_page_industry_trends=document.getElementById("list_page_industry_trends");
	var list_page_innovation=document.getElementById("list_page_innovation");

	document.getElementById('list_page_view_all').addEventListener("click", function() {
		list_page_view_all.style.border="solid 1px #000000";
		list_page_ai_insights.style.border="none";
		list_page_automation.style.border="none";
		list_page_industry_trends.style.border="none";
		list_page_innovation.style.border="none";
	})

	document.getElementById('list_page_ai_insights').addEventListener("click", function() {
		list_page_view_all.style.border="none";
		list_page_ai_insights.style.border="solid 1px #000000";
		list_page_automation.style.border="none";
		list_page_industry_trends.style.border="none";
		list_page_innovation.style.border="none";
	})

	document.getElementById('list_page_automation').addEventListener("click", function() {
		list_page_view_all.style.border="none";
		list_page_ai_insights.style.border="none";
		list_page_automation.style.border="solid 1px #000000";
		list_page_industry_trends.style.border="none";
		list_page_innovation.style.border="none";
	})

	document.getElementById('list_page_industry_trends').addEventListener("click", function() {
		list_page_view_all.style.border="none";
		list_page_ai_insights.style.border="none";
		list_page_automation.style.border="none";
		list_page_industry_trends.style.border="solid 1px #000000";
		list_page_innovation.style.border="none";
	})

	document.getElementById('list_page_innovation').addEventListener("click", function() {
		list_page_view_all.style.border="none";
		list_page_ai_insights.style.border="none";
		list_page_automation.style.border="none";
		list_page_industry_trends.style.border="none";
		list_page_innovation.style.border="solid 1px #000000";	
	})
} catch (TypeError) {}


/*конец блока list_page*/

/*начало блока detail_page*/
/*конец блока detail_page*/

/*начало блока contact*/
/*конец блока contact*/