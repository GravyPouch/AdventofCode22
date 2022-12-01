f = open('data.txt', 'r')

count = 0

elfs = []

elfTotal = 0

while True:
    count += 1

    line = f.readline()

    if not line:
        break
    currentLine = line.strip()
    if  currentLine == "":
        elfs.append(elfTotal)
        print("Total: ",elfTotal)
        elfTotal = 0
    else:
        elfTotal += int(line)
       
f.close()

elfs.sort()

print("The most caloric Elf: ",elfs[-1])

print("The top 3 most caloric Elfs: ",elfs[-1] + elfs[-2] + elfs[-3] )