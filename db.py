import sqlite3
import datetime

connection = sqlite3.connect("data/db/records.sqlite")
cur = connection.cursor()


def get_records():
    recv = """SELECT weapons.weapon, result, date FROM records
    INNER JOIN weapons ON weapons.id = records.weapon
    ORDER BY RESULT DESC
    LIMIT 10"""
    ans = cur.execute(recv).fetchall()
    print(ans)
    return ans


def load_record(weapon, result):
    recv = """INSERT INTO records (weapon, result, date) 
    SELECT id, ?, ? FROM weapons
    WHERE weapon = ?"""
    cur.execute(recv, (result, datetime.date.today().strftime("%d.%m.%Y"), weapon))
    connection.commit()
