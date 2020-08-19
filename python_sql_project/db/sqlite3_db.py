import sqlite3

conn = None

def get_sqlite():
    if (conn == None):
        conn = sqlite3.connect('../resource/database.db', isolation_level=None)
    
    return conn