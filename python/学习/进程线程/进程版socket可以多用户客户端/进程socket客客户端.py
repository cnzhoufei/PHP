
import socket
import threading,time

def myrecv(client):
	"""用线程来接受数据"""
	while True:
		data = client.recv(1024);#接受返回来的数据 指定大小为1024字节
		print(data.decode());


def min():
	client = socket.socket();#连接规定协议并且创建对象(连接类型默认为tcp)
	client.connect(('localhost',5555));#要连接的ip和端口
	t = threading.Thread(target=myrecv,args=(client,));
	t.start();
	while True:
		msg = input('请输入要发送的内容').strip();
		if msg:
			client.send(msg.encode('utf-8'));#发送数据 只能发送biz
			
	client.close()#关闭连接

if __name__ == '__main__':
	min()