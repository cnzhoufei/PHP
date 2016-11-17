/* 代码整理：懒人之家 www.lanrenzhijia.com */
window.onload=function  () {
	var linksone=getClass("titleone")[0].getElementsByTagName("a");
	var listsone=getClass("listone");
	tab(linksone,listsone);

	var links2=getClass("list2-title")[0].getElementsByTagName("a");
	var lists2=getClass("list2-list");
	tab(links2,lists2);

	var links4=getClass("list4-title")[0].getElementsByTagName("a");
	var lists4=getClass("list4-list");
	tab(links4,lists4);

	var closeBtn=getClass("close")[0];
	closeBtn.onclick=function  () {
		animate(imgs,"height",169,20);
	}
	var imgs=getClass("imgs")[0];
	var imgs1=getClass("imgs1");
	for (var i=0; i<4; i++) {
		imgs1[i].index=i;
		imgs1[i].onclick=function  () {
			animate(imgs,"height",0,20);
			for (var j=0; j<linksone.length; j++) {
				listsone[j].style.display="none";
			}
			listsone[(this.index)].style.display="block";
		}
	}
}
function tab (links,lists) {
for (var i=0; i<links.length; i++) {
    links[i].index=i;
    links[i].onclick=function  () {
	  for (var j=0; j<lists.length; j++) {
	    lists[j].style.display="none";
		links[j].style.background="";
		links[j].style.color="#000"
	  }
      lists[this.index].style.display="block";
	  this.style.background="#fff"  ;
	  this.style.color="red";
    }
  }
}
/* 代码整理：懒人之家 www.lanrenzhijia.com */