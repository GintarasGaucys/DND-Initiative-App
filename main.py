from random import randint

f = open("default.txt", "r")

names = []
initiatives = []

for i in f:
    if (i[0][0] == "/"):
        continue
    data = i.split(", ")
    names.append(data[0])
    initiatives.append(int(data[1]))

done = 'n'

while(done == 'n'):
    names.append(input("Enter name: "))
    initiatives.append(int(input("Enter initiative: ")))
    done = str(input("Is that it? (y/n) "))

rolledin = []

for i in range(len(initiatives)):
    rolledin.append(randint(1, 20) + initiatives[i])

for i in range(len(names)):
    for j in range(len(names) - i - 1):
        if rolledin[i] < rolledin[i+1]:
            temp1 = rolledin[i]
            temp2 = names[i]
            rolledin[i] = rolledin[i+1]
            rolledin[i+1] = temp1
            names[i] = names[i+1]
            names[i+1] = temp2


print("Turn order:")

for i in range(len(names)):
    print(names[i], rolledin[i])
