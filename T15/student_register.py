# Ask user for an input
num_of_students = input("How many students would you like to register: ")
# Created a for loop that runs through students number
for student in range(1, int(num_of_students)+1):
    # Asked user to enter a ech student ID
    student_id = input("Please provide a student ID: ")
    # Saves the student ID to a file and added dotted line for student signature
    with open("reg_form.txt", "a") as file:
        file.write(student_id+"\n"+"\n")
        file.write(25*"."+"\n"+"\n")
