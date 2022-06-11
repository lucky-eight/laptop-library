""" Main file for laptop library website. """

__copyright__ = "Copyright (C) 2022 lucky-8"

# External imports
from flask import Flask, render_template

# Internal imports
from server.utils.database import Database
from server.utils.common import Address

app = Flask(__name__)

@app.route("/")
def home():
    """ Home page. """
    return render_template("home.html")

@app.route("/about/")
def about():
    """ About page. """
    return render_template("about.html")

if __name__ == "__main__":


    db = Database("./server/test_data/laptop.csv",
                  "./server/test_data/user.csv",
                  "./server/test_data/user_address.csv",
                  "./server/test_data/laptop_assignment.csv")
    # db.print_inventory_db()
    # print("London", db.find_laptops(["London"]))
    address = Address("line_1", "city", "post_code")
    db.add_user("first_name", "last_name", "email_address", address)
    # db.mark_unavailable(2)
    app.run()