import sqlite3
import pandas as pd

#leer el archivo csv
df = pd.read_csv('pokemon.csv')

#crear la conexion
conexion = sqlite3.connect('pokemon.db')

#guardar el dataframe en la base de datos
df.to_sql('pokemon', conexion, if_exists='replace')

#realizar consutas sql a la base de datos
df = pd.read_sql_query('SELECT * FROM pokemon', conexion)


# Seleccionar todos los registros de una tabla
cursor = conexion.execute('SELECT * FROM tabla')
for fila in cursor:
    print(fila)

# Insertar un registro en una tabla
conexion.execute("INSERT INTO tabla (columna1, columna2) VALUES (?, ?)", ('valor1', 'valor2'))
conexion.commit()

# Actualizar un registro en una tabla
conexion.execute("UPDATE tabla SET columna2 = ? WHERE columna1 = ?", ('nuevo_valor', 'valor1'))
conexion.commit()

# Eliminar un registro de una tabla
conexion.execute("DELETE FROM tabla WHERE columna1 = ?", ('valor1',))
conexion.commit()

# Obtener el número de registros en una tabla
cursor = conexion.execute('SELECT COUNT(*) FROM tabla')
num_registros = cursor.fetchone()[0]
print(num_registros)

# Agrupar los datos de una tabla
cursor = conexion.execute('SELECT columna, COUNT(*) FROM tabla GROUP BY columna')
for fila in cursor:
    print(fila)

# Filtrar los datos agrupados
cursor = conexion.execute('SELECT columna, COUNT(*) FROM tabla GROUP BY columna HAVING COUNT(*) > 1')
for fila in cursor:
    print(fila)

# Ordenar los datos de una tabla
cursor = conexion.execute('SELECT * FROM tabla ORDER BY columna1 DESC')
for fila in cursor:
    print(fila)

#usar distinct
cursor = conexion.execute('SELECT DISTINCT columna1 FROM tabla')



# Cerrar la conexión a la base de datos
conexion.close()

