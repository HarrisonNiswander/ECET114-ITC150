#Harrison Niswander
#ECET 114 / ITC 150
#8-27-26
#This program will deal with input from users and how to obtain it

#--------------------------------------------------------------------------------------------

# General format for obtaining input from users:
#       variable = input("prompt")
#   
#       where:      variable = where the user's input is stored
#                   prompt = what the user sees when they are prompted for input
#                   input =  built in python function 

# -------------------------------------------------------------------------------------------- 

# Homework 1 - Exercise #2
# Objective: Ask the user for their name and age, then print a message repeating it back

# Start by creating an outline for what we need to do

# Create a variable to store the user's name and age

# Create a prompt to ask the user for their name and age

# Obtain input(s) from the user

# Print a message repeating the user's name and age back to them

#--------------------------------------------------------------------------------------------

# Homework 1 - Exercise #2
# Objective: Ask the user for their name and age, then print a message repeating it back

# Create a variable to store the user's name and age
name = ""
age = 0

# Create a prompt to ask the user for their name and age
namePrompt = "Please enter your name: "
agePrompt = "Please enter your age: "

# Obtain input(s) from the user
name = input(namePrompt)
age = int(input(agePrompt))

# Print a message repeating the user's name and age back to them
#print("Hello, " name "! You are " age " years old.")
print("Hello, ", name ,"! You are ", age ," years old.")

#--------------------------------------------------------------------------------------------