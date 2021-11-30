# Librerías
import mysql.connector
from flask import Flask, request, render_template, redirect, jsonify
from flask_expects_json import expects_json
from datetime import datetime


# Configuraciones
app = Flask(__name__)
PORT = 5000
DEBUG = False
medicionSchema = {
    'type': 'object',
    'properties': {
        'valorMedicion': {'type': 'number'},
        'idDispositivo': {'type': 'number'}
    },
    'required': ['valorMedicion', 'idDispositivo']
}


# Rutas


# Mostrar página principal
@app.route("/")
def index():
    return render_template("home.html")


# Mostrar sensores
@app.route("/sensores")
def mostrarSensores():

    # Buscar sensores
    try:
        # Conectar a la DB
        db = mysql.connector.connect(
            host = "us-cdbr-east-03.cleardb.com",
            user="b64c03ae0a0611",
            password="ddc2b455",
            database ="heroku_1a3d473a4d95416"
        )
        cursor = db.cursor(buffered=True)

        # Query al DB
        sql = "SELECT * FROM sensores"
        cursor.execute(sql)

        # Tratar la data para usar en html
        sensores = []
        for row in cursor:
            sensores.append(row)

        return render_template("sensores.html", sensores=sensores)

    except Exception as e:

        # Gestionar error
        print(e)
        error = {"message": "Hubo un error cargando los sensores.", "error": str(e)}
        return render_template("error.html", error=error)


# Añadir sensor
@app.route("/sensores/nuevo", methods=["GET", "POST"])
def agregarSensor():

    # Método GET - Mostrar formulario para añadir sensor
    if request.method == "GET":
        return render_template("nuevo_sensor.html")

    # Método POST - Recibir datos del form y crear sensor
    if request.method == "POST":

        # Recibir valores del request from
        modeloSensor = request.form["modeloSensor"]
        marcaSensor = request.form["marcaSensor"]
        precisionSensor = request.form["precisionSensor"]

        try:
            # Conectar a la DB
            db = mysql.connector.connect(
                host = "us-cdbr-east-03.cleardb.com",
                user="b64c03ae0a0611",
                password="ddc2b455",
                database ="heroku_1a3d473a4d95416"
            )
            cursor = db.cursor(buffered=True)

            # Commit al DB
            sql = "INSERT INTO sensores (modeloSensor, marcaSensor, precisionSensor) VALUES (%s, %s, %s)"
            val = (modeloSensor, marcaSensor, precisionSensor)
            cursor.execute(sql, val)
            db.commit()

            return redirect("/sensores")

        except Exception as e:

            # Gestionar error
            print(e)
            error = {"message": "Hubo un error creando el nuevo sensor.", "error": str(e)}
            return render_template("error.html", error=error)


# Eliminar sensor
@app.route("/sensores/eliminar/<int:idSensor>")
def eliminarSensor(idSensor):

    try:
        # Conectar a la DB
        db = mysql.connector.connect(
            host = "us-cdbr-east-03.cleardb.com",
            user="b64c03ae0a0611",
            password="ddc2b455",
            database ="heroku_1a3d473a4d95416"
        )
        cursor = db.cursor(buffered=True)

        # Commit al DB
        sql = f"DELETE FROM sensores WHERE idSensor={idSensor}"
        cursor.execute(sql)
        db.commit()

        return redirect("/sensores")

    except Exception as e:

            # Gestionar error
            print(e)
            error = {"message": "Hubo un error eliminando el sensor.", "error": str(e)}
            return render_template("error.html", error=error)


# Mostrar dispositivos
@app.route("/dispositivos", methods=["GET"])
def mostrarDispositivos():

    # Buscar dispositivos
    try:
        # Conectar a la DB
        db = mysql.connector.connect(
            host = "us-cdbr-east-03.cleardb.com",
            user="b64c03ae0a0611",
            password="ddc2b455",
            database ="heroku_1a3d473a4d95416"
        )
        cursor = db.cursor(buffered=True)

        # Query al DB
        sql = "SELECT * FROM dispositivos"
        cursor.execute(sql)

        # Tratar la data para usar en html
        dispositivos = []
        for row in cursor:
            dispositivos.append(row)

        return render_template("dispositivos.html", dispositivos=dispositivos)

    except Exception as e:

            # Gestionar error
            print(e)
            error = {"message": "Hubo un error cargando los dispositivos.", "error": str(e)}
            return render_template("error.html", error=error)


