#Harrison Niswander
#ECET 114 / ITC 150
#9-8-26
#This program will introduce logical operators (and, or, not) and boolean logic

#--------------------------------------------------------------------------------------------

# Logical Operators
# and     --  both conditions must be true
# or      --  at least 1 condition must be true
# not     --  opposite

#--------------------------------------------------------------------------------------------

# and Operator

#   -> connects 2 boolean expressions into 1 compound expression
# BOTH subexpressions must be true for the compound expression to be true

# Structure
# if( (expression) and (expression) )

# Truth Table for AND Operator  [T = True | F = False]
# T and F     -->  False
# F and T     -->  False
# F and F     -->  False
# T and T     -->  True

# Example
# (x > y) and (a < b)    ---     Is x greater than y AND is a less than b?

#--------------------------------------------------------------------------------------------

# or Operator

#   -> connects 2 boolean expressions into 1 compound expression
# Only ONE subexpressions must be true for the compound expression to be true

# Structure
# if( (expression) or (expression) )

# Truth Table for OR Operator  [T = True | F = False]
# T or F     -->  True
# F or T     -->  True
# F or F     -->  False
# T or T     -->  True

# Example
# (x > y) or (a < b)    ---     Is x greater than y OR is a less than b?

#--------------------------------------------------------------------------------------------

# not Operator

#   -> reverses the result of the condition
# If applied to expression that is true     -> false is returned
# If applied to expression that is false    -> true is returned

# Can only be applied to 1 expression!!!!

# Structure
# if( not (expression) )

# Truth Table for NOT Operator  [T = True | F = False]
# not T     -->  False
# not F     -->  True

# Example
# not(x > y)    ---     Is the expression x > y NOT true?

#--------------------------------------------------------------------------------------------

# Short-Circuit Evaluation for and & or Operators

# Simply means that both expressions in the compound expression won't be checked 
# if first sub-expression decides the final results

# For example

# When using the and operator, if the first sub-expression is false, the second sub-expression will not be checked
# -> This is because the result is already false since both sub-expressions must be true for the result to be true

#When using the or operatior, if the first sub-expression is true, the second sub-expression will not be checked
# -> This is because the result is already true since only 1 of the sub-expressions must be true for the result to be true

#--------------------------------------------------------------------------------------------

# Example: Checking Numeric Ranges with Logical Operators

# Check if the value in x is between 20 and 40
x = 30

# Using AND operator
if(x >= 20 and x <= 40):
    print("x is in the range of 20 and 40")

# Using OR operator
if(x < 20 or x > 40):
    print("x is in out of the range of 20 and 40")

# Using OR and NOT operator
if(not(x < 20 or x > 40)):
    print("x is in the range of 20 and 40")

# Be Careful of Logical Errors
if(not(x < 20 and x > 40)):
    print("x is out of the range of 20 and 40")
# -> x can't be less than 20 and greater than 40 at the same time

#--------------------------------------------------------------------------------------------

# Boolean Variables

# Can only have 1 of 2 values: either True or False

# Syntax:
# booleanVar = True
# booleanVar = False

# Boolean variables are commonly used as flag
#   flag => variable that signals when some condition exists in the program
#       When set to True    -> condition does exist
#       When set to False   -> condition does not exist

#--------------------------------------------------------------------------------------------

# Example using Boolean Variables as Flags

# Objective:
# Write a program that asks a user to enter in the temperature outside (in Farenheit).
# Use Boolean Variables to create a flag for if the temperature is below freezing or not.
# Print out a message using boolean logic for whether the temperature is above or below freezing.

# constant for temperature reference if freezing or not
TEMP_FREEZE = 32

# gather temperature input from user
userTemp = float(input("Please enter in the temperature outside: "))

# if statement to assign boolean flag

#if-> check if temperature is below 32 (freezing)
if(userTemp < TEMP_FREEZE):
    boolTemp = True

#else-> temperature above 32 (not freezing)
else:
    boolTemp = False

# if statement to print message of freezing or not
#if-> temperature is freezing
if(boolTemp == True):
    print(f"The temperature, {userTemp:,} is below freezing")

# else -> temperature not freezing
else:
    print(f"The temperature, {userTemp:,} is above freezing")

#--------------------------------------------------------------------------------------------