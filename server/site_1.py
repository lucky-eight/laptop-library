""" Main file for personal website. """

# Imports
from flask import Flask, render_template
import sqlite3 as db

app = Flask(__name__)
conn = db.connect('my_database.db')
c = conn.cursor()

@app.route("/")
def home():
    """ Home page. """
    return render_template("home.html")

@app.route("/about/")
def about():
    """ About page. """
    return render_template("about.html")
    # return "About page goes here"

if __name__ == "__main__":

    c.execute("CREATE TABLE IF NOT EXISTS laptops (laptopid INTEGER PRIMARY KEY, name NVARCHAR(20), city NVARCHAR(20))")

    # populate database
    new_laptops = [(1, 'MacBook Pro 16 inch', 'London')]

    c.executemany('INSERT INTO laptops VALUES (?, ?, ?)', new_laptops)

    c.execute("SELECT * FROM laptops;")
    print(c.fetchall())
    app.run(debug=True)

