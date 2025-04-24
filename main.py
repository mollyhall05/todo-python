import os
import sys
import tkinter as tk
from tkinter import ttk
import json

def main():

    def resource_path(relative_path):
        # Get absolute path to resource for PyInstaller or during development
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        return os.path.join(base_path, relative_path)

    # Create the main GUI window
    root = tk.Tk()
    root.title("Tasks")
    root.geometry("300x300")

    root.tk.call("source", resource_path("theme/light.tcl"))

    # FUNCTIONS

    # Save all tasks to local storage
    def save_tasks():
        if not os.path.exists(resource_path("tasks.json")):
            with open(resource_path("tasks.json"), "w") as file:
                json.dump([], file)

    # Load tasks from local storage
    def load_tasks():
        try:
            with open(resource_path("tasks.json"), "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    task_list = load_tasks()

    task_input = ttk.Entry(root, width=40)
    task_input.pack(pady=10, padx=10, anchor="center")
    
    tasks_frame = ttk.Frame(root)
    tasks_frame.pack(pady=10, padx=10, fill="both", expand=True)


    # Create task
    def create_task(description):
        return {"description" : description}
    
    def display_tasks(task):

        var = tk.BooleanVar()
        cb = tk.Checkbutton(tasks_frame, text=task["description"], variable=var)

        def on_checked():
            if var.get():
                cb.destroy()
                task_list.remove(task)
                save_tasks()

        cb.config(command=on_checked)
        cb.pack(anchor="w", pady=2)

    # Add task
    def add_task(event=None):
        description = task_input.get()

        if description:
            task = create_task(description)
            task_list.append(task)
            display_tasks(task)
            task_input.delete(0, tk.END)
            save_tasks()

    # Use 'Enter' key to add task
    task_input.bind("<Return>", add_task)

    for task in task_list:
        display_tasks(task)
        
    root.mainloop()

if __name__ == "__main__":
    main()