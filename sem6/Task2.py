from tkinter import *
from tkinter import ttk


def calculate(*args):
    ##try:
        value1 = float(feet1.get())
        value2 = float(feet2.get())
        imt.set(value1/(value2**2))
        imt1 = imt.get()
        imt2 = float(imt1)
        if imt2 < 16:
            text1 = "Severe body mass deficit"
        elif imt2 < 18.5:
            text1 = "Body mass deficit"
        elif imt2 < 25:
            text1 = "Normal body mass"
        elif imt2 < 30:
            text1 = "Excessive body weight"
        elif imt2 < 35:
            text1 = "Obesity grade 1"
        elif imt2 < 40:
            text1 = " Obesity grade 2"
        elif imt2 > 40:
            text1 = " Obesity grade 3"
        text.set(text1)
    ##except ValueError:
        ###pass
root=Tk()
root.title("IMT")



mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet1 = StringVar()
feet1_entry = ttk.Entry(mainframe, width=7, textvariable=feet1)
feet1_entry.grid(column=1, row=2, sticky=(W, E))

feet2 = StringVar()
feet2_entry = ttk.Entry(mainframe, width=7, textvariable=feet2)
feet2_entry.grid(column=2, row=2, sticky=(W, E))

imt = StringVar()
ttk.Label(mainframe, textvariable=imt).grid(column=3, row=2, sticky=(W, E))
text = StringVar()
ttk.Label(mainframe, textvariable=text).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text = "Calculate", command=calculate).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Your parameters").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="means that you have").grid(column=1, row=3, sticky=E)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet1_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()