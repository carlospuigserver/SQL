# SQL


El link de este repositorio es el siguiente: https://github.com/carlospuigserver/SQL.git



El código que hemos realizado para usar una serie de instancias sql a partir de un csv exixtente, pasado a base de datos y de este creado una tabla es el siguiente:

```
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
for i in cursor:
    print(i)

# UPDATE

cursor.execute("UPDATE Pokemon SET Name = 'Mewtwo' WHERE Name = 'Miguel'")

# DELETE

cursor.execute("DELETE FROM Pokemon WHERE Name = 'Raichu'")

# SELECT (no se ejecuta porque se eliminó el registro)

cursor.execute("SELECT * FROM Pokemon WHERE Name = 'Raichu'")

for i in cursor:

    print(i)

# obtener el numero de registros

cursor.execute("SELECT COUNT(*) FROM Pokemon")

for i in cursor:
    
        print(i)

# agrupar por tipo

cursor.execute("SELECT Type1, COUNT(*) FROM Pokemon GROUP BY Type1")

for i in cursor:
        
            print(i)

# obtener el promedio de ataque

cursor.execute("SELECT AVG(Attack) FROM Pokemon")

for i in cursor:

    print("El promedio de ataque es", i)

# filtrar por ataque mayor que 100

cursor.execute("SELECT * FROM Pokemon WHERE Attack > 100")

for i in cursor:
          
        print(i)



# pokemon con defensa entre 20 y 25

cursor.execute("SELECT * FROM Pokemon WHERE Defense BETWEEN 20 AND 25")







```







Los resultados de realizar estas instancias son los siguientes:


<img width="941" alt="pok1" src="https://user-images.githubusercontent.com/91721643/227001057-f909b23a-24ad-435c-b017-53b171277c5d.png">
<img width="960" alt="pok2" src="https://user-images.githubusercontent.com/91721643/227001106-e606046c-f247-4d60-94c4-92733390cbe6.png"><img width="937" alt="pok3" src="https://user-images.githubusercontent.com/91721643/227001126-77aaddcd-6a52-4b92-b1cf-2c6632379df2.png">





