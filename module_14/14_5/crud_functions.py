import sqlite3


connection = sqlite3.connect("telegram.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


def get_all_products():
    cursor.execute("SELECT title, description, price FROM Products")
    users = cursor.fetchall()
    return users

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                                       (username, email, age, 1000))
    connection.commit()

def is_included(username):

    if cursor.execute("SELECT username FROM Users WHERE username = ?", (username,)).fetchone():
        return True
    else:
        return False

initiate_db()


#
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f"Продукт{i}", f"Описание{i}", i * 100))
# connection.commit()
# connection.close()