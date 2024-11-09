class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def toggle_borrowed(self, borrowed):
        self.is_borrowed = borrowed
        status = "borrowed" if borrowed else "returned"
        print(f"'{self.title}' has been {status}.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"'{book.title}' is already borrowed.")
        else:
            book.toggle_borrowed(True)
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.toggle_borrowed(False)
            self.borrowed_books.remove(book)
        else:
            print(f"You haven't borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books borrowed.")

def main():
    books = [
        Book("Kidaga"),
        Book("The people"),
        Book(" Mockingbird",)
    ]
    member = LibraryMember("Abby", 101)

    while True:
        print("Library Borrowing System:\n")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Available Books:\n")
            for i, book in enumerate(books, start=1):
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{i}. {book.title} by {book.author} - {status}")

            book_choice = int(input("Enter the number of the book to borrow: ")) - 1
            if 0 <= book_choice < len(books):
                member.borrow_book(books[book_choice])
            else:
                print("Invalid choice.")

        elif choice == '2':
            if member.borrowed_books:
                print("Your Borrowed Books:")
                for i, book in enumerate(member.borrowed_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")

                return_choice = int(input("Enter the number of the book to return:")) - 1
                if 0 <= return_choice < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[return_choice])
                else:
                    print("Invalid choice.")
            else:
                print("You have no books to return.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            print("Exiting the library borrowing  system.")
            break

        else:
            print("Invalid choice. Please try again.")
main()