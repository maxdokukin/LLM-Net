import sqlite3

name = "hr"
full_name = f"../data/{name}.db"

conn = sqlite3.connect(full_name)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY
    )
""")

conn.commit()
conn.close()

print(f"Database {full_name} created with all sample entries.")
