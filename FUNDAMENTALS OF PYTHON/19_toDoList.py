tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("Your Tasks:", tasks)
    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to remove")
        else:
            print("Your Tasks:", tasks)
            idx = int(input("Enter index (0-based) to remove: "))
            tasks.pop(idx)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
