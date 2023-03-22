import pandas as pd
from pathlib import Path
import sqlite3

Path("tabla.db").touch()

# Connect to the database

conn = sqlite3.connect('tabla.db')

cursor = conn.cursor()

df = pd.read_csv('Pokemon.csv')
df.to_sql('Pokemon', conn, if_exists='replace', index = False)

# INSERT un registro

cursor.execute("INSERT INTO Pokemon (Number,Name,Type1,Type2,HP,Attack,Defense,SpAttack,SpDefense,Speed,Total,Image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (4, 'German', 'Ground', 'Fairy', 35, 55, 40, 50, 50, 90, 320, "null"))

# SELECT

cursor.execute("SELECT * FROM Pokemon WHERE Name = 'German'")

print("Seleccionamos el pokemon que acabamos de insertar")

for i in cursor:
    print(i)

# UPDATE

cursor.execute("UPDATE Pokemon SET Name = 'Mewtwo' WHERE Name = 'Miguel'")

cursor.execute("SELECT * FROM Pokemon WHERE Name = 'Miguel'")

print("Seleccionamos el pokemon que acabamos de actualizar")

for i in cursor:
    print(i)

# DELETE

print("Eliminamos a Raichu")

cursor.execute("DELETE FROM Pokemon WHERE Name = 'Raichu'")

# SELECT (no se ejecuta porque se eliminó el registro)

cursor.execute("SELECT * FROM Pokemon WHERE Name = 'Raichu'")

for i in cursor:

    print(i)

 
# obtener el numero de registros

print("El numero de registros es: ")

cursor.execute("SELECT COUNT(*) FROM Pokemon")

for i in cursor:
    
        print(i)

# agrupar por tipo

print("Agrupamos por tipo")

cursor.execute("SELECT Type1, COUNT(*) FROM Pokemon GROUP BY Type1")

for i in cursor:
        
            print(i)

# obtener el promedio de ataque

print("El promedio de ataque es: ")

cursor.execute("SELECT AVG(Attack) FROM Pokemon")

for i in cursor:

    print("El promedio de ataque es", i)

# filtrar por ataque mayor que 160

print("Los pokemon con ataque mayor que 160 son: ")

cursor.execute("SELECT * FROM Pokemon WHERE Attack > 160")

for i in cursor:
          
        print(i)

# pokemon con defensa entre 20 y 25

print("Los pokemon con defensa entre 90 y 100 son: ")

cursor.execute("SELECT * FROM Pokemon WHERE Defense BETWEEN 20 AND 25")

for i in cursor:
      
        print(i)







