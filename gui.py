import tkinter as tk
from tkinter import messagebox
from todo_list import add_task, view_tasks, delete_task, mark_task_as_completed

# Function to add a task using the GUI
def gui_add_task():
    task = task_entry.get()
    if task:
        message = add_task(task)
        status_label.config(text=message, fg="green")  # Update the status label with success message
        task_entry.delete(0, tk.END)  # Clear the input field
        update_task_list()            # Update the task list display
        task_entry.focus_set()        # Set focus back to the input box
    else:
        status_label.config(text="Task cannot be empty! Please enter a task.", fg="red")

# Function to update the task list displayed in the GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    tasks = view_tasks()
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to delete a task using the GUI
def gui_delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        message = delete_task(selected_index + 1)
        status_label.config(text=message, fg="green")
        update_task_list()
    except IndexError:
        status_label.config(text="Please select a task to delete.", fg="red")

# Function to mark a task as completed in the GUI
def gui_mark_task_as_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        message = mark_task_as_completed(selected_index + 1)
        status_label.config(text=message, fg="green")
        update_task_list()
    except IndexError:
        status_label.config(text="Please select a task to mark as completed.", fg="red")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x700")

# Entry field for adding tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Button to add a task
add_button = tk.Button(root, text="Add Task", command=gui_add_task)
add_button.pack(pady=5)

root.bind("<Return>", lambda event: gui_add_task())

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Button to delete a task
delete_button = tk.Button(root, text="Delete Task", command=gui_delete_task)
delete_button.pack(pady=5)

# Button to mark a task as completed
mark_done_button = tk.Button(root, text="Mark as Done", command=gui_mark_task_as_completed)
mark_done_button.pack(pady=5)

# Status label for feedback
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

# Initial display of tasks
update_task_list()

# Set focus to the input field when the app starts
task_entry.focus_set()

# Run the main loop
root.mainloop()