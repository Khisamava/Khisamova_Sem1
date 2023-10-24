from tkinter import *
from tkinter import ttk

def Color(*args):
    try:
        color1 = str(color.get())
        xx = int(color1[1:3], 16)
        yy = int(color1[3:5], 16)
        zz = int(color1[5:], 16)
        aa = hex(255 - xx)[2:]
        if len(aa) < 2:
            aa = '0' + aa
        bb = hex(255 - yy)[2:]
        if len(bb) < 2:
            bb = '0' + bb
        cc = hex(255 - zz)[2:]
        if len(cc) < 2:
            cc = '0' + cc
        color2 = '#' + aa + bb + cc
        comp_color.set(color2)

    except ValueError:
        pass

root = Tk()
root.title("Color Aesthetics")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

color = StringVar()
color_entry = ttk.Entry(mainframe, width=7, textvariable=color)
color_entry.grid(column=2, row=2, sticky=(W, E))

comp_color = StringVar()
ttk.Label(mainframe, textvariable=comp_color).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Paint my life", command=Color).grid(column=3, row=2, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
color_entry.focus()
root.bind("<Return>", Color)

root.mainloop()
