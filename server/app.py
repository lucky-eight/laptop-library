""" Main file for laptop library website. """

__copyright__ = "Copyright (C) 2022 lucky-8"

# Standard library imports
import datetime

# External imports
from flask import Flask, render_template

# Internal imports
from server.utils.database import Database
from server.utils.common import Address, User

app = Flask(__name__)

@app.route("/")
def home():
    """ Home page. """
    return render_template("home.html")

@app.route("/request-laptop/", methods=["POST"])
def requestLaptop():
    """ request and check for laptop """
    # Validate user request, return 400 if unsuccessful

    # Store user details

    # Check for available laptop, return 204 if unsuccessful

    # Assign laptop to user

    # Mark the laptop as unavailable
    # If there's an available laptop, return success with 202 and laptop details

    return  

if __name__ == "__main__":


    db = Database("./server/test_data/laptop.csv",
                  "./server/test_data/user.csv",
                  "./server/test_data/user_address.csv",
                  "./server/test_data/laptop_assignment.csv")
    # db.print_inventory_db()
    # print("London", db.find_laptops(["London"]))
    address = Address("line_1", "city", "post_code")
    user = User("first_name", "last_name", "email_address", datetime.datetime.utcnow(), address)
    db.add_user(user)
    # db.mark_unavailable(2)
    print(db.add_laptop_assignment(9,6))

    app.run()

