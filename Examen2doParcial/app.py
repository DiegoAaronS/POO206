from flask import Flask,jsonify,render_template,flash,redirect,url_for,request
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="1234"
app.config['MYSQL_DB']="dbConsulta"
app.config['MYSQL_PORT']=3007
app.secret_key='mysecretkey'

mysql = MySQL(app)

@app.route('/')
def home():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM dbConsulta WHERE state=1')
            consultaTodo= cursor.fetchall()
            return render_template('formulario.html', errores={}, contactos=consultaTodo)
        except Exception as e:
            print('Error al consultar todo: '+e)
            return render_template('formulario.html', errores={}, contactos=[])
        finally:
            cursor.close()
            
@app.route('/consultar/<id>')
def consulta():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM dbConsulta WHERE id=%s AND ',(id,))
            consultaTodo= cursor.fetchone()
            return render_template('consulta.html', contactos=consultaTodo)
        except Exception as e:
            print('Error al consultar: '+e)
            return redirect(url_for('home'))
        finally:
            cursor.close()

@app.route('/actualizar/<id>')
def actualizar():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE * FROM dbConsulta WHERE state=1')
            consultaTodo= cursor.fetchone()
            return render_template('formUpdate.html', errores={}, contactos=consultaTodo)
        except Exception as e:
            print('Error al eliminar: '+e)
            return render_template('formUpdate.html', errores={}, contacto=[])
        finally:
            cursor.close()
            
@app.route('/eliminar/<id>')
def eliminar():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM dbConsulta WHERE state=1')
            consultaTodo= cursor.fetchone()
            return render_template('confirmDel.html', errores={}, contactos=consultaTodo)
        except Exception as e:
            print('Error al eliminar: '+e)
            return render_template('confirmDel.html', errores={}, contacto=[])
        finally:
            cursor.close()              

@app.route('/guardarContacto', methods=['POST'])
def guardar():
    
    errores={}
    
    Vnombre = request.form.get('txtNombre', '').strip()
    Vcorreo = request.form.get('txtCorreo', '').strip()
    Vtelefono = request.form.get('txtTelefono', '').strip()
    Vedad = request.form.get('txtEdad', '').strip()
    
    if not Vnombre:
        errores['txtTitulo']= 'Nombre del contacto obligatorio'
    if not Vcorreo:
        errores['txtArtista']= 'Nombre del correo obligatorio'
    if not Vtelefono:
        errores['txtTelefono']= 'Telefono es obligatorio'
    elif not Vedad.isdigit() or int(Vedad) < 0 or int(Vedad) > 105:
        errores['txtEdad']= 'Ingresa una edad valida'
        
    if not errores:
    
    #Intentamos Ejecutar el INSERT
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO tb_album (album, artista, anio) VALUES (%s, %s, %s)', (Vtitulo, Vartista, Vanio))
            mysql.connection.commit() 
            flash('Álbum guardado con éxito') 
            return redirect(url_for('home'))
    
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo falló: ' + str(e))
            return redirect(url_for('home'))
    
        finally:
            cursor.close()
            
    return render_template('formulario.html', errores=errores)    

if __name__ == '__main__':
    app.run(port=3000,debug=True)