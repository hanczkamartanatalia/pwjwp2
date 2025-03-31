from typing import Dict, Optional


class Library:
    def __init__(self) -> None:
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)