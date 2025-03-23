class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def desc(self):
        return self.title + ' - ' + self.author + ' - ' + self.year
