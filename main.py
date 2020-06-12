

import os
from tkinter import *
import re



class Lesson:
    list1 = []  # 存放所有课程信息
    asw=[]
    answer=[]
    time=['8:00-8:50','9:00-9:50','10:00-10:50','11:00-11:50','13:50-14:40','14:50-15:40','15:50-16:40','16:50-17:40','18:30-19:20','19:30-20:20','20:30-21:20']
    # 测试函数
    def judge(self,var):
        # 搜索
        self.asw=[]
        self.answer=[]
        self.search1(var,'doweek','星期\d','\d')
        self.search1(var,'secnum','第\d{1,2}节','\d{1,2}')
        self.search2(var,'name',r'\b[^x00-xff]+\b')

        # 筛选结果
        k=0
        for dict in self.asw:
            j=0
            for item in self.asw:

                if dict['doweek'] == item['doweek'] and dict['secnum'] == item['secnum'] and k!=j:
                    self.answer.append(dict)  # 相同的元素保留
                else:
                    pass
                j+=1
            k+=1
        if self.answer==[]:
            self.answer=self.asw  # 无相同元素直接输出asw
        # 去重算法，无用
        from functools import reduce
        run_function = lambda x, y: x if y in x else x+[y]
        self.answer = reduce(run_function, [[], ] + self.answer)

        # 放置消息
        from tkinter import messagebox
        src=''
        for x in self.answer:
            src =src+ '星期%d 第%s节 %s %s\n' % (x['doweek'], x['secnum'], x['name'],x['time'])
        ms=messagebox.showinfo(title='搜索结果',message=src)
        print(ms)
        var=''
    def search1(self,var,key,mtcsrc,mtc1):
        if re.search(mtcsrc,var):
            x=re.search(mtcsrc,var)
            x=x.group()
            x1=re.search(mtc1,x)
            for x in self.list1:
                if x[key]==int(x1.group()):
                    self.asw.append(x)
    def search2(self, var, key, mtcsrc):
        if re.search(mtcsrc, var):
            a=re.search(mtcsrc, var)
            x1=a.group()
            x1=x1.strip()
            for x in self.list1:
                if x[key] == x1:
                    self.asw.append(x)
lesson1=Lesson()


top = Tk()  # 创建一个窗体
top.title('1班2019-2020第二学期课程表')
top.geometry("1100x400+200+50")  # 改变窗体的大小
def move(x):
    c.seek(x,os.SEEK_CUR)  # 移动指针

# 读取与显示
c= open('curriculum.txt', mode='rb')  # 打开文件
move(78)
i=1
j=1
def fuc():
    i=1
    while (i<6):
        b = c.read(6)
        a = b.decode('utf-8')
        locals()['lesson'+str(i)+str(j)]= {'doweek': i, 'name': a, 'secnum': j,'time':lesson1.time[j-1]}
        lesson1.list1.append(locals()['lesson'+str(i)+str(j)])  # 存入list1
        move(5)  # 指针移动
        scr = locals()['lesson'+str(i)+str(j)]['name']

        # 确认文本的位置
        Label(f1, text=scr,bg='lightblue',font='48').grid(row=j, column=i, padx=0, pady=0, ipadx=100, ipady=20)

        i=i+1



# 放置输入框
entry=Entry(top,bd=4)
entry.pack(side='top',anchor='ne')

# 搜索按钮
def insert_point1():
    var = entry.get()  # 获取输入内容
    alist=['星期一','星期二','星期三','星期四','星期五','第一节','第二节','第三节','第四节','第五节','第六节','第七节','第八节','第九节','第十节','第十一节']
    blist=['星期1','星期2','星期3','星期4','星期5','第1节','第2节','第3节','第4节','第5节','第6节','第7节','第8节','第9节','第10节','第11节']
    i=0
    while(i<16):
        if re.match(alist[i],var):
            var=re.sub(alist[i],blist[i],var)
        i+=1
    lesson1.judge(var)  # 测试
def insert_point2():
    var = entry.get()  # 获取输入内容
    alist=['第一节','第二节','第三节','第四节','第五节','第六节','第七节','第八节','第九节','第十节','第十一节']
    i = 0
    while (i < 11):
        if re.match(alist[i], var):
            from tkinter import messagebox
            ms = messagebox.showinfo(title='搜索结果', message=lesson1.time[i])
            print(ms)
        i += 1
b1 = Button(top,text="搜索",width=15,height=2,command=insert_point1)  # 按钮，绑定事件insert_input
b1.pack(side='top',anchor='ne')
b2 = Button(top,text="搜索时间",width=15,height=2,command=insert_point2)  # 按钮，绑定事件insert_input
b2.pack(side='top',anchor='ne')
f2=Frame(top)
f2.pack()
f4=Frame(f2)
f4.pack(side='top',anchor='ne')
f3 = Frame(f2)
f3.pack(side='left',fill='y')
f1=Frame(f2)
f1.pack(side='right',expand='yes', fill='both')

# 放置表格
i=1
Label(f4, text='                            ',bg='lightgreen',).grid(row=1, column=1, padx=0, pady=0, ipadx=48, ipady=20)
while(i<6):
    Label(f4, text='星期%s' % i,bg='lightgreen',font='48').grid(row=1, column=i+1, padx=0, pady=0, ipadx=95, ipady=20)
    i+=1


while(j<11):
    fuc()
    j=j+1
    move(7)  # 指针移动
j=11
move(3)  # 指针移动
fuc()
i=1
while(i<10):
    Label(f3, text='第%s节' % i,bg='lightyellow',font='48').grid(row=i, column=1, padx=0, pady=0, ipadx=80, ipady=20)
    i += 1
i=9
while(i<12):
    Label(f3, text='第%s节' % i,bg='lightyellow',font='48').grid(row=i, column=1, padx=0, pady=0, ipadx=76, ipady=20)
    i += 1
top.mainloop()  # 进入消息循环