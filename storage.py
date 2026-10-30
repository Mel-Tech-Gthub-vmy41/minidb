import csv
import os

DATA_DIR = "data"

def save_table(table_name, columns, rows):
    path = os.path.join(DATA_DIR, f"{table_name}.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)

def load_table(table_name):
    path = os.path.join(DATA_DIR, f"{table_name}.csv")
    if not os.path.exists(path):
        return None, []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return [], []
    return rows[0], rows[1:]

def table_exists(table_name):
    path = os.path.join(DATA_DIR, f"{table_name}.csv")
    return os.path.exists(path)


