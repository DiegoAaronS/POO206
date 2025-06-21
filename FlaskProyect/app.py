from flask import Flask,jsonify,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="1234"
app.config['MYSQL_DB']="dbFlask"
app.config['MYSQL_PORT']=3307 #Se usa solo en cambio de puerto
app.secret_key='mysecretkey'

mysql = MySQL(app)

#Ruta de inicio
@app.route('/')
def home():
    return render_template('formulario.html')

#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

    #Ruta para el insert
@app.route('/guardarAlbum', methods=['POST'])
def guardar():
    #obtener los datos para insertar
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()
    
    #Intentamos Ejecutar el INSERT
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO tb_album (album, artista, anio) VALUES (%s, %s, %s)', (Vtitulo, Vartista, Vanio))
        mysql.connection.commit() 
        flash('Album guardado con exito') 
        return redirect(url_for('home'))
    
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo fallo: ' + str(e))
        return redirect(url_for('home'))
    
    finally:
        cursor.close()

#Ruta try-catch
@app.errorhandler(404)
def pageNotFound(e):
    return 'Cuidado: Error de capa 8 !!!',404
@app.errorhandler(405)
def methosNotAllowed(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST)',405

#Ruta para probar la conexion a MySQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500

if __name__ == '__main__':
    app.run(port=3000,debug=True)