from parser import parse
from executor import execute

print("MiniDB - A tiny SQL database engine")
print("Supported: CREATE TABLE, INSERT INTO, SELECT, DROP TABLE")
print("Type 'exit' to quit\n")

while True:
    try:
        query = input("minidb> ").strip()
        if not query:
            continue
        if query.lower() == 'exit':
            print("Bye!")
            break
        parsed = parse(query)
        result = execute(parsed)
        print(result)
    except Exception as e:
        print(f"Error: {e}")



