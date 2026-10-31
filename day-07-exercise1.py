# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Find the length of the set it_companies
length = len(it_companies)
print(length)
#2 Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#3 Insert multiple IT companies at once to the set it_companies
it_companies.update(["MLPT", "Samsung", "X"])
print(it_companies)
#4 Remove one of the companies from the set it_companies

#5 What is the difference between remove and discard
    #Remove raises an error when the item that is chosen to be removed cant be found, while discard doesnt
