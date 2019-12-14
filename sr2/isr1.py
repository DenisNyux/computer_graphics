from tkinter import *

WD = 500
ZR = WD / 2
KF = 10
MAIN_TR = [(-15, -10), (0, 15), (15, -10)]


def dec_to_scr(cords: tuple):
    return cords[0] * KF + ZR, ZR - cords[1] * KF


def axis():
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


def divide(lst_of_tp, i):
    new_lst = list()
    for each in lst_of_tp:
        new_tp = (each[0] / i, each[1] / i)
        new_lst.append(new_tp)
    return new_lst


def draw():
    canv.delete('all')
    n = int(amount.get())
    for i in range(1, n+1):
        new_triangle = divide(MAIN_TR, i)
        new_triangle_scr = [dec_to_scr(i) for i in new_triangle]
        canv.create_polygon(new_triangle_scr, fill='white', outline='black')
    axis()


root = Tk()
root.title('Рисование')
root.geometry('500x600')
root.resizable(width=False, height=False)
# Создание холста
canv = Canvas(root, width=WD, height=WD, bg='white')
canv.place(x=0, y=100)
scr_triangle = [dec_to_scr(i) for i in MAIN_TR]
canv.create_polygon(*scr_triangle, fill='white', outline='black')
axis()
# Кнопка и поле ввода
Label(root, text='Количество\nтреугольников', font='sans 12', width=18).grid(row=0, column=0)
amount = Entry(root, font='sans 12', width=15)
amount.grid(row=0, column=1)
# Создание кнпоки, которая строит треугольники
drawer = Button(root, text='Нарисовать', font='sans 12', command=draw)
drawer.place(x=180, y=50)
root.mainloop()
