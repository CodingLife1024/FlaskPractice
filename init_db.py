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

connection.commit()
connection.close()
