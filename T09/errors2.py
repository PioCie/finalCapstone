# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"  # NameError: name 'Lion' is not defined, changed into string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  # Logical errors:
# unexpected output at print statement, to solve problem I used formatted string literals.

print(full_spec)  # Syntax error: missing parentheses on print statement.
