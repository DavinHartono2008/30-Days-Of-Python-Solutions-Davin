#No1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

#No2
my_age = 17
your_age = int(input("Enter your age: "))
if your_age > my_age:
    if (your_age-my_age) == 1:
        print("You are a year older than me")
    else:
        print(f"You are {your_age-my_age} years older than me")
else:
    if (my_age-your_age) == 1:
        print("You are a year younger than me")
    else:
        print(f"You are {my_age-your_age} years younger than me")

#No3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is bigger than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print("The numbers are equal")
