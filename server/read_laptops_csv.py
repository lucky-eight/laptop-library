
import pandas as pd

def read_laptops_csv(laptops_csv):
    db = pd.read_csv(laptops_csv, index_col="ID")
    print(db)
    return db

read_laptops_csv("server/laptops.csv")
