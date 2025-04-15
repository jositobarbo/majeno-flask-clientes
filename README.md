# Sistema de Gestión de Clientes con Flask

Este es un sistema de gestión de clientes desarrollado con Flask y Python. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una base de datos de clientes.

## Características

- Listado de clientes
- Agregar nuevos clientes
- Editar información de clientes existentes
- Eliminar clientes
- Gestión de membresías

## Tecnologías utilizadas

- Python
- Flask
- MySQL
- HTML
- Bootstrap

## Instalación

1. Clona este repositorio
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Configura la base de datos en el archivo de conexión
6. Ejecuta la aplicación: `python app.py`

## Estructura del proyecto

- `app.py`: Archivo principal de la aplicación Flask
- `cliente.py`: Modelo de Cliente
- `cliente_dao.py`: Objeto de Acceso a Datos para Cliente
- `cliente_forma.py`: Formulario para Cliente
- `templates/`: Directorio con las plantillas HTML 