from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('personas.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    personas = conn.execute('SELECT * FROM personas').fetchall()
    conn.close()
    return render_template('index.html', personas=personas)

@app.route('/agregar', methods=('GET', 'POST'))
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        correo_electronico = request.form['correo_electronico']
        calificacion_1 = float(request.form['calificacion_1'])
        calificacion_2 = float(request.form['calificacion_2'])
        calificacion_3 = float(request.form['calificacion_3'])
        conn = get_db_connection()
        conn.execute('INSERT INTO personas (nombre, edad, correo_electronico, calificacion_1, calificacion_2, calificacion_3) VALUES (?, ?, ?, ?, ?, ?)', 
                     (nombre, edad, correo_electronico, calificacion_1, calificacion_2, calificacion_3))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('agregar.html')

@app.route('/actualizar/<int:id>', methods=('GET', 'POST'))
def actualizar(id):
    conn = get_db_connection()
    persona = conn.execute('SELECT * FROM personas WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        correo_electronico = request.form['correo_electronico']
        calificacion_1 = float(request.form['calificacion_1'])
        calificacion_2 = float(request.form['calificacion_2'])
        calificacion_3 = float(request.form['calificacion_3'])
        conn.execute('UPDATE personas SET nombre = ?, edad = ?, correo_electronico = ?, calificacion_1 = ?, calificacion_2 = ?, calificacion_3 = ? WHERE id = ?', 
                     (nombre, edad, correo_electronico, calificacion_1, calificacion_2, calificacion_3, id))
        conn.commit()
        conn.close()
        return redirect('/')
    conn.close()
    return render_template('actualizar.html', persona=persona)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM personas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)