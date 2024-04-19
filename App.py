import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageFilter, ImageTk
import numpy as np


def background_color(window, color, blur_radius=11.012, width=700, height=550):
    bg_image = Image.new("RGB", (width, height), color)

    blurred_bg_image = bg_image.filter(ImageFilter.GaussianBlur(blur_radius))

    tk_bg_image = ImageTk.PhotoImage(blurred_bg_image)

    label = tk.Label(window, image=tk_bg_image)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    window.bg_image = tk_bg_image



def check_array(array):
    for i in array:
        if i != 1 and i != 0:
            return False
    return True

def rz(data):
    Array = []
    for i in data:
        if i == 1:
            Array.extend([1, 0])
        else:
           Array.extend([0, 0])
    Array.append(1)
    xs = np.repeat(range(len(Array)), 2)
    ys = np.repeat(Array, 2)
    xs = xs[1:]
    ys = ys[:-1]
    
    plot.clear()
    plot.grid(True)
    plot.set_ylabel('Y Axis', color = "#fff")
    plot.set_title('RZ', fontsize=10, color= c4)
    plot.set_xlabel(str(data), fontsize=10, color="#fff")
    plot.plot(xs, ys, color= rb)
    plot.set_ylim(-3, 3)
    plot.patch.set_facecolor(bg_color)
    plot.set_xlim(0, len(Array))

    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    plot_canvas.draw()



