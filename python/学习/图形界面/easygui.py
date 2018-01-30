import easygui as g
import sys
while 1:
    g.msgbox("显示一个窗口并且显示这些文字")# 只显示一个对话框并且只有一个ok
    msg="你希望学到什么呢?"
    title="小游戏互动"       # 在左上角的 标题旷里面
    choices=['谈恋爱','编程','ooxx','琴棋书画']  # 在选择框内 , 提供可选择项
    choice=g.choicebox(msg,title,choices) #  在这里 choice 可以得到上面你选择的那个选项
    g.msgbox("你的选择是:"+str(choice),'结果') # 打印出来
    msg='你希望再来一次么?'     
    title='请选择'
    if g.ccbox(msg,title):    #  ok为真  cancel为假
        pass
    else:
        exit(0)   # 用于退出程序  .


from tkinter import *
root = Tk() # 初始化Tk()
root.title("你好周飞")    # 设置窗口标题
root.geometry("200x300")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
l = Label(root, text="你好", bg="pink", font=("Arial",12), width=8, height=3)

l.pack(side=LEFT)   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环


# python 标准库图形界面 Tkinter