# shabtai getting routed in something real
#   import date time module to handle dates
from datetime import datetime
import json
from json import JSONEncoder
from typing import Any
from dateutil import parser
import tkinter as tk
# Initialize an empty list to store tasks

tasks = []

# Function to display tasks in the to-do list
# def show_tasks():
#     print("To-Do List:")
#     # Enumerate through tasks and display them with their index
#     for index, task in enumerate(tasks, start=1):
#         print(f"{index}. {task}")
#   modified to show the index of the task. and also display due dates
def show_tasks():
    listbox.delete(0, tk.END)
    for index, task_info in enumerate(tasks, start=1):
        task = task_info["task"]
        due_date = task_info["due_date"]
        
        if due_date:
            # Check if due_date is a string, convert it to a datetime object
            if isinstance(due_date, str):
                due_date = datetime.strptime(due_date, "%Y-%m-%d")

            listbox.insert(tk.END, f"{index}. {task} (Due: {due_date.strftime('%Y-%m-%d')})")
        else:
            listbox.insert(tk.END, f"{index}. {task} (No due date)")


# def show_tasks():
#     # print("To-Do List:")
#     listbox.delete(0, tk.END)
#     for index, task_info in enumerate(tasks, start=1):
#         task = task_info["task"]
#         due_date = task_info["due_date"]
#         if due_date:
#             # print(f"{index}. {task} (Due: {due_date.strftime('%Y-%m-%d')})")
#             listbox.insert(tk.END, f"{index}. {task} (Due: {due_date.strftime('%Y-%m-%d')})")
#         else:
#             # print(f"{index}. {task} (No due date)")
#             listbox.insert(tk.END, f"{index}. {task} (No due date)")

#  A function to remove a task form the list
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid index. Please enter a valid task index.")


# Function to add a new task to the to-do list & more importantly include the due dates


# def add_task(): # task, due_date=None#):
#     new_task = entry_task.get()
#     due_date = entry_due_date.get()
#     if due_date:
#         try:
#             #   parse the due date string into a datetime object
#             due_date = datetime.strptime(due_date, "%Y-%m-%d")
#         except ValueError:
#             # print("Invalid date format. please use YYYY-MM-DD.")
#             label_status.config(text="Invalid date format. Use YYYY-MM-DD.")
#             return

#     tasks.append({"task": new_task, "due_date": due_date, "priority": priority})

#     show_tasks()
#     entry_task.delete(0, tk.END)
#     entry_due_date.delete(0, tk.END)
        
def add_task():
    new_task = entry_task.get()
    due_date = entry_due_date.get()
    priority = entry_priority.get()  # Add this line to get the priority from user input

    # Validate priority input
    if priority.lower() not in ['high', 'medium', 'low']:
        label_status.config(text="Invalid priority. Please enter high, medium, or low.")
        return

    # Continue with the rest of the function...
    tasks.append({"task": new_task, "due_date": due_date, "priority": priority})
    show_tasks()
    entry_task.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)
    entry_priority.delete(0, tk.END)  # Clear the priority entry field

        # tasks.append({"task": task, "due_date": due_date})
        # # this gives the user a message about due date
        # if due_date:
        #     print(f"Task '{task}' added to the to-do list with due date {due_date.strftime('%Y-%m-%d')}.")
        # else:
        #     print(f"Task '{task}' added to the to-do list.")


# Load tasks from a file at the beginning of the program
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            loaded_tasks = json.load(file)
            for task_info in loaded_tasks:
                if task_info.get("due_date"):
                    task_info["due_date"] = parser.parse(task_info["due_date"])
            return loaded_tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task Entry
label_task = tk.Label(root, text="Task:")
label_task.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_task = tk.Entry(root)
entry_task.grid(row=0, column=1, padx=10, pady=10, sticky="w")

label_priority = tk.Label(root, text="Priority (high/medium/low):")
label_priority.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_priority = tk.Entry(root)
entry_priority.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Due Date Entry
label_due_date = tk.Label(root, text="Due Date (YYYY-MM-DD):")
label_due_date.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_due_date = tk.Entry(root)
entry_due_date.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Add Task Button
button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=3, column=0, columnspan=2, pady=10)

# Task List
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
listbox.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

# Status Label
label_status = tk.Label(root, text="")
label_status.grid(row=5, column=0, columnspan=2, pady=10)

# Show Tasks Button (Optional)
# button_show_tasks = tk.Button(root, text="Show Tasks", command=show_tasks)
# button_show_tasks.grid(row=5, column=0, columnspan=2, pady=10)

# Load tasks at the beginning
tasks = load_tasks()
show_tasks()



# Start the Tkinter event loop
root.mainloop()
# Load tasks from a file at the beginning of the program
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            # loaded_tasks = file.read().splitlines()
            # loaded_tasks = eval(file.read()) # Using eval to convert the string representation to a list
            loaded_tasks = json.load(file) # instead of eval() cause its much safe to handle handle the serialization and deserialization of my task
        for task_info in loaded_tasks:
            if task_info.get("due_date"):
                task_info["due_date"] = parser.parse(task_info["due_date"])

        return loaded_tasks
    # except FileNotFoundError:
    except (FileNotFoundError, json.JSONDecodeError): 
        return []
    
# Custom JSON encoder to handle datetime objects
class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d")
        return super().default(obj)

# Save tasks to a file before exiting the program
def save_tasks():
    try:
        with open("tasks.txt", "w") as file:
            # file.write(str(tasks)) -----used for eval no json
            json.dump(tasks, file, cls=DateTimeEncoder)
        print("Tasks saved successfully.")
            # for task in tasks:
            #     file.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")
# loads tasks and stores in tasks.txt where the tasks can be stored for the user not to re enter the data every time he or she runs the program again.
tasks = load_tasks()  
# Main program
if __name__ == "__main__":
    # Main loop to keep the program running until the user chooses to quit
    #  
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Remove task")
        print("4. Quit")

        # Get user input for the choice & give a nice message to handle an input error
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            # if 1 <= choice <= 4:
            #     break # Break out of the loop if the choice is valid
            # else:
            #     print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except ValueError as ve:
            print(f"Error: {ve}")
            print(f"Invalid input. Please enter a number. Input received: {input('Enter the task: ')}")
        # Check the user's choice and perform the corresponding action
        if choice == 1:
            show_tasks()
        elif choice == 2:
            #  Get user input for a  new task and due date, and add it to the  list
            new_task = input("Enter the task: ")
            due_date = input("Enter the due date (YYYY-MM-DD, optional): ")
            add_task(new_task, due_date)
        elif choice == 3:
             # Show tasks, get user input for the task index, and remove the task
            show_tasks()
            try:
                index_to_remove = int(input("Enter the index of the task you want to remove: "))
            except ValueError as ve:
                print(f"Error: {ve}")
                print(f"Invalid input. Please enter the number. Input received: {input('Enter the index of the task to remove: ')}")
                continue
            remove_task(index_to_remove)

        elif choice == 4:
            # Display a goodbye message and exit the program
            print("Goodbye!")
            save_tasks()
            break
        else:
            # Inform the user if an invalid choice is entered
            print(f"Invalid choice. Please enter 1, 2, 3, or 4. Input  received: {choice}")
        