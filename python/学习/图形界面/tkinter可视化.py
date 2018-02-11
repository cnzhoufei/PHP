from tkinter import *

#设置窗口
root = Tk()
root.title('测试')#设置title
root.geometry('500x500+200+200')#设置窗口大小和位置
# root.resizable(width=False, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

# Label 控件 文本
#root：窗口对象 text:文本  bg:背景颜色  font:字体类型和大小 wraplength:文字多宽后换行 justify:设置文本对齐方式 left right top bommon anchor:文本位置 n北 e东 s南 w西 center 居中 
l = Label(root, text="你好", bg="pink", font=("Arial",12), width=8, height=3,wraplength=10)#显示文本
# l.pack()#显示控件

def func():
	print('按钮')

#Button 按钮 command:传入点击后要执行的函数
button = Button(root,text='按钮',command=func,width=10,height=10)
button2 = Button(root,text='按钮',command=lambda:print('传入匿名函数'),width=10,height=10)
#点击后退出
button3 = Button(root,text='退出',command=root.quit,width=10,height=10)
# button.pack()
# button2.pack()
# button3.pack()

#关闭当前窗口
root.destroy()

#输入控件
#还可以用于简单的文本内容
entry = Entry(root)
# entry.pack()
entry2 = Entry(root,show="*")#用*号现在输入的字符 可以用于密码
# entry2.pack()

#绑定变量
e = Variable()#创建一个变量
entry3 = Entry(root,textvariable=e)
#设置值
e.set('要设置的值')
#获取值
# var = e.get()
# var = entry.get()
# print(val)
# entry3.pack()


#Text 控件  文本控件 用于显示多行文本的控件
# text = Text(root,width=100,height=2,)
# strs = '''很长一篇文章
# 		很长一篇文章
# 		很长一篇文章
# 		很长一篇文章'''
# text.insert(INSERT,strs)
# text.pack()

# scroll = Scrollbar()#创建滚动条
# text2 = Text(root,width=100,height=2,)
strs2 = '''很长一篇文章
		很长一篇文章
		很长一篇文章
		很长一篇文章'''
# text2.insert(INSERT,strs)
# scroll.pack(side=RIGHT,fill=Y)#side:放到窗体的那一边 Y:把y轴填满
# scroll.config(command=text.yview)#配置滚动条
# text2.config(yscrollcommand=scroll.set)
# text2.pack(fill=Y)

#多选框控件 CheckButton
def update():
	msg = ''
	hobbytext1 = hobby1.get()
	hobbytext2 = hobby2.get()
	hobbytext3 = hobby3.get()
	if hobbytext1 == True:
		msg += '选中了第一个 '
	if hobbytext2 == True:
		msg += '选中了第二个 '
	if hobbytext3 == True:
		msg += '选中了第三个 '
	#清除text中的所有内容
	text.delete(0.0,END)
	text.insert(INSERT,msg)

hobby1 = BooleanVar()#创建一个boole类型的变量
hobby2 = BooleanVar()#创建一个boole类型的变量
hobby3 = BooleanVar()#创建一个boole类型的变量
check1 = Checkbutton(root,text='11111',variable=hobby1,command=update)
check2 = Checkbutton(root,text='222222',variable=hobby2,command=update)
check3 = Checkbutton(root,text='33333',variable=hobby3,command=update)
# check1.pack()
# check2.pack()
# check3.pack()
# text = Text(root,width=50,height=50)
# text.pack()




#单选框 Radiobutton
def rupdate():
	print(r.get())
# r = StringVar() 字符串
r = IntVar()#整型
radiol1 = Radiobutton(root,text='one',value=1,variable=r,command=rupdate)
radiol1.pack()
radiol2 = Radiobutton(root,text='2',value=2,variable=r,command=rupdate)
radiol2.pack()


