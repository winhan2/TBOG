# coding: utf-8

import tkinter
import draw
from tkinter import colorchooser
from tkinter import ttk


class GUI:
    def __init__(self):
        self.tk = tkinter.Tk()
        self.tk.title('tbog')
        self.tk.geometry('300x150+500+150')
        self.color_code = None
        self.bgcc = (0, 0, 0)

        self.__interface()

    def __interface(self):
        tkinter.Label(self.tk, text="循环次数").place(x=10, y=10)
        self.entry_t = tkinter.Entry(self.tk, width=10)
        self.entry_t.place(x=65, y=10)

        tkinter.Label(self.tk, text="旋转角度").place(x=10, y=40)
        self.entry_a = tkinter.Entry(self.tk, width=10)
        self.entry_a.place(x=65, y=40)

        tkinter.Label(self.tk, text="图形步长").place(x=10, y=70)
        self.entry_s = tkinter.Entry(self.tk, width=10)
        self.entry_s.place(x=65, y=70)


        tkinter.Label(self.tk, text="颜色").place(x=170, y=10)
        self.value = tkinter.StringVar()
        self.value.set('随机')  # 默认值
        values = ['单色', '随机']
        self.combobox = ttk.Combobox(
            master=self.tk,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=5,  # 宽度
            state='',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled(禁止输入选择)
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('', 10),  # 字体
            textvariable=self.value,  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
        )
        # 绑定事件,下拉列表框被选中时，绑定__cevent函数
        self.combobox.bind("<<ComboboxSelected>>", self.__cevent)
        self.combobox.place(x=200, y=12)

        tkinter.Button(self.tk, text="背景颜色", command=self.__bg_event).place(x=170, y=45)

        tkinter.Button(self.tk, text='开始绘画', command=self.__bevent).place(x=235, y=115)

    def __bevent(self):
        num = self.entry_t.get()
        angle = self.entry_a.get()
        step = self.entry_s.get()
        colorcode = self.color_code

        if num:
            num = int(num)
        else:
            num = 0
        if angle:
            angle = int(angle)
        else:
            angle = 0
        if step:
            step = int(step)
        else:
            step = 0

        if colorcode is None:
            colorcode = 'rand'

        draw.draw(num, angle, step, colorcode, self.bgcc)

    def __cevent(self, e):
        data = self.combobox.get()
        if data == '单色':
            color_code = colorchooser.askcolor()[0]
            new_code = []
            for i in range(3):
                new_code.append(int(color_code[i]))
            self.color_code = new_code

    def __bg_event(self):
        cc = colorchooser.askcolor()[0]
        new_code = []
        for i in range(3):
            new_code.append(int(cc[i]))
        self.bgcc = new_code

    def run(self):
        self.tk.mainloop()