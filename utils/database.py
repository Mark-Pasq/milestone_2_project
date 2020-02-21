"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name, author, read\n
"""

import sqlite3


def create_book_table():
    conn = sqlite3.connect('data.db')
    cu = conn.cursor()

    cu.execute(f'''CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY, author TEXT, read_status INTEGER); ''')

    conn.commit()
    conn.close()


def prompt_add_book_to_the_list(name, author):
    conn = sqlite3.connect('data.db')
    cu = conn.cursor()

    cu.execute(f'''INSERT INTO books VALUES(?, ?, 0)''', (name, author))

    conn.commit()
    conn.close()


def list_all_books():
    conn = sqlite3.connect('data.db')
    cu = conn.cursor()

    cu.execute(f'''SELECT * FROM books ''')
    books = [{'name': row[0], 'author': row[1], 'read_status': row[2]} for row in cu.fetchall()]

    conn.close()

    return books


def prompt_mark_book_as_read(name):
    conn = sqlite3.connect('data.db')
    cu = conn.cursor()

    cu.execute('''UPDATE books SET read=1 WHERE name=?, (name, )''')

    cu.commit()
    cu.close()


def prompt_to_delete_a_book(name):
    conn = sqlite3.connect('data.db')
    cu = conn.cursor()

    cu.execute('''DELETE FROM books WHERE name=?, (name, )''')

    cu.commit()
    cu.close()
