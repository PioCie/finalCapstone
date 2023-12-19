# Set of variables for increments in loop
total_value = 0
num_of_loops = 0
# Start a loop to gathering user input
while True:
    user_input = int(input("Please enter a number: "))
    # Condition to break a loop
    if user_input == -1:
        # When the condition is met, we calculate the average of the entered numbers and round it to two decimal places.
        result = round(total_value / num_of_loops, 2)
        # Print the average of the entered numbers
        print(f"The average of the numbers entered is {result}")
        # Loop break
        break
    # If the condition is not met, we increment the variables with the data entered by the user and add another loop
    total_value += user_input
    num_of_loops += 1
