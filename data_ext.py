import sqlite3

def search_db(id):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM dataset WHERE UID=?", (id,))
    rows=cur.fetchall()
    conn.close()
    return rows

def view():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM dataset")
    rows=cur.fetchall()
    conn.close()
    return rows

def mssg(att):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM dataset WHERE Attendance_Status<=?",(att,))
    rows=cur.fetchall()
    conn.close()
    return rows

def att_update(id):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("UPDATE dataset SET Attendance_Status=Attendance_Status+1 WHERE UID=?",(id,))
    conn.commit()
    conn.close()

def carb_check(carb):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM dataset WHERE carbohydrates<?",(carb,))
    rows=cur.fetchall()
    conn.close()
    return rows

def prot_check(prot):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM dataset WHERE protein<?",(carb,))
    rows=cur.fetchall()
    conn.close()
    return rows

def vit_check(vit):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM dataset WHERE vits<?",(vit,))
    rows=cur.fetchall()
    conn.close()
    return rows

def fat_check(carb):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM DataSet WHERE fats<?",(fat,))
    rows=cur.fetchall()
    conn.close()
    return rows

def fetch_phone():
        conn=sqlite3.connect("database.db")
        cur=conn.cursor()
        cur.execute("SELECT First_Name,Phone FROM dataset")
        rows=cur.fetchall()
        conn.close()
        return rows
