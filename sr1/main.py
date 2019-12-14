from tkinter import *
import random


# Нарисовать 6 ячеек разного цвета
def make_cells():
    wd = 40
    hg = 20
    for i in range(6):
        color = '#' + hex(random.randint(0, 255))[2:] + hex(random.randint(0, 255))[2:] + hex(random.randint(0, 255))[2:]
        if len(color) < 7:
            color = color + '0' * (7-len(color))
        Canvas(root, width=wd, height=hg, bg=color).place(x=300, y=20 + i*50)
        Label(root, text=color, font='sans 12', width=15).place(x=50, y=20 + i*50)



# Параметры окна
root = Tk()
root.title('Рисование')
root.geometry('400x400')
root.resizable(width=False, height=False)
make_cells()
Button(root, text='Обновить цвета', font='sans 12', command=make_cells).place(x=125, y=350)
root.mainloop()
