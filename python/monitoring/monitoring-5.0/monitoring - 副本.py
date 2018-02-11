
import json
import pyquery
import requests
import re
import tkinter

# def code():

#等待所以登录完成

def validation_(url):
	"""手动验证 验证码"""
	root = tkinter.Tk()
	root.title(url+' 手动验证确定')#设置title
	root.resizable(width=False, height=False)
	root.geometry('500x300+200+200')#设置窗口大小和位置
	text = tkinter.Label(root, text=url, font=("Arial",15), width=100, height=3)#显示文本
	text.pack()
	text = tkinter.Label(root, text="请确认验证码验证成功后再点击下方按钮！", bg="#fff",fg='#f00', font=("Arial",13), width=100, height=3)#显示文本
	text.pack()
	res = tkinter.IntVar()
	res.set(1)
	def des():
		res.set(2)
		root.destroy()

	button = tkinter.Button(root,text='确认登录，登录失败后重新登录',command=des,width=30,height=2)
	button.pack()

	def des2():
		res.set(3)
		root.destroy()
	button2 = tkinter.Button(root,text='确认登录，登录失败后下次不再登录',command=des2,width=30,height=2)
	button2.pack()


	root.mainloop()
	print(int(res.get()))

validation_('dddd')
# loginstop= 0
# while True:
# 	if loginstop:
# 		break

# print('ssss')
# print(code())


# url = 'htttp:ssss'
# d = '''共 \033[0;31m 444444 \033[0m页'''
# print('共 \033[0;31m 444444 \033[0m页')
# print('共 \033[0;31m 444444 \033[0m页')
# print('共 \033[0;31m 444444 \033[0m页')
# print('共 \033[0;31m 444444 \033[0m页')
# s = re.match(".*?([0-9]+).*?",d,re.S)
# print(s[1])
# exit()

# strs = """<?xml version="1.0" encoding="utf-8"?>

# <root><![CDATA[

# 	<script type="text/javascript" reload="1">if($('succeedmessage')) {$('succeedmessage').innerHTML = '';}if(typeof succeedhandle_=='function') {succeedhandle_('http://www.lesmao.cc/home.php?mod=space&do=friend&view=online&type=member', '', {});}</script><script type="text/javascript">setTimeout("window.location.href ='http://www.lesmao.cc/home.php?mod=space&do=friend&view=online&type=member';", 3000);$('succeedmessage_href').href = 'http://www.lesmao.cc/home.php?mod=space&do=friend&view=online&type=member';$('main_message').style.display = 'none';$('main_succeed').style.display = '';$('succeedlocation').innerHTML = '欢迎您回来，Level 1 多AV网站vip分享，现在将转入登录前页面';</script>
# 	<script type="text/javascript" src="http://www.lesmao.cc/api/uc.php?time=1517887592&code=ea07LjdNu0wiKvHImxpaJ1YYpxnLvJ7LVyfXLM4loFw97YlrKfL2Tb9UrlxfKt6ROAaQD0BD39ww1cTsUGl%2FfXEXAYjoFwqDn0N%2B%2FFJYczo3Ex9CggkASzs9nM1Zm%2B5b1lzqplq22ugD8DfoYsz50OUoDIEle57zSTEWo7iStiCbxM5fDtn%2Fa1G%2BkXbutH9Q" reload="1">
# 	</script>
# 	<script type="text/javascript" src="http://a.kkmeizi.com/api/uc.php?time=1517887592&code=e3e2f%2BTdCarPaE%2BlZnN7CJtdfamGawBDl%2FctlHFw1nKh2X02T3pMFubv6sp6PqZ9opR4XwYwXfsJB8ifqOBZ8TcODKscMG2DPqIcaEDplI8rGHAPnMyzqZY8nJpdh3qXWoBLPFRjfWrBlCE5hVIK2Bdk9UtkGeLf8Aa3TuxW9Q1ZuAzp0Pfhc9RsbUKgs5gz" reload="1"></script>

