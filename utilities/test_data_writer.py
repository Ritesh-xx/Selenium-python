# utilities/data_writer.py

import csv
import os

def write_user_to_csv(filepath, user_data):
    file_exists = os.path.isfile(filepath)
    with open(filepath, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['email', 'password'])
        if not file_exists:
            writer.writeheader()
        writer.writerow({'email': user_data['email'], 'password': user_data['password']})
