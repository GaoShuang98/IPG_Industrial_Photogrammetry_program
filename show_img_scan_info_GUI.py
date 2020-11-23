# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# @Time    : 2020/8/27 14:50
# @Author  : 黄高爽
# @Email   : huanggaoshuang123@163.com
# @File    : show_img_scan_info_GUI.py
# @Software: PyCharm


import tkinter as tk
from tkinter import ttk
from time import sleep

import time
import threading
from tkinter import *


def update_progress_bar():
    for percent in range(1, 101):
        # hour = int(percent / 3600)
        # minute = int(percent / 60) - hour * 60
        # second = percent % 60
        green_length = int(sum_length * percent / 100)
        canvas_progress_bar.coords(canvas_shape, (0, 0, green_length, 25))
        # canvas_progress_bar.itemconfig(canvas_text, text='%02d:%02d:%02d' % (hour, minute, second))
        var_progress_bar_percent.set('%0.2f  %%' % percent)
        time.sleep(0.1)


def run():
    th = threading.Thread(target=update_progress_bar)
    th.setDaemon(True)
    th.start()

def show_img_info():
    top = Tk()
    top.title('Progress Bar')
    top.geometry('800x500+400+200')
    top.resizable(False, False)
    top.config(bg='#535353')

    # 进度条
    global sum_length
    global canvas_shape
    global canvas_text
    global canvas_progress_bar
    global var_progress_bar_percent
    sum_length = 630
    canvas_progress_bar = Canvas(top, width=sum_length, height=20)
    canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
    canvas_text = canvas_progress_bar.create_text(292, 4, anchor=NW)
    # canvas_progress_bar.itemconfig(canvas_text, text='00:00:00')
    var_progress_bar_percent = StringVar()
    var_progress_bar_percent.set('00.00  %')
    label_progress_bar_percent = Label(top, textvariable=var_progress_bar_percent, fg='#F5F5F5', bg='#535353')
    canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=CENTER)
    label_progress_bar_percent.place(relx=0.89, rely=0.4, anchor=CENTER)
    # 按钮
    button_start = Button(top, text='开始', fg='#F5F5F5', bg='#7A7A7A', command=run, height=1, width=15, relief=GROOVE, bd=2,
                          activebackground='#F5F5F5', activeforeground='#535353')
    button_start.place(relx=0.45, rely=0.5, anchor=CENTER)

    top.mainloop()


if __name__ == '__main__':
    show_img_info()
