# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_lt = set(age)

if len(age_lt) > len(age):
    print("The set of ages is bigger")
elif len(age_lt) == len(age):
    print("The sets and list are the same size")
else:
    print("The set of ages is smaller")
#2 Explain the difference between the following data types: string, list, tuple and set
"""
String is a sentence, letter, or anything that's counted as a word and is denoted by the symbols ""
List is a collection of data that is indexed and mutable. lt =[item1, item2, item3]
tuples are a collection of items that are indexed but are immutable. tpl = (item1, item2)
sets are a collection of items, that arent index but are mutable. st = {item1, item2}
"""
#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# (Use the split methods and set to get the unique words.)

sentence = "I am a teacher and I love to inspire and teach people"
seperated = []

for i in range(len(sentence)):
    while sentence[i].isalpha():
        seperated.append(sentence[i])
    print("seperated")


"""
test = []
A = ["A"]
B = ["B"]

result = "".join(A + B)
test.append(result)

print(test)
"""