# Añadir dispositivo
@app.route("/dispositivos/nuevo", methods=["GET", "POST"])
def agregarDispositivo():

    # Método GET - Mostrar formulario para añadir dispositivo
    if request.method == "GET":
        return render_template("nuevo_dispositivo.html")

    # Método POST - Recibir datos del form y crear dispositivo
    if request.method == "POST":

        # Recibir valores del request from
        macDispositivo = request.form["macDispositivo"]
        modeloDispositivo = request.form["modeloDispositivo"]
        marcaDispositivo = request.form["marcaDispositivo"]
        ubicacionDispositivo = request.form["ubicacionDispositivo"]
        idSensor = request.form["idSensor"]

        try:
            # Conectar a la DB
            db = mysql.connector.connect(
                host = "us-cdbr-east-03.cleardb.com",
                user="b64c03ae0a0611",
                password="ddc2b455",
                database ="heroku_1a3d473a4d95416"
            )
            cursor = db.cursor(buffered=True)

            # Commit al DB
            sql = "INSERT INTO dispositivos (macDispositivo, modeloDispositivo, marcaDispositivo, ubicacionDispositivo, idSensor) VALUES (%s, %s, %s, %s, %s)"
            val = (macDispositivo, modeloDispositivo, marcaDispositivo, ubicacionDispositivo, idSensor)
            cursor.execute(sql, val)
            db.commit()

            return redirect("/dispositivos")

        except Exception as e:

            # Gestionar error
            print(e)
            error = {"message": "Hubo un error creando el nuevo dispositivo.", "error": str(e)}
            return render_template("error.html", error=error)


# Eliminar dispositivo
@app.route("/dispositivos/eliminar/<int:idDispositivo>")
def eliminarDispositivo(idDispositivo):

    try:
        # Conectar a la DB
        db = mysql.connector.connect(
            host = "us-cdbr-east-03.cleardb.com",
            user="b64c03ae0a0611",
            password="ddc2b455",
            database ="heroku_1a3d473a4d95416"
        )
        cursor = db.cursor(buffered=True)

        # Commit al DB
        sql = f"DELETE FROM dispositivos WHERE idDispositivo={idDispositivo}"
        cursor.execute(sql)
        db.commit()

        return redirect("/dispositivos")

    except Exception as e:

        # Gestionar error
        print(e)
        error = {"message": "Hubo un error eliminando el dispositivo.", "error": str(e)}
        return render_template("error.html", error=error)


# Mostrar mediciones
@app.route("/mediciones")
def mostrarMediciones():

    # Buscar mediciones
    try:
        # Conectar a la DB
        db = mysql.connector.connect(
            host = "us-cdbr-east-03.cleardb.com",
            user="b64c03ae0a0611",
            password="ddc2b455",
            database ="heroku_1a3d473a4d95416"
        )
        cursor = db.cursor(buffered=True)

        # Query al DB
        sql = "SELECT * FROM mediciones"
        cursor.execute(sql)

        # Tratar la data para usar en html
        mediciones = []
        for row in cursor:
            item = []
            item.append(row[0])
            item.append(row[1])
            item.append(row[2].strftime("%d/%m/%Y - %H:%M:%S"))
            item.append(row[3])
            mediciones.append(item)

        return render_template("mediciones.html", mediciones=mediciones)

    except Exception as e:

        # Gestionar error
        print(e)
        error = {"message": "Hubo un error cargando las mediciones.", "error": str(e)}
        return render_template("error.html", error=error)


# Agregar medicion
@app.route("/mediciones/nuevo", methods=["POST"])
@expects_json(medicionSchema)  # Expects JSON Medición
def agregarMedicion():

    # Recibir información del request en formato JSON
    valorMedicion = request.json["valorMedicion"]
    tsMedicion = datetime.utcnow()
    idDispositivo = request.json["idDispositivo"]

    try:
        # Conectar a la DB
        db = mysql.connector.connect(
            host = "us-cdbr-east-03.cleardb.com",
            user="b64c03ae0a0611",
            password="ddc2b455",
            database ="heroku_1a3d473a4d95416"
        )
        cursor = db.cursor(buffered=True)

        # Commit al DB
        sql = "INSERT INTO mediciones (valorMedicion, tsMedicion, idDispositivo) VALUES (%s, %s, %s)"
        val = (valorMedicion, tsMedicion, idDispositivo)
        cursor.execute(sql, val)
        db.commit()

        return jsonify({"message": "Se ha creado una nueva medicion exitosamente."})

    except Exception as e:

        # Gestionar error
        print(e)
        return jsonify({"message": "Hubo un error creando la nueva medicion.", "error": str(e)})


# Eliminar medicion
@app.route("/mediciones/eliminar/<int:idMedicion>")
def eliminarMedicion(idMedicion):

    try:
        # Conectar a la DB
        db = mysql.connector.connect(
            host = "us-cdbr-east-03.cleardb.com",
            user="b64c03ae0a0611",
            password="ddc2b455",
            database ="heroku_1a3d473a4d95416"
        )
        cursor = db.cursor(buffered=True)

        # Commit al DB
        sql = f"DELETE FROM mediciones WHERE idMedicion={idMedicion}"
        cursor.execute(sql)
        db.commit()

        return redirect("/mediciones")

    except Exception as e:

        # Gestionar error
        print(e)
        error = {"message": "Hubo un error eliminando la medicion.", "error": str(e)}
        return render_template("error.html", error=error)


# Run App
if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)