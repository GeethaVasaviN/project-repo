import json
import os

TODO_FILE = "todo.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def list_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Add a task
def add_task(tasks):
    task_text = input("Enter new task: ")
    tasks.append({'task': task_text, 'done': False})
    print("📝 Task added.")

# Mark a task as done
def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("✅ Task marked as done.")
        else:
            print("❗Invalid task number.")
    except ValueError:
        print("❗Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Deleted task: {removed['task']}")
        else:
            print("❗Invalid task number.")
    except ValueError:
        print("❗Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("👋 Goodbye! Tasks saved.")
            break
        else:
            print("❗Invalid option. Try again.")

if __name__ == "__main__":
    main()
