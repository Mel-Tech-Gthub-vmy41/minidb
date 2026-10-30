def parse(query):
    query = query.strip().rstrip(';')
    tokens = query.split()
    command = tokens[0].upper()

    if command == 'CREATE':
        # CREATE TABLE users (id, name, age)
        table_name = tokens[2]
        cols_str = query[query.index('(')+1:query.index(')')]
        columns = [c.strip() for c in cols_str.split(',')]
        return {'type': 'CREATE', 'table': table_name, 'columns': columns}

    elif command == 'INSERT':
        # INSERT INTO users VALUES (1, Alice, 30)
        table_name = tokens[2]
        vals_str = query[query.index('(')+1:query.index(')')]
        values = [v.strip() for v in vals_str.split(',')]
        return {'type': 'INSERT', 'table': table_name, 'values': values}

    elif command == 'SELECT':
        # SELECT * FROM users WHERE age = 30
        from_idx = [t.upper() for t in tokens].index('FROM')
        table_name = tokens[from_idx + 1]
        result = {'type': 'SELECT', 'table': table_name, 'where': None}
        if 'WHERE' in [t.upper() for t in tokens]:
            where_idx = [t.upper() for t in tokens].index('WHERE')
            col = tokens[where_idx + 1]
            op = tokens[where_idx + 2]
            val = tokens[where_idx + 3]
            result['where'] = {'col': col, 'op': op, 'val': val}
        return result

    elif command == 'DROP':
        # DROP TABLE users
        table_name = tokens[2]
        return {'type': 'DROP', 'table': table_name}

    else:
        raise ValueError(f"Unsupported command: {command}")


