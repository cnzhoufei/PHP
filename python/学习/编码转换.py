https://www.cnblogs.com/ccnaie/p/6832430.html
msg.encode('utf8').decode('utf-8').encode('gbk')#requests 发送gbk网站消息时

python3中各个字符编码的转换
a='我很好'    ####python3 默认的编码为unicode
###unicode>gb2312
unicode_gb2312=a.encode('gb2312') ###因为默认是unicode所以不需要decode()，直接encode成想要转换的编码如gb2312
print('我的gb2312',unicode_gb2312)       ###返回结果: 我的gb2312 b'\xce\xd2\xba\xdc\xba\xc3'
###gb2312>utf8
gb2312_utf8=unicode_gb2312.decode('gb2312').encode('utf-8') ##当前字符为gb2312所以要先decode成unicode(decode中传入的参数为当前字符的编码集)然后再encode成utf-8
print('我是utf-8',gb2312_utf8)            ###返回结果: 我是utf-8 b'\xe6\x88\x91\xe5\xbe\x88\xe5\xa5\xbd'
###utf8>gbk
utf8_gbk=gb2312_utf8.decode('utf-8').encode('gbk')##当前字符集编码为utf-8要想转换成gbk先decode成unicode字符集再encode成gbk字符集
print("我是gbk",utf8_gbk)                 ###返回结果: 我是gbk b'\xce\xd2\xba\xdc\xba\xc3'
###utf8>uicode
utf8_unicode=utf8_gbk.decode('gbk')      ####注意当转换成unicode时 并不需要encode()
print('我是unicode',utf8_unicode)         ###返回结果: 我是unicode 我很好
###unicode>gb18030
unicode_gb18030=utf8_unicode.encode('gb18030')
print('我是gb18030',unicode_gb18030)      ###返回结果: 我是gb18030 b'\xce\xd2\xba\xdc\xba\xc3'
