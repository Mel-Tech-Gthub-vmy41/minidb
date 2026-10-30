# MiniDB - Mini SQL Database Engine

A relational database engine built from scratch in Python, without using any external database libraries.

## Features
- SQL query parsing (CREATE, INSERT, SELECT, DROP)
- WHERE clause filtering
- File-based CSV storage for data persistence
- Interactive SQL shell

## Tech Stack
- Python 3

## How to Run
```bash
python3 main.py
```

## Example Usage
```sql
minidb> CREATE TABLE employees (id, name, department, salary)
minidb> INSERT INTO employees VALUES (1, Alice, Engineering, 90000)
minidb> INSERT INTO employees VALUES (2, Bob, Marketing, 70000)
minidb> SELECT * FROM employees WHERE department = Engineering
id | name | department | salary
1  | Alice | Engineering | 90000
```

## Project Structure
- `storage.py` — saves/loads table data to CSV files
- `parser.py` — tokenizes and parses SQL queries
- `executor.py` — executes parsed queries against stored data
- `main.py` — interactive SQL shell
