import tkinter as tk
from tkinter import filedialog, Text #help us pick the apps
import os #allows us to run the apps into our apps

root = tk.Tk()# holds the whole apps

def addFile():
    filename= filedialog.askopenfilename(initialdir="/" , title="select File",
    filetypes=(("text", "*.txt"), ("all files" , "*.*")))

canvas = tk.Canvas(root, height=400, width=300, bg="#D8F1FF")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


openFile = tk.Button(frame, text="Open File", padx=10,
pady=5, fg="#0073B4", bg="#D8F1FF", command = addFile, highlightbackground ="#D8F1FF") #figure out how to change location
run = tk.Button(frame, text="Create TextFiles", padx=10,
pady=5, fg="#0073B4", bg="#D8F1FF", highlightbackground = "#D8F1FF") #figure out how to change location

openFile.pack()
run.pack()
root.mainloop()
