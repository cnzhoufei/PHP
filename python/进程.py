

from multiprocessing import Process,Queue;
import time;
def f(i):
	time.sleep(2);
	print('第 %s 个'%i);


if __name__ == '__main__':
	for i in range(10):
		p = Process(target=f,args=(i,));
		p.start();

#进程数据共享

def ff(q):
	print('子进程中get到的',q.get())
	q.put('ssssss');


if __name__ == '__main__':
	q = Queue();
	q.put('1111111111');
	p2 = Process(target=ff,args=(q,));
	p2.start();
	p2.join();
	print(q.get());