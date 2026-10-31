#No1

for i in range(11):
    print(i, end=" ")

print("")

i = 0
while i < 11:
    print(i, end=" ")
    i += 1
print("")

#No2

for i in range(10,-1,-1):
    print(i, end=" ")
print("")
i = 10
while i > -1:
    print(i, end=" ")
    i -= 1
print("")

#No3
for i in range(8):
    for j in range(i):
        print("*", end="")
    print("")

#No4
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print("")

#No5
for i in range(11):
    print(f"{i} x {i} = {i*i}")

#No6
list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for items in list:
    print(items)

#No7
for i in range(0,101,2):
    print(i, end=" ")

print("")
#No8
for i in range(0,101):
    if i % 2 != 0:
        print(i, end=" ")