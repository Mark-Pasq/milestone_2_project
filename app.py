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
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book_to_the_list()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            prompt_mark_book_as_read()
        elif user_input == 'd':
            prompt_to_delete_a_book()
        else:
            print('Unknown command or input.  Try your selection again.')

        user_input = input(USER_CHOICE)


def prompt_add_book_to_the_list():
    name = input(f'Enter the name of the new book:  ')
    author = input(f'Enter the name of the author of the new book:  ')

    database.insert_a_book(name, author)


def list_all_books():
    for book in database.list_all_books():
        read = 'YES' if book[3] else 'NO'   # Book [3] is a false value (0) if book is not read
        print(f'{book[1]} by {book[2]} - read: {read}')


def prompt_mark_book_as_read():
    name = input(f'Enter the name of the book you have just finished reading: ')

    database.prompt_mark_book_as_read(name)


def prompt_to_delete_a_book():
    name = input(f'Enter the name of the book you would like to delete from the list: ')

    database.prompt_to_delete_a_book(name)


menu()
