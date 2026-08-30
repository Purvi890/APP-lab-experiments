class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed=False
    def borrow(self):
     if not self.is_borrowed:
        self.is_borrowed = True
        print("Book borrowed")

     else:
        print("Already borrowed")
    def return_book(self):
       if self.is_borrowed:
          self.is_borrowed=False
          print('book returned')
       else:
          print('book not borrowed')
class Patron:
   def __init__(self,name,patron_id):
      self.name=name
      self.patron_id=patron_id
      self.borrowed_books=[name]
   def borrow_book(self,book):
      if not book.is_borrowed:
         book.borrow()
         print(self.name,"borrowed book",book.title)
         self.borrowed_books.append(book)
      else:
         print("book already borrowed")
   def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(self.name, "returned", book.title)
        else:
            print("Book was not borrowed")
class Library:
   def __init__(self):
      self.books=[]
      self.patrons=[]
   def add_book(self, book):
        self.books.append(book)

   def register_patron(self, patron):
        self.patrons.append(patron)

   def display_books(self):
        for book in self.books:
            print(book)
def main():

    library = Library()

    book1 = Book("Python", "Guido", "101")
    book2 = Book("Java", "James", "102")

    patron = Patron("Rahul", 1)

    # Adding books
    library.add_book(book1)
    library.add_book(book2)

    # Registering patron
    library.register_patron(patron)

    # Display books
    library.display_books()

    # Borrow book
    patron.borrow_book(book1)

    # Return book
    patron.return_book(book1)


if __name__ == "__main__":
   main()


