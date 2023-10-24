from tkinter import *
from tkinter import ttk
import pandas as pd
import random


films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])

complex_genres = []
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(film_genre)
for genre in complex_genres:
    film_genres_list.remove(genre)
genres_set = set(film_genres_list)

def choose(*args):
    try:
        value = film.get()
        films_filtered = films[films["Genre"].str.contains(value)]
        films_titles = list(films_filtered["Title"])
        filmfilm1 = random.choice(films_titles)
        filmfilm.set(filmfilm1)
    except ValueError:
        pass


root = Tk()
root.title("Random film")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

film = StringVar()
film_entry = ttk.Entry(mainframe, width=7, textvariable=film)
film_entry.grid(column=2, row=2, sticky=(W, E))

filmfilm = StringVar()
ttk.Label(mainframe, textvariable=filmfilm).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Choose", command=choose).grid(column=3, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Choose your genre").grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Your destiny for today is").grid(column=1, row=3, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
film_entry.focus()
root.bind("<Return>", choose)

root.mainloop()
