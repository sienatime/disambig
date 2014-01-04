import sqlite3
from csv import reader
import codecs

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("survivor.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    # open file and insert all rows into the Tweets table
    f = codecs.open("job_sim.csv", encoding='utf-8')
    r = f.readlines()

    for row in r:
        query = """INSERT INTO Tweets (tweet) VALUES (?)"""
        DB.execute(query, (row,))

    CONN.commit()

main()