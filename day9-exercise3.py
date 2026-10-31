person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:
    print (person['skills'][2])
    if "Python" in person["skills"]:
        print("This person has python skills")


if "JavaScript" in person['skills'] and "React" in person['skills']:
    print("He is a front end developer")
elif "Node" in person['skills'] and "Python" in person['skills'] and "MongoDB" in person['skills']:
    print("He is a back end developer")
elif "React" in person['skills'] and "Node" in person['skills'] and "MongoDB" in person['skills']:
    print("He is a fullstack developer")
else:
    print("Unknown Title") 

full_name = person['first_name'] + " " + person['last_name']
print(full_name)

if person['is_married'] and person['country'] == "Finland":
    print(f"{full_name} lives in Finland. He is married.")