# Directorio de Contactos - Flask MVC

Este proyecto es un ejercicio academico para practicar Git Bash y el patron MVC usando Python, Flask, Flask-SQLAlchemy, SQLite, HTML y CSS.

## Estructura MVC

- Modelo: `models.py` contiene la clase `Contacto`, que representa los datos guardados en SQLite.
- Vista: `templates/index.html` muestra formularios y una tabla con contactos.
- Controlador: `app.py` recibe las peticiones del navegador, consulta o modifica la base de datos y envia datos a la vista.

## Flujo de versiones con Git

### Parte 1 - Main

Persona A crea la version base del backend:

- `app.py`
- `models.py`
- Base de datos SQLite automatica
- Datos de muestra
- Consulta `Contacto.query.all()`
- Logica temporal en consola

Comandos sugeridos:

```bash
git checkout -b main
git add .
git commit -m "Crear version base del directorio"
```

### Parte 2 - Branch backend

Persona A crea una rama para servicios extra:

- Ruta `/add` con metodo POST
- Ruta `/search` con busqueda por nombre

Comandos sugeridos:

```bash
git checkout -b backend-servicios
git add .
git commit -m "Agregar rutas para registrar y buscar contactos"
```

### Parte 3 - Branch frontend

Persona B crea una rama para la interfaz:

- `index.html`
- `style.css`
- Tabla con Jinja2
- Formularios conectados a `/add` y `/search`

Comandos sugeridos:

```bash
git checkout -b frontend-interfaz
git add .
git commit -m "Crear interfaz del directorio de contactos"
```

### Parte 4 - Merge final

Se integran las ramas de backend y frontend:

```bash
git checkout main
git merge backend-servicios
git merge frontend-interfaz
git add .
git commit -m "Integrar backend y frontend del directorio"
```

## Como ejecutar

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```
