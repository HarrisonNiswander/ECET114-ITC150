#Harrison Niswander
#ECET 114 / ITC 150
#9-3-26
#This program will introduce formatting output with F-strings and more

#--------------------------------------------------------------------------------------------

# Escape Characters
#   \n = New Line
#   \t = Tab
#   \' = Single Quote
#   \" = Double Quote
#   \\ = Backslash

print("Hello Everyone!\nThere is a \t tab in this line\nThis is a single quote: \' and this is a double quote: \" This is a backslash: \\")
print()
#--------------------------------------------------------------------------------------------

# F-Strings

# F-strings allow you to embed expressions inside string literals, using curly braces {}.
# Notation: f"string {placeholder}"

# Example: Calculate the area of a rectangle where the side lengths are 10 and 8. Display the result
# Rectangle Lengths
lengthA = 10
lengthB = 8

# Calculate the area of the rectangle
area = lengthA * lengthB
print(f"The area of the rectangle is {area}.")

# This also works with multiple expressions
print(f"The area of the rectangle with lengths {lengthA} and {lengthB} is {area}.")

# Expressions can also be used directly in the placeholders
print(f"The area of the rectangle with lengths {10} and {8} is {10 * 8}.")
print()

#--------------------------------------------------------------------------------------------

# Formatting Data with F-Strings

# F-strings can also be used to format data, such as numbers and strings, in a specific way.
# Notation: {placeholder:format_specifier}

#--------------------------------------------------------------------------------------------

# Rounding Floating-Point Numbers (Decimals)
# Syntax: {value:.nf} where n is the number of decimal places to round to

# Example
value = 100 / 9
print(f"The value of 100 / 9 not formatted is: {value}")
print(f"The value of 100 / 9 formatted to 2 decimal places is: {value:.2f}")
print()

#--------------------------------------------------------------------------------------------

# Inserting Commas or Underscores in Numbers
# Syntax: {value:,} or {value:_}

# Example
number = 1000000
print(f"The number not formatted is: {number}")
print(f"The number formatted with commas is: {number:,}")
print(f"The number formatted with underscores is: {number:_}")
print()
# print(f"The number formatted with commas is: {number / 3:,.2f}")

#--------------------------------------------------------------------------------------------

# Floating-Point Number as Percentage
# Syntax: {value:%}
# Syntax: {value:.n%} - Rounding Percentage

# Example
number2 = 0.75
print(f"The percentage not formatted is: {number2}")
print(f"The percentage formatted is: {number2:%}")

# Example 2
decimalPercent = 0.234237
print(f"Percent: {decimalPercent:%}")
print(f"Percent (2 decimal places): {decimalPercent:.2%}")
print()

#--------------------------------------------------------------------------------------------

# Scientific Notation
# Syntax: {value:e}

# Example
number3 = 123456789
print(f"The number not formatted is: {number3}")
print(f"The number formatted in scientific notation is: {number3:e}")
print()

#--------------------------------------------------------------------------------------------

# Formatting Integers
# Syntax: {value:d}

# Example
number4 = 1234567890
print(f"The number not formatted is: \t\t{number4}")
print(f"The number formatted as an integer is: \t{number4:,d}")
print()

#--------------------------------------------------------------------------------------------

# Minimum Field Width
# Syntax: {value:n} where n is the minimum number of spaces that should be used to display the value

# Example
number5 = 123
print(f"The number not formatted is: {number5}")
print(f"The number is 10 spaces away: {number5:10}")
print()

#--------------------------------------------------------------------------------------------

# Aligning Text & Values in F-Strings
# Left Alignment: {value:<n}
# Right Alignment: {value:>n}
# Center Alignment: {value:^n}      where n is the index (space) at which the value should be aligned

# Example - Right Aligned
text1 = "Indiana"
text2 = "Ohio"
text3 = "Michigan"
print(f"{text1:>10}")
print(f"{text2:>10}")
print(f"{text3:>10}")
print()

# When showing example start out with not putting number in
# Then put in 5 - States are right aligned at index 5 (spaces)
# Finally, put in 10 - States are right aligned at index 10 (spaces)

#--------------------------------------------------------------------------------------------

# F-String Formatters Can be Combined Together
number6 = 1567.891011
print(f"The number not formatted is: {number6}")
print(f"Formatted: {number6:,.2f}")
print()

# Order in Which F-String Formatters are Applied
#   #1  Alignment                       ({placeholder:<n}, {placeholder:>n}, {placeholder:^n})
#   #1  Minimum Field Width             ({placeholder:n})
#   #2  Comma/Underscore Formatting     ({placeholder:,} or {placeholder:_})
#   #3  Rounding                        ({placeholder:.nf})
#   #4  All Other Types of Formatting   (Percentage, Scientific Notation, etc.)

#--------------------------------------------------------------------------------------------

# Concatenation With Strings
message = "Hello" + " " + "World"
print(message)
print()

# Long Line of Code
print("This is a really long string that should be broken up into multiple lines for better readability in a Python program. Even though it is not syntactically incorrect to have a long string on one line, it is good practice to break it up into multiple lines for better readability.\n")

# More Readable Version of the Above Code
print("This is a really long string that should be broken up into multiple lines for better readability in a Python program. " +
    "Even though it is not syntactically incorrect to have a long string on one line, it is good practice to break it up into " +
    "multiple lines for better readability.\n")

# Even Better - Print on Multiple Lines
print("This is a really long string that should be broken up into multiple lines for better readability in a Python program. \n" +
    "Even though it is not syntactically incorrect to have a long string on one line, it is good practice to break it up into \n" +
    "multiple lines for better readability.\n")

# Both Print Statements Output the Same Result, but the Second Version is More Readable

# IMPORTANT - Code should NOT only work but be readable!!!

#--------------------------------------------------------------------------------------------

# Concatenation With F-Strings
title = "Mr."
firstName = "Harrison"
lastName = "Niswander"

print(f"{title} {firstName} {lastName}")
print(f"{title}" + f"{firstName}" + f"{lastName}")
#print(f"{title} " + f"{firstName} " + f"{lastName}")


# Concatenation With Numbers
percent = .90242
largeNum = 7283742
decimal = 56.823472
print(f"These numbers are all formatted: {percent:.2%} --- " + f"{largeNum:,} --- " + f"{decimal:.4f}")
print()


#--------------------------------------------------------------------------------------------