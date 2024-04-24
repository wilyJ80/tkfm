import sqlite3

conn = sqlite3.connect('sistema_arquivos.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS directories (
                id INTEGER PRIMARY KEY,
                name TEXT,
                parent_id INTEGER,
                FOREIGN KEY(parent_id) REFERENCES directories(id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY,
                name TEXT,
                directory_id INTEGER,
                FOREIGN KEY(directory_id) REFERENCES directories(id)
                )''')

conn.commit()
conn.close()
