import sqlite3
import random
from texttable import Texttable
from anime_base import Anime

class DataBaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None
        self.cursor = None
    def __enter__(self):
        self.connect()
        self.create_table()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()
        
    def connect(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                sport TEXT,
                finished_airing BOOLEAN,
                rating REAL,
                seen BOOLEAN
            )
        ''')
        self.connection.commit()

    def insert_row(self, anime):
        self.cursor.execute("INSERT INTO anime (name, sport, finished_airing, rating, seen) VALUES (?, ?, ?, ?, ?)",
                            (anime.name, anime.sport, anime.finished_airing, anime.rating, anime.seen))
        self.connection.commit()

    def delete_row(self, id):
        self.cursor.execute("DELETE FROM anime WHERE id=?", (id,))
        self.connection.commit()

    def mark_as_seen(self, id):
        self.cursor.execute("UPDATE anime SET seen=True WHERE id=?", (id,))
        self.connection.commit()

    def select_all(self):
        self.cursor.execute("SELECT * FROM anime")
        data = self.cursor.fetchall()
        if not data:
            print("No anime records found.")
        else:
            self.print_table(data)

    def select_by_sport(self, sport):
        self.cursor.execute("SELECT * FROM anime WHERE sport=?", (sport.lower(),))
        data = self.cursor.fetchall()
        if not data:
            print(f"No anime records found for the sport: {sport}")
        else:
            self.print_table(data)

    def select_random(self):
        self.cursor.execute("SELECT * FROM anime WHERE finished_airing=? AND seen=?", (True, False))
        data = self.cursor.fetchall()
        if not data:
            print("No unseen finished anime found.")
        else:
            random_anime = random.choice(data)
            self.print_table([random_anime])

    def disconnect(self):
        self.connection.close()

    def print_table(self, data):
        table = Texttable()
        table.set_cols_align(["l", "l", "c", "c", "c", "c"])
        table.set_cols_valign(["t", "t", "c", "c", "c", "c"])
        table.add_row(["ID", "Name", "Sport", "Finished Airing", "Rating", "Seen"])
        for row in data:
            table.add_row([row[0], row[1], row[2], "Yes" if row[3] else "No", row[4], "Yes" if row[5] else "No"])
        print(table.draw())