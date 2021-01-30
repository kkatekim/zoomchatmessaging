import tkinter as tk
from tkinter import filedialog, Text #help us pick the apps
import os #allows us to run the apps into our apps

root = tk.Tk()# holds the whole apps
root.title("Zoom Chat Parser")

def addFile():
    filename= filedialog.askopenfilename(initialdir="/" , title="select File",
    filetypes=(("text", "*.txt"), ("all files" , "*.*")))
    label = tk.Label(frame, text=filename, bg="#99daff")
    label.pack()
def addFolder():
    foldername= filedialog.askdirectory(initialdir="/", title="select destination folder")
    print(foldername)
canvas = tk.Canvas(root, height=400, width=300, bg="#D8F1FF")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


openFile = tk.Button(frame, text="Open File", padx=10,
pady=5, fg="#0073B4", bg="#D8F1FF", command = addFile, highlightbackground ="#D8F1FF"
, activebackground="#99daff", activeforeground="#005180") #figure out how to change location


selectFile = tk.Button(frame, text="Select Destination folder", padx=10,
pady=5, fg="#0073B4", bg="#D8F1FF", command = addFolder, highlightbackground ="#D8F1FF"
, activebackground="#99daff", activeforeground="#005180")

run = tk.Button(frame, text="Create TextFiles", padx=10,
pady=5, fg="#0073B4", bg="#D8F1FF", highlightbackground = "#D8F1FF"
, activebackground="#99daff", activeforeground="#005180") #figure out how to change location



openFile.pack()
selectFile.pack()
run.pack()
root.mainloop()
