'''newFile = open("newfile.txt", "w")
with open('randomdata.txt','r') as file:
    x =[]
    y = []
    for line in file:
        x.append(int(line.split()[0]))  # 0 index bc that is the first position --> like a list
        y.append(int(line.split()[1]))  # 1 index bc that is the second position
    newx = []
    newy = []
    for i in x:
        value = 5 * i + 2
        newx.append(value)
    for j in y:  # j to not make any mistakes or confusion
        value = 5 * j + 2
        newy.append(value)
    for index in range(len(newx)):  # to be sure you get all the values in list
        newFile.write(str(newx[index]) + " " + str(newy[index]) + "\n")
newFile.close()'''

# Activity 2
listing = [2, 3, 4, 56, 10, 5, 44]
with open('newfile.txt', 'w') as f:
    for num in listing:
        f.write(str(num))
        f.write('\n')
with open('newfile.txt', 'r') as fr:
    print(fr.read())




