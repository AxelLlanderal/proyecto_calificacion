import sqlite3
conn = sqlite3.connect('personas.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    correo_electronico TEXT NOT NULL,
    calificacion_1 REAL NOT NULL,
    calificacion_2 REAL NOT NULL,
    calificacion_3 REAL NOT NULL
)
''')
conn.commit()
conn.close()