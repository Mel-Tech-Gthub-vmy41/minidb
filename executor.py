import os
from storage import save_table, load_table, table_exists

DATA_DIR = "data"

def execute(parsed):
    qtype = parsed['type']

    if qtype == 'CREATE':
        table = parsed['table']
        columns = parsed['columns']
        if table_exists(table):
            return f"Table '{table}' already exists."
        save_table(table, columns, [])
        return f"Table '{table}' created."

    elif qtype == 'INSERT':
        table = parsed['table']
        values = parsed['values']
        columns, rows = load_table(table)
        if columns is None:
            return f"Table '{table}' does not exist."
        rows.append(values)
        save_table(table, columns, rows)
        return f"1 row inserted into '{table}'."

    elif qtype == 'SELECT':
        table = parsed['table']
        columns, rows = load_table(table)
        if columns is None:
            return f"Table '{table}' does not exist."
        if parsed['where']:
            col = parsed['where']['col']
            val = parsed['where']['val']
            if col not in columns:
                return f"Column '{col}' not found."
            col_idx = columns.index(col)
            rows = [r for r in rows if r[col_idx] == val]
        result = [columns] + rows
        output = ""
        for row in result:
            output += " | ".join(row) + "\n"
        return output.strip()

    elif qtype == 'DROP':
        table = parsed['table']
        path = os.path.join(DATA_DIR, f"{table}.csv")
        if not os.path.exists(path):
            return f"Table '{table}' does not exist."
        os.remove(path)
        return f"Table '{table}' dropped."

    else:
        return "Unsupported query type."

