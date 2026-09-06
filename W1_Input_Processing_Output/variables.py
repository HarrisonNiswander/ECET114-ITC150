#Harrison Niswander
#ECET 114 / ITC 150
#8-27-26
#This program will go variables and their rules

#--------------------------------------------------------------------------------------------

#when creating an assignment statement:
#       variable = expression           (MUST ASSIGN A VALUE TO A VARIABLE FROM LEFT TO RIGHT)

#Practice creating variables
#10 = bananas       
    # Must assign value to variables
apples = 10
oranges = 15

#print variables
print("oranges")        
    #won't print the value of orangles, will print the string "oranges"
print(oranges)
print(apples)

#--------------------------------------------------------------------------------------------

#variables are case sensitive!!!
tree = 2
#print(Tree)
    # Variables are case sensitive, so Tree is not the same as tree
print(tree)

#--------------------------------------------------------------------------------------------

#variable naming rules:
    #1 Variable names must begin with a letter (lower or upper) or an underscore
    #2 Variable names cannot contain spaces
    #3 Variable names can contain letters, numbers, and underscores
    #4 Variable names cannot be Python keywords (ex print, etc.)

#Allowed
    #_variable
    #variable12
    #_a_b_c_12

#Not Allowed
    #12variable
    #variable 12
    #variable-12
    #print

#Variables should contain descriptive names, so that they are easier to read and understand
#camelCase naming convention

#underscore naming convention

#--------------------------------------------------------------------------------------------

#Variables in print() function
#Before
print("I have this many trees:")
print(tree)

#Now
print("I have this many trees:", tree)
print("There are ", tree, " in my yard")

#--------------------------------------------------------------------------------------------

#Types of Variables
#Integers - whole numbers
cups = 11

#Floats - decimal numbers
gallons = 3.5

#Strings - text
school = "Purdue Fort Wayne"

#--------------------------------------------------------------------------------------------

#Reassigning Variables
name = "Harrison"
print(name)
name = "Teacher"
print(name)

goals = 1
print(goals)
goals = 2
print(goals)

#can even change across variable types
goals = "I have 2 goals"
print(goals)

#--------------------------------------------------------------------------------------------

#Creating Constant Variables
MILE_IN_FEET = 5280
milesRan = 3
totalFeet = MILE_IN_FEET * milesRan
print(f"I ran {totalFeet:,} feet today")