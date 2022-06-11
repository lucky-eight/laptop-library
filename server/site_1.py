""" Main file for personal website. """

# Imports
from flask import Flask, render_template

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
    app.run(debug=True)
