# Exercises - Day 3

import math

age = 17
height = 178.4
complex_number = 3-2j

#script that prompts the user to enter base and height of triangle and calculate its area

t_base = int(input("Enter base: "))
t_height = int(input("Enter height:"))
t_area = (t_base*t_height)/2
print(f"The area of the triangle is {t_area}")

#Script that prompts the user to enter sides of triangle and calculate its perimeter
t_sideA = int(input("Enter side a of triangle:"))
t_sideB = int(input("Enter side b of triangle:"))
t_sideC = int(input("Enter side c of triangle:"))
t_perimeter = t_sideB + t_sideA + t_sideC
print(f"The total perimeter of your triangle is {t_perimeter}")

#Get length and width of a rectangle using prompt. Calculate area and perimeter.
r_length = int(input("Enter rectangle length: "))
r_width = int(input("Enter rectangle width: "))
r_area = r_width * r_length
r_perimeter = 2*(r_length+r_width)
print(f"The area of your rectangle is {r_area}")
print(f"The perimeter of your rectangle is {r_perimeter}")

#Get radius of a circle using prompt. Calculate the area and perimeter
r = int(input("Enter the radius of circle"))
c_area = math.pi * r**2
c_perimeter = 2*math.pi*r
print(f"Your circle's area is {c_area}, circumference is {c_perimeter}")

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope1 = 2
x_int1 = 1
y_int1 = -2

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope2 = int((10-2)/(6-2))
d = math.sqrt((2-6)**2 + (2-10)**2)

print(f"slope 1 is {slope1}, while slope2 is {slope2}, and the distance between (2,2) and (6,10) is {d}")

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values.
#Figure out at what x value y is going to be 0.

experimenting = True

while experimenting:
    x = int(input("Enter the value of x: "))
    y = (x**2 + 6*x + 9)
    print(y)
    cont = input("Continue? (Yes/No)").lower()
    if cont == "no":
        exit()
    else:
        pass

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
l1 = len("python")
l2 = len("dragon")

print(l1!=l2)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in "python" and "on" in "dragon")

print('jargon' in 'I hope this course is not full of jargon')

print('no' not in "python" and 'no' not in "dragon")

#Find the length of the text python and convert the value to float and convert it to string
py_length = len("python")
py_float = float(py_length)
py_string = str(py_float)
print(py_string)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
mynum = int(input("Enter a number: "))

if mynum % 2 ==0:
    print("Number is even")
else:
    print("Number is odd")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
checknumber = 7//3

print(checknumber == int(2.7))

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#Check if int('9.8') is equal to 10
print(int(9.8) == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
work_hours = int(input("Hours work: "))
rate_hours = int(input("Rate per hour: "))
print(f"Your weekly earnings are: {work_hours*rate_hours}")

#Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = int(input("Enter numbers of years lived: "))
print(f"You have lived for {years_lived*31536000}")

for i in range(1,6):
    print(i,end=" ")
    for j in range(0,4):
        print(i**j, end=" ")
    print("")
