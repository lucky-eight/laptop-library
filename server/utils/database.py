import sqlite3 as db
import pandas as pd

conn = db.connect('my_database.db')
c = conn.cursor()


class Database:

    def __init__(self, laptops_csv, user_csv, user_address_csv, laptop_assignment_csv):

        # create inventory table
        c.execute("CREATE TABLE IF NOT EXISTS laptop (id INTEGER PRIMARY KEY NOT NULL, name STRING NOT NULL, location_area STRING NOT NULL, is_available STRING NOT NULL)")

        # populate inventory table
        data_frame = pd.read_csv(laptops_csv)
        new_laptops = data_frame.apply(tuple, axis=1).tolist()
        c.executemany('INSERT INTO laptop VALUES (?, ?, ?, ?)', new_laptops)

        # create user address table
        c.execute("CREATE TABLE IF NOT EXISTS user_address (id INTEGER PRIMARY KEY NOT NULL, line_1 STRING NOT NULL, city STRING NOT NULL, post_code STRING NOT NULL)")

        # populate address table
        data_frame = pd.read_csv(user_address_csv)
        new_user_addresses = data_frame.apply(tuple, axis=1).tolist()
        print (new_user_addresses)
        c.executemany('INSERT INTO user_address VALUES (?, ?, ?, ?)', new_user_addresses)

        # create user table
        c.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY NOT NULL, name STRING NOT NULL, surname STRING NOT NULL, email_address STRING, address_id INTEGER, FOREIGN KEY(address_id) REFERENCES user_address(id))")

        # populate user table
        data_frame = pd.read_csv(user_csv)
        new_users = data_frame.apply(tuple, axis=1).tolist()
        c.executemany('INSERT INTO user VALUES (?, ?, ?, ?, ?)', new_users)

        # create laptop_assignment table
        c.execute("CREATE TABLE IF NOT EXISTS laptop_assignment (id INTEGER PRIMARY KEY NOT NULL, laptop_id STRING NOT NULL, user_id STRING NOT NULL, FOREIGN KEY(laptop_id) REFERENCES laptop(id), FOREIGN KEY(user_id) REFERENCES user(id))")

        # populate laptop_assignment table
        data_frame = pd.read_csv(laptop_assignment_csv)
        new_laptop_assignments = data_frame.apply(tuple, axis=1).tolist()
        c.executemany('INSERT INTO laptop_assignment VALUES (?, ?, ?)', new_laptop_assignments)


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
