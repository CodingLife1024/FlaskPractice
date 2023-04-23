import sqlite3

connection = sqlite3.connect('database.db')

with open('new.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Riddhi", "Riddhi"))
cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Mrunal", "Mrunal"))
cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Kanu", "Kanu"))

cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's first post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (2, "This is Mrunal's first post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (3, "This is Kanishka's first post."))

connection.commit()
connection.close()