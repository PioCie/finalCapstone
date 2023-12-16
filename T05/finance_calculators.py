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
    # Gathering data from user for calculation
    amount_of_deposit = float(input("Please enter the value of your deposit: "))
    interest_rate = float(input("Please indicate the value of the interest rate: "))
    # Convert interest rate input to actually percentage.
    interest_rate = (interest_rate / 100)
    length_of_investment = int(input("The number of years you plan on investing: "))
    # It takes the user's input and changes it to lowercase so that it can be matched to any input.
    interest = input('What type of interest would you like to count, "Simple" or "Compound": ').lower()

    # From the input given, the user selects which type of interest to use.
    if interest == "simple":
        # Simple interest is calculated
        result = amount_of_deposit * (1 + interest_rate * length_of_investment)
        # Counts the exact amount of interest earned
        interest_result = (result - amount_of_deposit)
        # Shows the interest value with two decimal places
        print(f"The amount of interest you'll earn on your investment is {interest_result:.2f} GBP.")
    elif interest == "compound":
        # Compound interest is calculated
        result = amount_of_deposit * math.pow((1 + interest_rate), length_of_investment)
        # Counts the exact amount of interest earned
        interest_result = (result - amount_of_deposit)
        # Shows the interest value with two decimal places
        print(f"The amount of interest you'll earn on your investment is {interest_result:.2f} GBP.")
        # Informed user about wrong input
    else:
        print("Incorrect input provided, please check your spelling and try again")

elif user_selection == "bond":
    # Gathering data from user for calculation
    house_value = float(input("What is the present value of the house: "))
    interest_rate = float(input("Please indicate the value of the interest rate: "))
    # Calculated the annual interest rate.
    interest_rate = (interest_rate / 100) / 12
    num_of_months = int(input("Number of months you plan to spend on repaying the bond: "))
    # Monthly payment is calculated
    result = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-num_of_months))
    # Show the amount to pay for ech month to pay off the house with two decimal places
    print(f"To pay off you house, you have to pay {result:.2f} GBP for next {num_of_months} months.")
    # Informed user about wrong input
else:
    print("Incorrect input provided, please check your spelling and try again")
