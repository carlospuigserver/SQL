import pandas as pd
from pathlib import Path
import sqlite3

Path("tabla.db").touch()

# Connect to the database

conn = sqlite3.connect('tabla.db')

cursor = conn.cursor()

df = pd.read_csv('Pokemon.csv')
df.to_sql('Pokemon', conn, if_exists='replace', index = False)

# Create a table in SQL Server

cursor.execute("SELECT * FROM Pokemon WHERE Name = 'Pikachu'")
for i in cursor:
    print(i)