#ListBox 列表框控件 可以包含一个或多个文本框
#作用：在llistbox控件中显示一个字符串
#selectmode：选择的模式 BROWSE SINGLE EXTENDED:可以使listbox 支持shift和control  MULTIPLE:支持多选
listbox = Listbox(root,selectmode=BROWSE)
lbv= StringVar()
listbox = Listbox(root,selectmode=SINGLE,listvariable=lbv)

listbox.pack()
for item in ['1111','22222','333333','444444','555555']:
	listbox.insert(END,item)#按顺序添加
	listbox.insert(ACTIVE,item+'sssss')#在开始添加

listbox.insert(END,['AAAA','BBBB'])
#删除
listbox.delete(1,2)#

#选中
listbox.select_set(2)
listbox.select_set(3,6)
#取消选中
listbox.select_clear(2,4)
listbox.select_clear(3)

listbox.size()#获取到列表元素的个数
listbox.get(2,4)#获取值
listbox.get(3)
listbox.curselection()#返回当前的索引项 获取选中项的索引不是值
listbox.selection_includes(2)#判断一个选项是否被选择

listbox.set((1,2,3))#改变所以值

#绑定事件
def myprint(event):
	print(listbox.curselection())
listbox.bind('<Double-Button-1>',myprint)#双击事件


#加滚动条
sc = Scrollbar(root)#创建滚动条
sc.pack(site=RIGHT,fill=Y)
listbox.configure(yscrollcommand=sc.set)
listbox.pack(side=RIGHT,fill=BOTH)#side:放到窗体的那一边)
#额外给属性赋值
sc['command'] = listbox.yview



#Scale控件 供用户通过拖拽指示器改变变量的值 可以通过水平 和 垂直
scale = Scale(win,from_0,to=100,orient=HORIZONTAL,tickinterval=10,length=200)#HORIZONTAL水平 VERTICAL垂直
scale.pack()
scale.get()
scale.set(20)


#Spinbox 数值范围控件
#increment 步长
#value 最好不要与from_和to一起用
v = StringVar()#绑定变量
def update2():
	print(v.get())
sp = Spinbox(root,from_0,to=100,increment=5,values(0,2,4,6,8),textvariable=v,command=update2)
sp.pack()
v.set(20)
v.get()


#Menu 顶层菜单
menu = Menu(root)#创建菜单条
root.config(menu=menu)#配置菜单
menu1 = Menu(menu,tearoff=False)#创建菜单选项
#给菜单选项添加内容
for item in ['python','c','c++','oc','php','c#','退出']:
	if item == "退出":
		menu1.add_command(label=item,command=lambda:root.quit)
	else:
		menu1.add_command(label=item,command=func)
def func():
	print()
	print('sssssss')
menu.add_cascade(label='语言',menu=menu1)#向菜单条上添加菜单


#绑定右键
def showMenu(event):
	menu.post(event.x_root,event.y_root)
root.bind('<Button-3>',showMenu)


#Combobox 下拉控件
com = ttk.Combobox(root)
com.pack()
com['value'] = ('111111','222222','3333333333')#设置下拉数据
com.current(0)#设置默认值
def func(event):
	print(com.get())
com.bind('<<ComboboxSelected>>',func)#绑定事件

#frame控件 框架控件 在屏幕上显示一个矩形区域，多作为容器控件
frm = Frame(root)
frm.pack()

frm_1 = Frame(frm)
Label(frm_1,text="左上",bg="pink").pack(side=TOP)
Label(frm_1,text="左下",bg="blue").pack(side=TOP)
frm_1.pack(side=LEFT)


frm_r = Frame(frm)
Label(frm_r,text="右上",bg="pink").pack(side=TOP)
Label(frm_r,text="右下",bg="blue").pack(side=TOP)
frm_r.pack(side=RIGHT)



#表格 Treeview
tree = ttk.Treeview(root)
tree['columns'] = ('姓名','年龄','身高')#定义列
tree.column('姓名',width=100)#设置列
tree.column('年龄',width=100)#设置列
tree.column('身高',width=100)#设置列
# 设置表头
tree.heading('姓名',text="姓名-name")
tree.heading('年龄',text="年龄-name")
tree.heading('身高',text="身高-name")

