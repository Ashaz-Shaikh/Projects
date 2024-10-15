print("------ToDo App------")
print("1. Add Task")
print("2. Remove Task")
print("3. View Tasks")
print("4. Exit")

def ToDo():
    tasks = []
    choice = input("Enter what you want to do: ")
    choice = choice.upper()

    while True:
        if choice == "ADD" or choice == "ADD TASK":
            task = input("Enter your task: ")
            if task in tasks:
                print(f"{task} is already in {tasks}")
                yesNo = input(f"Would you like to add {task} again? ")
                yesNo = yesNo.upper()
                if yesNo == "YES":
                    tasks.append(task)
                    print(f"{task} successfully added!")
                else:
                    print(f"{task} was not added!")
            else:
                tasks.append(task)
                print(f"{task} successfully added!")

        elif choice == "REMOVE" or choice == "REMOVE TASK":
            remo = input("Which task you want to remove? ")
            if remo in tasks:
                tasks.remove(remo)
                print(f"{remo} removed successfully!")
            else:
                print(f"{remo} Does not exist!")

        elif choice == "VIEW" or choice == "VIEW TASK":
            print(tasks)

        else:
            break

        choice = input("Enter what you want to do: ")
        choice = choice.upper()

ToDo()