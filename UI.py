import task
import datetime


def new_task():
    return task.Task(get_name(), get_description(), get_tags(), get_due_date(), get_percent_complete())


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


def get_tags():
    tags = []
    while True:
        print("Current tags are: " + ", ".join(tags))
        new_tag = input("Enter a new tag(type existing tag to remove, leave blank to continue: ")

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
