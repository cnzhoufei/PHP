

#安装lxml  pip install lxml 或者到python官网下载 whl文件来安装(需要先安装wheel pip install wheel然后可以用pip install whl文件路径 来安装lxml)

# pymongo  --mongodb

#flask 框架
#文档地址 docs.jinkan.org/docs/flask/quickstart.html

# jupyter  记事本 pip install jupyter  运行命令：jupyter ontebook

# python环境anaconda 官网：www.continuum.io 国内镜像清华大学：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/


#selenium
# pip install selenium

# 对应浏览器要安装driver   例： 安装谷歌的 -- 搜索 chromedriver 
#下载链接1  http://npm.taobao.org/mirrors/chromedriver/
#下载链接2  https://chromedriver.storage.googleapis.com/index.html
#下载完成后解压 把chromedriver.exe 放到也添加环境变量的目录下(如python的安装目录下)

#基本使用
from selenium import webdriver
from selenium.webdriver.common.by import By #
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#设置浏览器不加载图片
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)

#设置头信息
options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36"')

browser = webdriver.Chrome(chrome_options=options)#声明一个浏览器对象





browser = webdriver.Chrome()#声明一个浏览器对象
try:
	browser.get('https://www.baidu.com')
	input = browser.find_element_by_id('kw')#找到kw这个id
	input.send_keys('Python')#像id为kw这个input中输入一个pathon
	input.send_keys(Keys.ENTER)#敲击回车
	wait = WebDriverWait(browser,10)#等待
	wait.until(EC.presence_of_element_located((By.ID,'content_let')))#等待id为content_let的元素加载完成
	print(browser.current_url)#打印当前访问的url
	print(browser.get_cookies())#打印cookie
	print(browser.page_source)#打印源代码
finally:
	browser.close()#关闭


#声明浏览器对象
browser = webdriver.Chrome()
browser = webdriver.firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()


#不要界面的用phantomjs  官网phantomjs.org
#windows 下载完成解压后 把phantomjs的bin目录添加到环境变量
#linx 
#1. yum -y install wget fontconfig
#2. wget -c https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2
#3. tar -xjf phantomjs-2.1.1-linux-i686.tar.bz2
#4. mv phantomjs-2.1.1-linux-i686 phantomjs
#5. ln -s /usr/local/phantomjs/bin/phantomjs /usr/bin/

# driver = webdriver.PhantomJS()
# driver.get('http://www.baidu.com')
# print(driver.page_source)


#访问页面
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
print(browser.page_source)
browser.close()

#查找元素
input_hrst = browser.find_element_by_id('q')#查找id
input_second = browser.find_element_by_css_selector('#q')#查找id
input_third = browser.find_element_by_xpath('//[@id="q"]')#查找id
find_element_by_name 
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
#查找多个元素 区别在于多加了一个s --elements
find_elements_by_xpath

# 用By模块来查找元素
input_first = browser.find_element(By.ID,'q')
#多个
input_first = browser.find_elements(By.CSS_SELECTOR,'.SSSS li')



#元素的交互操作
input = browser.find_element_by_id('kw')#找到kw这个id
input.send_keys('iPHONE')#像id为kw这个input中输入一个pathon
time.sleep(2)
input.send_keys('ipad')#
button = browser.find_element_by_class_name('btn-search')#找到一个元素
button.click()#单击一下这个元素
# 更多查看文档 selenium-python.readthedocs.io/api.html



#交互动作
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = "http://www.runoob.com/try/try.php?filename-jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')#切换到一个iframe页面
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#draggable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)#拖拽
actions.perform()

2.ActionChains方法列表

click(on_element=None) ——单击鼠标左键

click_and_hold(on_element=None) ——点击鼠标左键，不松开

context_click(on_element=None) ——点击鼠标右键

double_click(on_element=None) ——双击鼠标左键

drag_and_drop(source, target) ——拖拽到某个元素然后松开

drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

key_down(value, element=None) ——按下某个键盘上的键

key_up(value, element=None) ——松开某个键

move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标

move_to_element(to_element) ——鼠标移动到某个元素

move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置

perform() ——执行链中的所有动作

release(on_element=None) ——在某个元素位置松开鼠标左键

send_keys(*keys_to_send) ——发送某个键到当前焦点的元素

send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素 
接下来用示例来详细说明和演示每一个方法的用法：





