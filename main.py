import os.path

def readAndWrite(inputFile, pathname):

    f = open(inputFile, 'r')

    convo = f.readlines()

    users = []
    lines = []
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
            print(matches)

            filename = os.path.join(pathname, str(users[list(matches.keys())[0]] + " " + users[list(matches.keys())[1]] + ".txt"))

            speaker = str(users[min(matches, key=matches.get)])

            if filename not in filenames:
                filenames.append(filename)
                o = open(filename, "w")

            else:
                o = open(filename, "a")


            o.write(speaker + a_line.split(")", 1)[1])
            o.close()
        

    f.close()

if __name__ == '__main__':
   readAndWrite("example.txt", r"C:\Users\kkate\Downloads\\")
