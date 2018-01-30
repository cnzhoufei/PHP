from multiprocessing import Process,Queue;
import socket;



def recvs(conn,addr,q):
	while True:
		try:
			data = conn.recv(1024);
			if not data:
				continue;
			# 从queue中取soket链接
			for i in range(q.qsize()): 
				g = q.get();
				g.send(data);
				q.put(g);#取出来在添加进去 下一次使用
		except Exception as e:
			conn.close();
		

		





def connect():
	server = socket.socket();
	server.bind(('0.0.0.0',5555));
	server.listen();
	q = Queue();
	while True:
		conn,addr = server.accept();
		q.put(conn);
		#交给进程去处理
		p = Process(target=recvs,args=(conn,addr,q,));
		p.start();
if __name__ == '__main__':
	connect();