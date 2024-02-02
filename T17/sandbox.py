new_task = {
        "username": "task_username",
        "title": "task_title",
        "description": "task_description",
        "due_date": "due_date_time",
        "assigned_date": "curr_date",
        "completed": False
    }

for value, data in enumerate(new_task.items(), 1):
    print(value, data)
