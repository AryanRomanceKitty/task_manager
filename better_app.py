def task():
    tasks = []
    print("=" * 40)
    print("    Welcome To Task Manager App    ")
    print("=" * 40)

    while True:
        try:
            total_task = int(
                input(
                    "\nHow many tasks do you want to add initially? (Enter 0 to skip): "
                )
            )
            if total_task < 0:
                print("Please enter a valid number!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\nEnter your initial tasks:")
    for i in range(1, total_task + 1):
        while True:
            task_name = input(f"  Task {i}: ").strip()
            if task_name:
                tasks.append(task_name)
                break
            else:
                print("Task cannot be empty! Try again.")

    def display_tasks():
        print("\n" + "=" * 40)
        print("           YOUR TASK LIST           ")
        print("=" * 40)
        if not tasks:
            print("    No tasks available. Add some!")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"  {idx}. {task}")
        print("=" * 40)

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new task")
        print("2. Update an existing task")
        print("3. Delete a task")
        print("4. View all tasks")
        print("5. Exit")

        try:
            operation = int(input("\nChoose an option (1-5): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if operation == 1:
            add = input("\nEnter the new task: ").strip()
            if add:
                tasks.append(add)
                print(f"Task '{add}' has been successfully added! ")
            else:
                print("Task cannot be empty!")

        elif operation == 2:
            display_tasks()
            if tasks:
                try:
                    index = int(input("\nEnter the task number to update: ")) - 1
                    if 0 <= index < len(tasks):
                        new_task = input("Enter the updated task: ").strip()
                        if new_task:
                            old = tasks[index]
                            tasks[index] = new_task
                            print(f"Task '{old}' → updated to '{new_task}' ")
                        else:
                            print("Task cannot be empty!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")

        elif operation == 3:
            display_tasks()
            if tasks:
                try:
                    index = int(input("\nEnter the task number to delete: ")) - 1
                    if 0 <= index < len(tasks):
                        removed = tasks.pop(index)
                        print(f"Task '{removed}' has been deleted! ")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")

        elif operation == 4:
            display_tasks()
            print(f"Total tasks: {len(tasks)}")

        elif operation == 5:
            print("\nThank you for using Task Manager!")
            print("Goodbye! Have a productive day! ")
            break

        else:
            print("Invalid option! Please choose between 1-5.")

task()
