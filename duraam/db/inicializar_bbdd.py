"""Este módulo crea la conexión a la base de datos.

Si la base de datos no estaba creada, la crea con todas sus tablas.
"""
import sqlite3 as db
import os

os.chdir(f"{os.path.abspath(__file__)}/../../..")

# Se conecta a la base de datos
con = db.Connection(
    f"{os.path.abspath(os.getcwd())}/duraam/db/duraam.sqlite3")
# Crea el cursor
cur = con.cursor()

# Abre el archivo duraam.sql
with open(f"{os.path.abspath(os.getcwd())}/duraam/db/duraam.sql", 'r', encoding='utf-8') as codigoSQL:
    # Con la función split, separa cada statement (es decir, cada código) en una lista.
    codigoSQL = codigoSQL.read().split(';')
    # Recorre la lista y ejecuta cada código.
    for statement in codigoSQL:
        cur.execute(statement)
    # Guarda los cambios en la base de datos.
    con.commit()
