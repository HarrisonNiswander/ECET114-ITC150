# Harrison Niswander
# ECET 114 / ITC 150
# 9-8-26
# Homework #1 Answer Key

#--------------------------------------------------------------------------------------------
# Exercise 1
print("-------------------------------------------------------------")
print("Exercise 1: \n")

#print out hello world & name
print("Hello World! My name is Harrison Niswander!")

print("\n-------------------------------------------------------------")

#--------------------------------------------------------------------------------------------
# Exercise 2
print("Exercise 2: \n")

# Create a variable to store the user's name and age
name = ""
age = 0

# Create a prompt to ask the user for their name and age
namePrompt = "Please enter your name: "
agePrompt = "Please enter your age: "

# Obtain input(s) from the user
name = input(namePrompt)
age = int(input(agePrompt))

# ALSO GOOD - combine into 1 step
# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))

#OPTION A - GOOD
# Print a message repeating the user's name and age back to them
print("Hello, ", name ,"! You are ", age ," years old.")

#OPTION B - BETTER
print(f"Hello, {name}! You are {age} years old.")

print("\n-------------------------------------------------------------")

#--------------------------------------------------------------------------------------------
# Exercise 3
print("Exercise 3: \n")

#print welcome message
print("Welcome to Willy Wonka's Chocolate Factory!")

#gather input
order = input("What would you like? ")

#display order and message
print(f"Your order of {order} is being prepared. Please wait a moment.")

print("\n-------------------------------------------------------------")

#--------------------------------------------------------------------------------------------
# Exercise 4
print("Exercise 4: \n")

#obtain user input of cookies wanted
cookies = int(input("Please enter in a quantity of cookies: "))

#convert cookies to miles
miles = (cookies / 1.23) + (15 * 1.1)

#print cookies to miles convertion results
print("Your inputed quantity of cookies is equal to ", miles, "miles")
print(f"Your inputed quantity of cookies is approximately equal to {miles:.2f} miles")
    # Exercise 5 - Part B

print("\n-------------------------------------------------------------")

#--------------------------------------------------------------------------------------------
# Exercise 5 Part A
print("Exercise 5 - Part A: \n")

#define animals
animal1 = "Dog"
animal2 = "Cat"
animal3 = "Alligator"
animal4 = "Velociraptor"
animal5 = "Ox"
animal6 = "Horse"
animal7 = "German Shepard"

#right align animals
print(f"*** {animal1:>14} ***")
print(f"*** {animal2:>14} ***")
print(f"*** {animal3:>14} ***")
print(f"*** {animal4:>14} ***")
print(f"*** {animal5:>14} ***")
print(f"*** {animal6:>14} ***")
print(f"*** {animal7:>14} ***")

print("\n-------------------------------------------------------------")

#--------------------------------------------------------------------------------------------
# Exercise 5 - Part B
# Line below is answer but should be with exercise 4 like instructed
#print(f"Your inputed quantity of cookies is approximately equal to {miles:.2f} miles")