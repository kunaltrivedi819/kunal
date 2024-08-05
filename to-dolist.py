import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Create task list
        self.task_list = tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        # Create new task entry
        self.new_task_label = tk.Label(self.root, text="New Task:")
        self.new_task_label.pack(padx=10, pady=5)
        self.new_task_entry = tk.Entry(self.root, width=40)
        self.new_task_entry.pack(padx=10, pady=5)

        # Create buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=5)
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=5)
        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(padx=10, pady=5)
        self.load_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(padx=10, pady=5)

    def add_task(self):
        task = self.new_task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning!", "You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showwarning("Warning!", "You must select a task.")

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Info", "Tasks saved!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
                self.task_list.delete(0, tk.END)
                for task in self.tasks:
                    self.task_list.insert(tk.END, task)
        except:
            messagebox.showwarning("Warning!", "No saved tasks.")

if __name__ == "__main__":
    root = tk.Tk()
    todo = ToDoList(root)
    root.mainloop()