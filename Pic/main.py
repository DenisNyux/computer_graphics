from tkinter import *

WD = 500
ZR = WD / 2
KF = 10


def dec_to_scr(cords):
    return round(cords[0] * KF + ZR), round(ZR - cords[1] * KF)


def axis():
    canv.create_line(0, 250, 500, 250, arrow=LAST, fill='green')
    canv.create_line(250, 500, 250, 0, arrow=LAST, fill='green')
    canv.create_text(WD-20, ZR+20, text='oX')
    canv.create_text(ZR-20, 20, text='oY', )
    vals = [i for i in range(-50, 50, 5)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        canv.create_oval(cords[i], ZR, cords[i]+2, ZR+2, fill='green')
        canv.create_text(cords[i]+5, ZR+10, text=str(vals[i]), fill='green')
        canv.create_oval(ZR, cords[i], ZR+2, cords[i]+2, fill='green')
        canv.create_text(ZR+5, cords[i]+10, text=str(-vals[i]), fill='green')


def draw():
    # Антенна
    canv.create_oval(dec_to_scr((-1, 22)), dec_to_scr((1, 24)), fill='gray', outline='black')
    canv.create_polygon(dec_to_scr((-0.5, 22)), dec_to_scr((-1.1, 15)), dec_to_scr((1.1, 15)), dec_to_scr((0.5, 22)),
                        fill='gray', outline='black')
    # Фон головы
    canv.create_oval(dec_to_scr((-12.5, -5)), dec_to_scr((12.5, 15)), fill='gray', outline='gray')
    canv.create_polygon(dec_to_scr((-12.5, 5)), dec_to_scr((12.5, 5)), dec_to_scr((12.5, -20)),
                        dec_to_scr((-12.5, -20)), fill='gray', outline='gray')
    # Глаза, задний фон
    canv.create_oval(dec_to_scr((5.5, -5.5)), dec_to_scr((15.5, 5.5)), fill='gray', outline='gray')
    canv.create_oval(dec_to_scr((-15.5, -5.5)), dec_to_scr((-5.5, 5.5)), fill='gray', outline='gray')
    canv.create_polygon(dec_to_scr((-10.5, -5.5)), dec_to_scr((10.5, -5.5)), dec_to_scr((10.5, 5.5)),
                        dec_to_scr((-10.5, 5.5)), fill='gray', outline='gray')

    # Глаза
    canv.create_oval(dec_to_scr((5, -5)), dec_to_scr((15, 5)), fill='black', outline='black')
    canv.create_oval(dec_to_scr((-15, -5)), dec_to_scr((-5, 5)), fill='black', outline='black')
    canv.create_polygon(dec_to_scr((-10, -5)), dec_to_scr((10, -5)), dec_to_scr((10, 5)),
                        dec_to_scr((-10, 5)), fill='black', outline='black')
    # Глазные яблоки
    canv.create_oval(dec_to_scr((2, -4.5)), dec_to_scr((12, 4.5)), fill='#fff399')
    canv.create_oval(dec_to_scr((-12, -4.5)), dec_to_scr((-2, 4.5)), fill='#fff399')
    canv.create_rectangle(dec_to_scr((6.5, -0.5)), dec_to_scr((7.5, 0.5)), fill='black')
    canv.create_rectangle(dec_to_scr((-7.5, -0.5)), dec_to_scr((-6.5, 0.5)), fill='black')
    # Рот задний фон
    canv.create_oval(dec_to_scr((-12, -16)), dec_to_scr((-10, -9)), fill='black', outline='black')
    canv.create_oval(dec_to_scr((10, -16)), dec_to_scr((12, -9)), fill='black', outline='black')
    canv.create_rectangle(dec_to_scr((-11, -16)), dec_to_scr((11, -9)), fill='black', outline='black')
    # Рот
    canv.create_oval(dec_to_scr((-11.5, -15.5)), dec_to_scr((-10, -9.5)), fill='#fff399', outline='#fff399')
    canv.create_oval(dec_to_scr((10, -15.5)), dec_to_scr((11.5, -9.5)), fill='#fff399', outline='#fff399')
    canv.create_rectangle(dec_to_scr((-11, -15.5)), dec_to_scr((11, -9.5)), fill='#fff399', outline='#fff399')
    # "Зубы"
    canv.create_line(dec_to_scr((-11.75, -11.5)), dec_to_scr((11.75, -11.5)))
    canv.create_line(dec_to_scr((-11.75, -13.5)), dec_to_scr((11.75, -13.5)))
    canv.create_line(dec_to_scr((-11, -9)), dec_to_scr((-11, -16)))
    canv.create_line(dec_to_scr((-6.6, -9)), dec_to_scr((-6.6, -16)))
    canv.create_line(dec_to_scr((-2.2, -9)), dec_to_scr((-2.2, -16)))
    canv.create_line(dec_to_scr((2.2, -9)), dec_to_scr((2.2, -16)))
    canv.create_line(dec_to_scr((6.6, -9)), dec_to_scr((6.6, -16)))
    canv.create_line(dec_to_scr((11, -9)), dec_to_scr((11, -16)))


root = Tk()
root.title('Рисование')
root.geometry('500x500')
root.resizable(width=False, height=False)
# Создание холста
canv = Canvas(root, width=WD, height=WD, bg='white')
canv.place(x=0, y=0)
draw()
root.mainloop()
