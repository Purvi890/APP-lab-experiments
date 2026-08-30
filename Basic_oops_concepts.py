from abc import ABC, abstractmethod

# Composition
class Address:
    def __init__(self, city):
        self.city = city

    def __str__(self):
        return self.city


# Abstraction
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_role(self):
        pass


# Inheritance and Encapsulation
class Patron(Person):

    # Class variable
    library_name = "MIT ADT Library"

    def __init__(self, name, patron_id, city):
        super().__init__(name)

        # Instance variables
        self.patron_id = patron_id

        # Encapsulation
        self.__borrowed_books = []

        # Composition
        self.address = Address(city)

    # Instance method
    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.__borrowed_books.append(book)
            print(self.name, "borrowed", book.title)
        else:
            print("Book is already borrowed")

    # Instance method
    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(self.name, "returned", book.title)
        else:
            print("Book was not borrowed")

    # Encapsulation
    def show_borrowed_books(self):
        for book in self.__borrowed_books:
            print(book.title)

    # Abstraction
    def display_role(self):
        print(self.name, "is a Patron")

    # Magic method
    def __str__(self):
        return f"Patron: {self.name}"


# Inheritance
class Librarian(Person):

    # Polymorphism
    def display_role(self):
        print(self.name, "is a Librarian")

    def __str__(self):
        return f"Librarian: {self.name}"


