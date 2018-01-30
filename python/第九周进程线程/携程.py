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


#遇到io操作自动切换
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





