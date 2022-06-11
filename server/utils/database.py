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
        c.executemany('INSERT INTO laptop VALUES (?, ?, ?, ?)', new_laptops)
        c.execute("SELECT * FROM laptop;")
        print(c.fetchall())

        # create and populate user table
        c.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY NOT NULL, name STRING NOT NULL, surname STRING NOT NULL, email_address STRING)")




    def print_inventory_db(self):
        c.execute("SELECT * FROM laptop;")
        print(c.fetchall())

    def find_laptops(self, location):
        """ Query the database for all available laptops in a given area. """

        c.execute(f"SELECT * FROM laptop WHERE location_area = ? AND is_available=1;", location)
        local_laptops = c.fetchall()
        return(local_laptops)

    def mark_unavailable(self, laptop_id):
        """ Mark a given laptop (selected by id) as unavailable. """

        c.execute("UPDATE laptop SET is_available=0 WHERE id = ?;", (laptop_id,))

        c.execute(f"SELECT * FROM laptop;")
        updated_database = c.fetchall()

        return updated_database





# read_laptops_csv("server/laptops.csv")
