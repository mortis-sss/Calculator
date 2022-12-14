from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

root = Tk()
root.title("Calculator")

bttn_list = [
    "7", "8", "9", "+", "*",
    "4", "5", "6", "-", "/",
    "1", "2", "3", "=", "xⁿ",
    "0", ".", "±", "C",
    "Exit", "π", "sin", "cos",
    "(", ")", "n!", "√2", "exp", "λ"]

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

        calc_entry = Entry(root, width=33)
        calc_entry.grid(row=0, column=0, columnspan=5)


# логика калькулятора
def calc(key):
    global memory, smooth_x, smooth_y
    if key == "=":
        # исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
        # исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    # очищение поля ввода
    elif key == "C":
        calc_entry.delete(0, END)

    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)

        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit()
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(float(calc_entry.get()))))
        y = lambda x: np.sin(x)
        fig = plt.subplots()
        x = np.linspace(0, 9, 1000)
        plt.plot(x, y(x))
        plt.show()
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(float(calc_entry.get()))))
        y = lambda x: np.cos(x)
        fig = plt.subplots()
        x = np.linspace(0, 9, 1000)
        plt.plot(x, y(x))
        plt.show()
    elif key == "exp":
        calc_entry.insert(END, "=" + str(math.cos(float(calc_entry.get()))))
        x = np.arange(0, 10, 2)
        y = np.exp(-x / 3.0)
        f = interpolate.interp1d(x, y, kind='quadratic')
        smooth_x = np.arange(0, 8, 0.01)
        smooth_y = f(smooth_x)
    elif key == "λ":
        calc_entry.insert(END, "=" + str((((8 * np.pi * 3 * 10 ** 8) / float(calc_entry.get()) ** 5) * (1 / (np.exp((6.62607015 * 10 ** (-34) * 3 * 10 ** 8) / (float(calc_entry.get()) * 1.380649 * 10 ** (-23) * 2500)) - 1))) * 10 ** 30))
        y = lambda x: (((8 * np.pi * 3 * 10 ** 8) / x ** 5) * (1 / (np.exp((6.62607015 * 10 ** (-34) * 3 * 10 ** 8) / (x * 1.380649 * 10 ** (-23) * 2500)) - 1))) * 10 ** 30
        fig = plt.subplots()
        x = np.arange(300, 5000, 0.01)
        plt.plot(x, y(x))
        plt.show()
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(float(calc_entry.get()))))
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(float(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


root.mainloop()
