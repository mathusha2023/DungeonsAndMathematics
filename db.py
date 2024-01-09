import sqlite3
import datetime

connection = sqlite3.connect("data/db/records.sqlite")
cur = connection.cursor()


def get_records():
    recv = """SELECT weapon, result, date FROM records
    ORDER BY RESULT
    LIMIT 9"""
    ans = cur.execute(recv).fetchall()
    return ans


def load_record(weapon, result):
    recv = """INSERT INTO records (weapon, result, date) 
    SELECT id, ?, ? FROM weapons
    WHERE weapon = ?"""
    cur.execute(recv, (result, datetime.date.today().strftime("%d.%m.%Y"), weapon))
    connection.commit()
