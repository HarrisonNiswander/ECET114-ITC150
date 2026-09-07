# [Name]
#ECET 114 / ITC 150
# [Date]
#This program will introduce nested if statements and if-elif-else statements

#--------------------------------------------------------------------------------------------

# Nested If Statements

# If statements can be nested within each other to perform multiple condition checks

# Structure:
#   if condition:
#       statement
#       if condition:
#           statement
#           statement
#           etc.
#       else:
#           statement
#           statement
#           etc.
#       statement
#       etc.
#   else:
#       statement
#       if condition:
#           statement
#           statement
#           etc.
#       else:
#           statement
#           statement
#           etc.
#       statement
#       etc.

# There is no limit on how many if statements you can include in an if statement or an else statement

#--------------------------------------------------------------------------------------------

# Solve the Objective using Nested If Statements

# Write a program that will ask the user for their grade in the class. 
# Print out a message with their letter grade according to this grading scale:
# A ->   >= 90
# B ->   80 - 89
# C ->   70 - 79
# D ->   60 - 69
# F ->   < 60

# Develop Plan:

#--------------------------------------------------------------------------------------------

# If-Elif-Else Statements

# A simplier version of how to write nested if statements

# Structure:
#   if condition:
#       statement
#       statement
#       etc.
#   elif condition:
#       statement
#       statement
#       etc.
#   INCLUDE AS MANY ELIF STATEMENTS AS NEEDED
#   else:
#       statement
#       statement
#       etc.

#--------------------------------------------------------------------------------------------

# Solve the Objective using Nested If Statements

# Write a program that will ask the user for their grade in the class. 
# Print out a message with their letter grade according to this grading scale:
# A ->   >= 90
# B ->   80 - 89
# C ->   70 - 79
# D ->   60 - 69
# F ->   < 60

# Constants to hold grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# obtain grade from user
grade = int(input("Enter in your grade in the class: "))

# Determine grade based on scale (90+ A, 80-89 B, 70-79 C, 60-69 D, <60 F)


#--------------------------------------------------------------------------------------------