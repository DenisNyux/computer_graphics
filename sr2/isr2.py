from tkinter import *

WD = 500
ZR = WD / 2
KF = 25

def dec_to_scr(cords):
    return cords[0] * KF + ZR, ZR - cords[1] * KF


def axis():
    canv.create_line(0, 250, 500, 250, arrow=LAST)
    canv.create_line(250, 500, 250, 0, arrow=LAST)
    canv.create_text(WD-20, ZR+20, text='oX')
    canv.create_text(ZR-20, 20, text='oY', )
    vals = [i for i in range(-10, 10)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        canv.create_oval(cords[i], ZR, cords[i]+2, ZR+2, fill='black')
        canv.create_text(cords[i]+5, ZR+10, text=str(vals[i]))
        canv.create_oval(ZR, cords[i], ZR+2, cords[i]+2, fill='black')
        canv.create_text(ZR+5, cords[i]+10, text=str(-vals[i]))


def draw():
    p1 = [1.0, 6.0]
    p2 = [1.0, 1.0]
    while p1[1] > 1.0:
        canv.create_line(dec_to_scr(p1), dec_to_scr(p2))
        p1[1] -= 0.2
        p2[0] += 0.2


root = Tk()
root.title('Рисование')
root.geometry('500x500')
root.resizable(width=False, height=False)
# Создание холста
canv = Canvas(root, width=WD, height=WD, bg='white')
canv.place(x=0, y=0)
axis()
draw()
root.mainloop()
