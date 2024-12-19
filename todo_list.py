# todo_list.py by Jack Ritchie

# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added successfully!"

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        return "Add some tasks first!"
    else:
        # Print the tasks with their index numbers, starting from 1
        return [f"{i}. {task}" for i, task in enumerate(tasks, start=1)]

# Function to delete a task from the list
def delete_task(task_num):
    try:
        if 1 <= task_num <= len(tasks):
            # Remove the task at the specified index
            remove_item = tasks.pop(task_num - 1)
            return f"Task '{remove_item}' successfully deleted!"
        else:
            return "Invalid task number :("

    except ValueError:
        return "Invalid input. Please enter a valid number."

    
    # Function to mark a task as completed
def mark_task_as_completed(task_num):
    # Display the current list of tasks
    view_tasks()
    try:
        # Check if the task number given is within the valid range
        if 1 <= task_num <= len(tasks):
            # Add a "Completed" prefix to the task to mark it as completed
            tasks[task_num - 1] = f"[Completed] {tasks[task_num - 1]}"
            return f"Task {task_num} marked as completed!"
        else:
            return "Invalid task number :("

    except ValueError:
        return "Invalid input. Please enter a valid number."