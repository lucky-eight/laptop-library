
import pandas as pd

def read_laptops_csv(laptops_csv):
    """ Reads a CSV and converts it to a list of tuples
    to be fed into a database through sqlite3."""

    data_frame = pd.read_csv(laptops_csv)
    db_contents = data_frame.apply(tuple, axis=1).tolist()
    return db_contents

read_laptops_csv("server/laptop.csv")
