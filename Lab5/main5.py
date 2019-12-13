from tkinter import *
import math


WD = 500
ZR = 250
PHI = 0
RADIUS = 200


# Преобразование угла в радианы
def atrd(x):
    return x * math.pi / 180


def draw():
    canv.delete('all')
    n = int(angl.get())
    ang = atrd(PHI)
    x0 = round(RADIUS * math.cos(ang))
    y0 = round(RADIUS * math.sin(ang))
    p1 = (x0 + ZR, ZR - y0)
    for i in range(n+1):
        ang = PHI + 2 * math.pi * i / n
        xi = round(RADIUS * math.cos(ang))
        yi = round(RADIUS * math.sin(ang))
        p2 = (xi + ZR, ZR - yi)
        print(p1, p2)
        canv.create_line(p1, p2)
        p1 = p2



root = Tk()
root.title('Рисование')
root.geometry('500x600')
root.resizable(width=False, height=False)
# Создание холста
canv = Canvas(root, width=WD, height=WD, bg='white')
canv.place(x=0, y=100)
# Ввод количества углов
angl_label = Label(root, text='Количество углов', font='sans 12', width=18)
angl_label.grid(row=0, column=0)
angl = Entry(root, font='sans 12', width=15)
angl.grid(row=0, column=1)
# Создание кнпоки, которая строит треугольники
drawer = Button(root, text='Нарисовать', font='sans 12', command=draw)
drawer.place(x=180, y=50)
root.mainloop()
