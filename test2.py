
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def graph():
    global plot_canvas
    entry_ = entry.get()
    entryArray = []   
    for char in entry_:
        if char.isdigit():
            digit = int(char)
            entryArray.append(digit)

    value = cBox.get()

    if value == "NRZ":
        nrz(entryArray)
    elif value == "NRZ-I":
        nrz_I(entryArray)

def nrz(data):
    data_nrz = [1 if i == 1 else 0 for i in data]
    xs = np.repeat(range(len(data_nrz)), 2)
    ys = np.repeat(data_nrz, 2)
    xs = xs[1:]
    ys = ys[:-1]

    plt.clf()  # Clear the current figure
    plt.grid(True)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title("NRZ-L", fontsize=10, color='black')
    plt.xlabel(str(data), fontsize=10, color='black')
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, len(data_nrz))
    plt.show()

def nrz_I(data):
    data_nrz_i = []
    temp = True
    for i in range(len(data)):
        if data[i] == 1 and temp:
            x = -1
            temp = False
        elif data[i] == 1 and not temp:
            x = 1
            temp = True
        elif data[i] == 0 and not temp:
            x = -1
        elif data[i] == 0 and temp:
            x = 1
        data_nrz_i.append(x)

    if data_nrz_i[0] == 0:
        data_nrz_i[0] = 1
    data_nrz_i.append(1)
    xs = np.repeat(range(len(data_nrz_i)), 2)
    ys = np.repeat(data_nrz_i, 2)
    xs = xs[1:]
    ys = ys[:-1]

    plt.clf()  # Clear the current figure
    plt.grid(True)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title("NRZ-I", fontsize=10, color='black')
    plt.xlabel(str(data), fontsize=10, color='black')
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, len(data_nrz_i))
    plt.show()



root = tk.Tk()
root.title("Reseau")
root.geometry("700x500")
root.resizable(False, False)

Codes = ["NRZ", "NRZ-I"]

cBox = ttk.Combobox(root, values= Codes)
cBox.place(x= 150, y = 50)

label = ttk.Label(root, text="Entrez un nombre binaire:",
               font=('Arial', 10, 'italic'),
               )

label.place(x= 150, y= 2)

plotbutton = tk.Button(root, text="->", command= graph ,
                        background= "green",
                        width= 9,
                        border= 0,
                        cursor= 'hand2',
                        font=('Arial', 8, 'bold', 'italic'),
                        )
plotbutton.place(x= 450, y = 50)

entry = ttk.Entry(root, width=50)
entry.place(x = 150, y = 24)



root.mainloop()