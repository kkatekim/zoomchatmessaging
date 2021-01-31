import tkinter as tk
from tkinter import filedialog, Text #help us pick the apps
import os #allows us to run the apps into our apps

root = tk.Tk()# holds the whole apps
root.title("Zoom Chat Parser")

canvas = tk.Canvas(root, height=500, width=400, bg="#b3e3ff")
canvas.pack()

def addFile():
    filename= filedialog.askopenfilename(initialdir="/" , title="select File",
    filetypes=(("text", "*.txt"), ("all files" , "*.*")))
    label = tk.Label(root, text=filename, bg="#b3e3ff", wraplength=300)
    label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
def addFolder():
    foldername= filedialog.askdirectory(initialdir="/", title="select destination folder")
    label = tk.Label(root, text=foldername, bg="#b3e3ff", wraplength=300)
    label.place(relx=0.5, rely=0.42, anchor=tk.CENTER)


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


openFile = tk.Button(frame, text="Open File",
fg="#0073B4", bg="#b3e3ff", command = addFile, highlightbackground ="#b3e3ff"
, activebackground="#99daff", activeforeground="#005180") #figure out how to change location
openFile.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

selectFile = tk.Button(frame, text="Select Destination folder", padx=10,
pady=5, fg="#0073B4", bg="#b3e3ff", command = addFolder, highlightbackground ="#b3e3ff"
, activebackground="#99daff", activeforeground="#005180")
selectFile.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

run = tk.Button(frame, text="Create TextFiles", padx=10,
pady=5, fg="#0073B4", bg="#b3e3ff", highlightbackground = "#b3e3ff"
, activebackground="#99daff", activeforeground="#005180") #figure out how to change location
run.place(relx=0.5, rely=0.75, anchor=tk.CENTER)



root.mainloop()
