from zaj3.zad3.library import Library

if __name__ == "__main__":
    library = Library()
    library.add_book("978-3-16-148410-0", "Python Basics")
    library.add_book("978-0-13-110362-7", "The C Programming Language")

    print(library.find_book("978-3-16-148410-0"))  # "Python Basics"
    print(library.find_book("978-1-23-456789-0"))  # None