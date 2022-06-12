""" Database class, including functions for interacting with the databases. """

__copyright__ = "Copyright (C) 2022 lucky-8"

# External imports
import pandas as pd
import sqlite3 as db

class Database:
    """ Database class, including functions for interacting with the databases. """

    def __init__(self, laptops_csv, user_csv, user_address_csv, laptop_assignment_csv):

        # Initialise connection to database
        conn = db.connect('my_database.db', check_same_thread=False)
        self.c = conn.cursor()

        # Create inventory table
        self.c.execute("CREATE TABLE IF NOT EXISTS laptop (id INTEGER PRIMARY KEY NOT NULL, name STRING NOT NULL, location_area STRING NOT NULL, is_available STRING NOT NULL)")

        # populate inventory table
        data_frame = pd.read_csv(laptops_csv)
        new_laptops = data_frame.apply(tuple, axis=1).tolist()
        self.c.executemany('INSERT INTO laptop VALUES (?, ?, ?, ?)', new_laptops)

        # Create user address table
        self.c.execute("CREATE TABLE IF NOT EXISTS user_address (id INTEGER PRIMARY KEY NOT NULL, line_1 STRING NOT NULL, city STRING NOT NULL, post_code STRING NOT NULL)")

        # Populate address table
        data_frame = pd.read_csv(user_address_csv)
        new_user_addresses = data_frame.apply(tuple, axis=1).tolist()
        print (new_user_addresses)
        self.c.executemany('INSERT INTO user_address VALUES (?, ?, ?, ?)', new_user_addresses)

        # Create user table
        self.c.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY NOT NULL, first_name STRING NOT NULL, last_name STRING NOT NULL, date_requested TEXT, email_address STRING, address_id INTEGER, FOREIGN KEY(address_id) REFERENCES user_address(id))")

        # Populate user table
        data_frame = pd.read_csv(user_csv)
        new_users = data_frame.apply(tuple, axis=1).tolist()
        print(new_users)
        self.c.executemany('INSERT INTO user(id,first_name,last_name,email_address,date_requested,address_id) VALUES(?, ?, ?, ?, ?, ?)', new_users)

        # Create laptop_assignment table
        self.c.execute("CREATE TABLE IF NOT EXISTS laptop_assignment (id INTEGER PRIMARY KEY NOT NULL, laptop_id STRING NOT NULL, user_id STRING NOT NULL, FOREIGN KEY(laptop_id) REFERENCES laptop(id), FOREIGN KEY(user_id) REFERENCES user(id))")

        # Populate laptop_assignment table
        data_frame = pd.read_csv(laptop_assignment_csv)
        new_laptop_assignments = data_frame.apply(tuple, axis=1).tolist()
        self.c.executemany('INSERT INTO laptop_assignment VALUES (?, ?, ?)', new_laptop_assignments)


    def print_inventory_db(self):
        self.c.execute("SELECT * FROM laptop;")
        print(self.c.fetchall())

    def find_laptops(self, location):
        """ Query the database for all available laptops in a given area. """

        self.c.execute("SELECT * FROM laptop WHERE location_area = ? AND is_available=1;", location)
        local_laptops = self.c.fetchall()
        return(local_laptops)

    def mark_unavailable(self, laptop_id):
        """ Mark a given laptop (selected by id) as unavailable. """

        self.c.execute("UPDATE laptop SET is_available=0 WHERE id = ?;", (laptop_id,))

        self.c.execute("SELECT * FROM laptop;")
        updated_database = self.c.fetchall()

        return updated_database

    def add_user(self, user):
        address = user.address
        """ Add a user to the user and user_address databases. """
        self.c.execute("INSERT INTO user_address(line_1, city, post_code) VALUES (?, ?, ?); ", (address.line_1, address.city, address.post_code))
        self.c.execute("INSERT INTO user(first_name, last_name, email_address, date_requested, address_id) VALUES (?, ?, ?, ?,?); ", (user.first_name, user.last_name, user.email_address, user.date_requested, self.c.lastrowid))
        return self.c.lastrowid

    def add_laptop_assignment(self, user_id, laptop_id):
        """ Add a new user/laptop pairing to the laptop_assignment table. """
        self.c.execute("INSERT into laptop_assignment(id,laptop_id,user_id) VALUES(NULL,?,?);", (laptop_id,user_id))

        self.c.execute("SELECT * FROM laptop_assignment;")
        updated_database = self.c.fetchall()

        return updated_database
