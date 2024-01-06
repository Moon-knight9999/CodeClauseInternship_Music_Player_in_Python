import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x600")
canvas.config(bg='black')

rootpath = "C:\\Users\Harini\Music\songs"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="prev_img.png")
stop_img = tk.PhotoImage(file="stop_img.png")
play_img = tk.PhotoImage(file="play_img.png")
pause_img = tk.PhotoImage(file="pause_img.png")
next_img = tk.PhotoImage(file="next_img.png")

def select(event=None):
    selected_song = listBox.get("active")
    label.config(text=selected_song)
    mixer.music.load(os.path.join(rootpath, selected_song))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    current_selection = listBox.curselection()
    if current_selection:
        current_selection = current_selection[0]
        next_song = (current_selection + 1) % listBox.size()
        listBox.select_clear(current_selection)
        listBox.activate(next_song)
        listBox.select_set(next_song)
        select()

def play_prev():
    current_selection = listBox.curselection()
    if current_selection:
        current_selection = current_selection[0]
        prev_song = (current_selection - 1) % listBox.size()
        listBox.select_clear(current_selection)
        listBox.activate(prev_song)
        listBox.select_set(prev_song)
        select()

def pause_song():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"

listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('DS-Digital', 14))
listBox.pack(padx=15, pady=15)
listBox.bind('<Double-Button-1>', lambda event: select(event))

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('DS-Digital', 14))
label.pack(pady=15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg='black', borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="play", image=play_img, bg='black', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="pause", image=pause_img, bg='black', borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="next", image=next_img, bg='black', borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
