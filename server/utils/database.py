import sqlite3 as db
import pandas as pd

conn = db.connect('my_database.db')
c = conn.cursor()

class Database:

    def __init__(self, laptops_csv):

        # read csv
        # db = pd.read_csv(laptops_csv, index_col="ID")
        # print(db)
        # return db
        data_frame = pd.read_csv(laptops_csv)
        new_laptops = data_frame.apply(tuple, axis=1).tolist()

        # populate inventory table
        c.execute("CREATE TABLE IF NOT EXISTS laptop (id INTEGER PRIMARY KEY NOT NULL, name STRING NOT NULL, location_area STRING NOT NULL, is_available STRING NOT NULL)")
        # new_laptops = [(1, 'MacBook Pro 16 inch', 'London', 'True'), (2, 'Dell', 'Amsterdam', 'False')]
        c.executemany('INSERT INTO laptops VALUES (?, ?, ?, ?)', new_laptops)
        c.execute("SELECT * FROM laptops;")
        print(c.fetchall())

        # create and populate user table
        c.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY NOT NULL, name STRING NOT NULL, surname STRING NOT NULL, email_address STRING)")




    def print_inventory_db(self):
        c.execute("SELECT * FROM laptops;")
        print(c.fetchall())




# read_laptops_csv("server/laptops.csv")
