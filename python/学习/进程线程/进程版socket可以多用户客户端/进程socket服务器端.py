from multiprocessing import Process;
import socket;



def recvs(conn,addr):
	while True:
		try:
			data = conn.recv(1024);
			if not data:
				continue;
			conn.send(data);
		except Exception as e:
			conn.close();
		

		





def connect():
	server = socket.socket();
	server.bind(('0.0.0.0',5555));
	server.listen();
	while True:
		conn,addr = server.accept();
		#交给进程去处理
		p = Process(target=recvs,args=(conn,addr,));
		p.start();
if __name__ == '__main__':
	connect();