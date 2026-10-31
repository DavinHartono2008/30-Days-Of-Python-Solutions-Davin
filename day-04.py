"""
words = ['Thirty', "Days", "Of", "Python"]
newstring = " ".join(words)
print(newstring)

words2 = ['Coding', "For", "All"]
newstring2 = " ".join(words2)
print(newstring2)
"""

company = "Coding For All"
print(company, len(company), company.upper(), company.lower(), company.capitalize(), company.title(), company.swapcase()
      , sep="\n")

wo_first_word = company[7:15]
print(wo_first_word)

print("Coding" in company)

print(company.replace("coding",  "python"))

random_word = "Python For Everyone"
print(random_word.replace("Everyone", "All"))

print(company.split(sep=" "))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
Companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(Companies.split(sep=","))

print(company[0],company[-1],company[10])

words = ["Python For Everyone",  'Coding For All']
for i in range(2): #Goes through the 2 words
      for j in range(len(words[i])):
            if words[i][j].isupper():
                  print(words[i][j],end="")
      print("")

print(words[1].find("C"),words[1].find("F"),"Coding For All People.".find("l"))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"),sentence.rfind("because"))
print(sentence[31:54])

#Does 'Coding For All' start with a substring Coding?
print(words[1].startswith("Coding"))
#Does 'Coding For All' end with a substring coding?
print(words[1].endswith("Coding"))

word = '   Coding For All      '  #remove the left and right trailing spaces in the given string.
print(word.strip(" "))

sentences = ["30DaysOfPython", "thirty_days_of_python"]
print(sentences[0].isidentifier(), sentences[1].isidentifier())

items = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(items))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name", "Age", "Country", "City", sep="\t")
print("Asabeneh", 250, "Finland", "Helsinki", sep="\t")

print("radius = {}".format(10))
print("area = {} * {} ** {}".format(3.14, "radius", 2))
print("The area of a circle with radius {} is {} meters square".format(10, 314))

"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

a = 8
b = 6

print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {}".format(a,b,a/b))
print("{} % {} = {}".format(a,b,a%b))
print("{} // {} = {}".format(a,b,a//b))
print("{} ** {} = {}".format(a,b,a**b))
