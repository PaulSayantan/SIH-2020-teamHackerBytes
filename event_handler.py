import sqlite3
import json


conn=sqlite3.connect("event.db")
cur=conn.cursor()
cur.execute("SELECT * FROM event")
rows=cur.fetchall()
conn.close()


with open("event.json","w")as json_file:
    json.dump(rows,json_file)
