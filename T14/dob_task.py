# Open the file for reading
with open("DOB.txt", "r", encoding="utf-8") as file:
    # Initialize lists to store names and birthdays
    names = []
    birthdays = []
    # Read each line from the file
    for line in file:
        # Split the line into name, surname and birthdate
        name, surname, birthdate = line.strip().split(" ", 2)
        # Added name and surname to create a full name
        full_name = name + " " + surname
        # Append the name and birthdate to their respective lists
        names.append(full_name)
        birthdays.append(birthdate)

# Print the names section
print("Name:")
print("\n".join(names))
print()
# Print the birthdays section
print("Birthdate:")
print("\n".join(birthdays))

