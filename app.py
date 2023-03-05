from flask import Flask, render_template, request, session, url_for, flash, redirect
import mysql.connector
app = Flask(__name__)
app.secret_key = 'aries2954013579'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aries1901",
  database="clinicasegura"
)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/index.html")
def inicio():
    return render_template("index.html")

@app.route("/especialidades.html")
def especialidades():
    return render_template("especialidades.html")

@app.route("/servicios.html")
def servicios():
    return render_template("servicios.html")

@app.route("/contactanos.html")
def contactanos():
    return render_template("contactanos.html")

#Conexion de base de datos
@app.route('/login', methods = ['GET','POST'])
def login():
    if mydb is None:
        return render_template('/login.html', mensaje='Error al conectarse a la base de datos')
    

    login = request.form['username']
    password = request.form['password']

    try:
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM usuarios WHERE login = %s AND password = %s", (login, password))

        usuario = mycursor.fetchone()

        if usuario:
                session['username'] = login # Almacenar el nombre de usuario en la sesión
                return render_template('/index.html', correcta = 'Has iniciado sesión correctamente')
        else:
           
            # Nombre de usuario o contraseña incorrectos
            return render_template('/login.html', error='Nombre de usuario o contraseña incorrectos')

    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta a la base de datos: {}".format(error))
        return render_template('/login.html', error='Error al ejecutar la consulta a la base de datos')


#Registro de la base de datos
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Aquí es donde se procesa el formulario de registro y se guardan los datos en la base de datos
        nombre_usuario = request.form['nombre_usuario']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        # Aquí debes insertar los datos en tu base de datos utilizando una consulta SQL
        # Ejemplo:
        # cursor.execute("INSERT INTO usuarios (nombre_usuario, correo, contrasena) VALUES (%s, %s, %s)", (nombre_usuario, correo, contrasena))
        # db.commit()
        
        return redirect(url_for('inicio')) # Después de procesar el formulario, redirigir al usuario a la página de inicio

    return render_template('registro.html') # Si el método HTTP es GET, renderizar el formulario de registro



if __name__ == "__main__":
    app.run(port=4000, host="0.0.0.0")
