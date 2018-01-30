import paramiko
#创建shh对象
ssh = paramiko.SSHClient();

#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='119.23.36.25',port=13689,username="root",password="j$dlsAa&dsD]f[Hiw@HuetVr*erFDg%nm");

#执行命令 标准输入 标准输出 标准错误
stdin,stdout,stderr = ssh.exec_command('df');


#获取命令
result = stdout.read();
if result:
	print(result.decode());
else:
	print(stderr)
#关闭
ssh.close();

#在linux上生成 公钥私钥 用xshell工具生成

#公钥放到服务器相对应用户的家目录下 .ssh/authorized_keys 文件中

#基于公钥登录
private_key = paramiko.RSAKye.from_private_key_file('私钥文件路径');
ssh = paramiko.SSHClient();
ssh.connect(hostname='119.23.36.25',port=13689,username="root",key=private_key);
stdin,stdout,stderr = ssh.exec_command('df');

#获取命令
result = stdout.read();
if result:
	print(result.decode());
else:
	print(stderr)
#关闭
ssh.close();




#ssh传送文件
scp -rp -P端口 文件 root@192.168.0.1:/tmp 

#python传送文件
trnasport = paramiko.Transport(('ip','端口'))
trnasport.connect(username="用户名",password="密码");
sftp = paramiko.SFTPClient.from_transport(trnasport);
#将 l.py 上传到服务器/tmp/test.py
sftp.put('/tmp/l.py','/tmp/test.py');
#将remove_path 下载到本地 local_path
sftp.get('remove_path','local_path');
trnasport.close();

