
#限制同时执行的进程数(进程多了服务器会死掉)
from  multiprocessing import Process, Pool,freeze_support
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':
    pool = Pool(processes=3) #允许进程池同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar) #callback=回调 当前进程执行完成后执行这个函数(由主进程调用执行而不是子进程调用执行)
        #pool.apply(func=Foo, args=(i,)) #串行方式执行
        #pool.apply_async(func=Foo, args=(i,)) #并行执行
    print('end')
    pool.close()
    pool.join() #进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。.join()