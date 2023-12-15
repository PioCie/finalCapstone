import math

# This simple script allows the user to access two different financial calculators: an investment calculator and a
# and a home loan repayment calculator.

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n")
print("Enter either 'investment' or 'bond' from the menu above to proceed\n")

# It takes the user's input and changes it to lowercase so that it can be matched to any input.
user_selection = input("Please specify which calculator to use: ").lower()

# From the input given, the user selects which calculator to use.
if user_selection == "investment":
    amount_of_deposit = float(input("Please enter the value of your deposit: "))
    interest_rate = float(input("Please indicate the value of the interest rate: "))
# Convert interest rate input to actually percentage.
    interest_rate = (interest_rate / 100)
    length_of_investment = float(input("The number of years you plan on investing: "))
# It takes the user's input and changes it to lowercase so that it can be matched to any input.
    interest = input('What type of interest would you like to count, "Simple" or "Compound": ').lower()
# From the input given, the user selects which type of interest to use.
    if interest == "simple":
        result = amount_of_deposit * (1 + interest_rate * length_of_investment)
# Counts the exact amount of interest earned
        interest_result = (result - amount_of_deposit)
        print(f"The amount of interest you'll earn on your investment is {interest_result} GBP.")
    elif interest == "compound":
        result = amount_of_deposit * math.pow((1 + interest_rate), length_of_investment)
    else:
        print("Incorrect input provided, please check your spelling and try again")

elif user_selection == "bond":
    pass
else:
    print("Incorrect input provided, please check your spelling and try again")

