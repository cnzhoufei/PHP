
# import tornado.web;

# class ClassName(tornado.web.RequestHandler):
# 	def get(self):
# 		u = self.get_argument('user');
# 		self.write(u)




# from wsgiref.simple_server import make_server;
# def RunServer(environ,start_response):
# 	print(1);
# 	start_response('200 ok',[('Content-Type','text/html')]);
# 	return '<h1>Hello web!</h1>';

# if __name__ == '__main__':
# 	httpd = make_server('',8000,RunServer)
# 	print('Serving HTTP on port 8000.....');
# 	httpd.server_forever();



# web 框架
# pip install django


# l = [1,2,3,4,5]
# # l = {'username':'周飞','sex':'男','email':'vzhoufei@qq.com'}
# for k,v in enumerate(l):
# 	print(k,v)
import random
import os,time;

def upload(filename,fileobj):
	fname = filename.split('.');#切割取后缀
	filename = 'upload/'+ time.strftime("%Y-%m-%d") + '/' + str(time.time()) + str(random.random()) + '.' + fname.pop();
	print(filename)
	# f = open()

upload('1.jpg','');