from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_graph():
    global plot_canvas

    entry_text = entry.get()
    entryArray = [int(char) for char in entry_text if char.isdigit()]


    encoding = comboBox.get()


    fig = Figure(figsize=(5, 4), dpi= 100)
    global plot
    plot = fig.add_subplot(1, 1, 1)
    plot_canvas = FigureCanvasTkAgg(fig, master= root)
    plot_canvas.get_tk_widget().place(x=90, y= 74)


    if encoding == "NRZ-L":
        nrz_L(entryArray)
    elif encoding == "NRZ-I":
        nrz_I(entryArray)
    elif encoding == "AMI":
        ami(entryArray)

def nrz_L(data):
    data_nrz = []
    for i in data:
        x = 1 if i == 1 else -1
        data_nrz.append(x)
    data_nrz.append(1)
    xs = np.repeat(range(len(data_nrz)), 2)
    ys = np.repeat(data_nrz, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plt.title("NRZ-L")
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
    plt.grid()
    plt.title("NRZ-I")
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plot_canvas.draw()


def ami(data):
    data_ami = []
    temp = True
    for i in range(len(data)):
        if data[i] == 1 and temp:
            x = 1
            temp = False
        elif data[i] == 1 and not temp:
            x = -1
            temp = True
        else:
            x = 0
        data_ami.append(x)

    data_ami.append(0)
    xs = np.repeat(range(len(data_ami)), 2)
    ys = np.repeat(data_ami, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.title("AMI")
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plt.show()


root = tk.Tk()
root.title("Line Code")
root.geometry("700x500")
root.resizable(False, False)

bg_color = '#141415'

c1 = "#11212D"
c2 = "#CCD0CF"


lineCodes = ["NRZ", "RZ", "NRZ-L", "AMI"]

comboBox = ttk.Combobox(root, values= lineCodes)
comboBox.place(x= 150, y = 50)

l1 = ttk.Label(root, text="Enter data (0s and 1s):",
               background= bg_color,
               foreground= c2,
               font=('Arial', 10, 'italic'),
               )

l1.place(x= 150, y= 2)

plot_button = tk.Button(root, text="Plot", command=plot_graph ,
                        background= c1,
                        foreground= c2,
                        activebackground= c2,
                        activeforeground= c1,
                        highlightthickness= 2,
                        highlightbackground= c2,
                        width= 9,
                        border= 0,
                        cursor= 'hand2',
                        font=('Arial', 8, 'bold', 'italic'),
                        )
plot_button.place(x= 450, y = 24)

entry = ttk.Entry(root, width=50)
entry.place(x = 150, y = 24)



root.mainloop()