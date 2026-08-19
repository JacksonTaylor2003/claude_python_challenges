class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return True
            elif book.title == title and book.is_checked_out:
                return False
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_checked_out = False
                return True
        return False

    def list_available_books(self):
        return [book for book in self.books if not book.is_checked_out]

library = Library()
library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
library.add_book(Book("Dune", "Frank Herbert"))

print(library.checkout_book("The Hobbit"))     # True
print(library.checkout_book("The Hobbit"))     # False (already checked out)
print(library.checkout_book("1984"))           # False (doesn't exist)
    
