def main():

    tasks = []
    completed = []

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add\n2. View\n3. Complete\n4. Delete\n5. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks, completed)
        elif choice == "3":
            complete_task(tasks, completed)
        elif choice == "4":
            delete_task(tasks, completed)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def add_task(tasks):
    response = input("add task: ")
    tasks.append(response)


def view_tasks(tasks, completed):
        if len(tasks) == 0:
            print("list is empty")
            return 
        else:
            print("What do you wanna see?\n1. Incompleted tasks.\n2. Completed tasks")
            choice = input("make a choice: ")
            if choice == "1":
                for i in range(len(tasks)):
                    print(f"{i + 1} -> {tasks[i]}")
            elif choice == "2":
                if len(completed) == 0:
                    print("no tasks finished yet. wrap some of em real quick!")
                    return 
                else:
                    for i in range(len(completed)):
                        print(f"{i + 1} -> {completed[i]}")
                

def complete_task(tasks, completed):
    if len(tasks) == 0:
        print("list is empty, can't proceed!")
        return 
    else:
        for i in range(len(tasks)):
            print(f"{i} -> {tasks[i]}")
        response = int(input("which one of these tasks are completed?"))

        if response in range(len(tasks)):
                completed.append(tasks[response])
                tasks.pop(response)
                print("Yessir, task completed!")


def delete_task(tasks, completed):
    print("Delete Task from?\n1. Unfinished tasks or\n2. Finished tasks")
    response = int(input("make a choice: "))

    if response == 1:
        if len(tasks) == 0:
            print("list empty, cannot proceed")
            return 
        
        for i in range(len(tasks)):
            print(f"{i} -> {tasks[i]}")


        ans = int(input("Which task you wanna remove? "))

        if ans in range(len(tasks)):
            tasks.pop(ans)
            print("done brother, now lock in w the remaining tasks!")
        else:
            return 
    elif response == 2:
        if len(completed) == 0:
            print("list empty, cannot proceed")
            return 
        
        for i in range(len(completed)):
            print(f"{i} -> {completed[i]}")
            
        ans = int(input("Which task you wanna remove? "))

        if ans in range(len(completed)):
            completed.pop(ans)
            print("done brother, now lock in w the remaining tasks!")
        else:
            return 
    else:
        print("error, choose either 1 or 2")


main()