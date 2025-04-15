# Importamos las clases necesarias de Flask
from flask import Flask, redirect, render_template, url_for
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave_secreta'

# Configuramos el modo debug
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Definimos una variable global para el título de la aplicación
titulo_app = "Zona Fit (GYM)"

# Definimos la ruta principal de la aplicación ('/')
# También definimos una ruta alternativa ('/index.html')
@app.route('/') # url: http://localhost:5000/
@app.route('/index.html') # url: http://localhost:5000/index.html
def inicio():
    # Registramos un mensaje de depuración en el log
    app.logger.debug("Entramos en la pagina de inicio /")
    # Renderizamos la plantilla index.html y le pasamos el título como variable
    clientes_db = ClienteDAO.seleccionar()
    # Creamos una instancia del formulario cliente form vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    #Creamos una instancia del formulario cliente form vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    if cliente_forma.validate_on_submit():
        #Guardamos los datos del formulario
        cliente_forma.populate_obj(cliente) # Tambien se recupera el id del formulario
        if not cliente.id:
            # Guardamos el nuevo cliente
                ClienteDAO.insertar(cliente)
        else:
            # Actualizamos el cliente existente
            ClienteDAO.actualizar(cliente)
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route("/editar/<int:id>") # localhost:5000/editar/1
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/eliminar/<int:id>') # localhost:5000/eliminar/1
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

# Verificamos si el script se está ejecutando directamente (no importado como módulo)
if __name__ == '__main__':
    # Iniciamos el servidor de desarrollo de Flask con modo debug activado
    app.run(debug=True, use_reloader=True)
    

