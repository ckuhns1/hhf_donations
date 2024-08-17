import pandas
import csv
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()



# Connect to the database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Insert data
cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', ('alice1', 'alice1@example.com'))


# Commit changes and close the connection
conn.commit()
conn.close()

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')

rows_ = cursor.fetchall()

for item in rows_:
    print(item)

