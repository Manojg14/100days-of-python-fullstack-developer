from datetime import datetime, timedelta

class BaseTask:
    def __init__(self, task_id=None, title=None, description=None, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

class Operations(BaseTask):
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Task Title: ")
        description = input("Enter Task Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/Completed): ")

        task = BaseTask(task_id, title, description, due_date, status)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nAll Tasks:")

        for task in self.tasks:
            print(f"ID: {task.task_id} | Title: {task.title} | Due: {task.due_date} | Status: {task.status}")

    def delete_task(self):

        task_id = input("Enter Task ID to delete: ")

        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted.")
                return
        print("Task not found.")

    def mark_completed(self):

        task_id = input("Enter Task ID to mark as completed: ")

        for task in self.tasks:
            if task.task_id == task_id:
                task.status = "Completed"
                print("Task marked as completed.")
                return
        print("Task not found.")

    def view_near_deadlines(self):

        print("\nTasks Near Deadline (within 2 days):")

        today = datetime.now().date()
        upcoming = today + timedelta(days=2)
        found = False

        for task in self.tasks:
            due = datetime.strptime(task.due_date, "%Y-%m-%d").date()
            if task.status.lower() == 'pending' and due <= upcoming:
                print(f"ID: {task.task_id} | Title: {task.title} | Due: {task.due_date} | Status: {task.status}")
                found = True

        if not found:
            print("No tasks near deadline.")

class TaskManager(Operations):
    def run(self):
        while True:
            print("\n--- Task Manager ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Mark Task as Completed")
            print("5. View Near Deadline Tasks")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.mark_completed()
            elif choice == '5':
                self.view_near_deadlines()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    manager = TaskManager()
    manager.run()