def manchester_diff(data):
    data_md = []
    last_bit = 1
    for i in data:
        if i == 1:
            data_md.extend([-last_bit, last_bit])
            last_bit *= -1
        else:
            data_md.extend([last_bit, -last_bit])
    xs = np.repeat(range(len(data_md)), 2)
    ys = np.repeat(data_md, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plot.clear()
    plot.grid(True)
    plot.plot(xs, ys, color= rb)
    plot.set_ylabel('Y Axis', color = "#fff")
    plot.set_title("Manchester Differential", fontsize=10, color= c4)  
    plot.set_xlabel(str(data), fontsize=10, color="#fff")
    plot.set_ylim(-3, 3)
    plot.patch.set_facecolor(bg_color)
    plot.set_xlim(0, len(data_md))

    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    plot_canvas.draw()


def miller(data):
    data_miller = []
    last_bit = 1
    for i in data:
        if i == 1:
            data_miller.extend([last_bit, last_bit, -last_bit])
        else:
            data_miller.extend([-last_bit, -last_bit, last_bit])
            last_bit *= -1
    xs = np.repeat(range(len(data_miller)), 2)
    ys = np.repeat(data_miller, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plot.clear()
    plot.grid(True)
    plot.plot(xs, ys, color= rb)
    plot.set_ylabel('Y Axis', color = "#fff")
    plot.set_title("Miller (Delay Modulation)", fontsize=10, color= c4)  
    plot.set_xlabel(str(data), fontsize=10, color= "#fff")
    plot.set_ylim(-3, 3)
    plot.patch.set_facecolor(bg_color)
    plot.set_xlim(0, len(data_miller))

    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    plot_canvas.draw()


def nrz(data):
    data_nrz = []
    for i in data:
        x = None
        if i == 1:
            x = 1
        else:
            x = 0
        data_nrz.append(x)
    data_nrz.append(1)
    xs = np.repeat(range(len(data_nrz)), 2)
    ys = np.repeat(data_nrz, 2)
    xs = xs[1:]
    ys = ys[:-1]
    
    plot.clear()
    plot.grid(True)
    plot.set_ylabel('Y Axis', color = "#fff")
    plot.set_title("NRZ", fontsize=10, color= c4)
    plot.set_xlabel(str(data), fontsize=10, color='#fff')
    plot.plot(xs, ys, color = rb)
    plot.set_ylim(-3, 3)
    plot.patch.set_facecolor(bg_color)
    plot.set_xlim(0, len(data_nrz))

    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    plot_canvas.draw()


def Manchester(data):
    data_manchester = []
    for i in data:
        if i == 1:
            data_manchester.extend([-1, 1])
        else:
            data_manchester.extend([1, -1])
    xs = np.repeat(range(len(data_manchester)), 2)
    ys = np.repeat(data_manchester, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plot.clear()
    plot.grid(True)
    plot.plot(xs, ys, color= rb)
    plot.set_title("Manchester", fontsize=10, color= c4)  
    plot.set_xlabel(str(data), fontsize=10, color='#fff')
    plot.set_ylim(-3, 3)
    plot.set_xlim(0, len(data_manchester))
    plot.patch.set_facecolor(bg_color)

    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    plot_canvas.draw()
    

def nrz_l(data):
    data_nrz = []
    for i in data:
        x = None
        if i == 1:
            x = 1
        else:
            x = -1
        data_nrz.append(x)
    data_nrz.append(1)
    xs = np.repeat(range(len(data_nrz)), 2)
    ys = np.repeat(data_nrz,2)
    xs = xs[1:]
    ys = ys[:-1]
    
    plot.clear()
    plot.grid(True)
    plot.set_ylabel('Y Axis', color="#fff")
    plot.set_title('NRZ-I', fontsize=10, color= c4)
    plot.set_xlabel(str(data), fontsize=10, color='#fff')
    plot.plot(xs, ys, color = rb)
    plot.set_ylim(-3, 3)
    plot.set_xlim(0, len(data_nrz))
    plot.patch.set_facecolor(bg_color)

    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    plot_canvas.draw()

def plot_btn():
    global plot_canvas
    if plot_canvas:
        plot_canvas.get_tk_widget().destroy()

    # Retrieve values from entry and convert to integers
    entry_text = entry.get()
    entry_values = [int(char) for char in entry_text if char.isdigit()]
    print(entry_values)

    #check if the entry array is empty
    if not entry_values:
        messagebox.showerror("Error", "Entry must contain at least one digit.")
        return
    
    if check_array(entry_values) == False:
        messagebox.showerror("Error", "Entry must be only 0 or 1.")
        return
    
    Sv = comboBox.get()

    if not Sv:
        messagebox.showerror("Error", "Please choose an encoding method.")
        return

    fig = Figure(figsize=(6, 4.5), dpi= 100)
    fig.patch.set_facecolor(bg_color)
    global plot
    plot = fig.add_subplot(1, 1, 1)
    plot_canvas = FigureCanvasTkAgg(fig, master= root)
    plot_canvas.get_tk_widget().place(x= 45, y= 86)


    if Sv == "NRZ-I":
        nrz_l(entry_values)
    elif Sv =="NRZ":
        nrz(entry_values)
    elif Sv == "RZ":
        rz(entry_values)
    elif Sv == "Manchester":
        Manchester(entry_values)
    elif Sv == "Manchester différentiel":
        manchester_diff(entry_values)
    elif Sv == "Miller":
        miller(entry_values)



root = tk.Tk()
root.title("Line Code")
root.geometry("700x550")
root.resizable(False, False)

bg_color = '#141415'
c1 = "#11212D"
c2 = "#CCD0CF"
rb = "royalblue"
c4 = "white"

background_color(root, bg_color)

plot_canvas = None

lineCodes = ["NRZ", "RZ", "NRZ-I", "Manchester", "Manchester différentiel", "Miller"]

comboBox = ttk.Combobox(root, values= lineCodes)
comboBox.place(x= 150, y = 62)

l1 = ttk.Label(root, text="Enter data (0s and 1s):",
               background= bg_color,
               foreground= c2,
               font=('Arial', 10, 'italic', 'bold',)
               )

l1.place(x= 150, y= 2)

plot_button = tk.Button(root, text="Plot", command=plot_btn ,
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


lb2 = ttk.Label(text="Choose an encoding technique: ",
                background= bg_color,
                foreground= c2,
                font=('Arial', 10, 'italic', 'bold',),
                )
lb2.place(x= 150, y= 44)

entry = ttk.Entry(root, width=50)
entry.place(x = 150, y = 24)



root.mainloop()