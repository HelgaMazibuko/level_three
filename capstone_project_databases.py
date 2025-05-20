import sqlite3

db = sqlite3.connect("ebookstore.db")
cursor = db.cursor()  # Get a cursor object

# Create the book table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INT PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        qty INT
    );
""")

# Insert the sample data into the book table
book_data = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

cursor.execute("SELECT COUNT(*) FROM book")
if cursor.fetchone()[0] == 0:
    cursor.executemany('INSERT INTO book VALUES (?,?,?,?)', book_data)
    db.commit()


def get_book(id):
    """This function retrieves book data from the database.

    Args:
        id (int): Unique book ID number.

    Returns:
        tuple: A row containing the book data.
    """

    cursor = db.cursor()
    query = "SELECT * FROM book WHERE id = ?"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    cursor.close()
    return result


def add_book(id, title, author, qty):
    """This function allows a user to add a new book to the database.

    Args:
        id (int): Unique book ID number.
        title (str): The title of the book.
        author (str): The author of the book.
        qty (int): The number of books available in stock.
    """

    cursor = db.cursor()
    query = "INSERT INTO book (id, Title, Author, Qty) VALUES (?, ?, ?, ?)"
    values = (id, title, author, qty)
    cursor.execute(query, values)
    db.commit()
    cursor.close()


def update_book(id, title, author, qty):
    """This function allows a user to update the details of an existing book in
    the database.

    Args:
        id (int): Unique book ID number.
        title (str): The title of the book.
        author (str): The author of the book.
        quantity (int): The number of books available in stock.
    """

    cursor = db.cursor()
    query = "UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?"
    values = (title, author, qty, id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()


def remove_book(id):
    """This function allows a user to remove or delete a book from the
    database.

    Args:
        id (int): Unique book ID number.
    """

    cursor = db.cursor()
    query = "DELETE FROM book WHERE id = ?"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()


# The main function of the program
def main():
    """This function is the main interface loop and handles all user inputs
    for the program.

    """
    print("Welcome to the eBookstore!")

    while True:
        print("1. Add book")
        print("2. Update book")
        print("3. Remove book")
        print("4. Search book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Add a new book to the database
        if choice == "1":
            id = input("Enter book id: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            qty = input("How many books in stock?: ")

            add_book(id, title, author, qty)
            print("Book added to the database!")

        # Update the details of an existing book in the database
        elif choice == "2":
            id = input("Enter book id: ")
            books = get_book(id)
            if books:
                title = input("Enter new book title: ")
                author = input("Enter new book author: ")
                qty = input("Enter new quantity: ")
                update_book(id, title, author, qty)
                print("Book details have been updated in the database!")

            else:
                print("No book found with that id!")

        # Remove a book from the database
        elif choice == "3":
            id = input("Enter book id: ")
            books = get_book(id)
            if books:
                remove_book(id)
                print("Book removed from the database!")

            else:
                print("No book found with that id!")

        # Search for a book in the database
        elif choice == "4":
            id = input("Enter book id: ")
            books = get_book(id)
            if books:
                print(f"Book found: {books}")

            else:
                print("No book found with that id!")

        # Exit the program
        elif choice == "5":
            print("Goodbye!")
            break

        # Handle invalid choices
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
