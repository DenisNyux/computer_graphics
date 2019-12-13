from tkinter import *


def adder_click():
    a = int(entering_number1.get())
    b = int(entering_number2.get())
    res = str(a+b)
    result.delete(0, END)
    result.insert(0, res)


# Описание окна
root = Tk()
root.title('Сложение')
root.geometry('340x100')
root.resizable(width=False, height=False)
# Описание поля ввода 1
entering_number1 = Entry(root, font='sans 12')
entering_number1.place(x=20, y=10, width=60)
# Описание поля ввода 2
entering_number2 = Entry(root, font='sans 12')
entering_number2.place(x=140, y=10, width=60)
# Лэйбл для +
plus = Label(text='+', font='sans 12')
plus.place(x=100, y=10, width=20)
# Лэйбл для =
eq = Label(text='=', font='sans 12')
eq.place(x=220, y=10, width=20)
# Результат
result = Entry(root, text='0', font='sans 12')
result.place(x=260, y=10, width=60)
# Кнопка
adder = Button(root, text='Сложить', font='sans 12', command=adder_click)
adder.place(x=120, y=50, width=90)


root.mainloop()
