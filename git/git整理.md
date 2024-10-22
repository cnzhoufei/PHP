在Linux上安装Git
首先，你可以试着输入git，看看系统有没有安装Git：
安装：sudo apt-get install git
旧版本系统：sudo apt-get install git-core


在Windows上安装Git
下载链接：https://git-for-windows.github.io
安装完成后，在开始菜单里找到“Git”->“Git Bash”，蹦出一个类似命令行窗口的东西，就说明Git安装成功！
安装完成后，还需要最后一步设置，在命令行输入：
git config --global user.name "Your Name"
git config --global user.email "email@example.com"


创建版本库
mkdir 文件夹名   创建文件夹
第二步，通过git init命令把这个目录变成Git可以管理的仓库：git init

提价文件
第一步，用命令git add告诉Git，把文件添加到仓库
把先增的文件给git管理：git add 文件名 ,可以多个文件 git add 文件1 文件2 , 所有用 . 代替：git add .
第二步，用命令git commit告诉Git，把文件提交到仓库：
git commit -m "这里填写注释文字"

查看状态：git status
查看修改了哪里：git diff 文件名

git log命令显示从最近到最远的提交日志，我们可以看到3次提交，最近的一次是append GPL，上一次是add distributed，最早的一次是wrote a readme file。
如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数：
git log
git log --pretty=oneline
结果：
3628164fb26d48395383f8f31179f24e0882e1e0 append GPL
ea34578d5496d7dd233c827ed32a8cd576c5ee85 add distributed
cb926e7ea50ad11b8f9e909c05226233bf755030 wrote a readme file
回退版本： git reset --hard cb926e7ea50ad11b8f9e909c05226233bf755030(版本号)

现在，你回退到了某个版本，关掉了电脑，第二天早上就后悔了，想恢复到新版本怎么办？找不到新版本的commit id怎么办？
在Git中，总是有后悔药可以吃的。当你用$ git reset --hard HEAD^回退到add distributed版本时，再想恢复到append GPL，就必须找到append GPL的commit id。Git提供了一个命令git reflog用来记录你的每一次命令：
 命令：git reflog
 结果：
 ea34578 HEAD@{0}: reset: moving to HEAD^
3628164 HEAD@{1}: commit: append GPL
ea34578 HEAD@{2}: commit: add distributed
cb926e7 HEAD@{3}: commit (initial): wrote a readme file
终于舒了口气，第二行显示append GPL的commit id是3628164，现在，你又可以乘坐时光机回到未来了。


不用shh这一步可以不要
第1步：创建SSH Key。在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果已经有了，可直接跳到下一步。如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：
ssh-keygen -t rsa -C "youremail@example.com"
第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：
然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容：
点“Add Key”，你就应该看到已经添加的Key：
为什么GitHub需要SSH Key呢？因为GitHub需要识别出你推送的提交确实是你推送的，而不是别人冒充的，而Git支持SSH协议，所以，GitHub只要知道了你的公钥，就可以确认只有你自己才能推送。



推送到远程仓库
第一次提交要执行的命令 关联远程仓库：git remote add origin https://github.com/vzhoufei/ThinkPHP.git
推送到远程仓库： git push -u origin master
由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令
后面修改后推送：git push origin master
拉取命令：git pull origin master 如果拉取失败用git reset --hard FETCH_HEAD 回到上一次pull后


克隆
git clone  https://github.com/vzhoufei/ThinkPHP.git

分支管理
创建分支：git checkout -b 分支名
切换分支：git checkout 分支名
查看分支：git branch
查看远程分支：git branch -a
拉取远程分支： git pull origin 分支名

删除本地分支：git branch -d xxxxx
删除远程分支  
git branch -r -d origin/branch-name  
git push origin :branch-name  
删除远程版本：git push origin :br-1.0.0  
合并分支：git merge seller



使用git pull文件时和本地文件冲突怎么办？
1、先将本地修改存储起来
git stash  --样本地的所有修改就都被暂时存储起来 。是用git stash list可以看到保存的信息

暂存了本地修改之后，就可以pull了。
git pull

还原暂存的内容
git stash pop stash@{0}

解决文件中冲突的的部分

删除stash
git stash drop stash@{0}  





第一步点击：Pull request
第二步点击：Create pull request
第三步点击：Create pull request
下一步去主账号合并即可







git 服务器安装  用yum安装好git后 执行 git init --bare sample.git等命令就可以了
yum install -y git

2. 生成公钥

Mac/Linux 打开命令行终端, Windows 打开 Git Bash 。 输入ssh-keygen -t rsa -C “username@example.com”,( 注册的邮箱)，接下来点击enter键即可（也可以输入密码）。

$ssh-keygen -t rsa -b 4096 -C "your_email@example.com"            // 按回车enter
# Creates a new ssh key, using the provided email as a label
# Generating public/private rsa key pair.
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]  

// 推荐使用默认地址,如果使用非默认地址可能需要配置 .ssh/config ，在前面标下划的对应目录下可以看到生成的公钥文件
成功之后

Your identification has been saved in /Users/you/.ssh/id_rsa.
# Your public key has been saved in /Users/you/.ssh/id_rsa.pub.
# The key fingerprint is:
# 01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db your_email@example.com


# 清除记住的账号密码
git config --system --unset credential.helper




