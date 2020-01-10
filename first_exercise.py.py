from math import sqrt

# Exercise (slide 9)
friends = 7
budget = 150
msg = "I am going with 7 friends"
meal_cost = 14

total_meal_price = meal_cost * friends
# 15% tip
total_cost = total_meal_price * 1.5

print("\nTotal cost is " + str(total_cost) + " and budget is " + str(budget))

if (total_cost > budget):
	print("Cannot afford :(")
else:
	print("Can afford :)")
	
	
# Functions
def multiply(x, y):
	return x*y

print('\nThe result of the multiplication is ', multiply(2,7), '\n')


# Lists
l = [1, 2.0, 'xyz', sqrt(37), str(2)+' Towels']
print("Our list: ", l)
print("First element: ", l[0])
print("Last element: ", l[-1])
print("Prints every two elements: ", l[::2])
print("Prints in reverse order: ", l[::-1])
print("Prints elements starting from the 4th one, in the third index: ", l[3:], '\n')


# Changes in the copied list result in the same changes in the original list and vice-versa
l2 = l
l2[0] = '1337'
l2[1] = 21
l[2] = 'abc'
l.append('last')
print(l2)
print(l)
# In order to create a copy of a list that does not change the original list as it goes through
#  changes, we can use the copy() function to do so.
l3 = l.copy()


# Exercise (slide 18)
neighbors = ['John', 'Jack']
missing = []
missing.append('Mike')
missing.append('Boris')
people = neighbors + missing	
print("\nNeighbors and people I am missing are: ", people, '\n')


# List Comprehension -> Quick way of creating lists in Python
squares = [i**2 for i in range(3, 10)] # OBS: range(10) is inclusive on the left side 
										# and exclusive on the right side
print(squares)

# Finds the indexes where this calculation does not output 0
# I used the built-in enumerate() function which returns both the index and the value
# of the current iteration.
zeroes = [1/x*x - 1 for x in range(1,100)]
for index, number in enumerate(zeroes):
	if (number != 0):
		print("Failed at index ", index)
		
		

# Tuples are NON-MUTABLE lists
b = (0, 1, 2, 3, 4, 5)
b[1]
# b[1] = -1   would produce the following error: "TypeError: 'tuple' object 
			# does not support item assignment"

			

# Dictionaries (maps)
d = {'name': 'Kong Ming', 'power': 7}
print('\ndict:\n', d)
print('Name is', d['name'], 'and their power is', d['power'])