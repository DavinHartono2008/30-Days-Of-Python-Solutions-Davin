#No1
sum = 0

for i in range(101):
    sum += i 


print(f"The sum of all numbers is {sum}.")

#No2
sumodd = 0
sumeven = 0

for i in range(0,101,2):
    sumeven += i
for i in range(101):
    if i % 2 != 0:
        sumodd += i
print(f"The sum of all evens is {sumeven}. And the sum of all odds is {sumodd}")