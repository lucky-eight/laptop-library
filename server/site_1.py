""" Main file for personal website. """

# Imports
from flask import Flask, render_template
from utils.database import Database

app = Flask(__name__)

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
    db = Database("test_data/laptop.csv")
    # db.print_inventory_db()
    # print("London", db.find_laptops(["London"]))
    # db.mark_unavailable(2)
    app.run()

    # setup_db.populate_inventory_db()
    # setup_db.print_inventory_db()
