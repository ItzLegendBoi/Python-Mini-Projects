def task():
    print("---WELCOME TO TASK MANAGER---")
    tasks = []
    total_task = int(input(print("How many tasks you want to add: ")))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    print('Todays tasks are /n {tasks}')
    while True:
        try:
            operation= int(input(print("1.Add tasks/n2.Update/n3.View/n4.Delete/n5.Exit")))
            if operation==1:
                add = input(print("Enter task to be added:"))
                tasks.append(add)
                print("Task added successfully./n")
            elif operation==2:
                update_task = input(print("Enter task to be updated:"))
                if update_task in tasks:
                    up = input(print("Enter updated task: "))
                    ind = tasks.index(update_task)
                    tasks[ind]=up
                    print("Task updated successfully./n")
                else:
                    print("Task not found./n")
            elif operation==3:
                print(f"{total_task} = {tasks}")
            elif operation==4:
                del_task = input(print("Enter tasks to be deleted: "))
                if del_task in tasks:
                    ind = tasks.index(del_task)
                    del tasks[ind]
                    print("Task deleted successfully./n")
                else:
                    print("Task not found./n")

            elif operation==5:
                print("Exiting..../n")
                break
            else:
                print("Invalid operation/n")
        except ValueError:
            print("Invalid input/n")
task()