# [Name]
#ECET 114 / ITC 150
# [Date]
#This program will introduce if statements and decision structures

#--------------------------------------------------------------------------------------------

# Decision Structure
# Used when executing a set of statements only under certain circumstances

# For Example
# A simple decision structure for if it is cold outside

# --> Is it cold outside? 
#       -> True ----> {Put on a coat}
#       -> False

#--------------------------------------------------------------------------------------------

# If Statements
# => If statements ask if this condition is true, then what statement(s) should happen

# Structure:
#   if condition:
#       statement
#       statement
#       etc.

# THE STATEMENT(S) MUST BE INDENTED OR YOU WILL HAVE AN ERROR!!!

#--------------------------------------------------------------------------------------------

# Relational Operators
# >     --  Greater Than
# <     --  Less Than
# >=    --  Greater Than or Equal To
# <=    --  Less Than or Equal To
# ==    --  Equal To
# !=    --  Not Equal To

#--------------------------------------------------------------------------------------------

# > and < Operators

# Checks if values are greater than or less than one another (depending on if using < or >)
#   Returns true/false depending if the value is less than or greater than (true) or not (false)

#--------------------------------------------------------------------------------------------

# >= and <= Operators

# Performs two checks:
#   1. Whether the values are greater than or less than (depending on whether you are using >= or <=)
#   2. Wheter the values are equal to each other

# Only ONE of the two checks needs to be true for the condition to return true

#--------------------------------------------------------------------------------------------

# == Operator

# Checks if values are equal to one another
#   If values are equal       -> condition returns true
#   If values are NOT equal   -> condition returns false


# Common Mistake

# IN PYTHON, = IS NOT THE SAME AS ==

#   =     --  Used when ASSIGNING values to variables
#   ==    --  Used when COMPARING two values to see if they are equal

#--------------------------------------------------------------------------------------------

# != Operator

# Checks if values are not equal to one another
#   If values are NOT equal   -> condition returns true
#   If values are equal       -> condition returns false

#--------------------------------------------------------------------------------------------

# Boolean Expressions using Relational Operators

#   x > y   --  Is x greater than y?
#   x < y   --  Is x less than y?
#   x >= y  --  Is x greater than or equal to y?
#   x <= y  --  Is x less than or equal to y?
#   x == y  --  Is x equal to y?
#   x !=    --  Is x not equal to y?

# Practice
# Assume that: a = 3, b = 3, and c = 5. Write whether the boolean expressions are true or false.

#   b < c   --> ___
#   a >= b  --> ___
#   a == c  --> ___
#   a > b   --> ___
#   a < b   --> ___
#   b != c  --> ___
#   c >= 8  --> ___

#--------------------------------------------------------------------------------------------

# Objective: 
# Write a program that will ask the user for their grade in the class. 
# If the user inputs a grade above a 90 (including 90), they print a message about how they have an A in the class.

# Develop Plan:

#--------------------------------------------------------------------------------------------

# If-Else Statements

# An If-Else statement will execute one block of statements if its condition is true and another if its condition is false

# Structure:
#   if condition:
#       statement
#       statement
#       etc.
#   else:
#       statement
#       statement
#       etc.

# THE STATEMENT(S) MUST BE INDENTED OR YOU WILL HAVE AN ERROR!!!
# The else statement must also be directly after an if statement or it will cause an error

# If-Else Statement Execution Steps
#   1. condition is checked for the if statement
#       - True -> Statements are Executed under the if Statement, then Else is skipped
#       - False -> Statements under if are skipped and jump to Else
#   2. else statements executed (only when if statement condition is false)

#--------------------------------------------------------------------------------------------

# Objective: 
# Write a program that will ask the user for their grade in the class. 
# If the user inputs a grade above a 90 (including 90), they print a message about how they have an A in the class.
# If the user inputs a grade below a 90, print a different message

# Devlop Plan:

#--------------------------------------------------------------------------------------------

# Comparing Strings

# two strings
text1 = "milk"
text2 = "mile"

# Comparing Strings using ==
# if (text1 == text2):
#     print("These are the same.")
# else:
#     print("These are the different.")

# Show The Following
# "milk" vs "mile"  -> ___
# "milk" vs "milk"  -> ___
# "milk" vs "Milk"  -> ___

# Strings can be compared using the !=

#--------------------------------------------------------------------------------------------

# Comparing Strings using greater than or less than

# All characters and Strings have a corresponding numerical representation
# Therefore, we can compare strings using their ASCII code

# ASCII - American Standard Code for Information Interchange

# ASCII Table (https://www.asciitable.com/)
# [A - Z]   ->  65 - 90
# [a - z]   ->  97 - 122
# [0 - 9]   ->  48 - 57
# Space     ->  32

# Example - abc123 would be stored in memory as codes: 97, 98, 99, 49, 50, 51

# Comparing Strings
# if ("a" < "b"):
#     print("The letter 1 is less than the letter 2")
# else:
#     print("The letter 1 is greater than the letter 2")

# a vs b        ->  a is less than b (97 vs 98)
# A vs a        ->  a is greater than A (97 vs 65)
# milk vs mile  ->  milk is greater than mile ([109, 105, 108, 107] vs [109, 105, 108, 101])
#   -> compares each character beginning with the first, or leftmost character

#--------------------------------------------------------------------------------------------
