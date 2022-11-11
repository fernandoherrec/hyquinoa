from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

# Conexión MySQL
app.config['MYSQL_HOST'] = 'labsac.com'
app.config['MYSQL_USER'] = 'labsacco_sac'
app.config['MYSQL_PASSWORD'] = 'sac15153232'
app.config['MYSQL_DB'] = 'labsacco_utopia'

conexion = MySQL(app)

@app.route('/')
def index():
    data={
        'titulo': 'Index',
        'bienvenida': '¡Saludos!'
    }
    return render_template('index.html')

@app.route('/granja/piura')
def solicitar_mediciones():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM vertical_farming ORDER BY Id DESC LIMIT 100"
        cursor.execute(sql)
        mediciones = cursor.fetchall()
        # print(mediciones)
        data['mediciones'] = mediciones
        data['mensaje'] = 'Exito'
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return render_template('dashboard.html', data=data)

if __name__=='__main__':
    app.run(debug=True, port=5000)