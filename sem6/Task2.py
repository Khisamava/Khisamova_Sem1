from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value1 = float(feet1.get())
        value2 = float(feet2.get())
        imt.set(value1/(value2)**2)
        if imt < 16:
            text = "Severe body mass deficit"
        elif imt < 18.5:
            text = "Body mass degicit"
        elif imt < 25:
            text = "Normal body mass"
        elif imt < 30:
            text = "Excessive body weight"
        elif imt < 35:
            text = "Obesity grade 1"
        elif imt < 40:
            text = " Obesity grade 2"
        elif imt > 40:
            text = " Obesity grade 3"
        text.set()
    except ValueError:
        pass
root = Tk()
root.title("IMT")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

feet1 = StringVar()
feet1_entry = ttk.Entry(mainframe, width = 7, textvariable = feet1)
feet1_entry.grid(column = 2, row = 1, sticky = (W, E))

feet2 = StringVar()
feet2_entry = ttk.Entry(mainframe, width = 7, textvariable = feet2)
feet2_entry.grid(column = 2, row = 2, sticky = (W, E))

imt = StringVar()
ttk.Label(mainframe, textvariable = imt).grid(column = 2, row = 3, sticky = (W, E))
text = StringVar()
ttk.Label(mainframe, textvariable = text)

ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 3, row = 3, sticky = W)
ttk.Label(mainframe, text="your parameters").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="means that you have").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="health").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

feet1_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()