# SQLite Viewer extention is also available to check db
import sqlite3
import pandas as pd



"""
conn = sqlite3.connect("mlflow.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print(tables)

df = pd.read_sql("SELECT * FROM experiments;", conn)
print(df)

"""



#View all metrics
"""

conn = sqlite3.connect("mlflow.db")

df = pd.read_sql("SELECT * FROM metrics;", conn)

print(df)

conn.close()
"""



#See all available tables
"""

conn = sqlite3.connect("mlflow.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

for table in cursor.fetchall():
    print(table[0])

conn.close()
"""




#See all metrics for each run
conn = sqlite3.connect("mlflow.db")

df = pd.read_sql("""
SELECT run_uuid, key, value
FROM metrics
ORDER BY run_uuid;
""", conn)

print(df)

conn.close()