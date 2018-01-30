#手动切换版 需要安装
from greenlet import greenlet;

def test1():
	print(12);
	gr2.switch();#切换到test2()
	print(34);
	gr2.switch();


def test2():
	print(56);
	grl.switch();
	print(78);


# gr1 = greenlet(test1);#启动携程
# gr2 = greenlet(test2);
# print(gr1);
# gr1.switch();


#遇到io操作自动切换 需要安装
import gevent;

def foo():
	print('foot 1');
	gevent.sleep(2);#模拟io操作
	print('foo 2');


def bar():
	print('bar 1');
	gevent.sleep(1);
	print('bar 2');

def func():
	print('func 1');
	gevent.sleep(0);
	print('func 2');


gevent.joinall([
	gevent.spawn(foo),
	gevent.spawn(bar),
	gevent.spawn(func),
])


#简单用urllib 下载网页
from urllib import request
import gevent,time
from gevent import monkey#由于gevent默认检测不到urllib的io操作 需要打上这个补丁
monkey.patch_all() #把当前程序的所有的io操作给我单独的做上标记

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/' ]
time_start = time.time()
for url in urls:
    f(url)
print("同步cost",time.time() - time_start)
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost",time.time() - async_time_start)




