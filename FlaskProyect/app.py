from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="1234"
app.config['MYSQL_DB']="dbflask"
app.config['MYSQL_PORT']=3307 #Se usa solo en cambio de puerto

mysql = MySQL(app)

#Ruta para probar la conexion a MySQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500

#Ruta simple
@app.route('/')
def home():
    return 'Hola Mundo FLASK'

#Ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola, '+nombre+'!!!'

#Ruta try-catch
@app.errorhandler(404)
def pageNotFound(e):
    return 'Cuidado: Error de capa 8 !!!',404
@app.errorhandler(405)
def methosNotAllowed(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST)',405

#Ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'

#Ruta POST
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'Soy un formulario'

if __name__ == '__main__':
    app.run(port=3000,debug=True)