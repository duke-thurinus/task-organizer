import task
import datetime


def main_menu():
    menu_options = {
        "new": new_task,
        "list": list_tasks,
        "update": update_task,
        "delete": remove_task
    }
    command = ""
    while True:
        print("Your command options are: ")
        list_dict(menu_options)
        print("quit")
        command = input("Enter a command: ").lower().strip()
        if command == "quit":
            break
        if command in menu_options:
            menu_options[command]()
        else:
            print("Command not available")
            print_spacer()


# Primary menu functions
def new_task():
    t = task.Task(get_name(), get_description(), get_tags(), get_due_date(), get_percent_complete())
    print_spacer()
    return t


def list_tasks():
    if not task.Task.tasks:
        print("No tasks")
    else:
        for t in task.Task.tasks:
            print(t.name)
    print_spacer()


def remove_task():
    subject_task = get_task()
    if subject_task is not None:
        subject_task.delete()
    print_spacer()


def update_task():
    attribute_function_dict = {
        "name": get_name,
        "description": get_description,
        "tags": get_tags,
        "due_date": get_due_date,
        "percent_complete": get_percent_complete
    }
    current_task = get_task()
    if current_task is None:
        print_spacer()
        return False

    attribute = get_attribute_name(attribute_function_dict)
    if attribute is None:
        print_spacer()
        return False

    current_task.change_att(attribute, attribute_function_dict[attribute]())
    print_spacer()


# Support functions
def list_dict(subject_dict):
    for key in subject_dict:
        print(key)


def print_spacer():
    print("---------")


def get_name():
    name = input("Enter a name: ")
    if name == "":
        print("Name cannot be left blank")
        return get_name()

    if name in task.Task.tasks:
        print("Name already in use")
        return get_name()

    return name


def get_description():
    description = input("Enter a Description: ")
    if description.strip() == "":
        description = None
    return description


def get_tags(tags=None):
    if tags is None:
        tags = []

    while True:
        print("Current tags are: " + ", ".join(tags))
        new_tag = input("Enter a new tag(type existing tag to remove, leave blank to continue: ").lower().strip()

        if new_tag.strip() == "":
            break

        if new_tag in tags:
            tags.remove(new_tag)
        else:
            tags.append(new_tag)

    return tags


def get_due_date():
    date_string = input("Enter the due date(empty is valid)(YYYY MM DD HH MM): ")
    if date_string.strip() == "":
        return None
    else:
        date_list = date_string.split()

        if len(date_list) < 3:  # check for minimum required number of datapoints
            print("Requires a minimum of YYYY MM DD")
            return get_due_date()

        if len(date_list) > 5:  # check for max number of datapoints
            print("There is maximum of 5 datapoints")
            return get_due_date()

        for index in range(len(date_list)):  # convert strings into ints
            try:
                date_list[index] = int(date_list[index])
            except ValueError:
                print("Input must be numbers only")
                return get_due_date()

        while len(date_list) < 5:  # pad list before calling datetime constructor
            date_list.append(0)

        return datetime.datetime(date_list[0], date_list[1], date_list[2], date_list[3], date_list[4])


def get_percent_complete():
    percent = input("Enter the percent complete this task is: 0-99: ")
    if percent == "":
        percent = 0
    else:
        try:
            percent = int(percent)
        except ValueError:
            print("Must input an integer")
            return get_percent_complete()

        if percent < 0 or percent > 99:
            print("Number must be between 0 and 99 inclusive")
            return get_percent_complete()

    return percent


def get_task():
    task_name = input("What is the name of the task do you want to modify (blank to cancel): ")
    if task_name == "":
        return None
    for index in range(len(task.Task.tasks)):
        if task_name == task.Task.tasks[index].name:
            return task.Task.tasks[index]
    print("No task matches that name")
    return get_task()


def get_attribute_name(attribute_function_dict):
    att = input("Enter the attribute you want to change (blank to cancel):")
    if att == "":
        return None
    if att in attribute_function_dict:
        return att
    else:
        print("Attribute does not exist")
        return get_attribute_name(attribute_function_dict)
