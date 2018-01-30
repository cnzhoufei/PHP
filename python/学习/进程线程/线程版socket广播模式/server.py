
import threading
import socket
li = {};
def run(conn,addr):
	li[str(addr[0]) + ':' + str(addr[1])] = conn;#存储起来用于全发
	print('进来了','conn：',conn,'addr',addr);
	while True:
		try:
			data = conn.recv(1024)#接受数据
			print(len(li),"\r\r\r\r")
			if not data:
				continue;

			for (k,i) in li.items():#循环发送给每一个客服端
				i.send(data.upper())#发送数据给客户端
			
		except Exception as e:#ConnectionResetError
			del li[str(addr[0]) + ':' + str(addr[1])];#客服端断开时从列表中删除对应的客服端链接

def min():
	server = socket.socket();
	server.bind(('localhost',9896));
	server.listen();
	while True:
		conn,addr = server.accept()#等待请求 会返回两个值 conn就是客户端连过来而在服务器的为其生成的一个连接实例
		t = threading.Thread(target=run,args=(conn,addr,));#每一个客服端用一个线程处理
		t.start();

if __name__ == '__main__':
	print('顶顶顶顶顶顶顶顶顶多多多多')
	min();