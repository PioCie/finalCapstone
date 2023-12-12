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
    type_of_interest =




elif user_selection == "bond":
    pass
else:
    print("Incorrect input provided, please check your spelling and try again")