# 	<script type="text/javascript" src="http://s.lsmpx.com/api/uc.php?time=1517887592&code=8588a5ILJlD9NgmTNACzJnFj6F%2BCU7BQJy8cwMjsaYvkI0ijbsr2QovcII8wYkemQht3faRRS3lpIkIbXMy3SX%2BMs7krDcofWr1M2VtPMm7qkMyrffFHfXLFMLJbxcZsQmLmWkRX3F4QRxm%2FsDcmryp8kJet414nxEUbQVF1zqQcCtfMJqXWVVZSHlT%2BY4nv" reload="1"></script>]]></root>"""
# # result2 = re.search(".*?([\u4E00-\u9FA5]+).*?([\u4E00-\u9FA5]+)",strs,re.S)
# result2 = re.findall("[\u4e00-\u9fa5].*?[\u4e00-\u9fa5]",strs)
# print('获取()中的内容',result2)

# words = 'study in 山海大学'
# regex_str = ".*?([\u4E00-\u9FA5]+)"
# match_obj = re.match(regex_str, words)
# if match_obj:
#     print(match_obj.group(1))


# li = ['1','2','','4','5']

# for i in li:
# 	# if not i:
# 		# continue
# 	print(i,' ssssssssssss')

# sr = 'data/cache/style_19_common.css?Sav'
# l = re.match(".*?\?",sr)
# # print(l.group(1))
# print(l.span(0)[1])
# exit()



c = {'111111111':'11111111111111111s'}

# print(int(False))

# print(c.get('sss'))



# htmltext = pyquery.PyQuery(html)
# li = htmltext('#friend_ul li')
# for i in li:
# 	# print(dir(type(i)))
# 	# ii = i.attrib.values
# 	iii = pyquery.PyQuery(i).attr('id')
# 	print(iii)

# from lxml import etree
# msg = """成功收听<script type="text/javascript" reload="1">if(typeof succeedhandle_followmod=='function') {succeedhandle_followmod('http://www.3ajiepai.com/home.php?mod=space&do=friend&view=online&type=member', '成功收听', {'fuid':'276636','type':'add','special':'0','from':'a_followmod_'});}setTimeout("hideWindow('followmod')", 2000);</script>"""

