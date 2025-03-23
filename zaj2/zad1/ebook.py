from zaj2.zad1.book import Book


class Ebook(Book):
    def __init__(self, title, author, year, size):
        super().__init__( title, author, year)
        self.size = size