#!/usr/bin/env python3

## This is the first problem set.  You task is to create and compute various variables
## and do other tricks in the code.
## Always provide suitable output by printing your results
## so that people who are familiar with the problem understand what is going on.
## 'People familiar...' include your graders and instructors and classmates,
## you do not have to cater for a random person from street
## (less context printing required if you use notebooks)

## You probably notice that these tasks are somewhat similar to your first problem sets in
## info 201.  However, now we ask you to perform these in python.

## -------------------- Defining variables --------------------
## Here we ask you to define, compute, and print a number of variables
## ---------- Example: ----------
## Create variable `my_name` that is equal to your first name
my_name = "Ott"
print("I am", my_name)
## ---------- end of the example ----------


## -------------------- 1. variables --------------------
## Using multiplication, create a variable `minutes_in_day` that is equal to the number of minutes in a day
minutes_in_day = 60 * 24
print("\nMinutes in a day:", minutes_in_day)

## Using multiplication, create a variable `hours_in_year` that is the number of hours in a year
hours_in_year = 24 * 365
print("\nHours in a year:", hours_in_year)

## Create a variable `minutes_rule` that is a logical value (True/False) by logical operations
## It should be True if there are more minutes in a day than hours in a year, otherwise False
if (minutes_in_day > hours_in_year):
    minutes_rule = True
else:
    minutes_rule = False

print("\nIt is " + str(minutes_rule) + " that there are more minutes in a day than hours in a year.")

## Compute the following a bit useful numbers.
## Assign the results to suitably named variables.
## 
## How many seconds are there in year?
seconds_in_year = 60 * minutes_in_day * 365
print("\nSeconds in a year:", seconds_in_year)

## How many seconds is a typical human lifetime?
# Source: https://www.disabled-world.com/calculators-charts/life-expectancy-statistics.php
print("\nAccording to the Disabled World website, the overall average life expectancy in the U.S. is 79 years old.")
human_lifetime_in_seconds = 79 * seconds_in_year
print("This translates to " + str(human_lifetime_in_seconds) + " seconds in total.")

## Age of the universe is 13.8 billion years.  What is it's age in seconds?
age_of_universe_in_seconds = 13800000000* seconds_in_year
print("\nAge of the universe in seconds:", age_of_universe_in_seconds)
## Comment: 435196800000000000 seconds
## If you find, based on timings on a scaled-down task, that your full task
## takes more than this many seconds on a fast computer,
## we can safely say that your code fails :-)


### ------------------------------ 2. working with lists, strings ------------------------------

## create a list 'things' that contains three things: mozarella, cinderella, salmonella
things = ['mozarella', 'cinderella', 'salmonella']
## print the list
print("\nThings in our list:", things)

## Capitalize the thing in the list that refers to a person.  Print the list
things[1] = things[1].capitalize()
print("\nThings in our list:", things)

## Put the cheese-thing in all upercase and print the list.
things[0] = things[0].upper()
print("\nThings in our list:", things)

## delete the disease element from the list.  Print the list.
del things[2]
print("\nThings in our list:", things)

## Create a list `movies` that contains the names of six movies you like
movies = ['Pulp Fiction', 'Aladdin', 'The Hateful Eight', 'Interstellar', 'Avengers: Endgame', 'Bacurau']
print("\nMy top 6 movies are:", movies)

## Create a list `top_three` that only contains the first three movies in the list.
## Use indexing and slicing!
top_three = movies[0:3]
print("\nMy top 3 movies are:", top_three)

### -------------------- 3. loops --------------------

## Using a loop, print out all the movies
print("\nMovies:")
for index, movie in enumerate(movies):
    print(" " + str(index+1) + ". "+ movie)

## Using a loop, create a new list `excited` that adds the phrase -
## " is a great movie!" to the end of each element in your movies list
##
## Hint: you need to concatenate strings
excited = []
for movie in movies:
    excited_phrase = movie + " is a great movie!"
    excited.append(excited_phrase)
print("\nList of excitement:", excited)

## Create a list `without_four` that has your first three movies, and your 5th and 6th movie.
without_four = movies.copy()
del without_four[3]
print('\nList without the 4th movie:', without_four)

## Create a list `numbers` that is the numbers 70 through 99
## note: `range()` does not give you a list.  Use a loop
## (don't use list comprehension here!)
numbers = []
for number in range(70, 100):
    numbers.append(number)
print("\nList of numbers:", numbers)

## Using the built in len function, create a variable `length` that is equal to the length of your list
## `numbers`
length = len(numbers)
print("\nLength of our 'numbers' list:", length)

## Use a loop to compute the mean value of the list.
total = 0.0
for number in numbers:
    total += number
mean_numbers = total / length
print("\nMean value of our 'numbers' list:", mean_numbers)

## Create a list `lower_numbers` containing numbers 60--69
lower_numbers = []
for number in range(60, 70):
    lower_numbers.append(number)
print("\nList of lower numbers:", lower_numbers)

## Create a list `all_numbers` that combines your `lower_numbers` and `numbers` lists
all_numbers = lower_numbers + numbers
print("\nList of all numbers:", all_numbers)

## Use loop to compute sum of numbers 1..100
total_sum = 0
for number in range(1, 101):
    total_sum += number
print("\nTotal sum of 1 to 100:", total_sum)

## Compute 100! (product of numbers 1..100)
total_product = 1
for number in range(1, 101):
    total_product *= number
print("\nTotal product of 1 to 100:", total_product)

## create a list of 20 numbers, and extract the odd numbers using slicing
list_of_numbers = list(range(1, 21))
odd_numbers = list_of_numbers[::2]
print("\nList of odd numbers:", odd_numbers)

