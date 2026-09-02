#Harrison Niswander
#ECET 114 / ITC 150
#9-1-26
#This program will introduce operations and how to use them (perform math)

#--------------------------------------------------------------------------------------------

# Common Math Operations in Python (Operators)
#   Addition (+)                - adds two numbers together
#   Subtraction (-)             - subtracts two numbers together
#   Multiplication (*)          - multiplies two numbers together
#   Division (/)                - divides two numbers together

#   Integer Division (//)       - divides two numbers together and returns the integer part of the result
#   Remainder / Modulus (%)     - returns the remainder of a division operation
#   Exponent (**)               - raises a number to a power

#--------------------------------------------------------------------------------------------

# Values on left and right of operators are called operands
# Example: 5 + 3
#        where:      5 = left operand
#                    3 = right operand
#                    + = operator

#--------------------------------------------------------------------------------------------

#Example: Calculate the area of a rectangle where the side lengths are 10 and 8. Display the result

# Define the side lengths of the rectangle
lengthA = 10
lengthB = 8

# Calculate the area of the rectangle
area = lengthA * lengthB

# Display Result
print("The area of the rectangle is: ", area)

#--------------------------------------------------------------------------------------------

# Rules with Integer Division
#   1. When the result is positive, it is truncated, which means that its fractional part is thrown away.
#   2. When the result is negative, it is rounded away from zero to the nearest integer.

# Floating Point and Integer Division Comparison

# Floating Point Division
print("Floating Point Division: 5 / 2 = ", 5 / 2)   #Output is 2.5

# Integer Division
print("Integer Division: 5 // 2 = ", 5 // 2)        #Output is 2

# Negative Numbers
print("Floating Point Division (negative): -5 / 2 = ", -5 / 2)   #Output is -2.5

# Integer Division
print("Integer Division (negative): -5 // 2 = ", -5 // 2)        #Output is -3

#--------------------------------------------------------------------------------------------

# Remainder / Modulus Operator (%)
# The modulus operator returns the remainder of a division operation
print("Remainder / Modulus: 5 % 2 = ", 5 % 2)   #Output is 1

#--------------------------------------------------------------------------------------------

# Exponent Operator (**)
# The exponent operator raises a number to a power
print("Exponent: 2 ** 3 = ", 2 ** 3)   #Output is 8

#--------------------------------------------------------------------------------------------

#Operator Precedence (Similar to PEMDAS)
#  1. Parentheses ()

#  2. Exponents **

#  3. Multiplication * 
#     Division / 
#     Integer Division //
#     Remainder / Modulus % 

#  4. Addition +
#     Subtraction -

# IMPORTANT: When operators have the same precedence, they are evaluated from left to right

print("Operator Precedence Example 1: 5 + 3 * 2 = ", 5 + 3 * 2)       #Output is 11
print("Operator Precedence Example 2: (5 + 3) * 2 = ", (5 + 3) * 2)   #Output is 16
print("Operator Precedence Example 3: 2**3**2 = ", 2**3**2)           #Output is 64
    # Evaluated as (2**3)**2 = 8**2 = 64

# Grouping with Parentheses is essential to ensure your calculation is performed correctly

#--------------------------------------------------------------------------------------------

# Converting Formulas to Python Code
# Example: Convert the following formula to Python code
#                    a + b
#                x = ----- - d
#                      c

# Answer: ((a + b) / c) - d

#--------------------------------------------------------------------------------------------

# Mixed-Type Expression

# Rules for Mixed-Type Expressions
#   1. Operation on two integers -> result is an integer
#   2. Operation on two floats -> result is a float
#   3. Operation on an integer and a float -> result is a float
#      =>  int temporarily converted to float for the operation

# Example: Int & Float
calculation = 5 * 2.0
print("Mixed-Type Expression Example: 5 * 2.0 = ", calculation)   #Output is 10.0

# Value 5 is temporarily converted to 5.0 for the operation, so the result is a float

#--------------------------------------------------------------------------------------------

# Data Type Conversion

# int() function
floatValue = 3.5
intValue = int(floatValue)
print("Data Type Conversion Example: int(3.5) = ", intValue)   #Output is 3

# float() function
intVal = 2
floatVal = float(intVal)
print("Data Type Conversion Example: float(2) = ", floatVal)   #Output is 2.0

#--------------------------------------------------------------------------------------------