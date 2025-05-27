import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('personas.db')
cursor = conn.cursor()

# Renombrar la tabla actual
cursor.execute('ALTER TABLE personas RENAME TO personas_old')

# Crear la nueva tabla con los campos actualizados
cursor.execute('''
CREATE TABLE personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    correo_electronico TEXT NOT NULL,
    calificacion_1 REAL NOT NULL,
    calificacion_2 REAL NOT NULL,
    calificacion_3 REAL NOT NULL
)
''')

# Transferir datos de la tabla antigua a la nueva, asignando valores por defecto
cursor.execute('''
INSERT INTO personas (id, nombre, edad, correo_electronico, calificacion_1, calificacion_2, calificacion_3)
SELECT id, nombre, edad, 'sin_correo@ejemplo.com', 0.0, 0.0, 0.0
FROM personas_old
''')

# Eliminar la tabla antigua
cursor.execute('DROP TABLE personas_old')

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()

print("Migración completada exitosamente.")