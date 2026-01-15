book_name = input()

books_checked_count = 0

while True:
    checked_book = input()


    if checked_book == book_name:
        print(f"You checked {books_checked_count} books and found it.")
        break

    elif checked_book == "No More Books":
        print(f"The book you search is not here!\nYou checked {books_checked_count} books.")
        break
    books_checked_count += 1