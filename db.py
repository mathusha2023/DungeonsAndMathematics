import sqlite3
import datetime

connection = sqlite3.connect("data/db/records.sqlite")
cur = connection.cursor()


def create_base():
    cur.execute("""CREATE TABLE IF NOT EXISTS records (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    weapon INTEGER REFERENCES weapons (id),
    result TEXT,
    date   TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS weapons (
    id     INTEGER PRIMARY KEY,
    weapon TEXT    NOT NULL)""")

    if not cur.execute("""SELECT * FROM weapons""").fetchone():
        cur.execute(
            """INSERT INTO weapons (id, weapon) VALUES 
            (0, "FIST"), (1, "RIFLE"), (2, "SHOTGUN"), (3, "AK47"), (4, "FLAMETHROWER")""")
    connection.commit()


def get_records():
    recv = """SELECT weapon, result, date FROM records
    ORDER BY LENGTH(RESULT), RESULT
    LIMIT 9"""
    ans = cur.execute(recv).fetchall()
    return ans


def load_record(weapon, result):
    recv = """INSERT INTO records (weapon, result, date) 
    SELECT id, ?, ? FROM weapons
    WHERE weapon = ?"""
    cur.execute(recv, (result, datetime.date.today().strftime("%d.%m.%Y"), weapon))
    connection.commit()


def clear_records():
    recv = """DELETE FROM records"""
    cur.execute(recv)
    connection.commit()
