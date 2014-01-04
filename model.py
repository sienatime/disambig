import sqlite3

DB = None
CONN = None
CURRENT_ID = 112

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("survivor.db")
    DB = CONN.cursor()

def get_relevant_tweets():
    query = """SELECT tweet FROM tweets where relevant = 1"""
    DB.execute(query)
    rows = DB.fetchall()
    return rows

def get_unrated_tweets(limit):
    query = """SELECT id, tweet FROM tweets where relevant is null LIMIT ?"""
    DB.execute(query, (limit,))
    rows = DB.fetchall()
    return rows

def get_tweet():
    global CURRENT_ID
    query = """SELECT id, tweet from Tweets where id == ?"""
    DB.execute(query, (CURRENT_ID,))
    row = DB.fetchone()
    CURRENT_ID += 1
    return row

def rate_tweet(t_id, relevant):
    query = """UPDATE Tweets SET relevant = ? WHERE id = ? """
    DB.execute(query, (relevant, t_id))
    CONN.commit()

def select_random_tweets(limit):
    query = """SELECT tweet, relevant FROM tweets ORDER BY RANDOM() LIMIT ?"""
    DB.execute(query, (limit,))
    rows = DB.fetchall()
    return rows