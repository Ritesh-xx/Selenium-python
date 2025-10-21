# utilities/data_loader.py

import csv

def read_login_data_from_csv(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['email'], row['password']) for row in reader]
