from tkinter import *
from sympy import symbols
from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        implicit_multiplication_application)
trf = (standard_transformations + (implicit_multiplication_application,))


def calculate_1():
    a = two_entry.get()
    a = int(a)
    b = three_entry.get()
    b = int(b)
    calculate_2(a, b)


def calculate_2(a, b):
    E_1 = four_entry.get()
    E_1 = float(E_1)
    if abs(b - a) < E_1:
        inp_1 = (a + b)/2
        five_entry.insert(0, inp_1)
        print((a+b)/2)
    else:
        c = (a + b) / 2
        calculate(a=a, b=b, c=c)


def calculate(a, b, c):
    x = symbols('x')
    input_form = one_entry.get()
    formula_str = input_form
    formula = parse_expr(formula_str, transformations=trf)
    res_a = formula.subs(x, a) # подставим вместо `x`
    res_b = formula.subs(x, b) # проблема с 4
    res_c = formula.subs(x, c)
    if res_a * res_c < 0:
        calculate_2(a=a, b=c)
    elif res_c * res_b < 0:
        calculate_2(a=c, b=b)


def clear():
    one_entry.delete(0, END)
    two_entry.delete(0, END)
    three_entry.delete(0, END)
    five_entry.delete(0, END)


root = Tk()
root.title("Diferenc_ur")                                # ввод уравнения + ввод параметров а и б + поле для вывода
root.geometry("720x170")                                 # + ввод погрешности + кнопка для получения ответа в поле для вывода

label_one = Label(text="Введите уравнение:", fg="#333", padx="20", pady="8", font="16",)
label_one.grid(row=1, column=0, padx=0, pady=5)

label_two = Label(text="Введите a:", fg="#333", padx="0", pady="8", font="16",)
label_two.grid(row=2, column=0, padx=0, pady=5)

label_three = Label(text="Введите b:", fg="#333", padx="20", pady="8", font="16",)
label_three.grid(row=2, column=2, padx=0, pady=5)

label_four = Label(text="Погрешность E:", fg="#333", padx="20", pady="8", font="16",)
label_four.grid(row=1, column=2, padx=0, pady=5)

label_five = Label(text="Найти х:", fg="#333", padx="20", pady="8", font="16",)
label_five.grid(row=3, column=0, padx=0, pady=5)

one_entry = Entry(font="16")
two_entry = Entry(font="16")
three_entry = Entry(font="16")
four_entry = Entry(font="16")
five_entry = Entry(font="16")

one_entry.grid(row=1, column=1, padx=0, pady=5)
two_entry.grid(row=2, column=1, padx=0, pady=5)
three_entry.grid(row=2, column=3, padx=0, pady=5)
four_entry.grid(row=1, column=3, padx=0, pady=5)
five_entry.grid(row=3, column=1, padx=0, pady=5)

btn = Button(text="Найти х:",
             foreground="white",
             background="#228b22",
             padx="20",
             pady="8",
             font="16",
             command=calculate_1)
btn.grid(row=3, column=0, padx=0, pady=5)

clear_button = Button(text="Очистить",
                      foreground="white",
                      background="#940000",
                      padx="20",
                      pady="8",
                      font="16",
                      command=clear)
clear_button.grid(row=3, column=2, padx=0, pady=5)

four_entry.insert(0, 0.0003)

root.mainloop()