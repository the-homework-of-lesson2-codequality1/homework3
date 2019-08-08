import  tkinter #导入TKinter模块
from tkinter import *


area=0.000000
transfer=2.54

window = Tk()
Label(window, text="矩形的长").grid(row=0)
Label(window, text="矩形的宽").grid(row=1)
Label(window, text="圆的直径").grid(row=2)
Label(window, text="三角形的底").grid(row=3)
Label(window, text="三角形的高").grid(row=4)
Label(window, text="面积").grid(row=5)
Label(window, text="计算一种图形的面积时请把其它图形的参数填为0",bg='red').grid(row=6)

contentVar_area=tkinter.StringVar(window,'')

rect1 = Entry(window)
rect2 = Entry(window)
circle = Entry(window)
triangle1 = Entry(window)
triangle2 = Entry(window)
e3 = Entry(window,textvariable=contentVar_area,width=50)

rect1.grid(row=0, column=1)
rect2.grid(row=1, column=1)
circle.grid(row=2,column=1)
triangle1.grid(row=3, column=1)
triangle2.grid(row=4, column=1)
e3.grid(row=5, column=1)
e3['state']='readonly'#文本框只能读，不能写

def unit():
    global area
    area_inch=area*(transfer**2)
    area_inch=round(area_inch,3)
    result_input=StringVar()
    result_area_inch=str(area_inch)
    if float(rect1.get())!=0:
        result_input='矩形 '+'长：'+str(float(rect1.get())*transfer)+'厘米 '+'宽：'+str(float(rect2.get())*transfer)+'厘米 '
    elif float(circle.get())!=0:
        result_input='圆 '+'直径：'+str(float(circle.get())*transfer)+'厘米 '
    elif float(triangle1.get())!=0:
        result_input='三角形 '+'底：'+str(float(triangle1.get())*transfer)+'厘米 '+'高：'+str(float(triangle2.get())*transfer)+'厘米 '
    result=result_input+'面积：'+result_area_inch+'平方厘米'
    contentVar_area.set(result)

def getarea():
    rect_lenth=float(rect1.get()) #获取文本框内容
    rect_width=float(rect2.get())
    circle_diameter=float(circle.get())
    triangle_bottom=float(triangle1.get())
    triangle_height=float(triangle2.get())
    global area
    area=rect_lenth*rect_width+3.14*(circle_diameter/2)**2+triangle_bottom*triangle_height/2
    area=round(area,3)
    result=StringVar()
    result_input=StringVar()
    if rect_lenth!=0:
        result_input='矩形 '+'长：'+str(rect_lenth)+'厘米 '+'宽：'+str(rect_width)+'厘米 '
    elif circle_diameter!=0:
        result_input='圆 '+'直径：'+str(circle_diameter)+'厘米 '
    elif triangle_bottom!=0:
        result_input='三角形 '+'底：'+str(triangle_bottom)+'厘米 '+'高：'+str(triangle_height)+'厘米 '
    result_area=str(area)
    result=result_input+'面积：'+result_area+'平方厘米'
    contentVar_area.set(result)
    
window.title('面积计算器')
tkinter.Button(window,text="英尺转化为厘米",command=unit).grid(row=6,column=1)
tkinter.Button(window,text="确定",command=getarea).grid(row=6,column=2)
mainloop( )