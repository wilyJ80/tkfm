import sqlite3


class DatabaseSetup:

    def __init__(self, dbname="sistema_arquivos.db"):
        self.dbname = dbname

    def setup_database(self):
        conn = sqlite3.connect(self.dbname)
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


def setup():
    db_setup = DatabaseSetup()
    db_setup.setup_database()
