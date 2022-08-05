import sqlite3
import mysql.connector


def init_database():
    db = mysql.connector.connect(host ="localhost", user = "root", password = "anishgupta2002", db ="password_manager")
    cursor = db.cursor()
#     cursor.execute("use tables")

#     cursor.execute("""
#             CREATE TABLE IF NOT EXISTS vault(
#             id INTEGER PRIMARY KEY,
#             platform TEXT NOT NULL,
#             userid TEXT NOT NULL,
#             password TEXT NOT NULL);
#             """)
    return db, cursor
