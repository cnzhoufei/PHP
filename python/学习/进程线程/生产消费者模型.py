import threading;
import queue;
import time;
baozi = [];#存储包子的
q = queue.Queue(maxsize=10);
def chuangZhao(name):
	"""创造包子"""
	i = 1;
	while True:
		q.put('包子%s'%i);
		print('[%s] 制造了[%s]'%(name,i));
		i += 1;
		time.sleep(0.5);




def chiBaoZi(name):
	while 1:
		print("[%s] 吃了 [%s]"%(name,q.get()));
		time.sleep(1);



c = threading.Thread(target=chuangZhao,args=("周飞",));
c.start();

b = threading.Thread(target=chiBaoZi,args=('狗',));
b.start();

w = threading.Thread(target=chiBaoZi,args=('旺财',));
w.start();