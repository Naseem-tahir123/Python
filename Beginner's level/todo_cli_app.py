# --- To-Do List CLI App (Beginner Level miletone) ---

tasks = []

def add_task():
    task_name = input("Enter the task name: ")
    task = {"name":task_name, "status":"pending"}
    tasks.append(task)
    print(f"Task '{task_name}' is successfully added.")

# add_task()

def view_tasks():
    if not tasks:
        print('No tasks is available.')
        return
    print('\n your to-do list:')
    for idx, task in enumerate(tasks,1):
        print(f'{idx}. {task['name']} - {task['status']}')
    print("********************************")
# view_tasks()

def update_task():
    """ Update the status of a task """
    view_tasks()
    if tasks: 
        task_index = input("Enter the task number to update: ")
        if task_index.isdigit():
            index = int(task_index) - 1
            if  0 <= index <  len(tasks):
                tasks[index]['status'] = 'completed'
                print(f"Task '{tasks[index]['name']}' is updated to complete")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")
# update_task()

def delete_task():
    """Delete a task from teh list"""
    view_tasks()
    if tasks:
        task_index = input("Enter the task number to delete:")
        if task_index.isdigit():
            index = int(task_index) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' is deleted from the list.")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")
# delete_task()

def main():
    while True:
        print("\n To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do list app . Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()



    
    
    





