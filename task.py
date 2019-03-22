import datetime


class Task:
    tasks = []

    def __init__(self, name: str, description: str, tags: list, due_date: datetime.datetime, percent_complete=0):
        self.name = name
        self.description = description
        self.tags = tags
        self.due_date = due_date
        self.percent_complete = percent_complete
        Task.tasks.append(self)

    def get_time_till_due(self):
        if self.due_date:
            return (self.due_date - datetime.datetime.now()).total_seconds()
        else:
            return None

    def change_att(self, attribute, value):
        setattr(self, attribute, value)

    def get_att(self, attribute):
        return getattr(self, attribute)

    def delete(self):
        Task.tasks.remove(self)
