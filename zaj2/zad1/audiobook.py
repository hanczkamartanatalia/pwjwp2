from zaj2.zad1.book import Book


class Audiobook(Book):
    def __init__(self, title, author, year, time):
        super().__init__(title, author, year)
        self.time = time
