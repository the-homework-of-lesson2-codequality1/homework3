import  tkinter #导入TKinter模块
from tkinter import *
from label import label
from text import text
from parameter import parameter

def unit(parameter):
    transfer=2.54
    area=parameter.num_list[0]*parameter.num_list[1]+3.14*(parameter.num_list[2]/2)**2+parameter.num_list[3]*parameter.num_list[4]/2
    area_inch=area*(transfer**2)
    area_inch=round(area_inch,3)
    result_input=StringVar()
    result_area_inch=str(area_inch)
    if parameter.num_list[0]!=0:
        result_input='矩形 '+'长：'+str(parameter.num_list[0]*transfer)+'厘米 '+'宽：'+str(parameter.num_list[1]*transfer)+'厘米 '
    elif parameter.num_list[2]!=0:
        result_input='圆 '+'直径：'+str(parameter.num_list[2]*transfer)+'厘米 '
    elif parameter.num_list[3]!=0:
        result_input='三角形 '+'底：'+str(parameter.num_list[3]*transfer)+'厘米 '+'高：'+str(parameter.num_list[4]*transfer)+'厘米 '
    result=result_input+'面积：'+result_area_inch+'平方厘米'
    parameter.contentVar_area.set(result)