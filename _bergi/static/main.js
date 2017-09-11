(function() {
	"use strict";

	function $(id){ return document.getElementById(id); }
	function $c(class_){
		var el = document.getElementsByClassName(class_)[0];
		return el ? el : null;
	}

	/* mobile toggle button changes max-height to open the menu. issues are:
	 * - max-height transition is awkward if we set { max-height: 100000px }. google "max height transition delay".
	 * - max-height transition is fragile if we inspect the menu and set its height in the stylesheet. what if another <li> element comes?
	 * so we calculate height(overflow + bar) at toggle time, set it as element height.
	 * spoiler: this is also how Bootstrap handles it. */
	function toggle(){
		var nav = $c("nav"),
			h = nav.offsetHeight + $c("nav-menu").offsetHeight;
		if(nav.classList.toggle("open")) nav.style.maxHeight = h + "px";
		else nav.style.maxHeight = "";
	}
	$("btn-toggle").onclick = toggle;
})();
