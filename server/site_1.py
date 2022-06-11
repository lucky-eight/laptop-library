""" Main file for personal website. """

# Imports
from flask import Flask, render_template
import sqlite3 as db
import utils.setup_db as setup_db

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
    setup_db.populate_inventory_db()
    setup_db.print_inventory_db()
    app.run(debug=True)

