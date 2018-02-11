from pyquery import PyQuery as pq

html = """<form method="post" autocomplete="off" id="addform_10029460" name="addform_10029460" action="http://www.yelang98.com/home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=10029460" >
<input type="hidden" name="referer" value="http://www.yelang98.com/./" />
<input type="hidden" name="addsubmit" value="true" />
<input type="hidden" name="formhash" value="1d4df9d0" />
<div class="c">
<table>
<tr>
<th valign="top" width="60" class="avt"><a href="space-uid-10029460.html"><img src="http://yonghu.baidu.com.baidu-taobao99.me/uc_server/avatar.php?uid=10029460&size=small" /></th>
<td valign="top">添加 <strong>1666549728</strong> 为好友，附言:<br />
<input type="text" name="note" value="" size="35" class="px"  onkeydown="ctrlEnter(event, 'addsubmit_btn', 1);" />
<p class="mtn xg1">(附言为可选，1666549728 会看到这条附言，最多 10 个字 )</p>
<p class="mtm">
分组: <select name="gid" class="ps"><option value="0" >其他</option>
<option value="1"  selected="selected">通过本站认识</option>
<option value="2" >通过活动认识</option>
<option value="3" >通过朋友认识</option>
<option value="4" >亲人</option>
<option value="5" >同事</option>
<option value="6" >同学</option>
<option value="7" >不认识</option>
</select>
</p>
</td>
</tr>
</table>
</div>
<p class="o pns">
<button type="submit" name="addsubmit_btn" id="addsubmit_btn" value="true" class="pn pnc"><strong>确定</strong></button>
</p>
</form>"""
d=pq(html) #传入html字符串
# d=pq(filename='test.html') #传入文件
# d=pq(url='http://www.baidu.com')#传入url 注意：此处url似乎必须写全

val = d('#addform_10029460').find('input').eq(2).val()
print(val)


#子元素选择
items = d('.list')
list = items.children()
list = items.children('.active')

#父元素
items.parent()
items.parents()
items.parents('.sss')

#兄弟元素
items = d('.list .item.active')#包含两个的 .item .active
items.siblings()


#遍历
doc = pq(filename='hello.html')
lis = doc('li')
for li in lis.items():
    print li.html()

print lis.each(lambda e: e)


lis = doc('li').items()
for li in lis:
	print(li)


#获取属性
items.attr('href')
items.href()


#获取文本
items.text()

#获取html
items.html()


#dom 操作和jquery 一样

items.find('p').remove()#删除p标签

# css选择器完全可以使用