# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # Syntax error: missing parentheses on print statement.
print("\n")  # Compilation error: incorrect space indentation, Syntax error: missing parentheses on print statement.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"  # Compilation error: incorrect space indentation, Name error: variable age_Str is not defined.
age = int(age_Str)  # Compilation error: incorrect space indentation, Value error: invalid literal for int(),
# unable to convert letters into numbers
print(f"I'm {age} years old.")  # Compilation error: incorrect space indentation, Type error: can only concatenate
# string to string.

# Variables declaring additional years and printing the total years of age
years_from_now = "3"  # Compilation error: incorrect space indentation.
total_years = age + int(years_from_now)  # Compilation error: incorrect space indentation, Type error: unable to add
# a string into an integer.

print(f"The total number of years: {total_years}")  # Syntax error: missing parentheses on print statement, Logical
# errors: unexpected output at print statement.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = round((total_years + 0.5) * 12)  # Name error: variable total is not defined, changed to total_years
# and added-additional 6 months.
print(f"In 27 years and 6 months, I'll be {total_months} months old.")  # Syntax error: missing parentheses on
# print statement, Type error: unable to add a string into an integer, Logical errors: unexpected output at print
# statement.

# HINT, 330 months is the correct answer
