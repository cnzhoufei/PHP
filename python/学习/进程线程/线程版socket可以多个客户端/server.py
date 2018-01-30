import threading
import socket



def run(conn,addr):
	print('进来了','conn：',conn,'addr',addr)
	while True:
		print('等待数据。。。')
		data = conn.recv(1024)#接受数据
		print(data)

		if not data:
			continue;
		print(data)
		conn.send(data.upper())#发送数据给客户端



def min():
	server = socket.socket();
	server.bind(('localhost',9896));
	server.listen();
	while True:
		conn,addr = server.accept()#等待请求 会返回两个值 conn就是客户端连过来而在服务器的为其生成的一个连接实例
		t = threading.Thread(target=run,args=(conn,addr,))
		t.start();


if __name__ == '__main__':
	print('顶顶顶顶顶顶顶顶顶多多多多')
	min();