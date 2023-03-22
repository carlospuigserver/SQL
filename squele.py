import sqlite3
import pandas as 
from pathlib

# Connect to the database

Path

data = pd.read_csv('Pokemon.csv')
df = pd.DataFrame(data, columns= ["Number","Name","Type1","Type2","HP","Attack","Defense","SpAttack","SpDefense","Speed","Total","Image"])

conn = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-2JQJQ0C\SQLEXPRESS;' 'Database=Pokemon;' 'Trusted_Connection=yes;')

cursor = conn.cursor()

# Create a table in SQL Server

cursor.execute("SELECT * FROM Pokemon WHERE Name = 'Pikachu'")

for i in cursor:
    print(i)

# SELECT * FROM Pokemon WHERE Name = 'Pikachu'

