from tkinter import *


def draw():
    c.delete("all")
    c.create_polygon(int(x1.get()), int(x2.get()), int(y1.get()), int(y2.get()), int(z1.get()), int(z2.get()),
                     fill='white', outline='black')


root = Tk()
root.title('Рисование')
root.geometry('400x520')
root.resizable(width=False, height=False)
# Создание холста
c = Canvas(root, width=400, height=400, bg='white')
c.place(x=0, y=120)
# Создание полей ввода координат
x = Label(root, text='x1, x2', font='sans 12', width=8)
x.grid(row=0, column=0)
x1 = Entry(root, font='sans 12', width=15)
x1.grid(row=0, column=1)
x2 = Entry(root, font='sans 12', width=15)
x2.grid(row=0, column=2)
y = Label(root, text='y1, y2', font='sans 12', width=8)
y.grid(row=1, column=0)
y1 = Entry(root, font='sans 12', width=15)
y1.grid(row=1, column=1)
y2 = Entry(root, font='sans 12', width=15)
y2.grid(row=1, column=2)
z = Label(root, text='z1, z2', font='sans 12', width=8)
z.grid(row=2, column=0)
z1 = Entry(root, font='sans 12', width=15)
z1.grid(row=2, column=1)
z2 = Entry(root, font='sans 12', width=15)
z2.grid(row=2, column=2)
# Создание кнпоки, которая строит треугольники
drawer = Button(root, text='Нарисовать', font='sans 12', command=draw)
drawer.place(x=10, y=80)
# Description
description = Label(root, text='Размер холста: 400х400', font='sans 12', width=20)
description.place(x=160, y=85)

root.mainloop()
