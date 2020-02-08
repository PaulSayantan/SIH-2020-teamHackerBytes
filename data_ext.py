import sqlite3

def search_db(id):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM DataSet WHERE UID=?", (id,))
    rows=cur.fetchall()
    conn.close()
    return rows

def view():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM DataSet")
    rows=cur.fetchall()
    conn.close()
    return rows

def mssg(att):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM DataSet WHERE Attendance_Status<=?",(att,))
    rows=cur.fetchall()
    conn.close()
    return rows
