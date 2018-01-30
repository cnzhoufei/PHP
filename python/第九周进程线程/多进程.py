
from multiprocessing import Process,Queue,freeze_support,Pool;
import time,os;

# os.getpid() 获取本进程id
# os.getppid() 获取主进程id
def run(name):
	print(name,os.getppid());
	time.sleep(1);


if __name__ == '__main__':
	for i in range(10):
		p = Process(target=run,args=(i,));
		p.start();


#进程通信
def f(q):
	q.put([42,None,'hello'])


if __name__ == '__main__':
	q = Queue();
	p = Process(target=f,args=(q,))
	p.start();
	print(q.get());
	p.join();


#进程池
def Foo(i):
	time.sleep(2);
	print("in process",os.getpid());

if __name__ == '__main__':
	pool = Pool(processes=5);#允许进程池同时放入5个进程
	print('主进程',os.getpid())
	for i in range(10):
		pool.apply_async(func=Foo,args(i,),callback=Bar)##callback=回调 每个进程执行完毕后执行bar方法
		#pool.apply(func=Foo, args=(i,)) #串行
        #pool.apply_async(func=Foo, args=(i,)) #并行
    print('end')
    pool.close()
    pool.join();#这个必须要 否则程序将直接结束