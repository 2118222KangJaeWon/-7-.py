# Quiz 1
import random

def generate_lotto_numbers():
    result = []
    while len(result) < 6:
        number = random.randint(1, 45)
        if number not in result:
            result.append(number)
    return result

# Example usage:
lotto_numbers = generate_lotto_numbers()
print("Generated Lotto Numbers:", lotto_numbers)

# Quiz 2
class GuguDan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1, 10):
            print(f"{self.num} X {i} = {self.num * i}")

# Example usage:
gugu = GuguDan(3)
gugu.output()

# Quiz 3
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"You have borrowed '{self.title}'."
        else:
            return f"'{self.title}' is already borrowed."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"You have returned '{self.title}'."
        else:
            return f"'{self.title}' was not borrowed."

class Borrower:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        message = book.borrow()
        if "You have borrowed" in message:
            self.borrowed_books.append(book)
        print(message)

    def return_book(self, book):
        message = book.return_book()
        if "You have returned" in message:
            self.borrowed_books.remove(book)
        print(message)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"'{book.title}' by {book.author} [{status}]")

# Example usage:
library = Library()
book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")
library.add_book(book1)
library.add_book(book2)

library.list_books()

borrower = Borrower("Alice")
borrower.borrow_book(book1)
library.list_books()
borrower.return_book(book1)
library.list_books()