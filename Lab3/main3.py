from tkinter import *

# Размеры холста
WD = 500
HG = 500
ZR = 250
KF = 10


def func(x):
    a = int(a_const.get())
    b = int(b_const.get())
    c = int(a_const.get())
    return a*x*x + b*x + c


def axis_descr():
    canv.create_text(WD-20, ZR+20, text='oX')
    canv.create_text(ZR-20, 20, text='oY', )
    vals = [i for i in range(-50, 51, 5)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        canv.create_oval(cords[i], ZR, cords[i]+2, ZR+2, fill='black')
        canv.create_text(cords[i]+5, ZR+10, text=str(vals[i]))
        canv.create_oval(ZR, cords[i], ZR+2, cords[i]+2, fill='black')
        canv.create_text(ZR+5, cords[i]+10, text=str(-vals[i]))



def draw():
    canv.delete("all")
    canv.create_line(0, 250, 500, 250, arrow=LAST)
    canv.create_line(250, 500, 250, 0, arrow=LAST)
    axis_descr()
    x_mn = int(x_min.get())
    x_mx = int(x_max.get())
    y_mn = int(y_min.get())
    y_mx = int(y_max.get())
    x = x_mn
    while x <= x_mx:
        xc = round(ZR + x*KF)
        yc = round(ZR - func(x)*KF)
        if ZR - y_mn*KF >= yc >= ZR - y_mx*KF:
            canv.create_oval(xc, yc, xc+1, yc+1)
        x += 1/100


# Объявление параметров окна
root = Tk()
root.title('График функции')
root.geometry('500x650')
root.resizable(width=False, height=False)
# Создание холста
canv = Canvas(root, width=WD, height=HG, bg='white')
canv.place(x=0, y=150)
# Рисование осей
canv.create_line(0, 250, 500, 250, arrow=LAST)
canv.create_line(250, 500, 250, 0, arrow=LAST)
axis_descr()
# Создание полей ввода констант a, b, c
abc_label = Label(root, text='a, b и с', font='sans 12', width=11)
abc_label.grid(row=0, column=0)
a_const = Entry(root, font='sans 12', width=12)
a_const.grid(row=0, column=1)
b_const = Entry(root, font='sans 12', width=12)
b_const.grid(row=0, column=2)
c_const = Entry(root, font='sans 12', width=12)
c_const.grid(row=0, column=3)
# Создание полей ввода нижней границы диапазона
xy_min = Label(root, text='x min, y min', font='sans 12', width=11)
xy_min.grid(row=1, column=0)
x_min = Entry(root, font='sans 12', width=12)
x_min.grid(row=1, column=1)
y_min = Entry(root, font='sans 12', width=12)
y_min.grid(row=1, column=2)
# Создание полей ввода верхней границы диапазона
xy_max = Label(root, text='x max, y max', font='sans 12', width=11)
xy_max.grid(row=2, column=0)
x_max = Entry(root, font='sans 12', width=12)
x_max.grid(row=2, column=1)
y_max = Entry(root, font='sans 12', width=12)
y_max.grid(row=2, column=2)
# Создание кнопки и описания
drawer = Button(root, text='Нарисовать', font='sans 12', command=draw)
drawer.place(x=10, y=90)
description = Label(root, text='Размер введите в\n декартовых координатах', font='sans 12')
description.place(x=160, y=90)

root.mainloop()

