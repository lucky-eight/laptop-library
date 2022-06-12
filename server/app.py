""" Main file for laptop library website. """

__copyright__ = "Copyright (C) 2022 lucky-8"

# Standard library imports
import datetime

# External imports
from flask import Flask, render_template, jsonify, make_response, request
import json

# Internal imports
from server.utils.database import Database
from server.utils.common import Address, User, Laptop

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the dark side :)"

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
        return jsonify({"status": 400})

    address = Address(data["address"]["line_1"],
                      data["address"]["city"],
                      data["address"]["postcode"])

    user = User(data["firstName"],
                data["lastName"],
                data["email"],
                datetime.datetime.utcnow(),
                address)
    # content_type = request.headers.get('Content-Type')
    # if (content_type != 'application/json'):
    #     return 'Content-Type not supported!'


    if not valid_user_details:

    # Validate user request, return 400 if unsuccessful

    # Store user details
    user_id = db.add_user(user)


    # Check for available laptop, return 204 if unsuccessful
    laptops_found = (db.find_laptops([address.city]))
    if not laptops_found:
        response = {'status': 204, 'statusMessage': 'No laptop found', 'data': {'laptopAvailable': False , 'laptop' : {} } }
        # response = {'statusMessage': 'No laptop found', 'data': {'laptopAvailable': False , 'laptop' : {} } }
        # response.headers["Content-Type"] = "application/json"
        return jsonify(response)

    laptop = Laptop(*laptops_found[0])

    # Assign laptop to user
    db.add_laptop_assignment(user_id, laptop.id)

    # Mark the laptop as unavailable
    db.mark_unavailable(laptop.id)

    # If there's an available laptop, return success with 202 and laptop details
    return ('202')

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

