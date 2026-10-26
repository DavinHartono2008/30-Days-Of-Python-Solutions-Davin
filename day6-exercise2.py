sisters = ("Jenny", "Jennifer", "Lily")
brothers = ("Darren", "Ben", "William")
siblings = sisters + brothers
parents = ("Mom", "Dad")
family_members = parents + siblings

#1 Unpack siblings and parents from family_members
Mom, Dad, *little_siblings = family_members
little_siblings = tuple(little_siblings)
parents = (Mom, Dad)
print(little_siblings)
print(parents)

#2 Create fruits, vegetables and animal products tuples.
#Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("apple", "banana", "fig", "orange")
veggies = ("carrots", "potatoes", "corn", "spinach")
animal_products = ("milk", "eggs", "leather")

food_stuff_tp = fruits + veggies + animal_products
#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = (len(food_stuff_lt)//2)
print(food_stuff_lt[middle])

#5 Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[-3:])
print(food_stuff_lt[:3])

#6 Delete the food_stuff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries, 'Iceland' in nordic_countries)
