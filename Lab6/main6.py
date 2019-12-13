from tkinter import *
import math

WD = 500
ZR = WD / 2
KF = 10
FLAG = [(5, 5), (5, 16), (10, 16), (7, 13), (10, 10), (6, 10), (6, 5)]


def dec_to_scr(cords: tuple):
    return cords[0] * KF + ZR, ZR - cords[1] * KF


def axis():
    canv.delete("all")
    canv.create_line(0, 250, 500, 250, arrow=LAST)
    canv.create_line(250, 500, 250, 0, arrow=LAST)
    canv.create_text(WD-20, ZR+20, text='oX')
    canv.create_text(ZR-20, 20, text='oY', )
    vals = [i for i in range(-50, 51, 5)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        canv.create_oval(cords[i], ZR, cords[i]+2, ZR+2, fill='black')
        canv.create_text(cords[i]+5, ZR+10, text=str(vals[i]))
        canv.create_oval(ZR, cords[i], ZR+2, cords[i]+2, fill='black')
        canv.create_text(ZR+5, cords[i]+10, text=str(-vals[i]))


def atrd(x):
    return x * math.pi / 180


def transfer():
    # Получаем матрицу преобразования
    axis()
    if int(angle.get()) == 0:
        matrix = ((float(a11.get()), float(a12.get())),
                  (float(a21.get()), float(a22.get())))
    else:
        matrix = ((math.cos(atrd(int(angle.get()))), math.sin(atrd(int(angle.get())))),
                  (-math.sin(atrd(int(angle.get()))), math.cos(atrd(int(angle.get())))))
    new_flag = list()
    for each in FLAG:
        new_cords = (each[0]*matrix[0][0] + each[1]*matrix[1][0],
                     each[0]*matrix[0][1] + each[1]*matrix[1][1])
        new_flag.append(new_cords)
    new_flag_scr = [dec_to_scr(i) for i in new_flag]
    canv.create_polygon(new_flag_scr)


root = Tk()
root.title('Рисование')
root.geometry('500x600')
# Создание холста
canv = Canvas(root, width=WD, height=WD, bg='white')
canv.place(x=0, y=100)
axis()
FLAG_scr = [dec_to_scr(i) for i in FLAG]
canv.create_polygon(*FLAG_scr)
# Создание кнопок и полей ввода матрицы
transfer_label = Label(root, text='Матрица преобразования', font='sans 10', width=25)
transfer_label.grid(row=0, column=0)
a11 = Entry(root, font='sans 10', width=5)
a11.grid(row=0, column=1)
a12 = Entry(root, font='sans 10', width=5)
a12.grid(row=0, column=2)
a21 = Entry(root, font='sans 10', width=5)
a21.grid(row=1, column=1)
a22 = Entry(root, font='sans 10', width=5)
a22.grid(row=1, column=2)
angle_label = Label(root, text='Угол поворота,\nесли не указан-0', font='sans 10', width=15)
angle_label.grid(row=3, column=0)
angle = Entry(root, font='sans 10', width=5)
angle.grid(row=3, column=1)
transfer_button = Button(text='Преобразовать', font='sans 10', command=transfer)
transfer_button.place(x=350, y=25)
root.mainloop()