# msges = re.match(".*?([\u4e00-\u9fa5]+).*?",msg,re.S)
# print(msges.group(1))
# exit()
# conn = requests.Session()
# c = [{'domain': 'www.smdywlt.com', 'expires': '周五, 08 2月 2019 06:40:42 GMT', 'expiry': 1549608042, 'httponly': False, 'name': 'yone_2132_connect_is_bind', 'path': '/', 'secure': False, 'value': '0'}, {'domain': 'www.smdywlt.com', 'expires': '周五, 09 2月 2018 06:40:42 GMT', 'expiry': 1518158442, 'httponly': False, 'name': 'yone_2132_lastact', 'path': '/', 'secure': False, 'value': '1518072042%09misc.php%09patch'}, {'domain': 'www.smdywlt.com', 'httponly': False, 'name': 'yone_2132_lip', 'path': '/', 'secure': False, 'value': '116.22.59.164%2C1518072035'}, {'domain': 'www.smdywlt.com', 'expires': '周五, 09 2月 2018 06:40:42 GMT', 'expiry': 1518158442, 'httponly': False, 'name': 'yone_2132_sid', 'path': '/', 'secure': False, 'value': 'H75mEQ'}, {'domain': 'www.smdywlt.com', 'expires': '周四, 08 2月 2018 06:50:41 GMT', 'expiry': 1518072641, 'httponly': False, 'name': 'yone_2132_noticeTitle', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.smdywlt.com', 'httponly': False, 'name': '__51laig__', 'path': '/', 'secure': False, 'value': '2'}, {'domain': 'www.smdywlt.com', 'httponly': False, 'name': '__51cke__', 'path': '/', 'secure': False, 'value': ''}, {'domain': 'www.smdywlt.com', 'httponly': False, 'name': '__tins__18886887', 'path': '/', 'secure': False, 'value': '%7B%22sid%22%3A%201518072033215%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201518073841576%7D'}, {'domain': 'www.smdywlt.com', 'expires': '周五, 08 2月 2019 07:40:41 GMT', 'expiry': 1549611641, 'httponly': False, 'name': 'a6887_times', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.smdywlt.com', 'expires': '周四, 08 2月 2018 07:40:41 GMT', 'expiry': 1518075641, 'httponly': False, 'name': 'a6887_pages', 'path': '/', 'secure': False, 'value': '2'}, {'domain': 'www.smdywlt.com', 'expires': '周四, 08 2月 2018 06:41:10 GMT', 'expiry': 1518072070, 'httponly': False, 'name': 'yone_2132_checkpm', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.smdywlt.com', 'expires': '周五, 08 2月 2019 06:40:40 GMT', 'expiry': 1549608040, 'httponly': False, 'name': 'yone_2132_nofavfid', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.smdywlt.com', 'expires': '周四, 08 2月 2018 18:40:35 GMT', 'expiry': 1518115235, 'httponly': False, 'name': 'yone_2132_security_cookiereport', 'path': '/', 'secure': False, 'value': '0b15Y2I%2FQx3FhDaGsQ3Epm4kGlN1Bg4x%2BDZs7jwlR8vjrzAIAuo9'}, {'domain': 'www.smdywlt.com', 'expires': '周四, 08 2月 2018 06:41:05 GMT', 'expiry': 1518072065, 'httponly': False, 'name': 'yone_2132_checkfollow', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.smdywlt.com', 'expires': '周五, 08 2月 2019 06:40:35 GMT', 'expiry': 1549608035, 'httponly': False, 'name': 'yone_2132_lastcheckfeed', 'path': '/', 'secure': False, 'value': '10008%7C1518072035'}, {'domain': 'www.smdywlt.com', 'httponly': True, 'name': 'yone_2132_auth', 'path': '/', 'secure': False, 'value': '6bf3AIxuhIc2UC5Ht1xBTQxMFFSB2nSBRLtzWghLQdGeaXFiTZeQXNh7Unt8J8nBtsbyFR8sIlQGfotucprO%2F6EOmQ'}, {'domain': 'www.smdywlt.com', 'expires': '周五, 08 2月 2019 06:40:35 GMT', 'expiry': 1549608035, 'httponly': False, 'name': 'yone_2132_ulastactivity', 'path': '/', 'secure': False, 'value': '1777KOnrr3zMN0iY0VZRu80fNi9Snb71TpYxvWmEsN7dY8RM6RiS'}, {'domain': 'www.smdywlt.com', 'expires': '周四, 08 2月 2018 06:45:32 GMT', 'expiry': 1518072332, 'httponly': False, 'name': 'yone_2132_sendmail', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.smdywlt.com', 'expires': '周六, 10 3月 2018 06:40:32 GMT', 'expiry': 1520664032, 'httponly': False, 'name': 'yone_2132_lastvisit', 'path': '/', 'secure': False, 'value': '1518068432'}, {'domain': 'www.smdywlt.com', 'expires': '周六, 10 3月 2018 06:40:32 GMT', 'expiry': 1520664032, 'httponly': True, 'name': 'yone_2132_saltkey', 'path': '/', 'secure': False, 'value': 'NRMl7mmR'}, {'domain': '.smdywlt.com', 'expires': '周五, 08 2月 2019 06:40:32 GMT', 'expiry': 1549608032, 'httponly': True, 'name': '__cfduid', 'path': '/', 'secure': False, 'value': 'dc163940f469c9b8fcfea33d6b3afefd91518072032'}]

# getheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
# response = conn.get('http://www.yldt1314.com/member.php?mod=logging&action=login&infloat=yes&frommessage&inajax=1&ajaxtarget=messagelogin',headers=getheaders);
# html = response.text

# # print((html))
# # print(dir(pyquery))
# q = pyquery.PyQuery(html.encode('gbk'))
# fromdata = q("form[name='login']").attr('action')
# print(fromdata)
# exit()








# conn = requests.Session() #开启会话维持
# getheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
# response = conn.get('http://www.3ajiepai.com/home.php?mod=space&do=friend&view=online&type=member',headers=getheaders);
# html = response.text
# q = pyquery.PyQuery(html)
# fromdata = q("input[name='password']").eq(0).attr('id')
# print(fromdata)
# exit()





data = {
'fastloginfield':'username',
'username':'多AV网站vip分享',
'password':'1666549728abc',
'quickforward':'yes',
'handlekey':'ls'
}




# leng = 0;
# for line in data.values():
# 	leng += len(line)


# print(fromdata)

