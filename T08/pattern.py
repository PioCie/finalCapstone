# Set of variables for increments in loop
index_number = 0
stars_number = ""
# Starting a for loop with a range of nine iterations
for i in range(1, 10):
    # Sets the condition for the creation of further asterisks if the length of the variable is less than five
    if len(stars_number) < 5:
        # Creates and print another asterisks after each iteration
        stars_number += "*"
        print(stars_number)
    # When the length of the variable reaches five, we move to the else condition
    else:
        # Increase of the index variable after each iteration
        index_number += 1
        # Use of reverse string slice notation together with index number variable to print less asterisks for each
        # iteration
        print(stars_number[:-index_number])