#截图 全屏
driver.get_screenshot_as_file("test.png")
driver.save_screenshot(r'photo.png')


#截取验证码
		driver.save_screenshot(r'photo.png')
		baidu = driver.find_element_by_id('code')
		left = baidu.location['x']
		top = baidu.location['y']
		elementWidth = baidu.location['x'] + baidu.size['width']
		elementHeight = baidu.location['y'] + baidu.size['height']
		picture = Image.open(r'photo.png')
		picture = picture.crop((left, top, elementWidth, elementHeight))
		picture.save(r'photo2.png')


#执行javascript
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
browser.execute_script('alert("滚动到底部了")')


#获取属性
from selenium.webdriver import ActionChains
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))


#获取文本
inputs = browser.find_element_by_class_name('test')
print(inputs.text)

inputs.get_attribute('innerHTML')
innerHTML 会返回元素的内部 HTML， 包含所有的HTML标签。 
textContent 和 innerText 只会得到文本内容，而不会包含 HTML 标签。 
textContent 是 W3C 兼容的文字内容属性，但是 IE 不支持
innerText 不是 W3C DOM 的指定内容，FireFox不支持


#获取ID、位置、标签名、大小
inputs.id
inputs.location
inputs.tag_name
inputs.size


#隐式等待
browser = webdriver.Chrome()
browser.implicitly_wait(10)#隐士等待
browser.get('https://www.zhihu.com')
inputs = browser.find_element_by_class_name('zu-top-add')
print(inputs)

#显式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://taobao.com')
wait = WebDriverWait(browser,10)
inputs = wait.until(EC.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.BNT-SEARCH')))
print(inputs.button)

title_is标H是某内容
title_contains标H包含某内容
 presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
visibility_of_elementjocatod元索可见，传入定位元组
visibility_of可见，传入元索对象
presence_of_all_elements_located 所有元索加载出
text_to_be_present_in_etement某个元索文本包含某文字
text_to_be__present_in_element_value 某个元索值包含某文字
frafne_to_be_availaWe_and_switch_to_it  frame 加致并切换
invisibility_of_element_located 元索不可见
element_to_be_clickabte 元素可点击
staJeness_of判断一个元索是否仍在DOM,可判断页面是否已经刷新
element_to_be_setected元素可选择，传元索对象
etement_located_to_be_selected元索可逸择，传入定位元组
etement_selection_state_to_be传入元素对象以及状态，相等返回True,否则返回False
element_located_se(ectk)n_state_to_be传入定位元组以及状态，相等返回True,否则返回False
atert_is_present 是否出现Alert
# 更多查看文档 http://selenium-python.readthedocs.ip/api.html



#前进后退
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')
browser.back()#后退
browser.forward()#后退
browser.close()

#跳转
browser.navigate().to("http://www.sina.com.cn");

#cookies
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())#获取cookie
browser.add_cookie({'name':'name','domain':'www.zhihu.com'})#设置cookies
browser.delete_all_cookies()#清空cookie
print(browser.get_cookies())


#浏览器选项卡管理
browser = webdriver.Chrome()
browser.get('https://www.badu.com')
driver.maximize_window()  #将浏览器最大化
browser.execute_script('window.open()')#新开一个窗口
print(browser.window_hendles)#所有窗口
browser.switch_to_window(browser.window_hendles[1])#切换到第一个窗口
browser.get('https://www.baidu.com')
time.sleep(1)
browser.switch_to_window(browser.window_hendles[0])#切换到第0个窗口
browser.get('https://python.org')


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.execute_script('window.open()')
driver.execute_script('window.open()')
# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])
driver.get('http://python.org')
driver.switch_to.window(windows[-2])
driver.get('http://localhost')
driver.close()
driver.switch_to.window(windows[-1])
driver.close()


 driver.get("http://anjuke.com");
driver.navigate().to("http://www.baidu.com");
//后退到anjuke.com
driver.navigate().back();
//前进到baidu.com
driver.navigate().forward();
//刷新当前页面
driver.navigate().refresh();



#异常处理
from selenium.common.exceptions import TimeoutException,NoSuchElementException
#异常处理文档地址 https://
try:
	browser.get('https://www.baidu.com')
except Exception as e:
	raise
else:
	pass
finally:
	pass




# driver.get('https://www.baidu.com')