#添加数据
tree.insert('',0,text="line1",values=('zhoufei','18','165'))


#树状数据
tree = ttk.Treeview(root)
tree.pack()
#添加一级树枝
treeF1 = tree.insert('',0,'中国',text="中国Chi",values=('f1'))
treeF1 = tree.insert('',0,'美国',text="美国USA",values=('f2'))
treeF1 = tree.insert('',0,'英国',text="英国ENG",values=('f3'))
#添加二级树枝
treeF1_1 = tree.insert(treeF1,0,'黑龙江',text="中国黑龙江",values("F1_1"))


#绝对布局
label1= Label(root,text="11111",bg="blue")
label2= Label(root,text="222222",bg="blue")
label3= Label(root,text="33333",bg="blue")
label4= Label(root,text="444444",bg="blue")
label1.place(x=10,y=10)
label1.place(x=20,y=10)
label1.place(x=30,y=10)
label1.place(x=40,y=10)
root.mainloop()

#相对布局
label.pack(fill=Y,SIDE=LEFT)

#表格布局
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)


#鼠标点击事件
def func(event):
	print(event.x,event.y)
button1 = Button(root,text="左单击")
button1.bind('<Button-1>',func)
button1.pack()

事件用字符串定义，有一个特殊的语法规则：
<modifier-type-detail>
type字段是最重要的，它指出了事件的种类，可以指定为Button，Key或者Enter，Configure等等。modifier和detail字段可以提供一些附加信息，在大多数情况下可以不指定。还有很多方法可以简化事件字符串，比如：为了匹配一个键盘键，你可以省略尖角括号，直接用 键 即可。除非它是空格 ， 或本身就是尖括号。 
让我们来看看最常用的事件格式： 
事件格式：

<Button-1>
一个鼠标点击事件。1代表左键，2代表中键，3代表右键。当你在一个widget上点击鼠标按键，tkinter会自动捕获并触发event，注意，当按键被抬起时才会执行handler。鼠标的位置（相对于widge）x，y会被发往event对象传入handler。你也可以这样:，<1>，它们是等价的。我比较喜欢这种方式。

<B1-Motion>
鼠标拖动事件。1代表按下左键拖动，2代表中键，3代表右键。同样的，鼠标的x，y会以event对象方式被送往handler。

<ButtonRelease-1>
鼠标按下之后释放

<Double-Button-1>
双击鼠标

<Enter>
注意，这里是鼠标指针进入到widget里，并不是代表按下键盘上的Enter键。

<Leave>
和上面的进入对应，鼠标离开widget。

<FocusIn> <FocusOut>
<Return> <Cancel> <BackSpace> <Tab> <Shift_L> <Control_L>
<Alt_L> <Home> <Left> <Up> <Right> <Down> <Delete> <F1> <F2>
这些按键都和键盘上的一一对应。

<Key>
随便一个按键，键值会以char的格式放入event对象。
a b c ... 1 2 ... 
对应键盘上的按键

<Configure>
这个关键了，如果widget的大小改变了，或者是位置，新的大小（width和height）会打包到event发往handler。

事件对象
事件对象是独立的python实例，有很多属性。 
对象属性：
widget  产生event的实例，不是名字，所有对象拥有
x，y     鼠标位置，单位：像素
x_root，y_root       鼠标相对于屏幕左上角的位置，像素
char        仅键盘事件，string
num     按钮num，仅鼠标事件
width，height        widget新大小
type        事件类型



#读csv文件
import csv 
def readCsv(path):
	with open(path,'r') as f:
		allFile = f.reader(f)
path = "c:\user\sss.csv"
readCsv(path)


#读取pdf
pip install pdfminer3K
import sys
import importlib
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFRes

106
http://www.iqiyi.com/v_19rrf05m8w.html#curid=879324300_b6b9f68666f94bcd111ca4a4742e62ff