# postheaders = {
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate',
# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Cache-Control':'max-age=0',
# 'Connection':'keep-alive',
# 'Content-Length':leng,
# 'Content-Type':'application/x-www-form-urlencoded',
# 'Cookie':response.cookies,
# 'Host':'www.smdywlt.com',
# 'Origin':'http://www.smdywlt.com',
# 'Referer':'http://www.smdywlt.com/home.php?mod=space&do=friend&view=online&type=member',
# 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'
# }
# 					http://www.3ajiepai.com/member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash=LKIXM&inajax=1
# 					http://www.3ajiepai.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1
# login = conn.post('http://www.3ajiepai.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1',headers=getheaders,data=data)
# # print('返回的类型',type(login))
# print('返回的状态',login.status_code)
# # print('返回的文本类型',type(login.text))
# print('返回的文本',login.text)
# print('返回的cookie',login.cookies)
# print('返回的headers',login.headers)
# print('返回的url',login.url)
# print('返回的history',login.history)
# uheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36',}
# userg = conn.get('http://www.smdywlt.com/home.php?mod=spacecp&ac=usergroup',headers=getheaders);

# print('返回的文本',userg.text)

















# <form method="post" autocomplete="off" name="login" id="loginform_LRW9N" class="cl" onsubmit="pwdclear = 1;ajaxpost('loginform_LRW9N', 'returnmessage_LRW9N', 'returnmessage_LRW9N', 'onerror');return false;" action="member.php?mod=logging&amp;action=login&amp;loginsubmit=yes&amp;frommessage&amp;loginhash=LRW9N">
# <div class="c cl">
# <input type="hidden" name="formhash" value="c4a710b2">
# <input type="hidden" name="referer" value="http://www.smdywlt.com/home.php?mod=space&amp;do=friend&amp;view=online&amp;type=member">
# <div class="rfm">
# <table>
# <tbody><tr>
# <th>
# <span class="login_slct">
# <select name="loginfield" style="float: left; display: none;" width="45" id="loginfield_LRW9N" selecti="0">


# <option value="username"></option></select><a href="javascript:;" id="loginfield_LRW9N_ctrl" style="width:45px" tabindex="1">用户名</a>
# </span>
# </th>
# <td><input type="text" name="username" id="username_LRW9N" autocomplete="off" size="30" class="px p_fre" tabindex="1" value=""></td>
# <td class="tipcol"><a href="member.php?mod=zhuce">点此注册会员</a></td>
# </tr>
# </tbody></table>
# </div>
# <div class="rfm">
# <table>
# <tbody><tr>
# <th><label for="password3_LRW9N">密码:</label></th>
# <td><input type="password" id="password3_LRW9N" name="password" onfocus="clearpwd()" size="30" class="px p_fre" tabindex="1"></td>
# <td class="tipcol"><a href="javascript:;" onclick="display('layer_login_LRW9N');display('layer_lostpw_LRW9N');" title="找回密码">找回密码</a></td>
# </tr>
# </tbody></table>
# </div>
# <div class="rfm">
# <table>
# <tbody><tr>
# <th>安全提问:</th>
# <td><select id="loginquestionid_LRW9N" width="213" name="questionid" onchange="if($('loginquestionid_LRW9N').value > 0) {$('loginanswer_row_LRW9N').style.display='';} else {$('loginanswer_row_LRW9N').style.display='none';}">
# <option value="0">安全提问(未设置请忽略)</option>
# <option value="1">母亲的名字</option>
# <option value="2">爷爷的名字</option>
# <option value="3">父亲出生的城市</option>
# <option value="4">您其中一位老师的名字</option>
# <option value="5">您个人计算机的型号</option>
# <option value="6">您最喜欢的餐馆名称</option>
# <option value="7">驾驶执照最后四位数字</option>
# </select></td>
# </tr>
# </tbody></table>
# </div>
# <div class="rfm" id="loginanswer_row_LRW9N" style="display:none">
# <table>
# <tbody><tr>
# <th>答案:</th>
# <td><input type="text" name="answer" id="loginanswer_LRW9N" autocomplete="off" size="30" class="px p_fre" tabindex="1"></td>
# </tr>
# </tbody></table>
# </div>


# <div class="rfm  bw0">
# <table>
# <tbody><tr>
# <th></th>
# <td><label for="cookietime_LRW9N"><input type="checkbox" class="pc" name="cookietime" id="cookietime_LRW9N" tabindex="1" value="2592000">自动登录</label></td>
# </tr>
# </tbody></table>
# </div>

# <div class="rfm mbw bw0">
# <table width="100%">
# <tbody><tr>
# <th>&nbsp;</th>
# <td>
# <button class="pn pnc" type="submit" name="loginsubmit" value="true" tabindex="1"><strong>登录</strong></button>
# </td>
# <td>
# </td>
# </tr>
# </tbody></table>
# </div>

# </div>
# </form>