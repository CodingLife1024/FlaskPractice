import sqlite3

connection = sqlite3.connect('database.db')

with open('new.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Riddhi", "Riddhi"))
cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Mrunal", "Mrunal"))
cur.execute("INSERT INTO users (username, pass_word) VALUES (?, ?)", ("Kanu", "Kanu"))

cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's first post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's second post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's third post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's fourth post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's fifth post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's sixth post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's seventh post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's eighth post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's ninthpost."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (1, "This is Riddhi's tenth post."))
cur.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (3, "This is Kanishka's first post."))

cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (1, 1, "Comment1"))
cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (1, 1, "Comment2"))
cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (1, 1, "Comment3"))
cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (1, 1, "Comment4"))
cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (1, 1, "Comment5"))
cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (1, 1, "Comment6"))
cur.execute("INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)", (1, 1, "Comment7"))

connection.commit()
connection.close()