## create a list of 10 odd numbers (use loop and range, and it's arguments)
list_of_odd_numbers = []
for number in range(11, 31):
    if (number % 2 != 0):
        list_of_odd_numbers.append(number)
print("\nList of odd numbers:", list_of_odd_numbers)

## -------------------- 4. dicts, sets

## create a dict of countries (keys) pointing to the corresponding capitals (value)
## (at least 5 countries/capitals).
countries = {'Argentina': 'Buenos Aires', 
             'Brazil': 'Brasilia', 
             'Chile': 'Santiago', 
             'Denmark': 'Copenhagen', 
             'Estonia': 'Tallinn'}

print('\nList of countries and their capitals:', countries)

## Use a loop to create an 'inverted' dict with capital (keys) pointing to a
## corresponding country (value).
## Hint: create an empty dict and add capital-coutry pairs to it.
inverted_dict = {}
for country, capital in countries.items():
    inverted_dict.update({capital: country})
    
print('\nList of capitals and their countries:', inverted_dict)

## Using these two dicts, print a table of capital, country
## where the capitals are alphabetically ordered.
## 
## Example:
## Almaty, Kazakhstan
## Beijing, China
## ...
## Wellington, New Zealand
##
## Hint: create a sorted list of all capitals using the dicts
sorted_capitals = sorted(inverted_dict)
print("\nTable of capital and country alphabetically ordered by capital name:")
for capital in sorted_capitals:
    print(capital + ", " + inverted_dict.get(capital))

## Here is a list of birthdays of 100 different people (the format is
## day of year).  How many different birthdays do we have?
birthdays = '''
206, 137,  97, 361,  62, 267, 296, 205, 183, 237, 221,  67, 265,
292, 129, 123, 104, 266, 236,  84, 124, 276, 109, 193,  31,  23,
306, 248, 195, 315,  82, 197,  11,   9, 274, 133, 143, 238, 292,
 75,  32, 257,  41,  96, 168, 295, 179,  70, 159,  19, 291, 267,
269, 250, 211, 184, 285, 187, 362, 338, 330, 104, 286, 256, 295,
 62, 347, 301, 224, 290, 279,  93, 167, 304,  80, 292, 356,  35,
320, 360,   7,  68, 192, 165, 248, 327, 290, 213,  63, 166, 206,
299,  72, 139, 256, 176, 200, 282, 193,   8
'''
## Hint: split this string into individual numbers, remove spaces, create a set
## split() method:
## "a b c".split() -> ['a', 'b', 'c']

import re
# Splits string into numbers based on multiple delimiters
list1 = re.split(', |\n', birthdays)
list1 = [element.strip() for element in list1]
for element in list1:
    # Removes non-numerical values
    if element == '':
        list1.remove(element)

# print(list1)
unique_days = set(list1)
# print("\nDifferent birthdays days:", unique_days)
print("\nNumber of different birthdays:", len(unique_days))


## create a word frequency table using dicts that take a (looong)
## string, splits it into individual words, and counts the number of
## occurrencies of each word (and prints the result).  Let's ignore
## punctuation.
##
## your code should run over individual words and increase the counter
## for that word, stored in a list.  It has to check if a word exists
## in the dictionary, and if not, take an appropriate action.
##
## Hint: use the split() method:
## "I have no clue".split() -> ['I', 'have', 'no', 'clue']
## Hint2: convert everything to lower case

string_test = 'I have no clue on what to do but I might have an idea'
word_list = string_test.split(' ')
print('\nString splitted into individual words:', word_list)

word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nOccurrence of each word in the given string:", word_count)

### -------------------- 5. Working with functions --------------------

## Write a function called `make_introduction` that takes in two arguments: name, and age. 
## This function should return a string value that says something like "Hello, my name is {name}, and I'm
## {age} years old".
## Note: it should _return_ a string, not print it!
def make_introduction(name, age):
    return "Hello, my name is " + name + " and I'm " + str(age) + " years old."

## Create a variable `my_intro` by passing your variables `my_name` and `my_age` into your `make_introduction`
## function.  Always print the result!\
my_name = 'Luiz Fernando Porto'
my_age = 21
my_intro = make_introduction(my_name, my_age)
print("\n", my_intro)

## Create a variable `casual_intro` by substituting "Hello, my name is ", with "Hey, I'm" in your `my_intro`
## variable.
## Hint: Check out str.replace and re.sub functions
casual_intro = my_intro.replace("Hello, my name is ", "Hey, I'm ")
print("\n", casual_intro)

## Write a function `RemoveDigits` that will remove all digits (i.e., 0 through 9) from all elements in a
## *list of strings*.
def RemoveDigits(list_of_strings):
    # Uses regex to remove every digit in the strings
    updated_list = [re.sub('[0-9]', '', elem) for elem in list_of_strings]
    return updated_list     

## Demonstrate that your approach is successful by passing a list of courses and other objects to your function
## For example, RemoveDigits(["INFO 201", "CSE 142", "mps-803c"])
no_digits_strings = RemoveDigits(["INFO 201", "CSE 142", "mps-803c"])
print("\n", no_digits_strings)

## Write an if/else statement that checks to see if your list has any digits left. If it does have
## digits, print "Oh no!", if it does not then print "Yay!"
for word in no_digits_strings:
    # If there are any digits in the strings
    if (re.search(r'/d', word)):
        print("Oh no!")
    else:
        print("Yay!")

### -------------------- grading --------------------

## Q1: 3pt
## Q2: 6pt
## Q3: 12pt
## Q4: 7 (capitals) + 4 (birthdays) + 7 (word frequency)
## Q5: 11pt
