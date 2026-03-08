# In this lesson, we will learn about classes and objects in Python.
# We will also learn about the concept of encapsulation
# and how to use it to create a simple task manager application.


# Create the Task class

class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

# Create the TaskManager class


class TaskManager:
    def __init__(self):
        self.tasks = []

# Add Task Methods
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print("Task Added!")

# View Tasks Method
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks):
            status = "Completed" if task.is_completed else "Pending"
            print(f"{index + 1}. {task.title} [{status}]")

# Complete Task Method
    def complete_task(self, index):
        try:
            self.tasks[index].mark_completed()
            print("Task Marked as Completed!")
        except IndexError:
            print("Invalid Task Index!")

# Delete Task Method
    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            print(f"Deleted task: {removed.title}")
        except IndexError:
            print("Invalid Task Number!")

#  Create the CLI Menu


def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            index = int(input("Enter task number to complete: ")) - 1
            manager.complete_task(index)

        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the Task Manager
if __name__ == "__main__":
    main()
