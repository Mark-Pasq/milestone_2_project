"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name, author, read\n
"""
from typing import Tuple, List

from utils.DatabaseConnection import DatabaseConnection

Book = Tuple[int, str, str, int]


def create_book_table() -> None:
    with DatabaseConnection('data.db') as conn:
        cu = conn.cursor()
        # SQLite automatically makes 'integer primary key' row auto-incrementing.
        cu.execute('CREATE TABLE IF NOT EXISTS books'
                   '(id INTEGER PRIMARY KEY, name TEXT, author TEXT, read_status INTEGER default 0);')


def list_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as conn:
        cu = conn.cursor()

        cu.execute(f'''SELECT * FROM books ''')
        books = cu.fetchall()
    return books


def insert_a_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as conn:
        cu = conn.cursor()

        cu.execute('INSERT INTO books (name, author) VALUES (?, ?)', (name, author))


def prompt_mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as conn:
        cu = conn.cursor()

        cu.execute('UPDATE books SET read_status=1 WHERE name=?', (name,))


def prompt_to_delete_a_book(name: str) -> None:
    with DatabaseConnection('data.db') as conn:
        cu = conn.cursor()

        cu.execute('DELETE FROM books WHERE name=?', (name,))


"""
These two functions below are options for the delete function of this
program.  They are not going to be used and are being saved for 
reference only.
"""
# def prompt_to_delete_a_book(name):
#     books = list_all_books()
#     books = [book for book in books if book['name'] != name]
#     _save_all_books(books)

# def prompt_to_delete_a_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
