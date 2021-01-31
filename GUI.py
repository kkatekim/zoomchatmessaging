import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, Text #help us pick the apps
import os #allows us to run the apps into our apps

root = tk.Tk()# holds the whole apps
root.title("Zoom Chat Parser")

canvas = tk.Canvas(root, height=800, width=700, bg="#b3e3ff")
canvas.pack()

def addFile():
    global f
    filename= filedialog.askopenfilename( initialdir="/" , title="select File",
    filetypes =(("text", "*.txt"), ("all files" , "*.*")))
    f= open(filename, 'r')
    label = tk.Label(root, text=filename, bg="#b3e3ff", wraplength=600)
    label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

def addFolder():
    global foldername
    foldername= filedialog.askdirectory(initialdir="/", title="select destination folder")
    label = tk.Label(root, text=foldername, bg="#b3e3ff", wraplength=600)
    label.place(relx=0.5, rely=0.42, anchor=tk.CENTER)


def readAndWrite():


    convo = f.readlines()

    users = []
    filenames = []

    #finds all private messages
    for a_line in convo:

        x = a_line.replace("(", " ", 1).split()

        if "Direct Message" in a_line:

            name1 = [x[i] for i in range(x.index("From")+1, x.index("to"))]
            name2 = [x[i] for i in range(x.index("to")+1, x.index("Direct"))]

            if " ".join(name1) not in users:
                users.append(" ".join(name1))

            if " ".join(name2) not in users:
                users.append(" ".join(name2))

            matches = {users.index(y):a_line.find(y) for y in users if y in a_line}

            filename = os.path.join(foldername, str(users[list(matches.keys())[0]] + " " + users[list(matches.keys())[1]] + ".txt"))

            speaker = str(users[min(matches, key=matches.get)])

            if filename not in filenames:
                filenames.append(filename)
                o = open(filename, "w")

            else:
                o = open(filename, "a")

            o.write(speaker + a_line.split(")", 1)[1])
            o.close()

    f.close()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)



pil_img = Image.open("pic.jpg")
img = ImageTk.PhotoImage(pil_img.resize((700, 800), Image.ANTIALIAS))
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)



openFile = tk.Button(frame, text="Open File", padx=10, pady=5,
fg="#0073B4", bg="#b3e3ff", command = addFile, highlightbackground ="#b3e3ff"
, activebackground="#99daff", activeforeground="#005180") #figure out how to change location
openFile.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

selectFile = tk.Button(frame, text="Select Destination folder", padx=10,
pady=5, fg="#0073B4", bg="#b3e3ff", command = addFolder, highlightbackground ="#b3e3ff"
, activebackground="#99daff", activeforeground="#005180")
selectFile.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

run = tk.Button(frame, text="Create TextFiles", padx=10,
pady=5, fg="#0073B4", bg="#b3e3ff", highlightbackground = "#b3e3ff"
, activebackground="#99daff", activeforeground="#005180", command=readAndWrite) #figure out how to change location
run.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

root.mainloop()
