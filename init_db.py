# import sqlite3

# connection = sqlite3.connect('database.db')


# with open('use.sql') as f:
#     connection.executescript(f.read())

# cur = connection.cursor()

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('First Post', 'Content for the first post')
# #             )

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('Second Post', 'Content for the second post')
# #             )



# connection.commit()
# connection.close()

import sqlite3

connection = sqlite3.connect('database.db')

with open('new.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user_info (username, pass_word) VALUES (?, ?)", ("Riddhi", "Riddhi"))
cur.execute("INSERT INTO user_info (username, pass_word) VALUES (?, ?)", ("Mrunal", "Mrunal"))
cur.execute("INSERT INTO user_info (username, pass_word) VALUES (?, ?)", ("Kanu", "Kanu"))

connection.commit()
connection.close()