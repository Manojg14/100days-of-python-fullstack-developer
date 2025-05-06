class Library:

    def __init__(self):
        self.display_book = ["PYTHON BOOK", "JAVA BOOK", "MACHINE LEARNING", "DATA STRUCTURE"]
        self.borrowed_books = {}

    def display(self):
        print("Available books:")
        for book in self.display_book:
            print(book)

    def borrow(self, borrow_book, user_name):
        if borrow_book in self.display_book:
            self.display_book.remove(borrow_book)
            self.borrowed_books[user_name] = borrow_book
            print(f"{user_name} borrowed the book: {borrow_book}")
        else:
            print("Book is not available in the library")

    def return_book(self, user_name):
        if user_name in self.borrowed_books:
            return_notes = self.borrowed_books.pop(user_name)
            self.display_book.append(return_notes)
            print(f"{user_name} returned the book: {return_notes}")
        else:
            print("No book to return for this user.")

    def exit_library(self):
        print("Thank you for accessing our library to improve your knowledge!")

class UserLibrary(Library):

    def __init__(self, user_name):
        super().__init__()
        self.user_name = user_name

    def user_library(self):
        while True:
            print("\n1. Display Books \n2. Borrow Book \n3. Return Book \n4. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.display()
                elif choice == 2:
                    borrow_book = input("Enter the book you want to borrow: ").upper()
                    self.borrow(borrow_book, self.user_name)
                elif choice == 3:
                    self.return_book(self.user_name)
                elif choice == 4:
                    self.exit_library()

                    break
                else:
                    print("Please enter a valid input choice.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")

user_choice = UserLibrary(input("Enter your name: "))
user_choice.user_library()
