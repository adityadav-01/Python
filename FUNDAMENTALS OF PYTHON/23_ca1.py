books =["python", "java", "c++", "javascript", "html", "css", "sql", "ruby", "go", "swift"]

is_books = []

while True:
    ch = input("Enter a book name : 1 : issue, 2 : return, 3 : exit : ")
    if ch == '1':
        book = input("Enter book name to issue : ")
        if book in books:
            print(f"You have issued {book}. Please return it within 30 days.")
            books.remove(book)
        else:
            print(f"Sorry, {book} is not available right now.")
    elif ch == '2':
        book = input("Enter book name to return : ")
        if book not in books:
            books.append(book)
            print(f"Thank you for returning {book}.")
        else:
            print(f"{book} does not belong to our library.")
    elif ch == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")