books = {
    "Kobzar": {
        "author": "Taras Shevchenko",
        "genre": "Poetry",
        "year": 1840,
        "pages": 115,
        "publisher": "Kyiv-Pechersk Lavra"
    },
    "1984": {
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "pages": 328,
        "publisher": "Secker & Warburg"
    }
}

while True:
    print("1. Show all books")
    print("2. Add a book")
    print("3. Delete a book")
    print("4. Search for a book by title")
    print("5. Edit book data")
    print("6. Exit")

    choice = input("\nSelect an option (1-6): ")

    if choice == '1':
        if not books:
            print("The collection is empty.")
        else:
            for title, info in books.items():
                print(f"\nTitle: {title}")
                for key, value in info.items():
                    print(f"  {key.capitalize()}: {value}")

    elif choice == '2':
        title = input("Enter book title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        year = input("Year of publication: ")
        pages = input("Number of pages: ")
        publisher = input("Publisher: ")

        books[title] = {
            "author": author,
            "genre": genre,
            "year": int(year) if year.isdigit() else year,
            "pages": int(pages) if pages.isdigit() else pages,
            "publisher": publisher
        }
        print(f"Book '{title}' successfully added!")

    elif choice == '3':
        title = input("Enter the title of the book to delete: ")
        if title in books:
            del books[title]
            print(f"Book '{title}' has been deleted.")
        else:
            print("Book not found.")

    elif choice == '4':
        title = input("Enter book title to search: ")
        if title in books:
            info = books[title]
            print(f"\nInformation for '{title}':")
            for key, value in info.items():
                print(f"- {key.capitalize()}: {value}")
        else:
            print("That book is not in the collection.")

    elif choice == '5':
        title = input("Enter the title of the book you want to change: ")
        if title in books:
            print("What would you like to change? (author, genre, year, pages, publisher)")
            field = input("Field: ").lower()
            if field in books[title]:
                new_value = input(f"Enter new value for {field}: ")
                if field in ["year", "pages"] and new_value.isdigit():
                    new_value = int(new_value)
                books[title][field] = new_value
                print("Data updated successfully.")
            else:
                print("That field does not exist.")
        else:
            print("Book not found.")

    elif choice == '6':
        print("Program terminated!")
        break

    else:
        print("Invalid choice. Please try again.")