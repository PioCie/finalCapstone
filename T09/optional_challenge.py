# Compilation Error 1: Missing colon after the if statement
if True
    print("This line will raise a compilation error")

# Compilation Error 2: Using an undefined variable
print(undefined_variable)

# Runtime Error: Division by zero
numerator = 10
denominator = 0
result = numerator / denominator  # Runtime Error: division by zero

# Logical Error: Incorrect formula for calculating the area of a rectangle
length = 5
width = 2
area = length * width  # Logical Error: should be length * width, not length + width

print("Program completed successfully")  # This line won't be reached due to the runtime error
