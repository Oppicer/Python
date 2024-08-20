import os

path = open("C:\\Users\\Turnb\Desktop\\Bill.txt", "r")
name0 = "virus_V"
i = 0
text = path.read()
path.close()
while i < 20:
    name = name0 + str(i)
    with open("C:\\Users\\Turnb\Desktop\\" + name + ".txt", "w" ) as file:
        file.write(text)
    i += 1




