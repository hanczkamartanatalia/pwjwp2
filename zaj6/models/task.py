class Task:
    tasksList = []

    def __init__(self, content: str, done: bool):
        self.content = content
        self.done = done

    @classmethod
    def appendTask(cls, content):
        task = Task(content, False)
        cls.tasksList.append(task)

    @classmethod
    def removeTask(cls, content):
        cls.tasksList = [task for task in cls.tasksList if task.content != content]

    @classmethod
    def setASDone(cls, content):
        for task in cls.tasksList:
            if task.content == content:
                task.done = True
                return task
