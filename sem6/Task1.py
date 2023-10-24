from tkinter import *
from tkinter import ttk

def calculate1(*args):
    try:
        value1 = int(num1.get())
        value2 = int(num2.get())
        result.set(value1+value2)
    except ValueError:
        pass

def calculate2(*args):
    try:
        value1 = int(num1.get())
        value2 = int(num2.get())
        result.set(value1-value2)
    except ValueError:
        pass

def calculate3(*args):
    try:
        value1 = int(num1.get())
        value2 = int(num2.get())
        result.set(value1*value2)
    except ValueError:
        pass

def calculate4(*args):
    try:
        value1 = int(num1.get())
        value2 = int(num2.get())
        result.set(value1//value2)
    except ValueError:
        pass

def calculate5(*args):
    try:
        value1 = int(num1.get())
        value2 = int(num2.get())
        result.set(value1%value2)
    except ValueError:
        pass

root = Tk()
root.title("Calculater")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

num1 = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=num1)
feet_entry.grid(column=1, row=1, sticky=(W, E))

num2 = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=num2)
feet_entry.grid(column=2, row=1, sticky=(W, E))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="+", command= calculate1).grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="-", command = calculate2).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="*", command= calculate3).grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="//", command = calculate4).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="%", command = calculate5).grid(column=3, row=2, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.mainloop()

