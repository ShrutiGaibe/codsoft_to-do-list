import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Create task list frame
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        # Create task list
        self.task_list = tk.Listbox(self.task_list_frame)
        self.task_list.pack(fill="both", expand=True)

        # Create entry frame
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(fill="x")

        # Create task entry
        self.task_entry = tk.Entry(self.entry_frame)
        self.task_entry.pack(side="left", fill="x", expand=True)

        # Create add task button
        self.add_task_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side="left")

        # Create delete task button
        self.delete_task_button = tk.Button(self.entry_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side="left")

        # Create clear all tasks button
        self.clear_all_tasks_button = tk.Button(self.entry_frame, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_all_tasks_button.pack(side="left")

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert("end", task)
            self.task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning!", "You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showwarning("Warning!", "You must select a task.")

    def clear_all_tasks(self):
        self.tasks = []
        self.task_list.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()