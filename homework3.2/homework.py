import  tkinter #导入TKinter模块
from tkinter import *
from label import label
from text import text
from unit import unit
from functools import partial
from parameter import parameter
area=0.000000
transfer=2.54
window = Tk()
contentVar_area=tkinter.StringVar(window,'')
Label(window, text="计算一种图形的面积时请把其它图形的参数填为0",bg='red').grid(row=6)
text_list=[]
num_list=[0,1,2,3,4]
text_rect_length=text("rect_length",num_list[0],window)
text_list.append(text_rect_length)
text_rect_width=text("rect_widdth",num_list[1],window)
text_list.append(text_rect_width)
text_circle_diameter=text("circle_diameter",num_list[2],window)
text_list.append(text_circle_diameter)
text_triangle_bottom=text("triagle_bottom",num_list[3],window)
text_list.append(text_triangle_bottom)
text_triangle_height=text("triagle_height",num_list[4],window)
text_list.append(text_triangle_height)

for text in text_list:
    text.show(window)


e3 = Entry(window,textvariable=contentVar_area,width=50)

e3.grid(row=5, column=1)
e3['state']='readonly'#文本框只能读，不能写

def getarea(area):
    i=0
    for text in text_list:
        num_list[i]=text.text_get()
        i=i+1
    print (num_list)

    area=num_list[0]*num_list[1]+3.14*(num_list[2]/2)**2+num_list[3]*num_list[4]/2
    area=round(area,3)
    result=StringVar()
    result_input=StringVar()
    if num_list[0]!=0:
        result_input='矩形 '+'长：'+str(num_list[0])+'厘米 '+'宽：'+str(num_list[1])+'厘米 '
    elif num_list[2]!=0:
        result_input='圆 '+'直径：'+str(num_list[2])+'厘米 '
    elif num_list[3]!=0:
        result_input='三角形 '+'底：'+str(num_list[3])+'厘米 '+'高：'+str(num_list[4])+'厘米 '
    result_area=str(area)
    result=result_input+'面积：'+result_area+'平方厘米'
    contentVar_area.set(result)
print (area)
window.title('面积计算器')
paramparameter1=parameter(num_list,contentVar_area)
tkinter.Button(window,text="英尺转化为厘米",command=partial(unit,paramparameter1)).grid(row=6,column=1)

tkinter.Button(window,text="确定",command=partial(getarea,area)).grid(row=6,column=2)
mainloop( )