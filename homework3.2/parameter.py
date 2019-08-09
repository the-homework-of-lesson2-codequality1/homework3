import  tkinter #导入TKinter模块
from tkinter import *
from label import label
from text import text
from functools import partial

class parameter:
    def __init__(self,num_list,contentVar_area):
        area=num_list[0]*num_list[1]+3.14*(num_list[2]/2)**2+num_list[3]*num_list[4]/2
        area=round(area,3)
        print (area)
        self.num_list=num_list
        self.contentVar_area=contentVar_area

