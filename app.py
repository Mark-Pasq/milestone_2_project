

from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit the program

Your choice:"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            prompt_mark_book_as_read()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command or input.  Try your selection again.')

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter the name of the new book: ')
    author = input('Enter the name of the author of the new book: ')

    database.add_book_to_list(name, author)


def list_all_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {book['read']}")


def prompt_mark_book_as_read():
    name = input('Enter the name of the book you have just finished reading: ')

    database.prompt_mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you would like to delete from the list: ')

    database.delete_book(name)


menu()

