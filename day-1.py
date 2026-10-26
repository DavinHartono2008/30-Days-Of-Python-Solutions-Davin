import math

# Day 1 - 30DaysOfPython Challenge, Level 2

#No 2
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

#No 3
print("Davin")
print("Hartono")
print("Indonesia")
print("I am enjoying 30 days of python")

#No 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Davin"))
print(type("Hartono"))
print(type("Indonesia"))

# Day 1 - 30DaysOfPython Challenge, Level 3

#No. 1
"""
Examples:
1. Numbers:
a) Integer = 1,2,3,4,5
b) Float = 3.14,2.17,3.1,2.3,16.2
c) Complex = 4-2j
2. String = "Hello World"
3. Boolean = True, False
4. List = ["Apple", "Banana", "Pineapple", "1", "2", "3"]
5. Tuple = ("Jakarta", "Banten", "Bandung") #Places in Indonesia
6. Set = {1,2,3,4,5}
7. Dictionary = 
my_dict={
    "First_Name": "Davin",
    "Last_Name": "Hartono",
    "Age" = 17,
    "Occupation" = "Student",
    "School" = "Narada",
    "Hobbies" = ["Badminton", "Programming", "Guitar"]
}
"""

#No.2 Find an Euclidean distance between (2, 3) and (10, 8)

ed = math.sqrt(((2-10)**2)+(3-8)**2)
print(ed)
