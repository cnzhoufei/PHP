import threading;
import time;

def run(n):
	print(n);
	time.sleep(2);


t1 = threading.Thread(target=run,args=("t1",));
t2 = threading.Thread(target=run,args=("t2",));

# t1.start();
# t2.start();



class MyThread(threading.Thread):
	def __init__(self,n):
		super(MyThread,self).__init__();
		self.num = n;


	def run(self):
		print(self.num)
		time.sleep(2)

t1 = MyThread('t1')
t2 = MyThread('t2')
t1.start();
t2.start();

t1.join();#等待线程执行结果  

# ------------------------------
start_time = time.time();
t_objs = [];
for i in range(50):
	t = threading.Thread(target=run,args=("t-%s"%i,));
	t.setDaemon(True);#设置成守护线程
	t.start();
	t_objs.append(t);


for t in t_objs:
	t.join();

print(time.time() - start_time);
threading.current_thread()#经常的个数
threading.active_count()#
# -------------------------------------------

# def num(n):
# 	lock.acquire();#加锁
# 	global num;
# 	num += 1;
# 	lock.release();#解锁

# lock = threading.Lock();#保证数据完整执行加上锁

# num = 0;
# for n in range(100):
# 	threading


#队列 先进先出
import queue#
q = queue.Queue();#先进先出
q = queue.LifoQueue();#先进后出
q = q.put(1)
q = q.put(2)
q = q.put(3)

q.get()#获取数据
q.qsize()#队列大小
#设置优先级
q = q.put(-1,'aaaa')
q = q.put(5,'bbbbb')
q = q.put(2,'ccccc')
q.PriorityQueue();