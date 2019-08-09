import  tkinter #导入TKinter模块
from tkinter import *
from label import label
class text:
    def __init__(self,label,row,window):
        self.label='1'
        self.label=label
        self.row=row
        self.column=0
        self.text_entry=Entry(window)
    def show(self,window):
        Label(window, text=self.label).grid(row=self.row)
        self.text_entry.grid(row=self.row,column=(self.column+1))
    def text_get(self):
        return float(self.text_entry.get())











    
