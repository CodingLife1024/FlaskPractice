import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Riddhi@2003",
    database="Tesser",
)

# Read the Terrer.sql file and execute its contents
with open('Tesser.sql') as f:
    commands = f.read().split(';')
    for command in commands:
        connection.cursor().execute(command)

# Insert a sample user into the user_info table
cur = connection.cursor()
cur.execute("INSERT INTO Tesser.user_info (username, pass_word, bio) VALUES (%s, %s, %s)", ('nickey', 'hithere', 'animal lover'))
connection.commit()

# Close the connection
connection.close()