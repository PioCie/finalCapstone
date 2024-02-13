# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


def reg_user(dict_with_user_data):
    """Add a new user to the user.txt file"""
    # Request input of a new username and converted to lower case.
    new_username = input("New Username: ").lower()
    # A new loop was started to prevent duplicate usernames.
    while new_username in dict_with_user_data.keys():
        print(f"Username {new_username} already exist in our record, please choose another username.")
        new_username = input("New Username: ").lower()
    # - Request input of a new password and converted to lower case
    new_password = input("New Password: ").lower()
    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ").lower()

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print(f"User {new_username} has been added to the system. ")
        dict_with_user_data[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_info = []
            for k in dict_with_user_data:
                user_info.append(f"{k};{dict_with_user_data[k]}")
            out_file.write("\n".join(user_info))
    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


def add_task(dict_with_user_data):
    """Allow a user to add a new task to task.txt file
                    Prompt a user for the following:
                     - A username of the person whom the task is assigned to,
                     - A title of a task,
                     - A description of the task and
                     - the due date of the task."""
    # Started new while loop to be able back to task_username input after provided wrong task_username
    while True:
        task_username = input("Name of person assigned to task: ").lower()
        if task_username not in dict_with_user_data.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list.append(new_task)
    with open("tasks.txt", "w") as tasks:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        tasks.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all(all_tasks):
    """Reads the task from task.txt file and prints to the console in the
               format of Output 2 presented in the task pdf (i.e. includes spacing
               and labelling)
            """
    for t in all_tasks:
        disp_str = f"Task: \t\t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine(all_tasks, logged_user):
    """Reads the task from task.txt file and prints to the console in the
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labeling)
    """
    # Enumeration in a loop was used to allow the user to select a specific task
    for task_number, task_details in enumerate(all_tasks, 1):
        if task_details['username'] == logged_user and not task_details['completed']:
            disp_str = f"Task number: \t {task_number}\n"
            disp_str += f"Task: \t\t\t {task_details['title']}\n"
            disp_str += f"Assigned to: \t {task_details['username']}\n"
            disp_str += f"Date Assigned: \t {task_details['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t {task_details['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {task_details['description']}\n"
            print(disp_str)

    # When the tasks are displayed, ask the user which task they want to select
    user_choice = input("Enter the task number you want to select (or enter -1 to return to the main menu): ")
    if user_choice.strip() == "-1":
        return
    try:
        task_number = int(user_choice)
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return  # If anything other than a number has been entered, terminate the function
    # Check that the task number is correct
    if 1 <= task_number <= len(all_tasks):
        selected_task = all_tasks[task_number - 1]
        handle_selected_task(selected_task)
    else:
        print("Invalid task number. Please enter a valid task number.")


def handle_selected_task(selected_task):
    print(f"Selected Task: {selected_task['title']}")
    print("1. Mark as complete")
    print("2. Edit task")
    print("Enter any other key to go back to the main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        mark_as_complete(selected_task)
    elif choice == "2":
        edit_task(selected_task)
    else:
        print("Returning to the main menu.")


def mark_as_complete(task):
    task['completed'] = 'Yes'
    print("Task marked as complete.")
    with open("tasks.txt", "w") as tasks:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        tasks.write("\n".join(task_list_to_write))


def edit_task(task):
    if task['completed'] == 'Yes':
        print("Cannot edit a completed task.")
        return

    print("1. Edit assigned user")
    print("2. Edit due date")
    print("Enter any other key to cancel")

    edit_choice = input("Enter your edit choice: ")

    if edit_choice == "1":
        new_username = input("Enter the new assigned username: ")
        task['username'] = new_username
        print("Assigned user edited.")
    elif edit_choice == "2":
        new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
        task['due_date'] = new_due_date
        print("Due date edited.")
    else:
        print("Editing canceled.")


def display_statistics(dict_with_user_data, all_tasks):
    """If the user is an admin they can display statistics about number of users
               and tasks."""
    num_users = len(dict_with_user_data.keys())
    num_tasks = len(all_tasks)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user(username_password)

    elif menu == 'a':
        add_task(username_password)

    elif menu == 'va':
        view_all(task_list)

    elif menu == 'vm':
        view_mine(task_list, curr_user)

    elif menu == 'ds' and curr_user == 'admin':
        display_statistics(username_password, task_list)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
