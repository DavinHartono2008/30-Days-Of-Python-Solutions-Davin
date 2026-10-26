#1 Create an empty tuple
tup = ()
#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Jenny", "Jennifer", "Lily")
brothers = ("Darren", "Ben", "William")
#3 Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
#4 How many siblings do you have?
print(f"I have {len(siblings)} siblings.")
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Mom", "Dad")
siblings = list(siblings)
siblings.append("Selena")
siblings = tuple(siblings)
family_members = parents + siblings
print(family_members)
