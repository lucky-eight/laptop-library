""" Main file for laptop library website. """

__copyright__ = "Copyright (C) 2022 lucky-8"

# Standard library imports
import datetime

# External imports
from flask import Flask, render_template, jsonify, make_response, request
import json
from flask_cors import CORS

# Internal imports
from server.utils.database import Database
from server.utils.common import Address, User, Laptop

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def home():
    """ Home page. """
    return render_template("home.html")

@app.route("/about/")
def about():
    """ About page. """
    return render_template("about.html")
    # return "About page goes here"

@app.route("/request-laptop/", methods=["POST"])
def requestLaptop():
    """ request and check for laptop """
    # Validate user request, return 400 if unsuccessful
    data = request.json
    if not validate_input(data):
        return create_response(400, "Invalid request", False, {})

    # Create address object
    address = Address(data["address"]["line_1"],
                      data["address"]["city"],
                      data["address"]["postcode"])

    # Create user object
    user = User(data["firstName"],
                data["lastName"],
                data["email"],
                datetime.datetime.utcnow(),
                address)

    # Store user details
    user_id = db.add_user(user)

    # Check for available laptop, return 200 if no laptop found
    laptops_found = (db.find_laptops([address.city]))
    if not laptops_found:
        return create_response(200, "No laptop found", False, {})

    # Assign laptop to user
    laptop = Laptop(*laptops_found[0])
    db.add_laptop_assignment(user_id, laptop.id)

    # Mark the laptop as unavailable
    db.mark_unavailable(laptop.id)

    # If there's an available laptop, return success with 202 and laptop details
    laptop_dict = {"laptopName": laptop.name, "laptopLocation": laptop.location}

    return create_response(202, "Success", True, laptop_dict)

def validate_input(data):

    # Check that expected user details are present
    user_expected = ["firstName", "lastName", "email", "address"]
    if not (set(user_expected).issubset(set(list(data.keys())))):
        return False

    # Check that expected address details are present
    address_expected = ["line_1", "city", "postcode"]
    if not (set(address_expected).issubset(set(list(data["address"].keys())))):
        return False

    return True

def create_response(status, statusMessage, laptopAvailable, laptop):
    reponse = {'statusMessage': statusMessage,
               'data': {'laptopAvailable': laptopAvailable,
                        'laptop' : laptop}
               }
    return make_response(jsonify({'body': reponse }), status)

if __name__ == "__main__":


    db = Database("./server/test_data/laptop.csv",
                  "./server/test_data/user.csv",
                  "./server/test_data/user_address.csv",
                  "./server/test_data/laptop_assignment.csv")
    # db.print_inventory_db()
    # print("London", db.find_laptops(["London"]))
    #db.add_user(user)
    # db.mark_unavailable(2)
    #print(db.add_laptop_assignment(9,6))

    app.run()

