
from mimetypes import init
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

n = int(input("How many enemies? "))

for i in range(n):
    names.append(input("Enter name: "))
    initiatives.append(int(input("Enter initiative: ")))

rolledin = []

for i in range(len(initiatives)):
    rolledin.append(randint(1, 20) + initiatives[i])

print(initiatives)
print(names)
print(rolledin)

for i in range(len(names)):
    for j in range(len(names) - i - 1):
        if rolledin[j] < rolledin[j+1]:
            temp1 = rolledin[j]
            temp2 = names[j]
            rolledin[j] = rolledin[j+1]
            rolledin[j+1] = temp1
            names[j] = names[j+1]
            names[j+1] = temp2


print("Turn order:")

for i in range(len(names)):
    print(names[i], rolledin[i])

input()
