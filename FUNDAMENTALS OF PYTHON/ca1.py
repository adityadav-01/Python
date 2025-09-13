books =["python", "java", "c++", "javascript", "html", "css", "sql", "ruby", "go", "swift"]

is_books = []

while True:
    ch = input("Enter a book name : 1 : issue, 2 : return, 3 : exit : ")
    if ch == '1':
        book = input("Enter book name to issue : ")
        if book not in is_books:
            print(f"You have issued {book}.")
            is_books.append(book)
        else:
            print(f"Sorry, {book} is not available right now.")
    elif ch == '2':
        bo = input("Enter book name to return : ")
        if bo in is_books:
            is_books.remove(bo)
            print(f"Thank you for returning {bo}.")
        else:
            print(f"{bo} does not belong to our library.")
    elif ch == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")