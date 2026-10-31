#1 Declare an empty list
lst = []
#2 Declare a list with more than 5 items
lst2 = [1, 2, 3, 4, 5, 6, 7]
#3 Find the length of your list
print(len(lst2))
#4 Get the first item, the middle item and the last item of the list
print(lst2[0],lst2[int(len(lst2)/2)],lst2[-1])
#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Davin", 17, "178", False, "Jakarta"]
#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7 Print the list using print()
print(it_companies)
#8 Print the number of companies in the list
print(len(it_companies))
#9 Print the first, middle and last company
print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])
#10, 11 Print the list after modifying one of the companies, Add an IT company to it_companies
it_companies[1] = "ASUS"
print(it_companies)
#12 Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2), "MLPT")
#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)
#14 Join the it_companies with a string '#;  '
result = "#; ".join(it_companies)
print(result)
"""
#15 Check if a certain company exists in the it_companies list.
company_check = input("Company name: ")
print(company_check in it_companies)
"""
#16 Sort the list using sort() method
it_companies.sort()
print(it_companies)
#17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
#18 Slice out the first 3 companies from the list
print(it_companies[:3]) #[start:end]
#19 Slice out the last 3 companies from the list
print(it_companies[-3:]) 
#20 Slice out the middle IT company or companies from the list
print(it_companies[3:5])
#21 Remove the first IT company from the list
del it_companies[0]
#22 Remove the middle IT company or companies from the list
del it_companies[3:5]
#23 Remove the last IT company from the list
del it_companies[-1]
#24 Remove all IT companies from the list
it_companies.clear()
#25 Destroy the IT companies list
del it_companies
#26 Join the following lists: 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end
new_langauges = ["Python", "SQL"]
full_stack.extend(new_langauges)
print(full_stack)
