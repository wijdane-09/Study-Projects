# library_system.py

# Base Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # __str__ method for Book
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# EBook class that inherits from Book
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    # __str__ method for EBook
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# PrintBook class that inherits from Book
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    # __str__ method for PrintBook
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class with composition
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
