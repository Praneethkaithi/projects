import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.mark_completed_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            self.task_listbox.insert(tk.END, f"{index}. [{status}] {task['task']}")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["completed"] = True
            self.update_task_listbox()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks.pop(task_index)
            self.update_task_listbox()

def main():
    root = tk.Tk()
    todo_list_app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
