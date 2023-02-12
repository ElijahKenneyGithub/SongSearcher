import tkinter as tk
import urllib.parse
from tkinter import ttk, Entry
from tkinter import *
from tkinter import messagebox
import webbrowser

# creating the main window
root = tk.Tk()
root.title("Song Searcher")
root.iconbitmap("icon.ico")
root.geometry("500x500")
root.resizable(0, 0)

# creating the top frame
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP)
top_frame.config(bg="black")

# creating the bottom frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM)
bottom_frame.config(bg="black")

# creating the song input
song_label = tk.Label(top_frame, text="Song:", bg="black", fg="white")
song_label.pack(pady=10)
song_input = tk.Entry(top_frame, width=50)
song_input.pack()
song_input.focus()

# creating the artist input
artist_label = tk.Label(top_frame, text="Artist:", bg="black", fg="white")
artist_label.pack(pady=10)
artist_input = tk.Entry(top_frame, width=50)
artist_input.pack()

search_history = []
# creating the search button
def search_song():
    song = song_input.get()
    artist = artist_input.get()
    if not song or not artist:
        messagebox.showerror("Error", "Please enter a song and an artist.")
        return
    url = f"https://www.youtube.com/results?search_query={song}+{artist}"
    webbrowser.open(url)

search_button = tk.Button(bottom_frame, text="Search", command=search_song)
search_button.pack(pady=20)


root.mainloop()



