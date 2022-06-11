import sqlite3 as db

conn = db.connect('my_database.db')
c = conn.cursor()

def populate_inventory_db():
    c.execute("CREATE TABLE IF NOT EXISTS laptops (laptopid INTEGER PRIMARY KEY, name NVARCHAR(20), city NVARCHAR(20), available NVARCHAR(20))")
    new_laptops = [(1, 'MacBook Pro 16 inch', 'London', 'True'), (2, 'Dell', 'Amsterdam', 'False')]
    c.executemany('INSERT INTO laptops VALUES (?, ?, ?, ?)', new_laptops)

def print_inventory_db():
    c.execute("SELECT * FROM laptops;")
    print(c.fetchall())
