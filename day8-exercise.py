#1 Create an empty dictionary called dog
dog = {}
#2 Add name, color, breed, legs, age to the dog dictionary
dog = {
    "Name": "",
    "Breed": "",
    "Legs": 4,
    "Age": 0
}
#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "First_name" : "Davin",
    "Last_name" : "Hartono",
    "Gender" : "Male",
    "Age" : 17,
    "Marital_Status" : False,
    "Skills" : ["Python", "Badminton", "Guitar"],
    "Country" : "Indonesia",
    "City" : "Jakarta",
    "Address" : "Home"
}
#4 Get the length of the student dictionary
print(len(student))
#5 Get the value of skills and check the data type, it should be a list
Student_Skills  = student.get("Skills")
print(Student_Skills)
print(type(student.get("Skills")))
#6 Modify the skills values by adding one or two skills
student["Skills"].append("Cooking")
print(student.get("Skills"))
#7 Get the dictionary keys as a list
print(student.keys())
#8 Get the dictionary values as a list
print(student.values())
#9 Change the dictionary to a list of tuples using items() method
print(student.items())
#10 Delete one of the items in the dictionary
del student["Address"]
#11 Delete one of the dictionaries
del dog