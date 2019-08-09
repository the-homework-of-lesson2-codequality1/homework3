import  tkinter #导入TKinter模块
from tkinter import *

def label(window):
    Label(window, text="矩形的长").grid(row=0)
    Label(window, text="矩形的宽").grid(row=1)
    Label(window, text="圆的直径").grid(row=2)
    Label(window, text="三角形的底").grid(row=3)
    Label(window, text="三角形的高").grid(row=4)
    Label(window, text="面积").grid(row=5)
