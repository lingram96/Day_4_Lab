from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

while (True):
    print_menu()
    option = get_option()
    if (option == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = get_description()
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        time = get_time()
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif option == '6':
        description = get_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = get_description()
        time_taken = get_time()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
