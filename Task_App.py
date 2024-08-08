tasks = []
index = []
task_number = 0


def instructions():
    print("To add a task, type 'add'. To delete a task, type 'delete', and if you want to list tasks, type 'list'. ")
    command = input()
    user_input(command)
def add_task(task_name):
    global task_number
    task_number += 1
    tasks.append(task_name)
    index.append(task_number)
    print("task added successfully.")
    instructions()


def delete_task(taskNum):
    if taskNum == len(tasks):
        tasks.pop(taskNum) 
        index.pop(taskNum)
        print("Task deleted successfully.")
        instructions()
    else:
        print("Task not found.") 
        instructions()

def list_tasks():
    for i in range(len(tasks)):
        print(str(index[i]) + ". " + tasks[i])  
    instructions()  
def user_input(command):

    if command == "add":
        task_name = input("Enter your task: ")
        add_task(task_name)
    elif command == "delete":
        taskNum = (input("Enter the task number to delete: "))
        delete_task(int(taskNum))
    elif command == "list":
        list_tasks()
    else:
        print("Invalid command. Please try again.")
        instructions()
        


    
        
print("Welcome to your task manager!")
instructions()
