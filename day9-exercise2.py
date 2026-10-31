#No1
"""
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F

"""

score = int(input("Enter score: "))
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif score > 100:
    print("Error")
    exit()
else:
    grade = "F"

print(grade)


#No2

Season = input("Current season: ").lower()

if Season in ("september", "october", "november"):
    print("The current season is autumn")
elif Season in ("december", "january", "february"):
    print("The current season is winter")
elif Season in ("march", "april", "may"):
    print("The current season is spring")
else:
    print("The current season summer")

#No3

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")
if fruit not in fruits:
    fruits.append(fruits)
    print(fruits)
else:
    print("That fruit already exist in the list")