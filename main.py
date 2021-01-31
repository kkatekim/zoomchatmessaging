
def readAndWrite(inputFile, outputFile):

    f = open(inputFile, 'r')
    o = open(outputFile, 'w')

    convo = f.readlines()

    name1 = input("Please enter the first and last name of first user: ")
    name2 = input("Please enter the first and last name of second user: ")

    for a_line in convo:
        if name1 or name2 in a_line:
            o.write(a_line)

    f.close()
    o.close()

if __name__ == '__main__':
    readAndWrite("meeting_saved_chat.txt", "output.txt")














