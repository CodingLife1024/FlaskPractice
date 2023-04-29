import sqlite3
import csv

connection = sqlite3.connect('database.db')

with open('new.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Riddhi", "Riddhi"))
cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Mrunal", "Mrunal"))
cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Kanu", "Kanu"))

with open('user.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        cur.execute("INSERT INTO users (username, pass_word, bio) VALUES (?, ?, ?)", row)

with open('post.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", row)

with open('comment.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", row)

connection.commit()
connection.close()
